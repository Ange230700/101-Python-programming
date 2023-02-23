from collections import Counter


def modes(values):
    count = Counter(values)
    best = max(count.values())
    return [k for k, v in count.items() if v == best]


num_array = list()

num = input("Enter how many elements you want: ")

print('Enter numbers : ')
for i in range(int(num)):
    n = input("num"+str(i+1)+": ")
    num_array.append(int(n))

print("Arithmetic Mode : " + str(modes(num_array)))
