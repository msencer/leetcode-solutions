class Solution(object):
    def intersect(self, nums1, nums2):
        lookup = {}
        result=[]
        for n in nums1:
            if n not in lookup:
                lookup[n]=0
            lookup[n]+=1
        for n in nums2:
            if n in lookup and lookup[n]>0:
               result.append(n)
               lookup[n]-=1
        return result

if __name__ == "__main__":
    assert [1,2,3,2] == Solution().intersect([1,2,3,2,4],[1,2,3,2])
    assert [] == Solution().intersect([1,2,3],[4,5,6])
