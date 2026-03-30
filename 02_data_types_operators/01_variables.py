# immutable
from gc import garbage


age = 33
print(age)
print(age)

age = 30
print(age)

# ------------
#   0x0001      <---- a = 33
# ------------


# ------------
#   0x0002      <---- a = 30
# ------------
#   0x0001      // garbage collected
# ------------