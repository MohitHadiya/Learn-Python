# link = https://www.hackerrank.com/challenges/finding-the-percentage/problem
n = int(input("Enter N : "))
student_marks = {}
for _ in range(n):
    name, *line = input("Enter Line : ").split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input("Enter Student Name : ")

marks = student_marks.get(query_name)
average_marks = sum(marks) / len(marks)
print(format(average_marks, ".2f"))
