import sys
N = int(sys.stdin.readline().rstrip())
stack = []
for _ in range(N):
    temp = sys.stdin.readline().rstrip().split()
    cmd = temp[0]
    if cmd == 'push':
        stack.append(temp[1])
    elif cmd == 'pop':
        if (not stack):
            print(-1)
        else:
            print(stack.pop())
    elif cmd == 'size':
        print(len(stack))
    elif cmd == 'empty':
        if (not stack):
            print(1)
        else:
            print(0)
    elif cmd == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)


