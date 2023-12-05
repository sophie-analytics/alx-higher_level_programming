#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    matrix_length = len(matrix)
    matrix_row = len(matrix[0])
    
    for number1 in range(matrix_length):
        for number2 in range(matrix_row):
           print("{:d}".format(matrix[number1][number2]), end="")
           if number2 < matrix_row - 1:
                print(" ", end="")
        print()
