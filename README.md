# PlayStation Game Patches

Version-specific performance patches maintained and tested by [adnmix](https://github.com/adnmix), developed with **OpenAI Codex assistance** for executable analysis, patch generation, verification, and documentation.

This is an independent community project, with no affiliation with Sony or the games' developers. It contains patch instructions and documentation only: no games, PKGs, executable dumps, assets, payloads, or bundled third-party tools.

## Use at your own risk

**These patches modify running game memory. They can crash a game or console, cause a kernel panic, interrupt writes, or corrupt data. Back up your saves first.**

You are responsible for deciding whether to use these files and for the consequences. They are provided **AS IS, without warranty or guaranteed performance, compatibility, safety, or support**. To the extent permitted by applicable law, adnmix and contributors accept no liability for damage, loss of data, or other losses arising from their use. See [LICENSE](LICENSE) and [testing limits](docs/TESTING.md).

Two console crashes occurred during live debugger checks in Mortuary research, including the abandoned 4K experiment. The exact cause was not isolated. No Mortuary v1.1 writes had been applied before the second crash. **The untested 4K patch is not included.**

## Available patches

| Game | Game platform | Exact title ID / app version | Patch | Result reported in testing |
| --- | --- | --- | --- | --- |
| [Green Hell](patches/ps5/green-hell/README.md) | PS5 | `PPSA21629` / `01.004.000` | [v1.0: 60 FPS target + 1080p](patches/ps5/green-hell/PPSA21629_60FPS_1080p_1.0.xml) | About 59.8–59.9 FPS in short sky/jungle samples; engine dimensions 1920×1080 |
| [The Mortuary Assistant](patches/ps4/the-mortuary-assistant/README.md) | PS4, tested on PS5 | `CUSA43772` / `01.08` | [v1.0: 60 FPS target](patches/ps4/the-mortuary-assistant/CUSA43772_01.08_60FPS_1.0.xml) | Maintainer reported working, fairly stable gameplay; resolution unchanged |

These are limited observations, **not a promise of locked 60 FPS**. Other title IDs, game updates, PS4 hardware, firmware versions, and loaders have not been validated. See [catalog.json](catalog.json) for machine-readable compatibility and [SHA256SUMS](SHA256SUMS) for file integrity.

## Install with CheatRunner

1. Confirm the exact title ID and installed app version above. Do not apply to another build.
2. Close the game completely. Disable older or overlapping patches and remove their autoload entries.
3. Download the XML for your game. In GitHub's file view, use **Download raw file**; do not save the HTML page as XML.
4. Copy it to the appropriate console folder:
   - PS5 game: `/data/cheatrunner/patches/xml_prospero/`
   - PS4 game: `/data/cheatrunner/patches/xml/`
5. Rescan patches in CheatRunner, launch the game, and apply **only the matching patch**. Check the log for the expected write count: Green Hell **12**, Mortuary **7**.
6. If desired, save it as an autoload profile. Verify that it actually reapplies after restarting; copying an XML alone does not enable it.

Folder conventions follow [CheatRunner](https://github.com/notmaj0r/CheatRunner). Its installed version was not recorded during testing, and other patch loaders are not certified here. **ps5debug-NG and the research tools are not required to load these XML files.**

To remove a patch, close the game, disable its autoload entry, then restart the game without it. These files patch process memory; they do not intentionally edit installed game files or saves. That does not eliminate crash-related data risks.

## Transparency and development

- [Tools, exact recorded versions, and credits](docs/TOOLS.md)
- [How the patches were developed](docs/DEVELOPMENT.md)
- [Testing evidence, limitations, and crash history](docs/TESTING.md)
- [Changelog](CHANGELOG.md)

Check repository files offline with Python 3.10 or newer:

```sh
python tools/validate.py
```

This only checks XML, compatibility metadata, and checksums. It does not contact a console or demonstrate runtime safety.

For bug reports, include the title ID, app version, console/firmware, patch loader/version, and observed behavior. Do not upload game dumps, PKGs, credentials, or logs containing private network details.
