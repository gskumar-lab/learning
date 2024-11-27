def get_input():
    """This function gets input"""
    
    subject=input("1. Subject:")
    verb=input("2. Verb:")
    adjective=input("3. Adjective:")

    fill_blanks(subject,verb,adjective)

def fill_blanks(word1,word2,word3):
    """This function fill in blanks"""
    print("The {2} brown fox {1} over the lazy {0} \n".format(word1,word2,word3))

print("Fill in the story :\nThe ___ brown fox ___ over the lazy ___ \n")

get_input()
