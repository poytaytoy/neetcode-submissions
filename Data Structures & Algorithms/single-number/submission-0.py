class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        store = set()

        for stuff in nums: 
            if stuff not in store: 
                store.add(stuff)
            else: 
                store.remove(stuff)

        return tuple(store)[0]
        