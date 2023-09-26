from collections import deque

t = int(input())

for _ in range(t):
    left_stack = deque()
    right_stack = deque()
    data = input()

    for char in data:
        if char == '<':
            if left_stack:
                right_stack.appendleft(left_stack.pop())
        elif char == '>':
            if right_stack:
                left_stack.append(right_stack.popleft())
        elif char == '-':
            if left_stack:
                left_stack.pop()
        else:
            left_stack.append(char)

    left_stack.extend(right_stack)
    print(''.join(left_stack))
