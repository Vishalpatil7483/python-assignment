# 20. Count Words in a Sentence
sentence = "hello world hello"
words = sentence.split()
word_count = {word: words.count(word) for word in set(words)}
print(word_count)