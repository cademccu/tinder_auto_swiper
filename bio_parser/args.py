import argparse


parser = argparse.ArgumentParser()

parser.add_argument("-n", "--number_of_swipes", type=int, action="store_const", help="test")






args = parser.parse_args()


print(args)
