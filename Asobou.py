from PIL import Image

from util.split_img import split_img_vertical, split_img_horizontal
from util.combine_img import combine_img_horizontal, combine_img_vertical


class Asobou:
    def __init__(self, fp: str, img_name: str):
        self.fp = fp
        self.img_name = img_name
        self.img = Image.open(fp)
        self.split_num = len(img_name)

    def gen_img_vertical(self, space_width: int, object_string: list[int]):
        splitted_images = split_img_vertical(self.img, self.split_num)
        initial_img = splitted_images[object_string[0]]
        res_img = initial_img

        for object_string_index in object_string[1:]:
            next_img = splitted_images[object_string_index]
            res_img = combine_img_vertical(res_img, next_img, space_width)

        return res_img

    def gen_img_horizontal(self, space_width: int, object_string: list[int]):
        splitted_imgs = split_img_horizontal(self.img, len(self.img_name))
        initial_img = splitted_imgs[object_string[0]]
        res_img = initial_img

        for object_string_index in object_string[1:]:
            next_img = splitted_imgs[object_string_index]
            res_img = combine_img_horizontal(res_img, next_img, space_width)

        return res_img
