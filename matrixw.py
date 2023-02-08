## By m7d9ng github.com/ojanrn
import random, os, sys

def matrix_get(char_count):
    wordlist = "abcdefghiojklmnopqrstuvwxyz1234567890"
    final_list = ""
    for i in range(char_count):
        final_list += random.choice(wordlist)
    return_list = final_list
    final_list = ""
    return return_list
    

def term_settings():
    term_size = os.get_terminal_size()
    term_width = term_size.columns
    return term_width
    
if __name__ == "__main__":
    while True:
        current_term_width = term_settings()
        base_term = matrix_get(current_term_width)
        print(base_term, end='')


