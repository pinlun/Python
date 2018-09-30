#text count
#%%
f = open("/Users/pinlunhuang/Desktop/PinTech/hw0/words.txt", 'r')
out = open("/Users/pinlunhuang/Desktop/PinTech/hw0/output.txt", "w")
lines = f.readline()
text = []
count = []
lines = lines.split(" ")
for i in lines:
    if i not in text:
        text.append(i)
        count.append(1)
    else:
        count[text.index(i)] = count[text.index(i)] + 1

for i in range(len(text)):
    out.write("%s %s %s\n" % (text[i], i, count[i]))

#圖片淡化
#%%
from PIL import Image
im = Image.open('/Users/pinlunhuang/Desktop/PinTech/hw0/westbrook.jpg')
source = im.split()
R, G, B = 0, 1, 2
source[R].paste(source[R].point(lambda i: i * 0.5))
source[G].paste(source[G].point(lambda i: i * 0.5))
source[B].paste(source[B].point(lambda i: i * 0.5))
im = Image.merge(im.mode, source)
im.save('/Users/pinlunhuang/Desktop/PinTech/hw0/output.jpg')

