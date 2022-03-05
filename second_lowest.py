marksheet = []
for _ in range(0,int(input())):
    marksheet.append([input(), float(input())])

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))

# students = []
# for i in range(int(input())):
#     tmp_stu = []
#     name = input()
#     score = float(input())
#     tmp_stu.append(name)
#     tmp_stu.append(score)
#     students.append(tmp_stu)
# lst = []
# for student in students:
#     lst.append(student[1])
# min_no = min(lst)
# while min(lst) == min_no:
#     lst.remove(min_no)
# second_min = min(lst)
# a = []
# for student in students:
#     if student[1] == second_min:
#         a.append(student[0])
# a.sort()
# for b in a:
#     print(b)
