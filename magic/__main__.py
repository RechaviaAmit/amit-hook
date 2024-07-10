# The hook must exit nonzero on failure or modify files.
# My choice is to edit the file

import argparse
import sys


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)
    for filename in args.filenames:
        with open(filename, 'r') as f:
            contents = f.read()
        if "hi" in contents:
            print("stop being so polite!")
            return 1
        with open(filename, 'w') as f:
            f.write(contents.replace('thanks', 'thanks May & Zohar for organizing this amazing meeting!'))
    return 0


if __name__ == "__main__":
    sys.exit(main())