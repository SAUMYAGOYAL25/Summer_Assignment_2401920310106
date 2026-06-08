class Solution(object):
    def canConstruct(self,ransomNote,magazine):
        for ch in ransomNote:
            if ransomNote.count(ch)>magazine.count(ch):
                return False
        return True        
