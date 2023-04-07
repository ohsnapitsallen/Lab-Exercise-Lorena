# First is to ask the user for their desired string to encrypt
string = str(input("Enter your string here in LOWER CASE: "))
# Using the .replace method, we can easily replace a specific character from the user's string to any of our desired character
decrypted = string.replace('*', 'a').replace('&', 'e').replace('#', 'i').replace('+', 'o').replace('!', 'u')
print(decrypted)
