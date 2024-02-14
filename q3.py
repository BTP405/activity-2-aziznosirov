def wordCount(t):
    word_dict = {}
    #Open text file
    with open(t, 'r') as file:
        #Iterate over each line in the file
        for line_num, line in enumerate(file, 1):
            #Tokenize the line into words
            words = line.strip().split()

            #Iterate over each word in the line
            for word in words:
                #If the words is already in the dictionary, append the line number
                if word in word_dict:
                    word_dict[word].append(line_num)
                #If the word is not in the dictionary, add it with the current line number
                else:
                    word_dict[word] = [line_num]

    return word_dict
