import cv2
from PIL import Image
image_cat = "cat.jpeg"
cat = Image.open(image_cat)
glasses = Image.open("glasses.png")
cigarette = Image.open("Cygared.png")
cat = cat.convert("RGBA")
glasses = glasses.convert("RGBA")
cigarette = cigarette.convert("RGBA")
cat_cascade = cv2.CascadeClassifier("haarcascade_frontalcatface_extended.xml")
img = cv2.imread(image_cat)
cat_face = cat_cascade.detectMultiScale(img)
print(cat_face)

for (x,y, w, h) in cat_face:
    glasses = glasses.resize((w, int(h/3)))
    cigarette = cigarette.resize((w, h))
    cat.paste(glasses, (x, int(y+h/4)), glasses)
    cat.paste(cigarette, (x - 15, int(y + h / 4)), cigarette)





cat.save("kat.png")
kat = cv2.imread("kat.png")
cv2.imshow('cat', kat)
cv2.waitKey(0)