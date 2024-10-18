sen = str(input("Enter the Sentence : "))
count =0
for i in sen:
    if i  in 'aeiouAEIOU':
        count +=1
print("no of vowels : ",count)