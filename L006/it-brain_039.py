def count_words(sentence):
    words = sentence.split()
    return len(words)


sentence = "This is a sample sentence. We're test count_words function."
word_count = count_words(sentence)
print("Number of words:", word_count)
