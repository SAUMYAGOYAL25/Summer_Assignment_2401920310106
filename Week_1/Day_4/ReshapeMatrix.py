class Solution:
    def matrixReshape(self,mat,r,c):
        m=len(mat)
        n=len(mat[0])
        if m*n!= r*c:
            return mat
        result=[]
        temp=[]
        for row in mat:
            for num in row:
                temp.append(num)
                if len(temp)==c:
                    result.append(temp)
                    temp=[]
        return result                
