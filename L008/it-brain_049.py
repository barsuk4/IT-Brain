import re

text = "Мій поштовий індекс - 12345, а у нього 98765. Валідним будк 12000 Але немає 00000."

pattern = r"\b(?!00)[0-9]{5}\b"
matches = re.findall(pattern, text)

print(matches)
