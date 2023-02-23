import argparse
from typing import Tuple


def euclid(a: int, b: int, extended: bool = False) -> int | Tuple[int, int, int]:
    if not extended:
        return b if a % b == 0 else euclid(b, a % b)
    if a % b == 0:
        return b, 0, 1
    d, x, y = euclid(b % a, a, extended)

    x_ = y - (b // a) * x
    y_ = x
    return d, x_, y_


def main(a: int, b: int, extended: bool):
    print(euclid(max([a, b]), min([a, b]), extended=extended))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Perform Euclid's Algorithm.")
    parser.add_argument("--one", "-o", required=True, type=int,
                        help="First argument to Euclid's Algorithm.")
    parser.add_argument("--two", "-t", required=True, type=int,
                        help="Second argument to Euclid's Algorithm.")
    parser.add_argument('--extended', '-e', action='store_true', required=False, default=False,
                        help="Perform Euclid's Extended Algorithm.")

    args = parser.parse_args()
    main(args.one, args.two, args.extended)
