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
                
            identity_string = ",".join(map(str, identity))

            if identity_string in classif:
                classif[identity_string].append(item)
            else: 
                classif[identity_string] = [item]

        return [v for k, v in classif.items()]
