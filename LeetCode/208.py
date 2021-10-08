# 208. Implement Trie (Prefix Tree)

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isEndOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        currentNode = self.root
        for char in word:
            if char in currentNode.children:
                currentNode = currentNode.children[char]
            else:
                currentNode.children[char] = TrieNode()
                currentNode = currentNode.children[char]

        currentNode.isEndOfWord = True

    def search(self, word: str) -> bool:
        currentNode = self.root
        for char in word:
            if char in currentNode.children:
                currentNode = currentNode.children[char]
            else:
                return False
        
        return currentNode.isEndOfWord 

    def startsWith(self, prefix: str) -> bool:
        currentNode = self.root
        for char in prefix:
            if char in currentNode.children:
                currentNode = currentNode.children[char]
            else:
                return False
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

responseList = []
trie = Trie()

responseList.append(trie.insert("apple")) 
responseList.append(trie.search("apple"))
responseList.append(trie.search("app") )
responseList.append(trie.startsWith("app"))
responseList.append(trie.insert("app"))
responseList.append(trie.search("app"))