#problem 1007 / minimum domino rotations for equal row
class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        def check(n):
            rotatea = rotateb = 0
            for i in range(len(A)):
                if A[i] != n and B[i] != n:
                    return -1
                if A[i] != n:
                    rotatea += 1
                elif B[i] != n:
                    rotateb += 1
            return min(rotatea,rotateb)
        rotation = check(A[0])
        if rotation != -1 or A[0] == B[0]:
            return rotation
        return check(B[0])