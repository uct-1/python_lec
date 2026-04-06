sentence = input("Bir cümle yazın: ")

counts = {}

for word in sentence.split():
    counts[word] = counts.get(word, 0) + 1

print("Kelime frekansları:")
print(counts)