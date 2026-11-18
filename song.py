from midiutil import MIDIFile
sc=[60,62,64,67,69,72,74,76,79]
rule="RLLR";N=60;g=[[0]*N for _ in range(N)];x=y=N//2;d=0
m=MIDIFile(1);m.addTempo(0,0,120);m.addProgramChange(0,0,0,12)
t=0
for s in range(160):
    c=g[y][x];d=(d+(1 if rule[c]=="R" else -1))%4;g[y][x]=(c+1)%4
    m.addNote(0,0,sc[(x+y*2+c*2)%9],t,0.25,70+d*8);t+=0.25
    dx,dy=[(0,-1),(1,0),(0,1),(-1,0)][d];x=(x+dx)%N;y=(y+dy)%N
m.writeFile(open('ant.mid','wb'))
