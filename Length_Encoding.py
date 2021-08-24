string = input()
freq = 1
en_string = []
for i in range(len(string)-1):
    if string[i]==string[i+1]:
        freq+=1
    else:
        en_string.append(str(freq))  #inserting frequency of the letter to the list
        en_string.append(string[i])  #inserting the letter to the list
        freq = 1  #resetting the frequency to 1
        
#inserting last frequency and letter in the string to the list
en_string.append(str(freq))
en_string.append(string[-1])
print(''.join(en_string))  #joining the list to string