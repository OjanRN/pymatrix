## By m7d9ng github.com/ojanrn
import random, os, time

def matrix_get(char_count):
    wordlist = "abcdefghiojklmnopqrstuvwxyz1234567890"
    final_list = ""
    for i in range(char_count - 1):
        final_list += random.choice(wordlist)
    return_list = final_list
    final_list = ""
    return return_list

def matrix_line(matrix_list):
    print_list = []
    for chars in matrix_list:
        des_put = random.randint(0,1)
        if des_put == 0:
            print_list.append(chars)
        else:
            print_list.append(" ")
    return print_list

def term_settings():
    term_size = os.get_terminal_size()
    term_width = term_size.columns
    return term_width
    
if __name__ == "__main__":
    while True:
        current_term_width = term_settings()
        base_term = matrix_get(current_term_width)
        print("".join(matrix_line(base_term)))
        time.sleep(0.01)



