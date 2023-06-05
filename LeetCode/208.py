# 208. Implement Trie (Prefix Tree)

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isEndOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        currentNode = self.root
        for letter in word:

            if letter not in currentNode.children:
                currentNode.children[letter] = TrieNode()
            currentNode = currentNode.children[letter]

        currentNode.isEndOfWord = True
        
    def search(self, word):
        currentNode = self.root
        for letter in word:
            if letter not in currentNode.children:
                return False
            currentNode = currentNode.children[letter]

        return currentNode.isEndOfWord
    
    def startsWith(self, prefix):
        currentNode = self.root
        for letter in prefix:
            if letter not in currentNode.children:
                return False
            currentNode = currentNode.children[letter]
            
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

print(responseList)