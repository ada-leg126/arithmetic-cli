import argparse


def main():
    parser = argparse.ArgumentParser(
        description="Perform basic arithmetic operations."
    )

    parser.add_argument(
        "-o",
        "--operation",
        choices=["add", "sub", "mul", "div"],
        required=True,
        help="Operation: add, sub, mul, or div.",
    )
    parser.add_argument("-n1", "--num1", type=float, required=True)
    parser.add_argument("-n2", "--num2", type=float, required=True)

    args = parser.parse_args()

    if args.operation == "add":
        result = args.num1 + args.num2
    elif args.operation == "sub":
        result = args.num1 - args.num2
    elif args.operation == "mul":
        result = args.num1 * args.num2
    elif args.operation == "div":
        if args.num2 == 0:
            parser.error("Cannot divide by zero.")
        result = args.num1 / args.num2

    print(result)


if __name__ == "__main__":
    main()
