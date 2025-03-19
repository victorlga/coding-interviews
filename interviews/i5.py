def swap_odd_even_bits(x: int) -> int:
    even_mask = 0b10101010101010101010101010101010
    odd_mask = 0b01010101010101010101010101010101

    evens = x & even_mask
    odds = x & odd_mask

    evens >>= 1
    odds <<= 1

    return evens | odds