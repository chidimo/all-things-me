"""Maximum element

https://www.hackerrank.com/challenges/maximum-element
"""

from pythonds.basic.stack import Stack

fh = open('test.txt', 'r').readlines()

number_of_queries = fh[0].strip()
save_stack = Stack()
first_max = Stack()
second_max = Stack()
first_max.push(-1)
max_count = 1

for each in fh[1:]:
    inputs = each.strip().split()

    if inputs[0] == '1':
        to_push = int(inputs[1])
        save_stack.push(to_push)

        if to_push > first_max.peek():
            previous_max = first_max.pop()
            first_max.push(to_push)
            max_count = 1

        elif to_push == first_max.peek():
            max_count += 1

    elif inputs[0] == '2':
        removed = save_stack.pop()
        if removed == first_max.peek():
            max_count -= 1
        if max_count == 0:
            first_max.pop()
            first_max.push(previous_max)
    elif inputs[0] == '3':
        print(first_max.peek())
