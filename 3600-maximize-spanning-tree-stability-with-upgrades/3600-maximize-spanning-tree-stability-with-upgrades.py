class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        class DSU:
            def __init__(self, size):
                self.parent = list(range(size))
                self.rank = [1] * size
                self.comps = size
                
            def find(self, i):
                root = i
                while root != self.parent[root]:
                    self.parent[root] = self.parent[self.parent[root]] # Path halving
                    root = self.parent[root]
                return root
                
            def union(self, i, j):
                root_i = self.find(i)
                root_j = self.find(j)
                if root_i != root_j:
                    if self.rank[root_i] > self.rank[root_j]:
                        self.parent[root_j] = root_i
                    elif self.rank[root_i] < self.rank[root_j]:
                        self.parent[root_i] = root_j
                    else:
                        self.parent[root_j] = root_i
                        self.rank[root_i] += 1
                    self.comps -= 1
                    return True
                return False

        must_edges = []
        free_edges = []
        max_possible = 0
        min_must_s = float('inf')

        # 1. Base Setup & Preliminary Integrity Check
        baseline_dsu = DSU(n)
        for u, v, s, m in edges:
            max_possible = max(max_possible, s * (2 if m == 0 else 1))
            if m == 1:
                must_edges.append((u, v, s))
                min_must_s = min(min_must_s, s)
                if not baseline_dsu.union(u, v):
                    return -1  # A cycle in the mandatory edges means no valid tree can exist
            else:
                free_edges.append((u, v, s))
        
        for u, v, s in free_edges:
            baseline_dsu.union(u, v)
            
        if baseline_dsu.comps > 1:
            return -1  # Even using all edges, the graph is completely disconnected

        # 2. The Verification Function
        def canAchieve(X: int) -> bool:
            # If our target is higher than a mandatory edge, it's instantly invalid
            if X > min_must_s:
                return False
                
            dsu = DSU(n)
            
            # Step A: Lock in all mandatory edges (Cost 0)
            for u, v, s in must_edges:
                dsu.union(u, v)
                
            # Step B: Greedily take all edges that naturally meet the target (Cost 0)
            for u, v, s in free_edges:
                if s >= X:
                    dsu.union(u, v)
                    
            # Step C: Fill the remaining gaps with upgradeable edges (Cost 1)
            upgrades_used = 0
            for u, v, s in free_edges:
                if s < X and s * 2 >= X:
                    if dsu.union(u, v): # Only count the upgrade if it successfully connected new components
                        upgrades_used += 1
                        if upgrades_used > k:
                            return False
                            
            return dsu.comps == 1

        # 3. Binary Search for the Maximum Minimum Stability
        low = 0
        high = max_possible
        ans = -1
        
        while low <= high:
            mid = (low + high) // 2
            if canAchieve(mid):
                ans = mid
                low = mid + 1  # Try to push for a higher stability
            else:
                high = mid - 1 # The current stability is too ambitious, scale back
                
        return ans