def swap_case(string):
    updated_string = ''
    for word in string:
        if word.islower():
            updated_string += word.upper()
        else:
            updated_string += word.lower();
    return updated_string


string = input("Enter String : ")
result = swap_case(string)
print(result)
