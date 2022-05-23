# link = https://www.hackerrank.com/challenges/python-mutations/problem
def mutate_string(string, position, character):
    list_str = list(string)
    list_str[position] = character
    return "".join(list_str)


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
