class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter
        counted = Counter(text)
        print(counted)
        balloon_count = 0
        while True:
            for char in "balloon":
                if counted[char] - 1 != -1:
                    balloon_count += 1
                    counted[char] = counted[char] - 1
                else:
                    return balloon_count // 7
    

        