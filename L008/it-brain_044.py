import re

def is_valid_email(email):
    pattern = r"[a-z0-9_-]+(?:\.[a-z0-9_-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
    matches = re.match(pattern, email)
    if matches:
        return len(email) <= 254
    return False

# Приклади перевірки
emails = ["vlad@gmail.com", "alex_gord@ukr.net", "vlad!ushakov@gmail.com"]
for email in emails:
    if is_valid_email(email):
        print(f"{email} - валідний")
    else:
        print(f"{email} - не валідний")
