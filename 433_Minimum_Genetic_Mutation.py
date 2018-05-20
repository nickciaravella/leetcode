# https://leetcode.com/problems/minimum-genetic-mutation/description/
# Medium

# Breadth-first-search, all edges have weight = 1
# start = starting node
# end = node searching for
# bank = valid edges between nodes
class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        queue = [(start, 0)]
        seen = {start}
        while queue:
            gene, moves = queue.pop()
            if gene == end:
                return moves

            for i in range(len(gene)):
                for c in "ACGT":
                    next_gene = gene[:i] + c + gene[i+1:]
                    if next_gene in bank and next_gene not in seen:
                        queue.insert(0, (next_gene, moves+1))
                        seen.add(next_gene)
        return -1
