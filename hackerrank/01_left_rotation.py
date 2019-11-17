"""Left Rotation"""

def left_rotation():
    inputs = input().split()
    # number_of_integers = int(inputs[0])
    number_of_left_rotations = int(inputs[1])
    input_array = input()
    array_list = [x for x in input_array.split()]

    while number_of_left_rotations > 0:
        array_list.append(array_list.pop(0))
        number_of_left_rotations -= 1
    print(' '.join(array_list))
