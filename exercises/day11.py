#!/bin/python3


def calculate_sum(arr, i, j):
    first_row_sum = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
    second_row_sum = arr[i + 1][j + 1]
    third_row_sum = arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]

    return first_row_sum + second_row_sum + third_row_sum


def largest_sum(arr):
    sum_result = -1000

    for i in range(0, 4):
        for j in range(0, 4):
            current_sum = calculate_sum(arr, i, j)

            # print(current_sum)

            if current_sum > sum_result:
                sum_result = current_sum

    return sum_result
