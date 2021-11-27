import cv2,copy
import numpy as np
img = cv2.imread('123.png')
img[img==255]=254
img2=img
img3=copy.deepcopy(img2)

m=[]
div=0
typeMat=int(input('Выберите матрицу '))

if(typeMat==1):
  div=9
  m=[1,1,1,1,1,1,1,1,1]
if(typeMat==2):
  div=10
  m=[1,1,1,1,2,1,1,1,1]
if(typeMat==3):
  div=16
  m=[1,2,1,2,4,2,1,2,1]
if(typeMat==4):
  div=16
  m=[2,1,2,1,4,1,2,1,2]
if(typeMat==5):
  div=1
  m=[1,1,1,1,-2,1,-1,-1,-1]
if(typeMat==6):
  div=1
  m=[-1,-1,-1,-1,9,-1,-1,-1,-1]
if(typeMat==7):
  div=1
  m=[1,-2,1,-2,5,-2,1,-2,1]
if(typeMat==8):
  div=1
  m=[0,-1,0,-1,4,-1,0,-1,0]
if(typeMat==9):
  div=1
  m=[-1,-1,-1,-1,8,-1,-1,-1,-1]
if(typeMat==10):
  div=1
  m=[1,-2,1,-2,4,-2,1,-2,1]




for i in range(0,img2.shape[0]):
  for j in range(0,img2.shape[1]):
    jj=j
    ii=i
    if jj==img2.shape[1]-1: jj=-1
    if ii==img2.shape[0]-1: ii=-1
    colorij=[img2[i-1,j-1],img2[i-1,j],img2[i-1,jj+1],img2[i,j-1],img2[i,j],img2[i,jj+1],img2[ii+1,j-1],img2[ii+1,j],img2[ii,jj+1]]
    r=(colorij[0][0]*m[0]+colorij[1][0]*m[1]+colorij[2][0]*m[2]+colorij[3][0]*m[3]+colorij[4][0]*m[4]+colorij[5][0]*m[5]+colorij[6][0]*m[6]+colorij[7][0]*m[7]+colorij[8][0]*m[8])/div
    g=(colorij[0][1]*m[0]+colorij[1][1]*m[1]+colorij[2][1]*m[2]+colorij[3][1]*m[3]+colorij[4][1]*m[4]+colorij[5][1]*m[5]+colorij[6][1]*m[6]+colorij[7][1]*m[7]+colorij[8][1]*m[8])/div
    b=(colorij[0][2]*m[0]+colorij[1][2]*m[1]+colorij[2][2]*m[2]+colorij[3][2]*m[3]+colorij[4][2]*m[4]+colorij[5][2]*m[5]+colorij[6][2]*m[6]+colorij[7][2]*m[7]+colorij[8][2]*m[8])/div
    while(r<0 or r>256):
      if r<0:
        r*=-1
      if r>256:
        r= 256-(r-256)
    while(g<0 or g>256):
      if g<0:
        g*=-1
      if g>256:
        g= 256-(g-256)
    while(b<0 or b>256):
      if b<0:
        b*=-1
      if b>256:
        b= 256-(b-256)
    img3[i,j]=(r,g,b)

cv2.imwrite('1.png',img3)
#open cv method
kernel = np.array([[m[0],m[1],m[2]],[m[3],m[4],m[5]],[m[6],m[7],m[8]]])
dst = cv2.filter2D(img,-1,kernel)

cv2.imwrite('2.png',dst)