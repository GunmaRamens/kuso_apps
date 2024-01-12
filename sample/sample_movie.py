from AsobouMovie import AsobouMovie
from Asobou import Asobou

if __name__ == "__main__":
    asobou = Asobou("./img/Monalisa.png", "monalisa")
    asobou_movie = AsobouMovie(asobou, ["inali", "imo", "nimono"])
    asobou_movie.gen_imgs_vertical(30).export_video("sample.mp4", 24)
