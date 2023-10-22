def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])

# Testing the function
english = "hello"
ukrainian = "привіт"

print(reverse_string(english))  # should print "olleh"
print(reverse_string(ukrainian))  # should print "тівирп"
