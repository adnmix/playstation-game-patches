"""Offline release-integrity checks. No network or console operations."""
from pathlib import Path
import hashlib
import json
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
catalog = json.loads((ROOT / 'catalog.json').read_text(encoding='utf-8'))
checksums = {}
for line in (ROOT / 'SHA256SUMS').read_text(encoding='utf-8').splitlines():
    digest, relative = line.split('  ', 1)
    assert re.fullmatch(r'[0-9a-f]{64}', digest), 'Malformed checksum'
    checksums[relative] = digest

expected_files = set()
for patch in catalog['patches']:
    relative = patch['file']
    assert relative not in expected_files, 'Duplicate catalog path'
    expected_files.add(relative)
    path = ROOT / relative
    assert path.resolve().is_relative_to(ROOT), 'Path outside repository'
    assert path.suffix == '.xml' and path.stat().st_size < 16384
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    assert digest == patch['sha256'] == checksums[relative], f'Hash mismatch: {relative}'
    root = ET.parse(path).getroot()
    assert root.tag == 'Patch'
    assert root.findtext('TitleID/ID') == patch['title_id']
    metadata = root.findall('Metadata')
    assert len(metadata) == 1
    meta = metadata[0]
    for key, wanted in [('AppVer', patch['app_version']), ('PatchVer', patch['patch_version']),
                        ('Author', 'adnmix'), ('AppElf', 'eboot.bin')]:
        assert meta.get(key) == wanted, f'{key} mismatch: {relative}'
    assert int(meta.get('ImageBase'), 16) == 0x400000
    lines = meta.findall('PatchList/Line')
    assert len(lines) == patch['write_count']
    ranges = []
    for line in lines:
        assert line.get('Type') == 'bytes'
        address = int(line.get('Address'), 16)
        value = line.get('Value', '')
        assert re.fullmatch(r'(?:[0-9A-Fa-f]{2})+', value)
        end = address + len(bytes.fromhex(value))
        assert 0x400000 <= address < end < 0x4000000
        assert all(end <= start or address >= stop for start, stop in ranges), 'Overlapping writes'
        ranges.append((address, end))
    print(f'PASS {patch["title_id"]} / {patch["app_version"]}: {len(lines)} writes, SHA-256 matches')

assert set(checksums) == expected_files
assert {p.relative_to(ROOT).as_posix() for p in (ROOT / 'patches').rglob('*.xml')} == expected_files
for path in ROOT.rglob('*.md'):
    for target in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
        if '://' in target or target.startswith('#'):
            continue
        target = target.split('#', 1)[0]
        assert (path.parent / target).exists(), f'Broken local link: {path.name} -> {target}'
print('PASS catalog, XML metadata, checksums, write ranges, and local documentation links')
