my_list = ["A","G","P","Z","M"]

# .append() 方法用于往列表的最后面添加内容
my_list.append("F")

print(my_list)

# .insert() 方法用于往列表的任意位置添加内容，整个列表会往右边移一格
my_list.insert(2,"O")

print(my_list)

# del 方法用于删除列表中指定位置的值，并且是永久删除
del my_list[-1]

print(my_list)

# .pop() 方法用于删除列表中指定位置的值，并且之后依旧可以访问它
missing_letter = my_list.pop(2)

print(f"{my_list}, the missing part is {missing_letter}")

another_missing = "A"

# .remove() 方法用于删除列表中的指定值，可以不指定位置
my_list.remove(another_missing)

print(f"{my_list}, the another missing part is {another_missing}")

my_list = ["B","A","P","Z","M"]

# .sort() 方法用按字母顺序排序列表，会永久影响列表
my_list.sort()

print(my_list)

my_list.sort(reverse=True)

print(my_list)

# sorted() 方法用按字母顺序排序列表，不会永久影响列表
print(sorted(my_list))

print(sorted(my_list,reverse=True))

print(my_list)

# .reverse() 方法可以反转列表的顺序
my_list.reverse()

print(my_list)

# len()方法可以提取列表的长度
print(len(my_list))