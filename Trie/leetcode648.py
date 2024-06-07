class TrieNode:
    def __init__(self):
        self.children = {}
        self.lastWord = False


class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.lastWord = True

    def canReplace(self, word):
        curr = self.root
        res = ""
        for w in word:
            if w not in curr.children:
                return word
            curr = curr.children[w]
            res += w
            if curr.lastWord:
                return res
        return word

    def replaceWords(self, dictionary, sentence):
        for word in dictionary:
            self.insert(word)
        result = []
        for word in sentence.split():
            result.append(self.canReplace(word))
        return " ".join(result)


x = Solution()
print(
    x.replaceWords(
        ["cat", "bat", "rat"],
        "the cattle was rattled by the battery",
    )
)
