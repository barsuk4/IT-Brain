import re

sentence = "Привіт, як справи? Сподіваюся, у Вас все добре. Hello, how are you?"

pattern = r"\b[А-ЯЄІЇҐA-Z][а-яєіїґa-z]*\b"
matches = re.findall(pattern, sentence)

print(matches)
