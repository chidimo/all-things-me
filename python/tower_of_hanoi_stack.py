"""Stack implementation of the tower of hanoi algorithm"""

from pythonds.basic.stack import Stack

def make_tower(number_of_disk):
    """Make a tower of n discs"""
    pole = Stack()
    for i in range(number_of_disk, 0, -1):
        pole.push(i)
    return pole

def move_disk(from_pole, to_pole):
    """Move a disc from one tower to the next

    It modifies both poles in place.
    """
    if from_pole.isEmpty():
        return
    disc = from_pole.pop()
    # print("moving {} from {} to {}".format(disc, from_pole, to_pole))
    to_pole.push(disc)
