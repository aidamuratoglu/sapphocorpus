# sapphocorpus
A computationally creative system that creates new verses based on Sappho's 
poetry (trans. Jim Powell). 

# How to Run

To run: go to write_poetry.py. Run this program. Follow commands to view or 
save all poems or just the best poem. During runtime, sapphocorpus builds a 
library of poems from Jim Powell's translation of Sappho. Then, "write_poetry"
chooses a random number of fragments (between 1 and 20) from which to generate
new poems. To do so, sapphocorpus uses the natural language processing system
spaCy to parse each poem into noun phrases and verbs, creating two new lists to
pull from. To write a new poem, sapphocorpus places nouns and verbs from these
new lists at random intervals into a new list. This list is then shuffled,
line breaks are added to it randomly, and the list is made into a poem object. 
Each run of the program creates 10 new poems. The program evaluates each poem 
based on two factors: the ratio of noun phrases to verbs and the length of each
line (ideally 5 words). sapphocorpus will automatically read the best poem 
aloud at the end of its runtime.

# Some Background

Sappho's entire body of work exists in our contemporary moment only in 
fragments. sapphocorpus plays on this idea, writing poems that are inherently
fragmented--each line break also includes a "]", the academic notation for
when a pottery shard or parchment has a large chunk missing. The computer
mimics the fragmented nature of Sapphic poetry. In its naming schema,
sapphocorpus uses the framework "Sappho fr xxx," where xxx is a number between
60 and 500, again mimicking the academic numbering system for Sappho's poetry
(which do not have titles, save for two poems where the titles have been
preserved).

# Some Reflections

Working on this program has challenged me as a computer scientist to really
think about runtime when dealing with NLP. Furthermore, I felt challenged
when coming up with the fitness function and ways to have the system evaluate
itself. I dabbled in Euclidian distance before deciding a simpler, absolute
value-based approach might work better. Lastly, I felt challenged as a 
computer scientist to push the program beyond mere generation, to implement
the "inception" piece of Ventura's Odyssey, and to create an interface that
was as user-friendly as possible.

# Conclusions / Future Thoughts

Future versions of this program would pay closer attention to the pieces of
each poem beyond noun phrases and verbs. Ideally, the program will take
in and analyze the speaker's relationship to the characters, places, images, 
and gods that populate Sappho's poetry. From here, the program would build 
poems based on these relationships, potentially creating a new body of Sapphic
work that has since been lost to time.

# Works Cited

Alan R. Champneys, P. G. H., Harry Man. (2010). The Numbers Lead a Dance: 
Mathematics of the Sestina. Non-linear partial differential equations, 
mathematical physics, and stochastic analysis: the Helge Holden anniversary 
volume, 15. doi:https://doi.org/10.4171/186-1/3

Hartman, C. O. (1996). Virtual Muse: Experiments in Computer Poetry. 
Middletown, CT: Wesleyan University Press.

Jukka M. Toivanen, H. T., Alessandro Valitutti, Oskar Gross. (2012). 
Corpus-Based Generation of Content and Form in Poetry. Paper presented at the 
International Conference on Computational Creativity, Dublin, Ireland. 



