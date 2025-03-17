def is_permutation_of_palindrome(phrase: str) -> bool:
    phrase = ''.join(char.lower() for char in phrase if char.isalpha())
    bit_array = 0

    for c in phrase:
        i = ord(c) - ord('a')

        # flips binary digit corresponging to char (0 -> 1 and 1 -> 0)
        bit_array ^= (1 << i) # bit_array XOR power of 2 binary corresponding to char

    return bit_array == 0 or (bit_array & (bit_array - 1)) == 0 # bit_array is 0 or power of 2