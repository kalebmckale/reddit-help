"""
Python Lottery Program Help

I am very new to Python. I am trying to create a lottery game where both the winning numbers and my numbers are random. When checking my numbers against winning numbers it says there are x amount matching but it isn't accurate. I think I have to add a function to define the lotterynumbers but I am not sure how to do that. 
"""
import random

LOTTERY_CHOICES = range(1, 61)
NUM_CHOICES = 8

def choose_nums():
    return sorted(random.sample(LOTTERY_CHOICES, k=NUM_CHOICES))

def main(verbose=True):
    lottery_nums = choose_nums()
    my_nums = choose_nums()
    
    if verbose:
        print(f"Today's Lottery numbers are: {' '.join(map(str, lottery_nums))}")
        print(f"My numbers are: {' '.join(map(str, my_nums))}")
    
    if (num_correct := sum(num in lottery_nums for num in my_nums)) > 4:
        print("You win a prize!")
        print(f"You guessed {num_correct} number(s) correctly.")
        
    return num_correct