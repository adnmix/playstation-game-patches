# Testing and known limits

Recorded on 7–8 October 2026. The maintainer tested on PS5 firmware 13.60. No large test matrix, extended playthrough, independent certification, or guarantee of crash-free operation exists.

## Green Hell — PPSA21629 / 01.004.000 / patch 1.0

- The final XML contains 12 writes. The local record states that all 12 matched the running process.
- Real engine screen dimensions were read as 1920×1080.
- Short samples of roughly five seconds measured approximately 59.8 FPS looking at the sky and 59.9 FPS looking at the jungle. The maintainer also reported 59 FPS.
- Instruction emulation checked presentation arguments, forced setters, and stack/prologue behavior.
- An early 10-write draft did not request 1080p automatically after restart. The released 12-write version adds a native screen-update hook to request it without a separate manual memory operation. This correction was tested in a relaunched process.
- Automatic loading of the final corrected XML on a subsequent fresh launch was not conclusively recorded. Verify your autoload setup yourself.

This supports the observed scenes and session only. It does not establish a locked 60 FPS across all scenes, saves, hardware, or loader configurations.

## The Mortuary Assistant — CUSA43772 / 01.08 / patch 1.0

- The PS4 update was extracted locally; executable bytes were checked against the running game before writing.
- Before patching, the Unity target was 30 and the native presentation interval was 2.
- All seven patch writes were applied and read back successfully.
- Offline emulation checked forced setters, presentation rate arguments, initialization, and stack preservation.
- The maintainer's feedback was: “works great. pretty stable.” No timed FPS benchmark or full playthrough was captured.
- A later, separate inspection after reopening found the 60 FPS target and interval 1 active. This does not certify all autoload timing cases.
- Version 1.0 does not patch resolution. A later inspection reported a 3840×2160 screen/output, dynamic scale factors of 1, and an 80% scale in the serialized PS4 URP preset. **Screen/output dimensions alone do not prove native 4K scene rendering.** Actual scene render-target dimensions were not independently captured.

The PS4 version was tested on PS5 only. Physical PS4 / PS4 Pro operation is unverified. The PS5 edition of Mortuary is not supported by this release.

## Console crash history and excluded v1.1

Two console crashes were reported during Mortuary live-debugger research: one during the earlier PS5-edition investigation, and another during checks for a PS4 4K experiment. The exact cause was not isolated; the timing implicates live debugger operations but does not prove a particular payload or API caused them.

The second crash happened before any v1.1 writes were applied. A candidate v1.1 XML had passed limited offline instruction checks, but **it was never applied or validated on console**. It is deliberately absent from this repository and its release downloads. Offline checks did not justify calling it safe.

No further console access was performed to prepare this repository. Raw debugger helpers, memory dumps, game files, and the experimental XML are not distributed.

## What repository validation does

The offline validator checks file hashes, XML metadata, title IDs, app/patch versions, author credit, write counts, hex encoding, and overlapping write ranges. Passing these checks proves only packaging consistency. It cannot establish correct offsets on another build, kernel safety, game performance, or save integrity.
