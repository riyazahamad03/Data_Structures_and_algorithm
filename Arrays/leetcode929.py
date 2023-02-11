class solution:
    def numUniqueEmails(self,emails:list[str]):
        UniqueSet = set()
        for em in emails:
            i,loc = 0,""
            while (em[i] != "@" and em[i] != "+"):
                if em[i]!=".":
                    loc += em[i]
                i += 1
            while em[i] != "@":
                i += 1
            dom = em[i+1 :]
            UniqueSet.add((loc,dom))
        return len(UniqueSet)
x = solution()
print(x.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))