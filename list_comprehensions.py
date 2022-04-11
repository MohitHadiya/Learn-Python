# link = https://www.hackerrank.com/challenges/list-comprehensions/problem
x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))
n = int(input("Enter n: "))
ans = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if(i+j+k) != n]
print(ans)
