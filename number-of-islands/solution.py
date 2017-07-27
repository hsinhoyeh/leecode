class Solution(object):
    num_island = 0
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        num_island = 0

        mp = {}
        for x in range(0, len(grid)):
            for y in range(0, len(grid[0])):
                if self.isConnected(grid, x, y):
                    label = self.getLabel(mp, x, y)
                    self.setLabel(mp, x,y, label)
        valset = set()
        for key in mp.keys():
            valset.add(mp[key])
        return len(valset)


    def setLabel(self, mp, x, y, val):
        pos = "%d-%d" % (x, y)
        mp[pos] = val

    def getLabel(self, mp, x, y):
        left = "%d-%d" % (x-1, y)
        right = "%d-%d" % (x+1, y)
        top = "%d-%d" % (x, y-1)
        bottom = "%d-%d" % (x, y+1)

        lset = set()

        if left in mp:
            lset.add(mp[left])
        if right in mp:
            lset.add(mp[right])
        if top in mp:
            lset.add(mp[top])
        if bottom in mp:
            lset.add(mp[bottom])

        if len(lset) == 0:
            label = self.num_island
            self.num_island = self.num_island + 1
            return label

        # if we have multiple set, unify them
        keep = lset.pop()
        while len(lset) > 0:
            frm = lset.pop()
            for key in mp.keys():
                if mp[key] == frm:
                    mp[key] = keep
        return keep

    def isConnected(self, grid, x, y):
        if grid[x][y] == "0":
            return False
        else:
            return True

