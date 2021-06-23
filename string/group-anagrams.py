from collections import defaultdict

# method 1
# time complexity: O(nklog(k)), where n is number of words in the file and k is the length of the longest word
def sort_based(file: str) -> list:

    map = defaultdict(list)
    with open(file, 'r', encoding='utf-8') as rf:
        words = rf.readlines()
        for word in words:
            word = word.lower()
            word_sorted = ''.join(sorted(word))
            map[word_sorted].append(word)

    return map.values()

# method 2
# time complexity: O(nk), where n is number of words in the file and k is the length of the longest word
def map_based(file: str) -> list:

    map = defaultdict(list)
    #with open(file, 'r', encoding='utf-8') as rf:
    #    words = rf.readlines()
    for word in file:
        word = word.lower()
        key = [0]*26
        for ch in word:
            key[ord(ch) - ord('a')] += 1
        key = tuple(key)
        map[key].append(word)

    return map.values()