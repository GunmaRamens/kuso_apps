from PIL import Image


def split_img_vertical(
    raw_img: Image.Image,
    split_num: int,
):
    width, hight = raw_img.size
    split_width = hight / split_num
    splitted_images = []

    for order in range(split_num):
        offset = split_width * order

        crop_box = (left, upper, right, downer) = (
            0, offset, width, offset + split_width
        )

        cropped_img = raw_img.crop(crop_box)
        splitted_images.append(cropped_img)

    return splitted_images


def split_img_horizontal(
    raw_img: Image.Image,
    split_num: int
):
    width, hight = raw_img.size
    split_width = width / split_num
    splitted_images = []

    for order in range(split_num):
        offset = split_width * order

        crop_box = (left, upper, right, downer) = (
            offset, 0, offset + split_width, hight
        )

        cropped_img = raw_img.crop(crop_box)
        splitted_images.append(cropped_img)

    return splitted_images
