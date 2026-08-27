class Solution(object):
    def finalValueAfterOperations(self, operations):
        table = {
            "++X": 1,
            "X++": 1,
            "X--": -1,
            "--X": -1,
        }
        x = 0
        for op in operations:
            x += table[op]
        return x