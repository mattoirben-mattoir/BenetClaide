# Sound design for the Centre Auto Alonzo videos (no voice-over).
# Builds a music bed + synthesized sound effects placed on the animation's own
# event list (window.SFX in anim.html, exported by render.js), so every cue
# lands on the frame where the element moves.
# Usage: python3 sfx.py <events.json> <duration_s> <out.wav>
import json, sys
import numpy as np
import soundfile as sf
from scipy import signal

SR = 44100
rng = np.random.default_rng(7)


def t_(d):
    return np.arange(int(d * SR)) / SR


def env(n, a, d):
    t = np.arange(n) / SR
    return np.minimum(t / max(a, 1e-4), 1) * np.exp(-t / d)


def band(x, lo, hi, order=2):
    sos = signal.butter(order, [lo, hi], 'bandpass', fs=SR, output='sos')
    return signal.sosfilt(sos, x)


def lowp(x, f, order=2):
    return signal.sosfilt(signal.butter(order, f, 'lowpass', fs=SR, output='sos'), x)


def highp(x, f, order=2):
    return signal.sosfilt(signal.butter(order, f, 'highpass', fs=SR, output='sos'), x)


def norm(x, peak=1.0):
    return x / (np.abs(x).max() + 1e-9) * peak


# ---------------------------------------------------------------- effects
def whoosh(d=0.45, lo=300, hi=4000, peak=0.6):
    """Air sweep: noise bands that peak one after the other (up then down)."""
    n = int(d * SR); x = rng.standard_normal(n); out = np.zeros(n)
    centres = np.geomspace(lo, hi, 7); tt = np.linspace(0, 1, n)
    for i, c in enumerate(centres):
        pos = .25 + .5 * i / (len(centres) - 1)
        e = np.exp(-((tt - pos) / .22) ** 2)
        out += band(x, c / 1.4, min(c * 1.4, SR / 2 - 100)) * e
    out *= np.sin(np.pi * tt) ** 1.5
    return norm(out, peak)


def swoosh():
    return whoosh(.25, 900, 7000, .35)


def camera():
    return whoosh(.6, 120, 1800, .55)


def pop(pitch=1.0):
    d = .09; t = t_(d)
    f = (380 + 700 * np.exp(-t / .012)) * pitch
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * env(len(t), .001, .03)
    return s * .5


def tick():
    n = int(.03 * SR); x = highp(rng.standard_normal(n), 3000)
    return x * env(n, .0005, .004) * .25


def ding():
    """Success: two bright bell notes (E6, B6)."""
    out = np.zeros(int(.8 * SR))
    for k, (f, at) in enumerate([(1318.5, 0), (1975.5, .09)]):
        t = t_(.7); s = sum(a * np.sin(2 * np.pi * f * m * t) for m, a in [(1, 1), (2.76, .3), (5.4, .1)])
        s *= env(len(t), .002, .18 if k == 0 else .3)
        i = int(at * SR); out[i:i + len(s)] += s[:len(out) - i]
    return norm(out, .35)


def error():
    """Wrong: two short descending buzzes."""
    out = np.zeros(int(.38 * SR))
    for f, at in [(240, 0), (185, .16)]:
        t = t_(.14); s = signal.square(2 * np.pi * f * t) * .6 + np.sin(2 * np.pi * f * t)
        s = lowp(s, 1800) * env(len(t), .004, .08)
        i = int(at * SR); out[i:i + len(s)] += s
    return norm(out, .32)


def hiss():
    """Air pump: two short puffs."""
    out = np.zeros(int(.7 * SR))
    for at in (0, .3):
        n = int(.28 * SR); x = band(rng.standard_normal(n), 2500, 9000) * env(n, .03, .09)
        i = int(at * SR); out[i:i + n] += x
    return norm(out, .3)


def rattle(d=1.0):
    t = t_(d); x = lowp(rng.standard_normal(len(t)), 500)
    am = .5 + .5 * np.sign(np.sin(2 * np.pi * 28 * t))
    s = x * am + .4 * np.sin(2 * np.pi * 70 * t) * am
    s *= np.minimum(t / .05, 1) * np.minimum((d - t) / .2, 1)
    return norm(s, .35)


def roll(d=1.1):
    t = t_(d); x = lowp(np.cumsum(rng.standard_normal(len(t))), 400); x = highp(x, 40)
    x *= .6 + .4 * np.sin(2 * np.pi * 9 * t)
    x *= np.minimum(t / .08, 1) * np.exp(-np.maximum(t - .5, 0) / .25)
    return norm(x, .45)


def impact():
    t = t_(.8); f = 45 + 80 * np.exp(-t / .05)
    b = np.sin(2 * np.pi * np.cumsum(f) / SR) * env(len(t), .001, .25)
    n = lowp(rng.standard_normal(len(t)), 1500) * env(len(t), .001, .04)
    return norm(b + .5 * n, .7)


def riser(d=0.8):
    t = t_(d); f = 200 * (6 ** (t / d))
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * .3 + band(rng.standard_normal(len(t)), 1500, 8000) * .6
    return norm(s * (t / d) ** 2, .3)


def step(h=1.0):
    n = int(.09 * SR); x = lowp(rng.standard_normal(n), 380) * env(n, .002, .025)
    th = np.sin(2 * np.pi * 90 * t_(.09)) * env(n, .001, .03)
    return norm(x + th, .38 * h)


def stumble():
    out = np.zeros(int(.4 * SR)); s = step(1.2); out[:len(s)] += s
    n = int(.25 * SR); sc = band(rng.standard_normal(n), 900, 4000) * env(n, .02, .08) * .12
    i = int(.1 * SR); out[i:i + n] += sc
    return out


def snap():
    n = int(.05 * SR); x = band(rng.standard_normal(n), 1500, 6000) * env(n, .0005, .008)
    return norm(x, .4)


FX = {'whoosh': whoosh, 'swoosh': swoosh, 'camera': camera, 'pop': pop, 'tick': tick, 'ding': ding,
      'error': error, 'hiss': hiss, 'rattle': rattle, 'roll': roll, 'impact': impact, 'riser': riser,
      'step': step, 'stumble': stumble, 'snap': snap}
# where the "hit" of each effect sits inside its sample (so the hit lands on the event time)
HIT = {'whoosh': .2, 'swoosh': .12, 'camera': .3, 'riser': .8}
GAIN = {'tick': .8, 'pop': 1.0}


# ---------------------------------------------------------------- music bed
def music(dur, bpm=118):
    N = int(dur * SR); m = np.zeros(N); beat = 60 / bpm

    def add(sig, at, buf=m):
        i = int(at * SR)
        if 0 <= i < N:
            j = min(N, i + len(sig)); buf[i:j] += sig[:j - i]

    def kick():
        t = t_(.35); f = 48 + 95 * np.exp(-t / .035)
        return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(len(t), .001, .13)

    def hat(op=False):
        n = int((.12 if op else .045) * SR)
        return highp(rng.standard_normal(n), 7000) * env(n, .0005, .045 if op else .012) * .22

    def clap():
        n = int(.18 * SR); x = band(rng.standard_normal(n), 900, 5000)
        e = sum(env(n, .0005, .01) * (np.arange(n) >= int(k * .011 * SR)) for k in range(3)) + env(n, .001, .05)
        return x * e * .22

    def pluck(midi, d, amp):
        f = 440 * 2 ** ((midi - 69) / 12); t = t_(d)
        s = signal.sawtooth(2 * np.pi * f * t) + signal.sawtooth(2 * np.pi * f * 1.006 * t)
        return lowp(s, 2600) * amp * env(len(t), .004, d * .35)

    def bass(midi, d):
        f = 440 * 2 ** ((midi - 69) / 12); t = t_(d)
        s = np.sin(2 * np.pi * f * t) + .25 * np.sin(4 * np.pi * f * t)
        return s * .32 * np.minimum(t / .005, 1) * np.exp(-t / (d * .6))

    prog = [(57, [64, 69, 72]), (53, [65, 69, 72]), (48, [64, 67, 72]), (55, [62, 67, 71])]  # Am F C G
    end = dur - .9
    t, b = 0.0, 0
    while t < end:
        root, ch = prog[(b // 4) % 4]
        add(kick() * .85, t)
        add(hat(), t + beat / 2); add(hat(b % 4 == 3), t + beat * .75)
        if b % 2 == 1:
            add(clap(), t)
        add(bass(root - 24, beat * .48), t + beat / 2)
        if b % 2 == 0:
            for k, n in enumerate(ch):
                add(pluck(n, beat * .9, .045), t + k * .012)
        # small melodic hook every other bar
        if b % 8 in (2, 3):
            add(pluck(ch[-1] + 12, beat * .5, .03), t + beat * .5)
        t += beat; b += 1
    add(kick(), end); add(norm(lowp(rng.standard_normal(int(.5 * SR)), 3000) * env(int(.5 * SR), .001, .12), .2), end)
    for n in prog[0][1]:
        add(pluck(n + 12, 1.2, .05), end)
    m = norm(m, .9)
    # gentle fade-in / fade-out
    fi = int(.08 * SR); m[:fi] *= np.linspace(0, 1, fi)
    fo = int(.4 * SR); m[-fo:] *= np.linspace(1, 0, fo)
    return m


def main():
    events, dur, out = json.load(open(sys.argv[1])), float(sys.argv[2]), sys.argv[3]
    N = int(dur * SR)
    fx = np.zeros(N)
    for ev in events:
        at, kind = ev[0], ev[1]
        kw = ev[2] if len(ev) > 2 else {}
        s = FX[kind](**kw) * GAIN.get(kind, 1.0)
        i = int((at - HIT.get(kind, 0)) * SR)
        if i < 0:
            s = s[-i:]; i = 0
        j = min(N, i + len(s)); fx[i:j] += s[:j - i]
    mix = music(dur) * .55 + fx
    # stereo: a little width on the effects
    left, right = mix + .08 * np.roll(fx, 220), mix + .08 * np.roll(fx, -220)
    st = np.stack([left, right], 1)
    st = st / np.abs(st).max() * .95
    sf.write(out, st.astype(np.float32), SR)
    print('ok', len(events), 'events')


if __name__ == '__main__':
    main()
