import hashlib

#we ask the user for the code 
password = input("give the password to encode: ")

# we code the password to utf-8
passcode=password.encode('utf-8')

#now we hash the password to md5
hashcode= hashlib.md5(passcode)

#print it and get the hex format of the original hash
print("\n The hash password is :" ,hashcode.hexdigest())
