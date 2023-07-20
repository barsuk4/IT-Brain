import re

texts = ["1928346", "123Д02349", "1234567890"]

for text in texts:
  if re.match(r"^[0-9]+$", text):
    print("Послідовність {} містить лише цифри.".format(text))
  else:
    print("Послідовність {} не містить лише цифри.".format(text))
