#Count each Words occurance frequency

def occurance(UserText):
    freq_count = dict()
    words= UserText.split()
    for text in words:
        if text in freq_count:
            freq_count[text] += 1 
        else: freq_count[text]=1

    return freq_count

UserText= input("Enter your Sentence: ")
print(occurance(UserText))


