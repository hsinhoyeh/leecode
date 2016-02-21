import sys

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        
        # rooted nodes should be in
        # 1. longtest path
        # 2. non-leaf node (where leaf node refers to the node with one edge)

        # build a map['v1'] = ['v2', 'v3']
        ajlist = {} # adjacency list
        for edge in edges:
            head = edge[0]
            tail = edge[1]
            if head not in ajlist:
                ajlist[head] = []
            ajlist[head].append(tail)

            head, tail = tail, head
            if head not in ajlist:
                ajlist[head] = []
            ajlist[head].append(tail)

        # then traverse the tree to find out longest path with dfs
        traced = {}
        longest = None
        for start in ajlist.keys():
            if start in traced:
                continue

            # start from leaf nodes
            if len(ajlist[start]) > 1:
                continue
            subpathes = self.dfs(ajlist, None, start)
            subpath = subpathes[0]
            traced[subpath[0]] = True
            traced[subpath[-1]] = True
            if longest == None or len(longest) < len(subpath):
                longest = subpath

        # find out depth of a node in longest path
        depth_per_node={}
        for index in range(0, len(longest)):
            front = index
            end = len(longest) - front - 1
            depth_per_node[longest[index]] = max(front, end)

        # find roots which has minimum depth
        min_dist = sys.maxint
        roots = []
        for index in range(1, len(longest)-1):
            node = longest[index]
            if min_dist == depth_per_node[node]:
                roots.append(node)
            elif min_dist > depth_per_node[node]:
                min_dist = depth_per_node[node]
                roots = [node]
        return sorted(roots)

    def dfs(self, ajlist, prestart, start):
        if len(ajlist[start]) == 1 and ajlist[start][0] ==prestart:
            return [[start]] # reached to the end

        longest = []
        for next_node in ajlist[start]:
            # avoid cyclic
            if next_node == prestart:
                continue
            next_subpathes = self.dfs(ajlist, start, next_node)
            for next_subpath in next_subpathes:
                if len(longest) < len(next_subpath):
                    longest = next_subpath
                    longest.append(start)
        return [longest]
