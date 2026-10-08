# The Mortuary Assistant — 60 FPS target

| Item | Supported value |
| --- | --- |
| Game platform | PS4; tested in PS5 backward compatibility |
| Title ID | `CUSA43772` |
| App version | `01.08` |
| Patch version | `1.0` |
| Expected writes | 7 |
| Resolution | Unchanged |
| File | [CUSA43772_01.08_60FPS_1.0.xml](CUSA43772_01.08_60FPS_1.0.xml) |

Targets 60 FPS and changes the native presentation interval to one refresh. The maintainer reported working, fairly stable gameplay. No timed FPS benchmark was recorded.

Use `/data/cheatrunner/patches/xml/`. This is for the **PS4 build**, not the PS5 edition. Physical PS4 / PS4 Pro performance is unverified. See the root [installation steps](../../../README.md#install-with-cheatrunner) and [testing record](../../../docs/TESTING.md).

**Use at your own risk.** Console crashes occurred during related live-debugger research. The untested v1.1 / 4K experiment is excluded; v1.0 does not force native 4K.
