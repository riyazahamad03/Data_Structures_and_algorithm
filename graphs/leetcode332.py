class solution:
    def reconstructItenary(self, tickets: list[list[str]]):
        adj = {source: [] for source, _ in tickets}
        tickets.sort()
        for src, dest in tickets:
            adj[src].append(dest)

        res = ['JFK']

        def dfs(node):
            if len(res) == len(tickets) + 1:
                return True
            if node not in adj:
                return False

            for idx, v in enumerate(adj[node]):
                adj[node].pop(idx)
                res.append(v)

                if dfs(v):
                    return True

                adj[node].insert(idx, v)
                res.pop()
            return False
        dfs("JFK")
        return res


x = solution()
print(x.reconstructItenary(tickets=[["JFK", "SFO"], ["JFK", "ATL"], [
      "SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
