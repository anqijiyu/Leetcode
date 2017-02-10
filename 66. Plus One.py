class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = reduce(lambda x, y: x*10+y, digits)
        return [int(i) for i in str(num+1)]
    
    class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ans=[]
        count=0
        digits[len(digits)-1]+=1
        for i in digits[::-1]:
            tmp=i+count
            if tmp>9:
                ans.insert(0,tmp-10)
                count=1
            else:
                ans.insert(0,tmp)
                count=0
        if count:
            ans.insert(0,count)
        return ans
