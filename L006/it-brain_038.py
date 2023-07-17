def concatenate_strings(*args):
    concatenated_string = ''.join(args)
    return concatenated_string

a = ["Hello", " ", "world", "!", " ", "How", " ", "are", " ", "you?"]
# result = concatenate_strings("Hello", " ", "world", "!", " ", "How", " ", "are", " ", "you?")
result = concatenate_strings(*a)
print(result)
