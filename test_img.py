from PIL import Image
import numpy as np
#src=Image.open("aa.png")
#print(src.mode)
# src=src.convert('P')
# print(src.mode)

label="bb.png"
lbl = np.asarray(Image.open(label))
print(lbl.dtype)

print(np.unique(lbl))
print(lbl.shape)

# k=np.zeros((3,3),np.uint8)
# k[2][1]=3
# print(k)