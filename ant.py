N=120;g=[[0]*N for _ in range(N)];x=y=N//2;d=0
for s in range(11000):
    if g[y][x]==0:d=(d+1)%4;g[y][x]=1
    else:d=(d-1)%4;g[y][x]=0
    dx,dy=[(0,-1),(1,0),(0,1),(-1,0)][d];x=(x+dx)%N;y=(y+dy)%N
r=''.join(f'<rect x="{i*4}" y="{j*4}" width="4" height="4" fill="#e3c14a"/>' for j in range(N) for i in range(N) if g[j][i])
open('ant.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 480"><rect width="480" height="480" fill="#1a1410"/>{r}</svg>')
