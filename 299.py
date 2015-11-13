class Solution(object):
    def getHint(self, secret, guess):
        A = 0
        B = 0
        temp = [0]*10;
        for i in xrange(len(secret)):
            if secret[i] == guess[i]:
                A += 1
            else:
                if temp[int(secret[i])] < 0:
                    B += 1
                if temp[int(guess[i])] > 0:
                    B += 1
                temp[int(secret[i])] += 1
                temp[int(guess[i])] -= 1
        return str(A)+"A"+str(B)+"B"
