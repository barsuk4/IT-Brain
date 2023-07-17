def capitalize_first_letters(sentence):
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    new_sentence = ' '.join(capitalized_words)
    return new_sentence

sentence = "hello world! this is a test. Ну що, як вам робота?"
new_sentence = capitalize_first_letters(sentence)
print("Похідний рядок: ", sentence)
print("Капіталізований рядок: ",new_sentence)
