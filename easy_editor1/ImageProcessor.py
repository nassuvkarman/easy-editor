from PIL import Image, ImageFilter
import os 
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


class ImageProcessor:
    def __init__(self,ui):
        self.current_image: Image = None
        self.filename: str = None
        self.modified_folder = "modified"
        self.workdir = ""
        self.ui = ui

    def open(self, dir, fn):
        self.workdir = dir
        self.filename = fn
        self.path = os.path.join(self.workdir, self.filename)
        self.current_image = Image.open(self.path)
        

    def show(self):
        self.ui.photo_lb.hide()

        pixmapimage = QPixmap(self.path) 
        w,h = self.ui.photo_lb.width(), self.ui.photo_lb.height()
        pixmapimage.scaled(w,h, Qt.AspectRatioMode.KeepAspectRatio) 
        self.ui.photo_lb.setPixmap(pixmapimage)
        self.ui.photo_lb.show()

    def save (self):
        save_path = os.path.join(self.workdir, self.modified_folder)

        if not os.path.isdir(save_path):
            os.mkdir(save_path)
        
        full_path = os.path.join(save_path,self.filename)
        self.current_image.save(full_path)

    def do_bw(self):
        self.current_image = self.current_image.convert("L")
        self.save()
        new_path = os.path.join(self.workdir, self.modified_folder, self.filename)
        self.path = new_path
        self.show()

    def do_left(self):
        self.current_image = self.current_image.Transpose(Image.ROTATE_270)
        self.save()

    def do_mirror(self):
        self.current_image = self.current_image.transpose(Image.FLIP_LEFT_RIGHT)