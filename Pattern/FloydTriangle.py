def floyd(rowcount):
    rows = [[1]]
    while len(rows) < rowcount:
        n = rows[-1][-1] + 1
        rows.append(list(range(n, n + len(rows[-1]) + 1)))
    return rows


def pfloyd(rows):
    colspace = [len(str(n)) for n in rows[-1]]
    for row in rows:
        print(' '.join('%*i' % space_n for space_n in zip(colspace, row)))


input = int(input("Enter the number of rows of floyd's triangle : "))
pfloyd(floyd(input))
