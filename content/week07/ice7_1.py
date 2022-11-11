def do_trick(a_list):
    a_list = a_list + a_list[1:3] + [a_list[3]]
    print(a_list)


my_list = ['a', 'b', 'c', 'd']
do_trick(my_list)
print(my_list)

# [a, b, c, d, b, c, d] -> a_list local variable
# [a, b, c, d] -> a_list global list in memory is not modified


def do_trick(a_list):
    a_list.append(a_list[1:3] + [a_list[3]])
    print(a_list)


my_list = ['a', 'b', 'c', 'd']
do_trick(my_list)
print(my_list)

# [a, b, c, d, [b, c, d]] -> + operation is completed prior to appending. appending modifies the list rather than reassigning it, a_list list global is modified
# [a, b, c, d, [b, c, d]]


my_str = '123'

for index in range(0, len(my_str)-1):
    n = int(my_str[index] + my_str[index+1])
    print(n)
    m = int(my_str[index:index+2])
    print(m)

# 12
# 12
# 23
# 23
