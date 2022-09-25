# %% [markdown]
# # EX 1.1- basic python: Pyramid case
# Implement a function that get a string input and outputs the same word, only each odd char is lower
# case and each even letter is upper case
# You can assume that the input is a valid string which contains only english letters.
# %%

""" 
def pyramid_case_clara(in_word):
    final = []
    newl = []
    for i in range(len(in_word)):
        lst= [i for i in in_word[i]]
        for i in range(len(lst)):
            if ord(lst[i])%2 == 1 and ord(lst[i])<97 and ord(lst[i])<65:
                lst[i]=ord(lst[i])
                newl.append(chr(lst[i]+32))
            if ord(lst[i])%2 == 0 and ord(lst[i])<97 and ord(lst[i])>65:
                lst[i] = ord(lst[i])
                newl.append(chr(lst[i]-32))
            else:
                continue
        final.append(newl)
    print(*final)
    pass
 """

'''
def pyramid_case_clara_working(in_word):
    final = []
    lst = [i for i in in_word]
    for i in range(len(lst)):
        newl = lst[i]
        if i % 2 == 1  and lst[i] >= 'A' and lst[i] <= 'Z':            
            newl= chr(ord(lst[i])-ord('A') +ord('a'))
        elif i % 2 == 0 and lst[i] >= 'a' and lst[i] <= 'z':
            newl= chr(ord(lst[i])-ord('a') +ord('A'))
        final.append(newl)
    return "".join(final)
'''

def pyramid_case(in_word):
    # TODO: return the pyramid case word.
    # WRITE IN 10 CODE LINES MAX!!!
    list_word = list(in_word)
    for i in range(len(list_word)):
        if i%2 == 0: 
            list_word[i] = list_word[i].upper()
        else:
            list_word[i]= list_word[i].lower()

    return "".join(list_word)

# %%


def pyramid_case_one_liner(in_word):
    # TODO: ~~~BONUS~~~
    # return the pyramid case word in one line of code inside the function.
    # DO NOT USE ";" IN YOUR CODE.
    return "".join([ in_word[i].upper() if i%2 ==0 else in_word[i].lower() for i in range(len(in_word))])


# %%
# test functions here
input_words = ["hello", "world", "", "I", "am", "LEARNING", "Python"]

print("==== pyramid_case() results:")
for word in input_words:
    print(pyramid_case(word))

print("\n==== pyramid_case_one_liner() results:")
for word in input_words:
    print(pyramid_case_one_liner(word))


# %%
