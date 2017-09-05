# jimmy shen
# Sep 2, 2017
# Output
some_word = input("please input a word in lower case::")
new_word = ''
for c in some_word:
    if c=='a':
        new_word=new_word+'z'
    else:
        new_word=new_word+chr(ord(c)-1)
print(new_word)
