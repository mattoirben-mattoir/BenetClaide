# Voice-over (Kokoro TTS, French voice ff_siwis). Brand names use phonetic spellings.
# Usage: python3 gen_tts.py <model_dir> <out_dir> <speed>
import sys, soundfile as sf, numpy as np
from kokoro_onnx import Kokoro
k = Kokoro(sys.argv[1] + "/kokoro-v1.0.onnx", sys.argv[1] + "/voices-v1.0.bin")
out, speed = sys.argv[2], float(sys.argv[3])
segs = [
    "À Mayotte, prenez la route comme un champion, avec Djoïe-rôde !",  # Joyroad
    "Pneus normaux : confort et contrôle.",
    "Renforcés : pour ceux qui n'ont pas de limites.",
    "Ol-terrain : l'aventure sous tous les angles.",                    # All-Terrain
    "Meud-terrain : tous les terrains, sans concession.",              # Mud-Terrain
    "Et aussi Fulda, Goudiyeur et Michelin !",                          # Goodyear
    "Centre Auto Alonzo, à Combani. Appelez-nous !",
]
for i, s in enumerate(segs):
    a, sr = k.create(s, voice="ff_siwis", speed=speed, lang="fr-fr")
    idx = np.where(np.abs(a) > 0.01)[0]
    a = a[max(idx[0] - 200, 0):idx[-1] + 800]
    sf.write(f"{out}/seg{i}.wav", a, sr)
    print(i, round(len(a) / sr, 2))
