import string

str_c = str(input())
str_letter = string.ascii_letters
dict_letter = {}
for letter in str_letter:
    dict_letter[letter] = []
for i in str_c:
    dict_letter[i].append(i)
for count in str_letter:
    if len(dict_letter[count]) != 0:
        print("%s的个数为%d" % (count, len(dict_letter[count])))


class Node(object):
    def __init__(self, is_word=False):
        self.is_word = is_word
        self.node = {}


class Trie(object):
    def __init__(self):

        self.size = 0
        self.root = Node()

    def __len__(self):
        return self.size

    def add(self, word):
        cur = self.root
        for char in word:
            if cur.node.get(char) is None:
                cur.node[char] = Node()
            cur = cur.node[char]
        if not cur.is_word:
            cur.is_word = True
            self.size += 1

    def add_by_recursion(self, word):
        self.__add(word, 0, self.root)

    def __add(self, word, i, cur):
        if i == len(word):
            if not cur.is_word:
                cur.is_word = True
                self.size += 1
            return
        if cur.node.get(word[i]) is None:
            cur.node[word[i]] = Node()
        self.__add(word, i + 1, cur.node[word[i]])

    def __contains__(self, item):
        cur = self.root
        for char in item:
            if cur.node.get(char) is None:
                return False
            cur = cur.node[char]
        return cur.is_word

    def is_prefix(self, prefix):
        cur = self.root
        for char in prefix:
            if cur.node.get(char) is None:
                return False
            cur = cur.node[char]
        return True
