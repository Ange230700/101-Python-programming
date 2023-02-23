def avg(data):
    if len(data) == 0:
        return 0
    else:
        return sum(data)/float(len(data))


num_array = list()
num = input("Enter how many elements you want: ")
print('Enter numbers : ')
for i in range(int(num)):
    n = input("num"+str(i+1)+": ")
    num_array.append(int(n))
print("Arithmetic Mean : "+str(avg(num_array)))
