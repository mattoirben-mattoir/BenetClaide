# Voice-over (Kokoro TTS, French voice ff_siwis).
# Usage: python3 gen_tts.py <model_dir> <out_dir> <speed>
import sys, soundfile as sf, numpy as np
from kokoro_onnx import Kokoro
k = Kokoro(sys.argv[1] + "/kokoro-v1.0.onnx", sys.argv[1] + "/voices-v1.0.bin")
out, speed = sys.argv[2], float(sys.argv[3])
segs = [
    "Garde tes roues droites, garde le cap !",
    "C'est comme marcher : jambes droites, on avance facilement.",
    "Tordues, la démarche devient bancale !",
    "Pour vos roues, c'est pareil : la géométrie doit être juste.",
    "Un bon parallélisme, ce sont des pneus qui durent,",
    "une voiture stable,",
    "et du carburant économisé.",
    "Passez au Centre Auto Alonzo, et roulez droit en toute sécurité !",
]
for i, s in enumerate(segs):
    a, sr = k.create(s, voice="ff_siwis", speed=speed, lang="fr-fr")
    idx = np.where(np.abs(a) > 0.01)[0]
    a = a[max(idx[0] - 200, 0):idx[-1] + 800]
    sf.write(f"{out}/seg{i}.wav", a, sr)
    print(i, round(len(a) / sr, 2))
