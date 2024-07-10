# The hook must exit nonzero on failure or modify files.

import argparse
import sys


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)
    for filename in args.filenames:
        with open(filename, 'r') as f:
            contents = f.read()
        if "thank you" in contents:
            print("stop being so polite!")
            sys.exit(1)
        with open(filename, 'w') as f:
            f.write(contents.replace('thanks', 'thanks May & Zohar for organizing this amazing meeting!'))
    sys.exit(0)


if __name__ == "__main__":
    main()