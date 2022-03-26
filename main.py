

from asyncio.windows_events import NULL
import math
import numbers


def number_in_array_of_base_n(base_n: int, remaining: int, numbers: list = [], last_exponent: int = NULL) -> list:
    exponent = math.floor(math.log(remaining) / math.log(base_n))

    factor = math.floor(remaining / base_n**exponent)
    numbers.append(factor)

    for x in range(1, (exponent-last_exponent)-2):
        if (x == 1):
            continue
        numbers.append(0)

    remaining -= factor * base_n**exponent

    print("Factor", factor, f" of {base_n}^{exponent}")
    print("Remaining:", remaining)

    if (remaining == 0):
        for x in range(0, exponent):
            numbers.append(0)

    if(remaining > 0 and exponent > 0):
        return number_in_array_of_base_n(base_n, remaining, numbers, exponent)
    else:
        return numbers


def base_10_to_base_n(base_n: int, number: int):
    # hittar n i ekvationen: base_n^n >= log number
    print(f"Input: {number}")
    print(f"Base: 10")

    if (base_n > 10):
        raise 'Maximum supported base is 10'

    number_in_base_n = ''.join(str(x) for x in number_in_array_of_base_n(base_n, number))

    print(f"Output: {number_in_base_n}")
    print(f"Base: {base_n}")


def main():
    base = int(input('Base:'))
    number = int(input('Number:'))
    base_10_to_base_n(base, number)


if __name__ == "__main__":
    main()
