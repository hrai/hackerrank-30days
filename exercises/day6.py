
num_strings = input()
arr = [input() for item in range(0, int(num_strings))]

for string in arr:
    odd = "".join([string[i] for i in range(0,len(string),2)])
    even = "".join([string[i] for i in range(1,len(string),2)])

    print(odd + " " + even)

