import numpy as np, soundfile as sf
SR=24000; DUR=12.0; N=int(SR*DUR)
rng=np.random.default_rng(3)
def env(n, a=0.002, d=0.2):
    t=np.arange(n)/SR; return np.minimum(t/a,1)*np.exp(-t/d)
mus=np.zeros(N)
bpm=124; beat=60/bpm
def add(buf, sig, t):
    i=int(t*SR); j=min(N,i+len(sig)); 
    if i<N: buf[i:j]+=sig[:j-i]
# kick
def kick():
    n=int(.35*SR); t=np.arange(n)/SR
    f=50+90*np.exp(-t/0.04); ph=2*np.pi*np.cumsum(f)/SR
    return np.sin(ph)*np.exp(-t/0.12)
def hat(open_=False):
    n=int((.12 if open_ else .05)*SR); s=rng.standard_normal(n)
    s=np.diff(np.concatenate([[0],s]))  # highpass-ish
    return s*env(n,0.001,0.04 if open_ else 0.012)*0.25
def clap():
    n=int(.2*SR); s=rng.standard_normal(n); s=np.diff(np.concatenate([[0],s]))
    return s*env(n,0.001,0.06)*0.35
chords=[[45,57,60,64],[41,53,57,60],[48,55,60,64],[43,55,59,62]]  # Am F C G
def note(m, n, amp):
    f=440*2**((m-69)/12); t=np.arange(n)/SR
    s=np.sign(np.sin(2*np.pi*f*t))*0.3+np.sin(2*np.pi*f*t)*0.7
    s+=0.5*np.sin(2*np.pi*f*1.005*t)
    return s*amp*np.minimum(t/0.01,1)*np.exp(-t/0.5)
t=0.0; b=0
while t<DUR:
    if t<11.4:
        add(mus,kick()*0.9,t)
        add(mus,hat(),t+beat/2)
        if b%2==1: add(mus,clap(),t)
        add(mus,hat(),t+beat*0.75)
        ch=chords[(b//4)%4]
        bn=int(beat*0.45*SR)
        add(mus,note(ch[0]-12,bn,0.18),t+beat/2)
        if b%2==0:
            for m in ch[1:]: add(mus,note(m+12,int(beat*0.3*SR),0.035),t+beat*0.25)
    t+=beat; b+=1
# final hit
add(mus,kick()*1.0,11.4); 
# lowpass light smoothing
k=np.ones(3)/3; mus=np.convolve(mus,k,'same')
# whooshes at transitions
fx=np.zeros(N)
def whoosh(t0,d=0.35):
    n=int(d*SR); s=rng.standard_normal(n)
    # band sweep via moving avg of varying width -> approximate with filtered noise
    tt=np.linspace(0,1,n); e=np.sin(np.pi*tt)**2
    s=np.convolve(s,np.ones(6)/6,'same')
    add(fx,s*e*0.35,t0-d*0.5)
for tt in [2.2,4.3,6.5,9.25]: whoosh(tt)
# pop/ding at title punches
def pop(t0,f=880):
    n=int(.18*SR); tt=np.arange(n)/SR
    add(fx,np.sin(2*np.pi*f*tt*(1+0.5*np.exp(-tt/0.02)))*np.exp(-tt/0.05)*0.12,t0)
for tt in [0.35,2.4,4.5,6.7]: pop(tt)
pop(9.5,1320)
# voice
voice=np.zeros(N)
starts=[0.2,2.35,4.4,6.6,9.4]
for i,s in enumerate(starts):
    v,sr=sf.read(f"tts/seg{i}.wav"); assert sr==SR
    add(voice,v,s)
voice/=np.abs(voice).max()+1e-9
# duck music under voice
vel=np.convolve(np.abs(voice),np.ones(2400)/2400,'same'); duck=1-0.55*np.clip(vel/0.08,0,1)
duck=np.convolve(duck,np.ones(2400)/2400,'same')
mus/=np.abs(mus).max()
fade=np.ones(N); fi=int(0.15*SR); fade[:fi]=np.linspace(0,1,fi); fo=int(0.5*SR); fade[-fo:]=np.linspace(1,0,fo)
out=voice*0.9+mus*0.32*duck+fx
out*=fade
out/=np.abs(out).max()/0.95
sf.write("audio.wav",out.astype(np.float32),SR)
print("ok")
