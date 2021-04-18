"""
Space to test things
"""

import spacy
import os
import random

os.environ['KMP_DUPLICATE_LIB_OK']='True'

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_trf")

# Process whole documents
text = ("Artfully adorned Aphrodite, deathless "
        "child of Zeus and weaver of wiles I beg you "
        "please don’t hurt me, don’t overcome my spirit, "
        "goddess, with longing, "
        "but come here, if ever at other moments "
        "hearing these my words from afar you listened "
        "and responded: leaving your father’s house, all "
        "golden, you came then, "
        "hitching up your chariot: lovely sparrows "
        "drew you quickly over the dark earth, whirling "
        "on fine beating wings from the heights of heaven "
        "down through the sky and "
        "instantly arrived—and then O my blessed "
        "goddess with a smile on your deathless face you "
        "asked me what the matter was this time, what I "
        "called you for this time, "
        "what I now most wanted to happen in my "
        "raving heart: “Whom this time should I persuade to "
        "lead you back again to her love? Who now, oh "
        "Sappho, who wrongs you? "
        "If she flees you now, she will soon pursue you; "
        "if she won’t accept what you give, she’ll give it; "
        "if she doesn’t love you, she’ll love you soon now, "
        "even unwilling.” "
        "Come to me again, and release me from this "
        "want past bearing. All that my heart desires to "
        "happen—make it happen. And stand beside me, "
        "goddess, my ally.")
doc = nlp(text)

# Analyze syntax
np = [chunk.text for chunk in doc.noun_chunks]
print("length nouns: ", len(np))
print()
v = [token.lemma_ for token in doc if token.pos_ == "VERB"]
print("length verbs: ", len(v))

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)

"""
list_po = ['hunt', 'Kronos', 'consent', 'you', 'injure', 'the gods', 'speak', 'whom', 'see', 'a desire', 'forget', 'her']
my_str = " ".join(list_po)
list_po = my_str.split(r"\S+")
print(list_po)
si = iter(list_po)
pair_iter = [c+next(si, " ") for c in si]
new_list = list(pair_iter)
print(new_list)

si = iter(['abcd', 'e', 'fg', 'hijklmn', 'opq', 'r'])
map(str.__add__, si, si)


list_po = ['hunt', 'Kronos', 'consent', 'you', 'injure', 'the gods', 'speak', 'whom', 'see', 'a desire', 'forget', 'her']
x = 1
line_breaks = random.randint(0, 10)
while x < line_breaks:
        list_po.insert(random.randint(0, len(list_po)), "\n]")
        x += 1
print(list_po)
poem = " ".join(list_po)
print(poem)
"""