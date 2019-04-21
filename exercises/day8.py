# Enter your code here. Read input from STDIN. Print output to STDOUT
entries = input()
phone_book = {}

for index in range(0, int(entries)):
    data = input()
    data_arr = data.split()
    phone_book[data_arr[0]] = data_arr[1]

while True:
    try:
        data = input()
        if data in phone_book:
            print("{}={}".format(data, phone_book[data]))
        else:
            print("Not found")
    except EOFError:
        break

