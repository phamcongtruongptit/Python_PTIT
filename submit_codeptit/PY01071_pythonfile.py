import re
s = input()
s = s.lower()

if s.endswith(".py") and len(s) >= 3  : print("yes")
else: print("no")