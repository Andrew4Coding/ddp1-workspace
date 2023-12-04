'''
Nama    : Andrew Devito Aryo
NPM     : 2306152494
Kelas   : DDP1-C
Asdos   : GAN
'''

from File_Pendukung.htmlFunctions import *
import string

def main():
    print('''
Program to create word cloud from a text file 
--------------------------------------------- 
The result is stored as an HTML file, 
which can be displayed in a web browser.    
''')
    # Prompt file name from user
    file_prompt = input("Please enter the file name: ")

    # Define every symbols in word that have to be removed
    symbols_to_remove = string.punctuation + '�ï¿½'
    dir = r'./File_Pendukung/'
    
    file_read = open(dir + file_prompt, "r").read().lower()

    # Replace all of unnecessary symbols
    for symbol in symbols_to_remove:
        file_read = file_read.replace(symbol, '')

    # Make file_read variable into list typed
    file_read = file_read.split()
    stop_text_file = [i.strip() for i in open(dir + "stopWords.txt", "r").readlines()]

    list_of_tuple = []
    for index, word in enumerate(file_read):
        # If stopped word is not in list of words (file_read)
        if word not in stop_text_file and (word not in file_read[:index]):
            list_of_tuple.append((file_read.count(word), word))

    # Sort the tuple based on count (python sort the list based on first element of each tuple)
    list_of_tuple.sort(reverse=True)

    # TODO: We want the tuple configuration inside list_of_tuple is (word, count) not (count, word), so we do: 
    list_of_tuple = [(j, i) for i, j in list_of_tuple][:60] # Reversed the tuple config from (count, word) to (word, count)

    for i in range(0, len(list_of_tuple), 3):
        try:
            # TODO: Show 3 values for each iteration
            a = f"{list_of_tuple[i][0]:<20} : {list_of_tuple[i][1]}"
            b = f"{list_of_tuple[i+1][0]:<20} : {list_of_tuple[i+1][1]}"
            c = f"{list_of_tuple[i+2][0]:<20} : {list_of_tuple[i+2][1]}"
            print(f"{a:<30} {b:<30} {c:<30}")
        except:
            # To prevent list index out ouf range error
            pass

    # TODO: Because we reversed sort the list based on count, so the first element must be the highest count
    # TODO" the last element must be the lowest count
    high_count = list_of_tuple[0][1]
    low_count = list_of_tuple[-1][1]

    # TODO: This will sort the list_of_tuples based on Alphabet (first element of the tuple)
    list_of_tuple.sort()
    

    # TODO: HTML Section
    body=''
    for word, cnt in list_of_tuple:
        body = body + " " + make_HTML_word(word,cnt,high_count,low_count)
    box = make_HTML_box(body)  # creates HTML in a box

    print_HTML_file(box, file_prompt)  # Writes HTML to File
    input("Press type Enter to exit ...")


if __name__ == "__main__":
    main()