

def longest_ones(num):
    num_bin = str("{0:b}".format(num))
    longest_1s = 0

    count = 0
    for i in range(0, len(num_bin)):
        if int(num_bin[i]) == 1:
            count += 1

        if int(num_bin[i]) != 1:
            if count > 0 and count > longest_1s:
                longest_1s = count

            count = 0

    if count > 0 and count > longest_1s:
        longest_1s = count

    return longest_1s

# number = int(input())
# longest_ones(number)
