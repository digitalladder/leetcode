#problem 1233 / remove sub-folders from the filesystem
class Solution(object):
    def removeSubfolders(self, folder):
        folder.sort()
        cleaned = [folder[0]]  # first folder is shortest or unique
        prev, prev_n = folder[0]+"/", len(folder[0])+1
        for each in folder[1:]:
            if each[:prev_n] != prev:
                cleaned.append(each)
                prev, prev_n = each + "/", len(each)+1
        return cleaned
