import re

class TreeNode(object):
    def __init__(self, startIndex, endIndex, substr, endList):
        self.startIndex = startIndex
        self.endIndex = endIndex
        self.substr = substr
        self.endList = endList
    
    
        
class Solution(object):
    def getKey(self, TreeNode):
        return (TreeNode.startIndex)
     
    def printNodes(self, res):
        for r in res:
            print (r.startIndex, r.endIndex, r.substr, r.endList)
    
    def printNode(self, r):
        print (r.startIndex, r.endIndex, r.substr, r.endList)
            
    def graphTraversal(self, node, res, lengthOfString):
        if node.endList == []:
            if lengthOfString == node.endIndex:
                return True
            else:
                return False
        for indxs in node.endList:
            t = self.graphTraversal(res[indxs], res, lengthOfString)
            if t:
                break
        return t
    
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        #filter the dictionary
        res = []
        it = 0
        length = len(s)
        while it < len(wordDict):
            #print (wordDict[it], wordDict, it)
            word = wordDict[it]
            t = s.find(word)
            if word == s:
                return True
            #if not found remove
            if t == -1:
                wordDict.remove(word)
                it = it - 1
            #else create TreeNode
            else:
                #for each instance of word found in s
                temp = [m for m in re.finditer('(?=%s)' % (word), s)]#[a for a in list(re.finditer(word, s))]
                for t in temp:
                    res.append(TreeNode(t.start(), t.start() + len(word), word, []))
            it = it + 1

        #sort the unconnected graph
        res = sorted(res, key = self.getKey)
        
        #build graph
        for one in res:
            for two in range(len(res)):
                if one.endIndex == res[two].startIndex:
                    one.endList.append(two)
                    
        #self.printNodes(res)
        print (len(res))
        out = False

        #graph traversal
        for one in res:
            if not one.startIndex:
                out = self.graphTraversal(one, res, length)
                if out:
                    break
        return out
        
        
        #Better Solution - for reference
        #def wordBreak(self, s, wordDict):
        #trackArray = [False] * (len(s) + 1)
        #First element true
        #trackArray[0] = True

        #for i in range(1, len(s) + 1):
            #for j in range(i):
                #if trackArray[j] and s[j:i] in wordDict:
                    #trackArray[i] = True
        #return trackArray[len(s)]
