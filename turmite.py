rule="RLLR";cols=["#1a1410","#e3c14a","#d9573f","#7fae6a"]
N=100;g=[[0]*N for _ in range(N)];x=y=N//2;d=0
for s in range(60000):
    c=g[y][x];d=(d+(1 if rule[c]=="R" else -1))%4;g[y][x]=(c+1)%4
    dx,dy=[(0,-1),(1,0),(0,1),(-1,0)][d];x=(x+dx)%N;y=(y+dy)%N
r=''.join(f'<rect x="{i*4}" y="{j*4}" width="4" height="4" fill="{cols[g[j][i]]}"/>' for j in range(N) for i in range(N))
open('rllr.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400">{r}</svg>')
