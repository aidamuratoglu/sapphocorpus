"""
Aida Muratoglu
4/6/21
M6: Poetry Slam

Writes new poems and evaluates them using natural language processing tools
and poetic lineation rules.
"""

from numpy import random
import numpy as np
from build_library import build_library
from Poem import Poem
import pyttsx3

def write_poetry():
    """Writes and evaluates 10 new poems. Returns the best one.
        Returns:
            poems (list): 10 new poems.
    """
    x = 0
    new_poems = []
    frags = call_fragments()
    verbs = get_verbs(frags)
    nouns = get_noun_phrases(frags)

    while x < 10:
        num_nouns = random.randint(1, 20)
        num_verbs = random.randint(1, 20)
        list_poem = make_list_poem(verbs, nouns, num_nouns, num_verbs)
        line_breaks = random.randint(0, 15)
        y = 0
        while y < line_breaks:
            list_poem.insert(random.randint(0, len(list_poem)), "\n]")
            y += 1
        text = " ".join(list_poem)
        new_poem = Poem(text, num_nouns, num_verbs)
        new_poems.append(new_poem)
        x += 1
    
    return new_poems

def make_list_poem(verbs, nouns, num_nouns, num_verbs):
    """Populates list with random number of noun phrases and verbs at random
        intervals (i.e. noun noun verb noun verb verb, etc.). 
        Args:
            verbs (list): verbs to use
            nouns (list): nouns to use
            num_nouns (int): number of noun phrases
            num_verbs (int): number of verbs

        Returns: 
            list_poem (list): noun phrases and verbs as list
    """
    # Chooses random number of verbs and nouns for new poem
    list_poem = []
    y = 0
    while y < num_nouns + num_verbs:
            # If randint is False (0), place a verb from list
            if (random.randint(0, 1) == False):
                list_poem.append(random.choice(verbs))
            # If randint is True (1), place a noun from list
            list_poem.append(random.choice(nouns))
            y += 1
    # Shuffles contents of poem
    random.shuffle(list_poem)
    return list_poem
    
def call_fragments():
    """Chooses a random number of Poems to pull from the library and returns 
        them as a list.
        Returns: 
            frags (list): list of Poems
    """
    # Generates a random number
    num_frag = random.randint(1, 15)
    frags = []
    library = build_library()
    x = 0
    # Populates a list with the number of fragments (chosen at random)
    while x < num_frag:
        frags.append(random.choice(library))
        x += 1
    return frags

def get_verbs(frags):
    """Uses  natural language processing calls from the Poem class to return
        all verbs in the given fragments.
        Args:
            frags (list): list of Poems

        Returns: 
            verbs (list): list of verbs from fragments
    """
    verbs = []
    x = 0
    while x < len(frags):
        verbs.extend(frags[x].get_verbs())
        x += 1
    return verbs

def get_noun_phrases(frags):
    """Uses  natural language processing calls from the Poem class to return
        all noun phrases in the given fragments.
        Args:
            frags (list): list of Poems

        Returns: 
            nouns (list): list of noun phrases from fragments
    """
    nouns = []
    x = 0
    while x < len(frags):
        nouns.extend(frags[x].get_noun_phrases())
        x += 1
    return nouns

def get_all_scores(poems):
    """Prints all Poems with corresponding fitness scores.
        Returns:
            fitness_scores (dict): Poem objects and fitness scores.
    """
    fitness_scores = {}
    for poem in poems:
        fitness_scores[poem._evaluate()] = poem
    return fitness_scores

def choose_best_poem(poems):
    """Evaluates all poems using two parameters: ratio of noun phrases to verbs
        and line length. Returns best poem.

        Returns:
            best poem (according to fitness scores)
    """
    fitness_scores = {}
    for poem in poems:
        fitness_scores[poem.evaluate()] = poem
        max_score = max(fitness_scores.keys())
    return fitness_scores[max_score]

def read_aloud(poem):
    """Reads poems aloud using text-to-speech software.

        Args:
            poem (str): poem to read aloud
    """
    engine = pyttsx3.init()

    # Changes voice to female.
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    engine.say(poem.text)
    engine.runAndWait()

def main():
    poems = write_poetry()
    
    best = choose_best_poem(poems)

    best_or_rank = input("See best poem or rank all poems? Enter b or r: ")
    while best_or_rank != "b" and best_or_rank != "r":
        best_or_rank = input("See best poem or rank all poems? Enter b or r: ")

    print_or_save = input("Print or save the poem? Enter p or s: ") 
    while print_or_save != "p" and print_or_save != "s":
        print_or_save = input("Print or save the poem? Enter p or s: ")

    if best_or_rank == "b":
        if print_or_save == "p":
            print(best)
        
        if print_or_save == "s":
            best.make_text_file()

    if best_or_rank == "r":
        if print_or_save == "p":
            for poem in poems:
                print(poem)
                print("Fitness score = ", poem.evaluate())

        if print_or_save == "s":
            poem_files = []
            for poem in poems:
                poem_files.append(poem.make_text_file())

    print("Reading best poem out loud...")
    # read out loud!
    read_aloud(best)

if __name__ == "__main__":
    main()