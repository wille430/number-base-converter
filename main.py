import math

alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]

def num_to_char(num):
    if (num <= 9):
        return num
    else:
        return alphabet[num-10]

def char_to_num(char):
    if (alphabet.count(char)):
        return alphabet.index(char) + 10
    else:
        # TODO: catch when char is not a number
        return int(char)
        
def from_base_10_to_n(base_n: int, remaining: int, numbers: list = [], fractions: list = []) -> list:

    # hittar den största exponenten som är mindre än resterande tal
    exponent = math.floor(math.log(remaining) / math.log(base_n))

    # hittar den största faktorn framför exponenten
    factor = math.floor(remaining / base_n**exponent)

    if (factor >= base_n):
        raise BaseException(f"Number is not in base {base_n}")

    # om exponenten är större än noll läggs faktorn till i listan med 
    if (exponent >= 0):
        # lägger till faktorn i listan
        numbers += [num_to_char(factor)]
    else:
        fractions += [num_to_char(factor)]

    # beräknar resterande summa
    remaining -= factor * base_n**exponent

    if(remaining > 0):
        return from_base_10_to_n(base_n, remaining, numbers, fractions)
    else:
        return ''.join(list(map(lambda x: str(x), numbers))) + '.' + ''.join(list(map(lambda x: str(x), fractions)))

def from_base_n_to_base_10(base_n, number) -> list:
    # skapa en lista med varje siffra i numret

    split_number = str(number).split('.')
    
    nums = [char_to_num(x) for x in split_number[0]]
    decimals = []

    if len(split_number) > 1:
        decimals = [char_to_num(x) for x in split_number[1]]

    sum = 0

    i = 0
    for num in (nums + decimals):

        if (num >= base_n):
            raise BaseException(f"Number is not in base {base_n}")

        exponent = (len(nums) - 1)-i
        sum += num * base_n**exponent

        i += 1

    return sum


def main():
    base_a = int(input('From base:'))
    number = input('Number to convert:')
    base_b = int(input('To base:'))

    num_base_10 = from_base_n_to_base_10(base_a, number)
    num_base_b = from_base_10_to_n(base_b, num_base_10) if base_b != 10 else num_base_10

    print("Result: ", num_base_b)


if __name__ == "__main__":
    main()
