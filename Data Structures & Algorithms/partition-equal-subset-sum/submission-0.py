class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #1) reverse sum list check if val > sum[i] 
        #2) use set to kill dups
        #3) use abs to merge -1 1
        #use two sets to not have err

        prev = {0}
        curr = set()
        nums.reverse()
        s = []
        for i,n in enumerate(nums):
            if i==0:
                s.append(n)
            else:
                s.append(n+s[i-1])
        s.reverse()
        s.append(0)
        s.remove(s[0])
        print(s)
        nums.reverse()

        for i,n in enumerate(nums):
            #case where no viable options
            print(prev)
            if not prev:
                return False
            #choose + or -
            for m in prev:
                if m+n == s[i] or abs(m-n) == s[i]:
                    return True
                elif m+n > s[i] and abs(m-n) > s[i]:
                    continue
                elif m+n > s[i]:
                    curr.add(abs(m-n))
                elif abs(m-n) > s[i]:
                    curr.add(m+n)
                else:
                    curr.add(m+n)
                    curr.add(abs(m-n))
            prev = curr
            curr=set()
        if 0 not in prev:
            return False
        else:
            return True


                
        