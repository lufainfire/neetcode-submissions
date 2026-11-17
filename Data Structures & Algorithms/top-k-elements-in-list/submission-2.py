import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #using a hashmap O(n) O(n) max_h

        #hashmap freq then reverse this hashmap freq as key and num as val
        # take freq.values() turn it into a max_h by min_h but with negative values
        #for i in range(k) heapq.heappop(heap) then answer.append(rev[p])
        freq = {}
        rev= {}
        
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        
        for i in freq:
            if freq[i] in rev:
                rev[freq[i]].append(i)
            else:
                rev[freq[i]] = deque()
                rev[freq[i]].append(i)
        
        heap = (list(freq.values()))
        for i in range(len(heap)):
            heap[i]*=-1
        heapq.heapify(heap)
        
        answer=[]
        for i in range(k):
            answer.append(rev[-heapq.heappop(heap)].popleft())
        return answer





        