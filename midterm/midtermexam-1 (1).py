#----1----
# --Original code
N = input("Enter your characters: ")
# changed L = []
L = ""
for letters in N:
    letters.split()
    # changed L.append (letters)
    L = L + (letters*4)
# changed print (L*4)
print (L)


#----2----
# --Original code
handle = open('word_list.csv','r')
top2 = ["",""]
for line in handle:
   #Strip the input from each line in the file and add it to the word variable.
    word = line.strip()
   # Compare the lengths of each word that is coming in each word that is in each location.
    for i in range(0,2):
        top2.sort(key = len)
        # removed the less-than indication from the condition if (len(word) len(top2[i])):
        if (len(word) > len(top2[i])):
            top2[i] = word
            break
        # Print the words
# wrote print ("\nThe 2 longest words are:"), top2
print ("\nThe 2 longest words are:",top2)


#----3----
# --Original code
vowels_list = ['a','e','i','o','u']
while True:
    #prompts for user input and receives it
    char = input('Please enter an alphabetical character:')
    if len(char) > 1: #checks if input is more than one character
        print ('Invalid input')
        # added break command
        break
    else:
        if char.lower() in vowels_list: #verifies that the input contains more than one character.
            print ('False')
            # added break command
            break
        else:
            print ('True')
            break



# Third Question
keanumycins = []
stopwords_en = []

my_file = open("keanumycins.txt", "r")
data = my_file.readlines()
for i in data:
    one = i.strip("\n").strip(" ").split(" ")
    for word in one:
        keanumycins.append(word)
my_file.close()

for i in range(len(keanumycins)):
    keanumycins[i] = keanumycins[i].lower()
keanumycins.remove("")

my_file = open("stopwords_en.txt", "r")
data = my_file.readlines()

for i in data:
    word = i.strip("\n")
    if word in keanumycins:
        count = keanumycins.count(word)
        for j in range(count):
            keanumycins.remove(word)
#Get unique elements in keanumycins list
unique_list = []
for x in keanumycins:
    if x not in unique_list:
        unique_list.append(x)
print("The number of unique words:", len(unique_list))

#The 5 most frequent words
word_freq = {}
for word in keanumycins:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

top_5_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:5]
print("\n",top_5_words,"\n")

#Relevance of top 5 frequenent words
for i in top_5_words:
    print("Relevance of ",i[0],": ",i[1]/len(unique_list))