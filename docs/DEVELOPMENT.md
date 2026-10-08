# Development notes

Maintained and tested by **adnmix**, with **OpenAI Codex assistance**. The XML files have fixed offsets for the exact builds listed in the catalog. They do not discover compatible offsets on other game versions.

## Green Hell 1.0

The patch combines a Unity target of 60 FPS with a presentation interval of one refresh. It also forces native resolution requests to 1920×1080, prevents automatic restoration to 4K, and queues a resolution change from the native screen update if required. The engine performs its normal buffer recreation. The hook avoids repeating the request once the desired dimensions are active.

There are 12 writes in total, including code hooks and their small instruction stubs. Details and literal bytes are in the published XML. Early drafts were superseded and are not distributed.

## The Mortuary Assistant 1.0

Seven writes set and retain a Unity frame-rate target of 60, use one refresh for effective frame timing, force the native presentation interval setter and initialization to 1, and make the presentation path request `sceVideoOutSetFlipRate` argument 0. Resolution is unchanged.

The PS4 update was inspected as ELF, Unity internal-call names were mapped to functions, and the native presentation import and call sites were identified. Small live reads confirmed the matching executable and current timing values. Offline instruction emulation checked the candidate before applying it; live write readback and maintainer gameplay feedback followed.

## Reproducibility limits

This repository distributes the useful patch files, compatibility records, and an offline packaging validator. It is **not a complete reproducible reverse-engineering bundle**: original executables, proprietary metadata/assets, raw dumps, private logs, and development debugger scripts are excluded. Emulator checks model selected instructions, not the whole game or console.

Third-party tools retain their own authorship and licenses. AI assistance is disclosed rather than represented as wholly manual development. No claim is made that these are official patches or that anyone else's work or tools belong to the maintainer.
