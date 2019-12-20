import re


def validate_string(raw_string, types='email'):

    if types == 'email':
        types_email = re.findall(r'^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$', raw_string)
        if types_email:
            print("{} cocok dengan {}".format(types, raw_string))
        else:
            print("{} tidak cocok dengan {}".format(types, raw_string))
    
    elif types == 'username':
        types_username = re.findall(r'^[a-zA-Z0-9]+(?:[_ -]?[a-zA-Z0-9])\w{3,14}$', raw_string)
        if types_username:
            print("{} cocok dengan {}".format(types, raw_string))
        else:
            print("{} tidak cocok dengan {}".format(types, raw_string))

    elif types == 'password':
        types_password = re.findall(r'^[a-zA-Z0-9]\w{3,14}$', raw_string)
        if types_password:
            print("{} cocok dengan {}".format(types, raw_string))
        else:
            print("{} tidak cocok dengan {}".format(types, raw_string))

    return


# email
validate_string('john@123doe.abc', 'email')
validate_string('john@doe.com', 'email')
print("\n")

# username
validate_string('th1s1sw*ayt00l0ngt', 'username')
validate_string('th1s123', 'username')
print("\n")

# password
validate_string('aBc45DSD_sdf', 'password')
validate_string('\tth1s1234', 'password')


url_string = 'https://www.youtube.com/watch?v=9U6meqmEsrY'

text = re.sub(r'((www\.[^\s]+)|(https?://[^\s]+))', 'terhapus', url_string)

print(text)
