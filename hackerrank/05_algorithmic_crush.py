"""
Algorithmic crush from hackkerank
https://www.hackerrank.com/challenges/crush
"""

def increment_elements(some_list, integer_a, integer_b, integer_k):
    """Algorithmic crush"""
    for j in range(integer_a-1, integer_b):
        some_list[j] += integer_k
    return some_list

def main():
    """Main"""
    initial = input()
    parts = initial.split()
    big_n = int(parts[0])
    big_m = int(parts[1])
    zero_list = [0]*big_n

    for i in range(big_m):
        print(i)
        say_intput = input()
        operands = say_intput.split()
        integer_a = int(operands[0])
        integer_b = int(operands[1])
        integer_k = int(operands[2])
        zero_list = increment_elements(zero_list, integer_a, integer_b, integer_k)

    return max(zero_list)




def main2():
    """Main"""
    initial = input()
    parts = initial.split()
    big_n = int(parts[0])
    big_m = int(parts[1])
    zero_list = [0]*big_n

    for i in range(big_m):
        say_intput = input()
        operands = say_intput.split()
        integer_a = int(operands[0])
        integer_b = int(operands[1])
        integer_k = int(operands[2])

        func = lambda item: item + integer_k
        zero_list[integer_a-1:integer_b] = map(func, zero_list[integer_a-1:integer_b])
        # print('a: {}, b: {}, k: {}'.format(integer_a, integer_b, integer_k))
        # print(zero_list)
        return max(zero_list)
