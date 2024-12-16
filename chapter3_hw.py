#3.1
names = ["gav","roger","leo"]
# print(names[0],'\n',names[1],'\n',names[2])
print(names[0])
print(names[1])
print(names[2])


#3.2
print(f"Hello, this is my friend {names[0]}")
print(f"Hello, this is my friend {names[1]}")
print(f"Hello, this is my friend {names[2]}")


#3.3
my_trasports = ["train","bicycle","viecle","walk","motorcycle"]
my_pre_trans = f"I would like to own a Honda {my_trasports[-1]}"
print(my_pre_trans)


#3.4
#嘉宾名单与邀请语句
dinner_guest = ["gav","roger","leo"]

print(f"Hey {dinner_guest[0]}, want to go out for dinner?")
print(f"Hey {dinner_guest[1]}, want to go out for dinner?")
print(f"Hey {dinner_guest[2]}, want to go out for dinner?")

print(f"{dinner_guest[2]} cannot join dinner")


#3.5
#删除无法参加的人员
del dinner_guest[-1]
# print(dinner_guest)


#3.6
#在列表末尾添加新人员
dinner_guest.append("andrew")
# print(dinner_guest)

print(f"Hey {dinner_guest[0]}, want to go out for dinner?")
print(f"Hey {dinner_guest[1]}, want to go out for dinner?")
print(f"Hey {dinner_guest[2]}, want to go out for dinner?")

print("I find a bigger dinner table")


#3.7
#添加新的三个人员
dinner_guest.insert(0,"lora")
print(dinner_guest)

dinner_guest.insert(2,"dixson")
print(dinner_guest)

dinner_guest.append("alex")
print(dinner_guest)

print(f"Hey {dinner_guest[0]}, want to go out for dinner?")
print(f"Hey {dinner_guest[1]}, want to go out for dinner?")
print(f"Hey {dinner_guest[2]}, want to go out for dinner?")
print(f"Hey {dinner_guest[3]}, want to go out for dinner?")
print(f"Hey {dinner_guest[4]}, want to go out for dinner?")
print(f"Hey {dinner_guest[5]}, want to go out for dinner?")


#3.8
print("the table is not big enough, so only 2 people can join")

out_people = dinner_guest.pop(2)
print(f"sorry {out_people}, we can meet another day")

out_people = dinner_guest.pop(3)
print(f"sorry {out_people}, we can meet another day")

out_people = dinner_guest.pop(0)
print(f"sorry {out_people}, we can meet another day")

out_people = dinner_guest.pop(2)
print(f"sorry {out_people}, we can meet another day")

# print(dinner_guest)

print(f"Hey {dinner_guest[0]}, want to go out for dinner?")
print(f"Hey {dinner_guest[1]}, want to go out for dinner?")


#3.9
num_people = len(dinner_guest)
print(num_people)

del dinner_guest[0]
del dinner_guest[0]
print(dinner_guest)

#-------------------------------------------------------------------------------
my_travel_plan = ["New zealand","Polnad","Iceland","Roma","France"]
print(my_travel_plan)

# print(sorted(my_travel_plan))
sorted_plan = sorted(my_travel_plan)
print(sorted_plan)

print(my_travel_plan)

sorted_reverse_plan = sorted(my_travel_plan,reverse=True)
print(sorted_reverse_plan)

print(my_travel_plan)

my_travel_plan.reverse()
print(my_travel_plan)

my_travel_plan.reverse()
print(my_travel_plan)

my_travel_plan.sort()
print(my_travel_plan)

my_travel_plan.sort(reverse=True)
print(my_travel_plan)

num_of_plan = len(my_travel_plan)
print(num_of_plan)

#3.10
my_list = ["World","Platinum","Lover","Fate","Sun"]
print(my_list)

#对中文字符进行字母顺序排序时可能会出错
# my_list = ["世界","白金","恋人","命运","太阳"]
# print(my_list)

num_list = len(my_list)
print(num_list)

my_list.sort()
print(my_list)

my_list.sort(reverse=True)
print(my_list)

my_list.reverse()
print(my_list)

my_list.reverse()
print(my_list)

sorted_list = sorted(my_list)
print(sorted_list)

sorted_list_rev = sorted(my_list,reverse=True)
print(sorted_list_rev)

my_list.append("Sky")
print(my_list)

my_list.insert(3,"Moon")
print(my_list)

del my_list[2]
print(my_list)

my_list.pop(0)
print(my_list)

my_list.remove("Sun")
print(my_list)

del my_list[0]
del my_list[0]
del my_list[0]
print(my_list)

print(my_list[-1])