#
# #    A  B  C  D  E  F  G  H  J
#     [0][1][0][1][0][0][1][0][0],
#     [1][0][1][1][1][0][0][0][0],
#     [0][1][0][0][0][1][0][0][0],
#     [1][1][0][0][1][0][0][1][0],
#     [0][1][0][1][0][1][0][1][0],
#     [0][0][1][0][1][0][0][0][1],
#     [1][0][0][0][0][0][0][1][0],
#     [0][0][0][1][1][0][1][0][1],
#     [0][0][0][0][0][1][0][1][0]

graph_map = [
    #    A  B  C  D  E  F  G  H  J
    [0, 1, 0, 1, 0, 0, 1, 0, 0],
    [1, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0],
    [1, 1, 0, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 1, 0]
]
# create array with 100 elements
array_a = [[None]* 8] * 8
def equation(n):
    return (5 * n + 3) % 8

def put_in_list(item, index):
        if array_a[index] is not None:
            array_a[index].append(item)
        else:
            array_a.insert(index, item)

array_list = [50, 27, 59, 1, 43, 52, 40, 63, 9, 56]

for i in array_list:
    print(equation(i))
    put_in_list(i, equation(i))

print(array_a)

for i in array_list:
    print(i, equation(i))

