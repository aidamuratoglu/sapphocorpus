"""
Aida Muratoglu
4/6/21
M6: Poetry Slam

Holds information for the Poem object, including the evaluation function that 
evaluates the poem based on the following SPECS protocols: Domain Competence,
Originality, and Thinking and Evaluation.  
"""
import spacy
import os
import numpy as np
from numpy import random

os.environ['KMP_DUPLICATE_LIB_OK']='True'

class Poem:
    def __init__(self, text, num_nouns, num_verbs):
        self.text = text
        self.num_lines = text.count("\n")
        self.num_nouns = num_nouns
        self.num_verbs = num_verbs
        self.fitness_score = None

    def get_noun_phrases(self):
        """Parses text using natural language processing tools to analyze and 
            return all noun phrases.
            Returns:
                noun_phrases (list): list of all noun phrases in given text.
        """
        doc = self.parse_text()
        noun_phrases = [chunk.text for chunk in doc.noun_chunks]
        return noun_phrases

    def get_verbs(self):
        """Parses text using natural language processing tools to analyze and 
            return all verbs. 
            Returns:
                verbs (list): list of all verbs in given text.
        """
        doc = self.parse_text()
        verbs = [token.lemma_ for token in doc if token.pos_ == "VERB"]
        return verbs
    
    def parse_text(self):
        """Prepares text for future NLP actions by loading spacy and creating
            a new NLP object.
            Args: 
                text (str): poem to be parsed
            
            Returns: 
                doc (NLP object): processed text
        """
        # Load English tokenizer, tagger, parser and NER
        nlp = spacy.load("en_core_web_trf")
        lines = self.text
        # Adds whitespace at end of line and strips line breaks
        words = lines.split()
        poem = " ".join(words)
        doc = nlp(poem)
        return doc

    def make_text_file(self):
        """Makes and saves a text file of the poem."""
        with open(f"sappho fr {random.randint(60, 500)}", "w+") as file:
            file.write(self.text)
    
    def __repr__(self):
        return f"text: {self.text}\nnouns: {self.get_noun_phrases()}\nverbs: "\
            f"{self.get_verbs()}\nnumber of lines: {self.num_lines}"

    def __str__(self):
        return f"{self.text}"

    def evaluate(self):
        """Evaluates a poem based on line length and ratio of noun phrases to 
        verbs. Line length is weighted more than ratio. Updates fitness score 
        instance variable with score.
        
        Args:
            poem (Poem): poem to analyze

        Returns:
            fitness_score (int): fitness score based on parameters
        """
        # Evaluates along noun phrase to verb ratio (ideal ratio 62:38, based 
        # on "Ode to Aphrodite", the only complete Sappho poem). 2 is highest.
        ratio_score = 2 - ((abs(self.num_nouns / self.num_verbs)) / (62/38))
        self.fitness_score = ratio_score

        # Evaluate along line length. Ideal line length = 5 words.
        if self.num_lines == 0:
            if self.num_nouns + self.num_verbs == 5:
                self.fitness_score += 2
            else:
                self.fitness_score -= 1
        else:
            line_score = ((self.num_nouns + self.num_verbs) / self.num_lines) / 5
            if line_score == 1:
                line_score == 4
            if line_score > 1:
                line_score == 3
            if line_score > 2:
                line_score -= 2
            if line_score > 3:
                line_score -= 1

        return self.fitness_score