class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        classif = {}

        for item in strs: 

            if item == "": 
                if "empty" in classif:
                    classif["empty"].append("")
                else: 
                    classif["empty"] = [""]

                continue

            identity = [0] * 26

            for char in item:
                identity[ord(char) - ord('a')] += 1 

            if tuple(identity) in classif:
                classif[tuple(identity)].append(item)
            else: 
                classif[tuple(identity)] = [item]

        return [v for k, v in classif.items()]
