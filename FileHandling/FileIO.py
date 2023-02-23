# file io example
# encoding=utf-8
import io

f = io.open("text.txt", "wt", encoding="utf-8")
inputtext = input("Enter text in the file : ")
f.write(unicode(inputtext))
f.close()

print()
print ("Contents in the file text.txt are : ")
text = io.open("text.txt", encoding="utf-8").read()
print(text)
