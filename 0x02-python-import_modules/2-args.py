#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) - 1 == 1:
        print("{} argument:".format(len(sys.argv) - 1))
        print("{}: {}".format(1, sys.argv[1]))
    elif len(sys.argv) - 1 == 0:
        print("0 arguments.")
    else:
        print("{} argurments:".format(len(sys.argv) - 1))
    for i in range(len(sys.argv) - 1):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
