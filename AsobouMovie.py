from Asobou import Asobou
from PIL import Image
from moviepy.editor import *
from numpy import asarray

class AsobouMovie:
    def __init__(self,asobou:Asobou ,wordlist: list[str] ) -> None:
        self.asobou = asobou

        self.img_name:dict[str,int] = dict()
        for i, name in enumerate(asobou.img_name):
            self.img_name[name] = i

        self.words = dict[str, list[int]]()
        for word in wordlist:
            self.words[word] = [self.img_name[char] for char in word]
        self.video = None
    
    def gen_imgs_vertical(self, space_width: int):

        # 生成された画像たち
        imgs: list[Image.Image] = []
        for word in self.words.values():
            imgs.append(self.asobou.gen_img_vertical(space_width, word))

        clips:list(ImageClip) = []
        for img in imgs:
            clips.append(ImageClip(asarray(img)).set_duration('00:00:01.00'))

        self.video = concatenate_videoclips(clips, method="compose")
        return self

    def export_video(self, fp: str, fps: int):
        if (self.video == None):
            raise Exception("You have to call gen_imgs_vertical before export_video")
        
        self.video.write_videofile(fp, fps=fps)


