import re
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = re.findall('(?i)[aeiou]', s)
        return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)
    
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        tmp="aeiouAEIOU"
        i,j=0,len(s)-1
        s=list(s)
        while i<j:
            while s[i] not in tmp and i<j:
                i+=1
            while s[j] not in tmp and i<j:
                j-=1
            s[i],s[j]=s[j],s[i]
            i,j=i+1,j-1
        return ''.join(s)
