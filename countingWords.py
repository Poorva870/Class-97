introString=input('Enter your introduction:')
#print(introString)
characterCount=0
wordCount=1

for i in introString:
    characterCount=characterCount+1
    #print(characterCount)
    if(i==' '):
        wordCount=wordCount+1

print('Number of the words in the string:')
print(wordCount)

print('Number of the characters in the string:')
print(characterCount)