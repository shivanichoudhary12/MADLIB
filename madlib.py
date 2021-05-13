# string concatenation
# there will be a paragraph that have some blanks and we have to take the input from user to fill those blank

adjective = input("adjective:")
noun = input("noun:")
verb_past_tense = input("verb, past tense:")
adverb = input("adverb :")
adjective2 = input("adjective:")
noun2= input("noun:")

madlib = f"""Today I went to the zoo. I saw a(n) {adjective} {noun} jumping up and down in its tree.\
He {verb_past_tense} {adverb} through the large tunnel that led to its {adjective2} {noun2}"""

print(madlib)