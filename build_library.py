"""
Aida Muratoglu
4/6/21
M6: Poetry Slam

Builds a library of Poem objects pulled from the complete works of Sappho (trans.
James Powell), stripped of its academic numbering system (i.e. Lobel-Page 3).
"""

from Poem import Poem
import os
import sys
os.environ['KMP_DUPLICATE_LIB_OK']='True'

def build_library():
    """Builds library of Poem objects that each contain a Sappho fragment from
        the input text (James Powell's translations).
        Returns:
            library (list): list of Poem objects
    """
    library = {}
    # Create Poem objects out of strings
    poem_list = import_poems()
    # Build library of Poem objects
    library = make_poems(poem_list)
    return library

def import_poems():
    """Reads file with fragments. Turns text file into individual poems. 
        Returns:
            poem_list (list): list of poems as strings
    """
    all_poems = open("poetry_of_sappho.txt", "r")
    content = all_poems.read()
    # Split fragments into individual poems at double space (formatting of
    # text file)
    poem_list = [poem.strip('\n\n') for poem in content.split('\n\n')]
    all_poems.close()
    return poem_list

def make_poems(poem_list):
    """Converts poem strings into poem objects.
        Args:
            poem_list (list): list of poems (as strings)

        Returns:
            poems (list): list of poems (as Poem objects)
    """
    poems = []
    for text in poem_list:
        poems.append(Poem(text, num_nouns = None, num_verbs = None))
    return poems

def main():
    build_library()
    #print(l[5])

if __name__ == "__main__":
    main()
        

