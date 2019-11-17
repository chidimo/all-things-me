import argparse
from math import sqrt

parser = argparse.ArgumentParser(prog="Area of Triangle")
parser.add_argument("data_set", help="what triangle data are available? comes first in arg list",
                    choices = ["hero", "bh"])
parser.add_argument("-v", "--verbose", type=int, help="turn verbosity ON/OFF", choices=[0,1])
parser.add_argument("-sA", "--sideA", type=float, help="side A of triangle")
parser.add_argument("-sB", "--sideB", type=float, help="side B of triangle")
parser.add_argument("-sC", "--sideC", type=float, help="side C of triangle")
parser.add_argument("-b", "--base", type=float, help="base of triangle")
parser.add_argument("-he", "--height", type=float, help="height of triangle")
args = parser.parse_args()

if args.data_set=="hero":
    s = (args.sideA + args.sideB + args.sideC)/2
    area_hero = sqrt(s*(s-args.sideA)*(s-args.sideB)*(s-args.sideC))

    if args.verbose==1:
        print("for triangle of sides {:<6f}, {:<6f}, {:<6f}, ".format(args.sideA, args.sideB, args.sideC))
        print("the semi perimeter is {:<6f} while the area is {:<6f}".format(s, area_hero))
    else:
        print("area = {:<6f}".format(area_hero))

elif args.data_set=="bh":
    area_bh = (1/2)*args.base*args.height

    if args.verbose==1:
        print("for triangle of base {:<6f} and height {:<6f}".format(args.base, args.height))
        print("the area is {:<6f}".format(area_bh))
    else:
        print("area = {:<6f}".format(area_bh))
print('Done')
