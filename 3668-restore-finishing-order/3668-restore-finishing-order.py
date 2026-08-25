class Solution(object):
    def recoverOrder(self, order, friends):
        res = []
        for i in order:
            if i in friends:
                res.append(i)
        return res
        