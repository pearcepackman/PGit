import argparse
import sys

def main(): 
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest="command", required=True)

    main_parser = subparser.add_parser("main")
    main_parser.set_defaults(func=default)

    args = parser.parse_args()
    args.func()

def default():
    print("MEOW")