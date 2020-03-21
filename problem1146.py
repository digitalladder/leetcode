#problem 1146 / snapshot array
class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.length = length
        self.snapid = 0
        self.array = [[[-1,0]] for i in range(self.length)]

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0 or index >= self.length:
            return
        self.array[index].append([self.snapid,val])

    def snap(self):
        """
        :rtype: int
        """
        self.snapid += 1
        return self.snapid-1

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        i = bisect.bisect(self.array[index],[snap_id+1])-1
        return self.array[index][i][1]

# more faster way
class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """

        self.snaps = collections.defaultdict(dict)
        self.n_snap = 0

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.snaps[self.n_snap][index] = val        #只记录变化的值

        
    def snap(self):
        """
        :rtype: int
        """
        self.snaps[self.n_snap+1]=self.snaps[self.n_snap].copy()    #浅拷贝，self.snaps是字典，拷贝后只有父对象（键值）是独立的，内部子对象（value）是引用
        self.n_snap += 1                                            #这里直接对value内容拷贝，所以新值刷新后，上一个snapsid里的值维持原样
        return self.n_snap-1

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        return self.snaps[snap_id].get(index, 0)

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)