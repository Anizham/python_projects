user_input = input("Enter a Phrase to generate the acronym: ")
words = user_input.split()
a = " "
for i in words:
    a = a + str(i[0]).upper()
print(a)
