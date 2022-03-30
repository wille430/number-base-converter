import math
import warnings

alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]

# returnerar en bokstav eller siffra, där a motsvarar 10 och b 11 osv.
def num_to_char(num):
    if (num <= 9):
        return num
    else:
        return alphabet[num-10]

# samma som num_to_char men tvärtom
def char_to_num(char):
    if (alphabet.count(char)):
        return alphabet.index(char) + 10
    else:
        # TODO: catch when char is not a number
        return int(char)

def join_array(array: list):
    return ''.join(list(map(lambda x: str(x), array)))

def base_n_to_10(base_n: int, number: float):

    split_number = str(number).split('.')

    # siffrorna före decimalen
    int_part = split_number[0]
    # siffrorna efter
    frac_part = ""

    if (len(split_number) > 1):
        frac_part = split_number[1]

    is_neg_factor = 1
    if (int_part.count('-') % 2 != 0):
        is_neg_factor = -1
        
        # ta bort '-'
        int_part = int_part.replace('-', '', -1)


    sum = 0
    i = len(int_part)-1

    # adderar ex 2*2^3
    for num in (int_part+frac_part):
        print(num)
        sum += char_to_num(num)*(base_n**i)
        i -= 1

    return is_neg_factor * sum

def base_10_to_m(base_m: int, remaining: int, int_part = [], frac_part = [], is_negative = False, last_exponent: None or int = None):

    # kollar om talet är negativt
    if (remaining < 0):
        remaining *= -1
        is_negative = True

    exponent = last_exponent

    # om det är första iterationen:
    if last_exponent is None:
        if remaining > 0:
            exponent = math.floor(math.log(remaining) / math.log(base_m))
        else:
            exponent = 0
    else:
        exponent -= 1

    # htitar största möjliga faktor till termen
    factor = math.floor(remaining / (base_m ** exponent))

    # ett tal i bas m kan inte a en siffra som är större eller lika med m
    if (factor >= base_m):
        warnings.warn(f"Found a number which is greater than the base. Input number might not be in base {base_m}.")

    # om exponenten >= 0 är siffran en del av siffrorna framför decimaltecknet
    if (exponent >= 0):
        int_part += [num_to_char(factor)]
    else:
        frac_part += [num_to_char(factor)]

    # resterande summa
    remaining -= factor * (base_m ** exponent)

    print(factor, base_m, exponent)

    if (remaining > 0 or exponent > 0):
        return base_10_to_m(base_m, remaining, int_part, frac_part, is_negative, exponent)
    else:
        array_to_join = []

        if is_negative:
            array_to_join += ['-']
        
        array_to_join += int_part

        if len(frac_part):
            array_to_join += ['.']+frac_part

        return join_array(array_to_join)
    
def main():
    input_number = input("Enter a number:") # kommer vara string
    base_n = int(input("from base:"))
    base_m = int(input("to base:"))

    num_base_10 = base_n_to_10(base_n, input_number)
    num_base_m = base_10_to_m(base_m, num_base_10)

    print("Result number:", num_base_m)

if __name__ == '__main__':
    main()