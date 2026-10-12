#!/bin/bash
# Builds one video: sound-effect events -> sound design -> frames + mux.
# Usage: video/build.sh <video_dir> <duration_s> <out.mp4>
set -e
R=$(dirname "$(readlink -f "$0")")
cd "$1"
export NODE_PATH=/opt/node22/lib/node_modules PAGE=anim.html
SFX_OUT=sfx-events.json node "$R/render.js" x x
python3 "$R/sfx.py" sfx-events.json "$2" audio.wav
DUR="$2" node "$R/render.js" audio.wav "$3"
