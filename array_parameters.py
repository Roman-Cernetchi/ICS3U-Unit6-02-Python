#!/usr/bin/env python3

# Created by: Roman Cernetchi
# Created on: January 2021
# This program prints 10 random integers and finds the average

import random


def main():
    # Generates 10 random numbers and finds average

    random_numbers = []

    addition = 0

    for loop_counter in range(0, 10):
        random_numbers.append(random.randint(1, 100))

        if loop_counter < 9:
            print(random_numbers[loop_counter], end=" ")
        else:
            print(random_numbers[loop_counter])

    for loop_counter in range(0, 10):
        addition = addition + random_numbers[loop_counter]

    average = addition / 10

    print("Average = {}".format(average))


if __name__ == "__main__":
    main()
