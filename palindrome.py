def palindrome():
    word= "madam"
    if word == word[::-1]:
        print ("The word is a palindrome")
    else:
        print ("The word is not a palindrome")
print(palindrome())