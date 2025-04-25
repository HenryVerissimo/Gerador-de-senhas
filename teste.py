import string

senha = "16"


for digito in senha:
    if digito in string.digits:
        print(True)