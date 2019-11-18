"""Computation of weighted average of squares."""

import argparse
import statistics
import math

def average_of_squares(list_of_numbers, list_of_weights=None):
    """
    Return the weighted average of a list of values.
    By default, all values are equally weighted, but this can be changed
    by the list_of_weights argument.

    Example:
    -------
    >>> average_of_squares([1, 2, 4])
    7.0
    >>> average_of_squares([2, 4], [1, 0.5])
    6.0
    >>> average_of_squares([1, 2, 4], [1, 0.5])
    Traceback (most recent call last):
    AssertionError: weights and numbers must have same length
    """
    if list_of_weights is not None:
        assert len(list_of_weights) == len(list_of_numbers), \
            "weights and numbers must have same length"
        effective_weights = list_of_weights
    else:
        effective_weights = [1] * len(list_of_numbers)
    squares = [
        weight * number * number
        for number, weight
        in zip(list_of_numbers, effective_weights)
    ]
    return sum(squares)


def convert_numbers(list_of_strings):
    """
    Convert a list of strings into numbers, ignoring whitespace.

    Example:
    -------
    >>> convert_numbers(["4", " 8 ", "15 16", " 23    42 "])
    [4, 8, 15, 16]
    """
    all_numbers = []
    for s in list_of_strings:
        # Take each string in the list, split it into substrings separated by
        # whitespace, and collect them into a single list...
        all_numbers.extend([token.strip() for token in s.split()])
    # ...then convert each substring into a number
    return [float(number_string) for number_string in all_numbers]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process weighted averages from two files")
    print("Do you want to use weights?")
    choice = input("> ")
    if choice == "Yes":
        parser.add_argument('numbers')
        parser.add_argument('weights')
        args = parser.parse_args()

        with open(args.numbers, "r") as numbers_file:
            numbers_strings = numbers_file.readlines()

        with open(args.weights, "r") as weights_file:
            weights_strings = weights_file.readlines()

        numbers = convert_numbers(numbers_strings)
        weights = convert_numbers(weights_strings)
        result = average_of_squares(numbers, weights)
        print(result)

        print("Do you also want to compute the square root?")
        choice2 = input("> ")
        if choice2 == "Yes":
            result2 = math.sqrt(result)
            print(result2)
        elif choice2 == "No":
            None 

        print("Do you want to save result in a file?")
        choice3 = input("> ")
        if choice3 == "Yes":
            f = open("result.txt", "w")
            f.write(str(result)) 
        # TODO Can we write the result in a file instead of printing it?
        
    elif choice == "No":
        parser.add_argument('numbers')
        parser.add_argument('weights')
        args = parser.parse_args()

        with open(args.numbers, "r") as numbers_file:
            numbers_strings = numbers_file.readlines()

        numbers = convert_numbers(numbers_strings)
        result = statistics.mean(numbers) 
        print(result)
