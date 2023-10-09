the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""
print(len(the_text))
count = 0
word = 0
for i in the_text:
    if i == ' ':
        #continue
        count += 1
    else:
        word += 1
print('Total Number of Space in the passage: {}'.format(count))
print('Total Number of word in the passage: {}'.format(word))
print('Total Number of Space and Word:= {}'.format(count + word))