# LEDGER-Q bilingual animated guide

Animated explanation of actual saved synthetic case values. It is not live browser footage or a processing-speed benchmark. Scripts need Python 3, Pillow, edge-tts and ffmpeg. Narration uses verified Microsoft Edge Indian English and Hindi neural voices; public synthetic script text only is sent to that service. No user/company documents or credentials are used.

1. `python narrate.py` creates natural-paced speech takes and rejects takes over 14.9 seconds. Rewrite a long script rather than speeding the voice.
2. `python render.py ledger` builds eight 15-second 1920x1080/30fps explanatory scenes with directional cursor movement.
3. `python mux.py` creates two AAC/H.264 120-second MP4s, scene-aligned phrase captions, transcripts and technical verification receipts.

Scripts write to `../media`; final assets live in `public/videos`. Caption timing follows scene/phrase duration, not word-level forced alignment. The generated frame design reconstructs an explanatory workflow panel, not the exact rendered application UI. Cursor highlights evidence, not real server operations.

Native video controls remain visible. The language selector preserves viewing position; changing narration does not write to a workspace. No autoplay or new analytics were added.
