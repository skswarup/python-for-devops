#check String is Palindrome or not?
def isPalindrome(text):
    if len(text)<2 : return True

    for i in range(0,int(len(text)/2)):
        if text[i] != text[len(text)-i-1]:
            return False
        
    return True
#Main
text=input("please provide your word: ")
text = text.lower()
result= isPalindrome(text)

if result:
    print(f"{text} is a Palindrome!")
else:
    print(f"{text} not a Palindrome!")


