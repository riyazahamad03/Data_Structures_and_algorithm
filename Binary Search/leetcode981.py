class TimeMap:
    def __init__(self) -> None:
        self.hashStore = {}
    def set(self, key : str , value : str , timestamp : int):
        if key not in self.hashStore:
            self.hashStore[key] = []
        self.hashStore[key].append([value , timestamp])
    def get(self, key , timestamp):
        res = ""
        val = self.hashStore.get(key , [])
        l , r = 0 , len(val)
        while l <= r:
            m = (l + r)//2
            if val[m][1] <= timestamp:
                l = m + 1
                res = val[m][0]
            else:
                r = m - 1
        return res
x = TimeMap()

