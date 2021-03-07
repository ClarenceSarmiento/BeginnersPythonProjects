# Word count program

""" Word count takes a sentence as input and out the number
of words in it. Duplications of words still counts."""

sentence = str(input("Enter Sentence: ")).split()
print(f"Word Count: {len(sentence)}")
