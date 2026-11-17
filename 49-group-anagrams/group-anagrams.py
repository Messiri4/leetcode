class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}   #create an empty dict to group anagrams
        for word in strs: 
            sort_word = "".join(sorted(word)) #sort characters of the individual word
            if sort_word not in words:
                words[sort_word] = []
            words[sort_word].append(word)
        return list(words.values())
        

        