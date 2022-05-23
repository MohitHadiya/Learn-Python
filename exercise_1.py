# link: https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/2_Arrays/2_arrays_exercise.md

expenses = [2200, 2350, 2600, 2130, 2190]

print(expenses)
print("dollars you spent extra compare to January is ", expenses[1] - expenses[0])
print("your total expense in first quarter is ",expenses[0] + expenses[1] + expenses[2])
expenses.append(1980)
print(expenses)
expenses[3] = expenses[3] - 200