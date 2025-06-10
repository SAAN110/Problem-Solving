import re

text = 'AN INVESTMENT IN KNOWLEDGE PAYS THE BEST INTREST'

while True:
    # print("\nEnter The Pattern You Want To Search In Text:")
    Pattern = input("\nEnter The Pattern You Want To Search In Text:")

    if re.search(Pattern,text,re.IGNORECASE):
        print("\nMatch Found")
    else:    
        print("\nMatch not Found")

    cont = input("\nDo you want to search another Pattern (yes/no): ")
    if cont.lower() != "yes":
        break
