filename = input("Dosya adı: ")
handle = open(filename)

counts = {}

for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

big_word = None
big_count = None

for word, cnt in counts.items():
    if big_count is None or cnt > big_count:
        big_word = word
        big_count = cnt

print("En çok geçen kelime:", big_word, "(", big_count, ")")