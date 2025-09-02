phrase = "thi1s phrase4 a3 i2s"
phrase.split()
new_list = phrase.split()

sentence = sorted(new_list, key=lambda word: next(c for c in word if c.isdigit()))
final_sentence = ' '.join(sentence)

print(final_sentence)