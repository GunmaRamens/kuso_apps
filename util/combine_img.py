from PIL import Image


def combine_img_vertical(
    primary_img: Image.Image,
    secondary_img: Image.Image,
    space_width,
):
    res_width = max(primary_img.width, secondary_img.width)
    res_hight = primary_img.height + secondary_img.height + space_width

    res = Image.new("RGB", (res_width, res_hight), (255, 255, 255))

    res.paste(primary_img, (0, 0))
    res.paste(secondary_img, (0, primary_img.height + space_width))
    return res


def combine_img_horizontal(
    primary_img: Image.Image,
    secondary_img: Image.Image,
    space_width,
):
    res_width = primary_img.width + secondary_img.width + space_width
    res_hight = max(primary_img.height, secondary_img.height)

    res = Image.new("RGB", (res_width, res_hight), (255, 255, 255))

    res.paste(primary_img, (0, 0))
    res.paste(secondary_img, (primary_img.width + space_width, 0))
    return res
