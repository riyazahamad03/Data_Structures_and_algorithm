import collections
class Solution:
    def minDeletions(self, s: str) -> int:
        count = collections.Counter(s)

        st , res = [] , 0
        for c , freq in count.items():
            while freq > 0 and freq in st:
                freq -= 1
                res += 1
            st.append(freq)
        return res

x  = Solution()
print(x.minDeletions("aaabbbcc"))