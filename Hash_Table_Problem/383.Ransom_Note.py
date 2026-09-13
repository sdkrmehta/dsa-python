from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter1 = Counter(ransomNote)
        counter2 = Counter(magazine)

        for nums in counter1:
            if nums not in counter2:
                return False

            if counter1[nums] > counter2[nums]:
                return False

        return True