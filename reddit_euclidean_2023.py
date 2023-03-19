"""
The remainder of (69 * 420 * 69420 * 1678151232229625532) / 12345678910987654321 is 2023
"""
########################################################################################

import functools
import operator as op
import random

########################################################################################

modulus = 12_345_678_910_987_654_321
remainder = 2023
factors = [69, 420, 69_420]

secret_unknown = 1_678_151_232_229_625_532

########################################################################################

prod = functools.partial(functools.reduce, op.mul)

def test_prod(verbose=False):
    num_factors = random.randint(2, 10)
    factors = [random.randint(1, 10) for _ in range(num_factors)]
    product = factors[0]
    for factor in factors[1:]:
        product *= factor
    if verbose:
        print(f"{' * '.join(str(factor) for factor in factors)} = {product}")
    assert product == prod(factors)

def create_year_expression(modulus=12_345_678_910_987_654_321, factors=(69, 420, 69_420), year=2023):
    remainder = year
    unknown = (remainder * pow(prod(factors), modulus - 2, modulus)) % modulus
    print(
        f"The remainder of ({' * '.join(f'{factor:_}' for factor in [*factors, unknown])}) "
        f"/ {modulus:_} is {remainder}."
    )
    
########################################################################################

# x = remainder * prod(factors)**(modulus - 2) % modulus
