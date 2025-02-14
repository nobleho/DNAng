#!/usr/bin/env python3
import argparse
from dnagen import dnagen
from __init__ import __version__, __credits__, __copyright__
import sys
from platform import system as osname

def main():
    # ArgParse
    parser = argparse.ArgumentParser(
        prog="dnaserv", description="DNA Next Gen serv.")

    # Args
    parser.add_argument("-i", "--input", help="Input schema file")
    parser.add_argument("-f", "--file", nargs="?",
                        type=argparse.FileType("r"), help="library file")
    parser.add_argument("-o", "--output", nargs="?",
                        type=argparse.FileType("w"), help="Output file")
    parser.add_argument("-I", "--stdin", action="store_true",
                        help="Standard input")
    parser.add_argument("-d", "--decode", action="store_true",
                        help="Decode sentence")
    parser.add_argument("-e", "--encode", action="store_true",
                        help="Encode sentences.")
    parser.add_argument("-C", "--convert", action="store_true",
                        help="Convert Raw to Codec value")
    parser.add_argument("-G", "--generate",
                        action="store_true", help="Generate source")
    parser.add_argument("-hp", "--helper",
                        action="store_true", help="Helper")
    parser.add_argument("-v", "--version",
                        action="store_true", help="Version")
    args = parser.parse_args()

    def outputHandeler(dnagenfn):
        if args.output:
            output = dnagenfn
            print(output)
            args.output.write(output)
        else:
            output = dnagenfn
            print(output)

    # Start main If statement
    if args.version:  # Print Version
        outputHandeler(
            f"""DNAng-cli {__version__} ({osname()}) DNAngcode {__version__}\nRelease Date: Fer 14, 2025\ncredits: {", ".join(__credits__)}\n{__copyright__}""")
        exit(0)

    elif args.helper:
        outputHandeler(dnagen.helper())
        exit(0)
    # Check for input
    elif args.input:
        # if other input methods then exit(1)
        if args.stdin or args.file:
            print(
                "Can't process other input methods with with \"input option\" at the same time.\n")
            exit(1)

        # Set input variable
        input = args.input

        if args.decode:
            if args.encode or args.generate or args.convert:
                print(
                    "Can't process \"encode or generate or convert\" with \"decode option\" at the same time!\n")
                parser.print_help()
                exit(1)
            outputHandeler(dnagen.decode(input))
            exit(0)

        elif args.encode:
            if args.convert or args.generate:
                print(
                    "Can't process \"convert or generate\" with \"decode option\" at the same time!\n")
                parser.print_help()
                exit(1)
            outputHandeler(dnagen.encode(input))
            exit(0)

        elif args.convert:
            if args.generate:
                print(
                    "Can't process \"generate option\" with \"convert option\" at the same time!\n")
                parser.print_help()
                exit(1)
            outputHandeler(dnagen.dnagenConvert(str(input)))
            exit(0)

        elif args.generate:
            outputHandeler(dnagen.gendnagent(input))
            exit(0)

        else:
            parser.print_help()
            exit(1)

    elif args.file:

        if args.stdin:
            print("Can't process \"stdin\" with \"file option\" at the same time.\n")
            parser.print_help()
            exit(1)

        input = str(args.file.readline())

        if args.decode:
            if args.encode or args.generate or args.convert:
                print(
                    "Can't process \"encode or generate or convert\" with \"decode option\" at the same time!\n")
                parser.print_help()
                exit(1)
            outputHandeler(dnagen.decode(input))
            exit(0)

        elif args.encode:
            if args.convert or args.generate:
                print(
                    "Can't process \"convert or generate\" with \"decode option\" at the same time!\n")
                parser.print_help()
                exit(1)
            outputHandeler(dnagen.encode(input))
            exit(0)

        elif args.convert:
            if args.generate:
                print(
                    "Can't process \"generate option\" with \"convert option\" at the same time!\n")
                parser.print_help()
                exit(1)
            outputHandeler(dnagen.dnagenConvert(str(input)))
            exit(0)

        elif args.generate:
            outputHandeler(dnagen.gendnagent(input))
            exit(0)

        else:
            parser.print_help()
            exit(1)
    elif args.stdin:
        # sys.stdin is a list so we join them together
        input = "".join(sys.stdin.readlines())

        if args.decode:
            if args.encode or args.generate or args.convert:
                print(
                    "Can't process \"encode or generate or convert\" with \"decode option\" at the same time!\n")
                parser.print_help()
                exit(1)
            outputHandeler(dnagen.decode(input))
            exit(0)

        elif args.encode:
            if args.convert or args.generate:
                print(
                    "Can't process \"convert or generate\" with \"decode option\" at the same time!\n")
                parser.print_help()
                exit(1)
            outputHandeler(dnagen.encode(input))
            exit(0)

        elif args.convert:
            if args.generate:
                print(
                    "Can't process \"generate option\" with \"convert option\" at the same time!\n")
                parser.print_help()
                exit(1)
            outputHandeler(dnagen.dnagenConvert(str(input)))
            exit(0)

        elif args.generate:
            outputHandeler(dnagen.gendnagent(input))
            exit(0)
    parser.print_help()
    exit(1)


if __name__ == "__main__":
    main()