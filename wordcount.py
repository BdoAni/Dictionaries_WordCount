import sys
"""Count words in file."""
input_file =sys.argv[1]

def word_count(input_file):
    input_file =open(input_file)
    my_dict={}
    
    for line in input_file:
        line  =line.rstrip()
        print(f"We are printing thr spases  {line}")
        words=line.split()
        print(f"We are printing thr words  {words}")
        for word in words:
            my_dict[word] = my_dict.get(word, 0) + 1
    for word, count in my_dict.items():
            print(word, count)
        # return my_dict 
    print(my_dict)  
    
word_count(input_file)
     


