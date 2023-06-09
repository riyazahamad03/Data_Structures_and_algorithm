class solution:
    def nextGreatestLetter(self , letters:list[str], target : str):
        l , r = 0 , len(letters) - 1
        while l <= r:
            m = (l + r)//2
            if letters[m] <= target:
                l = m + 1
            else:
                r = m - 1
        return letters[m] if m < len(letters) else letters[0]
x = solution()
print(x.nextGreatestLetter(letters = ["c","f","j"], target = "a"))