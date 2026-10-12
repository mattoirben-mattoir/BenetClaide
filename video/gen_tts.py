import sys, soundfile as sf, numpy as np
from kokoro_onnx import Kokoro
k = Kokoro(sys.argv[1]+"/kokoro-v1.0.onnx", sys.argv[1]+"/voices-v1.0.bin")
speed=float(sys.argv[2])
segs = [
 "Trois conseils pour faire durer vos pneus !",
 "Un : vérifiez la pression chaque mois.",
 "Deux : surveillez l'usure et les vibrations.",
 "Trois : faites vérifier équilibrage et parallélisme.",
 "Besoin d'un tchèk-eup ? Centre Auto Alonzo !",  # « check-up » en graphie phonétique
]
for i,s in enumerate(segs):
    a, sr = k.create(s, voice="ff_siwis", speed=speed, lang="fr-fr")
    # trim silence
    idx = np.where(np.abs(a) > 0.01)[0]
    a = a[max(idx[0]-200,0):idx[-1]+800]
    sf.write(f"{sys.argv[1]}/seg{i}.wav", a, sr)
    print(i, round(len(a)/sr,2))
