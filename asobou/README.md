# Asobou
[これ](https://dic.nicovideo.jp/a/%E2%97%8B%E2%97%8B%E3%81%A7%E3%81%82%E3%81%9D%E3%81%BC%E3%81%86)をいいかんじに作りたかった
## サンプルコード
### 最初のやつ
```python
from Asobou import Asobou

IMG_PATH = "./img/Monalisa.png"
IMG_NAME = "Monalisa"
SPACE_PX = 30

asobou = Asobou(IMG_PATH, IMG_NAME)
image = asobou.gen_img_vertical(SPACE_PX, list(range(len(IMG_NAME))))
image.save("./img/hoge.png")
```
[Monalisa.png](/asobou/img/Monalisa.png)  
![Monalisa.png](/asobou/img/Monalisa.png)  
[hoge.png](/asobou/img/hoge.png)  
![hoge.png](/asobou/img/hoge.png)  

### いなり
```python
from Asobou import Asobou

IMG_PATH = "./img/Monalisa.png"
IMG_NAME = "Monalisa"
SPACE_PX = 30

table = dict()
for index, char in enumerate(IMG_NAME):
    table[char] = index

inali = [table[c] for c in "inali"]

asobou = Asobou(IMG_PATH, IMG_NAME)
image = asobou.gen_img_vertical(SPACE_PX, inali)
image.save("./img/inali.png")
```
[inali.png](/asobou/img/inali.png)  
![inali.png](/asobou/img/inali.png)  
