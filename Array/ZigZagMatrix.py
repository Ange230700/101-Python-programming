def zigzag(n):
    indexorder = sorted(((x, y) for x in range(n) for y in range(n)), key=lambda (x, y): (x+y, -y if (x+y) % 2 else y))
    return {index: n for n, index in enumerate(indexorder)}


def printzz(myarray):
    n = int(len(myarray) ** 0.5 + 0.5)
    for x in range(n):
        for y in range(n):
            print("%2i" % myarray[(x, y)]),
        print


number = int(input("Enter number : "))
print("Zig-Zag Matrix : ")
printzz(zigzag(number))
