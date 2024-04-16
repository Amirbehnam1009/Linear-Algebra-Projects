import matplotlib.pyplot as matplotlibpyplot
import matplotlib.image as matplotlibimage
import numpy as np



def render(k,
           ur,sr,vr,
           ug,sg,vg,
           ub,sb,vb):
    print("creating... k is ", k)
    mr = np.dot(ur[:,:k],np.dot(np.diag(sr[:k]),vr[:k,:]))
    mg = np.dot(ug[:,:k],np.dot(np.diag(sg[:k]),vg[:k,:]))
    mb = np.dot(ub[:,:k],np.dot(np.diag(sb[:k]),vb[:k,:]))
    img2 = np.zeros(img.shape)
    img2[:,:,0] = mr
    img2[:,:,1] = mg
    img2[:,:,2] = mb
    for i1, rrr in enumerate(img2):
         for i2, ccc in enumerate(rrr):
             for i3, value in enumerate(ccc):
                 if value < 0:
                     img2[i1,i2,i3] = abs(value)
                 if value > 255:
                     img2[i1,i2,i3] = 255
    img3 = img2.astype(np.uint8);
    return img3
 


k = [10,150,250]
path = input("Enter image path: ")

for x in range(0,len(k)):
    print(k[x])
print("reading...")
img = matplotlibimage.imread(path)
r = img[:, :, 0]
g = img[:, :, 1]
b = img[:, :, 2]
matplotlibpyplot.figure(1)
matplotlibpyplot.imshow(img)
print("r: " , len(r), "x ", len(r[0]))
print("g: " , len(g), "x ", len(g[0]))
print("b: " , len(b), "x ", len(b[0]))
print("run svd...")
ur,sr,vr = np.linalg.svd(r,full_matrices=False)
ug,sg,vg = np.linalg.svd(g,full_matrices=False)
ub,sb,vb = np.linalg.svd(b,full_matrices=False)


for x in range(0,len(k)):
  im = render(k[x],ur,sr,vr,ug,sg,vg,ub,sb,vb);
  matplotlibpyplot.figure(x+1)
  matplotlibpyplot.title("k is "+str( k[x]))
  matplotlibpyplot.imshow(im)



matplotlibpyplot.show()
 