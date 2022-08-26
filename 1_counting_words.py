# Script that takes any txt file
# And then it counts every word in the text

trigger = True
while trigger:
    try:
        file = input('Enter file name: ')
        handle = open(file, 'r')
        trigger = False
    except:
        print('Something went wrong, try again...')

word_dict = dict()
for line in handle:
    words = line.split()
    for word in words:
        # Create key:value pairs of every word and
        # assign amount of its occurrence in the text 
        word_dict[word] = word_dict.get(word, 0) + 1

# Loop through the dictionary 
# and select the word with the most occurrences in the text
biggest_word = None
word_count = None
for word, count in word_dict.items():
    if biggest_word is None or count > word_count:
        biggest_word = word
        word_count = count
print("Most common word in the text: ", biggest_word, word_count)


# Loop through the key:value pairs in the dictionary
# Create temporary tuple and reverse the order of key:value pairs
# Append temporary tuple to the word list
word_list = list()
for k,v in word_dict.items():
    tmp_tuple = (v, k)
    word_list.append(tmp_tuple)

# Show top 10 most common words in the text
word_list = sorted(word_list, reverse=True)
print('Top 10 most common words:')
for v, k in word_list[:10]:
    print(k, v)

# Shorter version
# print('Top 10 most common words:')
# print( sorted( [ (v, k) for k, v in words_dict.items() ], reverse=True )[:10] )