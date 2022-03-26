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
        

def from_base_10_to_n(base_n: int, remaining: int, numbers: list = [], last_exponent: int = None) -> list:

    if ((last_exponent == 0 and last_exponent) or remaining == 0):
        return ''.join(list(map(lambda x: '0' if x == None else str(x), numbers)))

    # hittar den största exponenten
    exponent = math.floor(math.log(remaining) / math.log(base_n))

    # hittar den största faktorn framför exponenten
    factor = math.floor(remaining / base_n**exponent)

    # Om numbers är tom tilldela den en lista med samma antal element som exponentens värde (index 0 kommer motsvara a**n, index 1: a**(n-1) osv)
    if (len(numbers) == 0):
        numbers = [None] * (exponent + 1)
        
    # lägger till faktorn i listan
    numbers[len(numbers) - exponent - 1] = num_to_char(factor)

    # beräknar resterande summa
    remaining -= factor * base_n**exponent

    if(exponent > 0):
        return from_base_10_to_n(base_n, remaining, numbers, exponent)
    else:
        return ''.join(list(map(lambda x: '0' if x == None else str(x), numbers)))

def from_base_n_to_base_10(base_n, number) -> list:
    # skapa en lista med varje siffra i numret
    nums = [char_to_num(x) for x in str(number)]

    sum = 0

    i = 0
    for num in nums:
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
