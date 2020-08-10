class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        d = [[a, "a"], [b, "b"], [c, "c"]]
        total = a + b + c
        res = ""
        def canAdd(res, x):
            return len(res) < 2 or res[-1] != x or res[-2] != x
        while total > 0:
            d.sort(reverse=True)
            for i, (count, char) in enumerate(d):
                if count == 0: continue
                if canAdd(res, char):
                    res += char
                    d[i][0] -= 1
                    total -= 1
                    break
            else:
                break
        return res
val=Solution()
A,B,C=map(int,input().split())
if(val.longestDiverseString(A,B,C))=="":
  print(-1)
else:
  print(val.longestDiverseString(A,B,C))
