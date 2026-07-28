# Logical operators: and, or, not

print("True and False  =", True and False)   # both must be True
print("True or False   =", True or False)    # at least one True
print("not True        =", not True)         # reverses the value
print("not False       =", not False)

print("True and not False =", True and not False)
print("False or not True  =", False or not True)

# Combining with parentheses (order of evaluation)
print("(True and False) or (not True)  =", (True and False) or (not True))
print("(True or False) and (not False) =", (True or False) and (not False))
print("(not True) or (not False)       =", (not True) or (not False))
