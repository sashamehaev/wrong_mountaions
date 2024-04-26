import sys
from array import array


def main():
    def find_right_mountain(mountains):
        mountains_array = array('b', mountains)
        if len(mountains_array) < 3:
            return False

        mountain_max_height_index = 0
        uphill_climb = False
        downhill_climb = False
        for index in range(len(mountains_array) - 1):
            if mountains_array[index] < mountains_array[index + 1]:
                mountain_max_height_index = index + 1

        for index in range(mountain_max_height_index):
            if mountains_array[index] >= mountains_array[index + 1]:
                return False
            else:
                uphill_climb = True

        for index in range(mountain_max_height_index,
                           len(mountains_array) - 1):
            if mountains_array[index] <= mountains_array[index + 1]:
                return False
            else:
                downhill_climb = True

        if uphill_climb and downhill_climb:
            return True
        else:
            return False

    mountains = sys.stdin.readline().rstrip().split()
    mountains = [int(item) for item in mountains]
    print(find_right_mountain(mountains))


if __name__ == '__main__':
    main()
