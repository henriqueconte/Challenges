class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isLastLetter = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        currentNode = self.root
        for char in word:
            if char not in currentNode.children:
                currentNode.children[char] = TrieNode()
            currentNode = currentNode.children[char]
            
        currentNode.isLastLetter = True
        
    def search(self, word):
        currentNode = self.root
        for char in word:
            if char in currentNode.children:
                currentNode = currentNode.children[char]
            else:
                return False
        return True
        

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        foundWordList = []
        
        for element in words:
            trie.insert(element)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie.root.children:
                    discoveredStates = [(i, j)]
                    while len(discoveredStates) < 4:
                        wordFound, discoveredStates = self.searchAround(board, trie.root.children[board[i][j]], words, (i, j), board[i][j], discoveredStates)
                        if wordFound and wordFound not in foundWordList:
                            foundWordList.append(wordFound)
                        
        return foundWordList
    
    def searchAround(self, board, trie, words, currentPosition, currentWord, usedNodes):
        x = currentPosition[0]
        y = currentPosition[1]
        currentTrie = trie
        stateList = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        usedNodesCopy = usedNodes
        discoveredStates = []
        # print(x, y)
        
        for state in stateList:  
            if x + state[0] >= 0 and y + state[1] >= 0 and x + state[0] < len(board) and y + state[1] < len(board[0]):
                if (x + state[0], y + state[1]) not in usedNodes:
                    if board[x + state[0]][y + state[1]] in currentTrie.children:
                        usedNodesCopy.append((x + state[0], y + state[1]))
                        print(currentWord)
                        return self.searchAround(board, currentTrie.children[board[x + state[0]][y + state[1]]], words, (x + state[0], y + state[1]), currentWord + board[x + state[0]][y + state[1]], usedNodesCopy)
            
            discoveredStates.append(state)
                
        
        # print(currentWord)
        if currentWord in words:
            print("returned!")
            return currentWord, discoveredStates
        else:
            return None, discoveredStates
                    
        
            
        
                    