# Tools and credits

These are development-session records, not recommended minimum versions or a promise that this setup works elsewhere. No third-party binaries or source distributions are bundled. Links identify upstream projects; their authors did not endorse or validate these patches.

## Test environment

| Component | Version recorded | Role / limits |
| --- | --- | --- |
| PlayStation 5 system software | 13.60 | Console used for the reported tests; PS4 Mortuary ran in backward compatibility |
| etaHEN | Not recorded | Homebrew/patch environment used during the work; no broader compatibility claim |
| kstuff / ShadowMount | Exact installed versions not recorded | Present in the console workflow; Mortuary PS4 was launched from an installed PKG |
| [CheatRunner](https://github.com/notmaj0r/CheatRunner) | Installed version not recorded | Applying XML patches and autoload profiles. A separately downloaded source snapshot identified itself as 0.17.1; this is **not evidence of the installed version** |
| PS5Upload | 5.41.0, from the session's screenshot | File browsing/transfers; an available update was not proof of an installed update |

## Analysis and verification

| Tool | Version recorded | Use |
| --- | --- | --- |
| [PS Neighborhood](https://github.com/GronedWaffel/ps-neighborhood) | 0.13.0 | Exports and local debugger client code |
| ps5debug-NG by OSR | 1.3.2; reported build `5d2c3bbc4bd42087` | Live process/known-address reads and writes. Console crashes occurred during live research; see TESTING.md |
| [Python](https://www.python.org/) | 3.13.11 | Local analysis and XML generation |
| [Node.js](https://nodejs.org/) | 22.20.0 | Direct local `.mjs` debugger helpers. PS Neighborhood's package declares Node >=24; this recorded helper runtime is not a supported-runtime recommendation for the full app |
| [Capstone](https://www.capstone-engine.org/) | 5.0.9 | x86-64 disassembly |
| [Unicorn](https://www.unicorn-engine.org/) | 2.1.4 | Offline instruction, stack, branch, and setter checks; not full-console emulation |
| [LibOrbisPkg / PkgTool](https://github.com/maxton/LibOrbisPkg) | 0.2.231.0 | PS4 update extraction for local analysis; game files excluded from this repository |
| `decrypt_fself.py`, bundled under Auto-Backpork in Lazy_AMPR | Bundle 0.0.1; standalone script version not recorded | Convert fake-signed executable containers to ELF for local inspection; script credits john-tornblom and Nazky. This was analysis, not an FPS-patch dependency |
| [UnityPy](https://github.com/K0lb3/UnityPy) | 1.25.4 | Asset inspection during the **excluded** Mortuary 4K experiment; not needed for either released XML |
| [OpenAI Codex](https://openai.com/codex/) | Exact model/build not recorded | AI assistance with analysis, scripting, patch generation, and documentation. Human console testing and feedback came from adnmix |

The inspected [shadPS4 VideoOut implementation](https://github.com/shadps4-emu/shadPS4/blob/main/src/core/libraries/videoout/video_out.cpp) helped identify the PS4 `sceVideoOutSetFlipRate` import. [Il2CppDumper metadata definitions](https://github.com/Perfare/Il2CppDumper/blob/master/Il2CppDumper/Il2Cpp/MetadataClass.cs) informed local analysis during the excluded 4K experiment. General presentation-patching research included [illusion's published work](https://illusion0001.com/legacy-website/patches/2021/07/01/QDR.Infraworld-Res-Letterbox-Patch/).

Git branches downloaded for reference were not pinned during the original session; no exact upstream commit is claimed. Do not infer a tested version from an upstream project's current release.
