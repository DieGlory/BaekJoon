import sys

sen = list(sys.stdin.readline().strip())
n = int(sys.stdin.readline().strip())

back = []
\
for _ in range(n):
    cmd = sys.stdin.readline().strip()
    if len(cmd) > 1:
        sen.append(cmd.split()[1])
    else:
        if cmd == "L":
            if sen:
                back.append(sen.pop())
        if cmd == "D":
            if back:
                sen.append(back.pop())
        if cmd == "B":
            if sen:
                sen.pop()
sen = sen + back[::-1]
print(*sen,sep='')