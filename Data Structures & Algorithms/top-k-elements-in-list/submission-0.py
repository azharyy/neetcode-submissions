from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        result = []
        pairs = c.most_common(k)
        for pair in pairs:
            result.append(pair[0])
        return result
