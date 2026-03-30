# igazságtábla

# A   B  A and B
# 0   0     0
# 0   1     0
# 1   0     0
# 1   1     1


# A   B  A or B
# 0   0     0
# 0   1     1
# 1   0     1
# 1   1     1

age = 30
young_age_threshold = 18
old_age_threshold = 65

if age < young_age_threshold:
    print("Kiskorú")
elif old_age_threshold > age >= young_age_threshold:
    # elif age >= 18 and age < 65:
    print("Felnőtt")
else:
    print("Nyugdíjas")


prog_language = "JavaScript"
script_languages = ["python", "javascript", "ruby", "php"]
# if prog_language == "Python" or prog_language == "JavaScript":
if prog_language.lower() in script_languages:
    print("script nyelv")


temperature = 50
humidity = 60
rain = True
# save magic values in variables to make the code more readable


# not rain         --> False
# humidity < 70    --> True
# False and True   --> False
# temperature > 30 --> True
# true or False    --> True
if temperature > 30 or humidity < 70 and not rain:
    print("Dry weather")

# temperature > 30 --> True
# humidity < 70    --> True
# True or True     --> True
# not rain         --> False
# True and False   --> False


if (temperature > 30 or humidity < 70) and not rain:
    print("Dry weather")
