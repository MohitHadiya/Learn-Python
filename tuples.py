# link = https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=false
n = int(input())
integer_list = map(int, input().split())
print(hash(tuple(integer_list)))
