# Read text from a file, and count the occurrence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open('./story.txt') as file:
      filename = file.read()
      print (filename)
    return filename

read_file_content("/story.tx")



def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    count ={}
    word = text.split(" ")
    for i in word:
        if i in count:
            count[i] +=1
        else:
            count[i] =1
    for key in list(count.keys()):
            print(key, ":", count[key])
    return count_words
    
print(count_words())