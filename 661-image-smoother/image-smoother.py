class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        sm_image = []
        for items in range(len(img)):
            sm_image.append([0]*len(img[0]))


        for i in range(len(img)):
            for j in range(len(img[0])):
                sum = 0
                count = 0
                for x in (i-1,i,i+1):
                    for y in (j-1,j,j+1):

                        if 0 <= x < len(img) and 0 <= y < len(img[0]):
                            count += 1
                            sum = sum + img[x][y]
                avg = (sum // count)
                sm_image[i][j] = avg            





        return sm_image