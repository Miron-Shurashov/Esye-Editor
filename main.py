import os
from PyQt5.QtWidgets import ()

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PIL import Image
from PIL import ImageFilter
from PIL. ImageFilter import SHARPEN

app = QApplication([])
win = QWidget()
win. resize(700, 500)
win.setWindowTitle("Easy Editor")
lb_image = QLabel("Картинка")
btn_dir = QPushButton("Выбрать папку")

lw_files = QListWidget()
btn_left = QPushButton("Лево")
btn_right = QPushButton("Право")
btn_flip = QPushButton("Зеркало")
btn_sharp = QPushButton("Резкость")
btn_bw = QPushButton("Ч/Б')
btn_save = QPushButton("Coхранить")
btn_reset = QPushButton("Сбросить фильтры")

row = HBoxLayout()
col1 = QVBoxLayout()
col2 - QVBoxLayout()
col1.addWidget(btn_dir)
col1.addwidget(lw_files)
col2.addwidget(lb_image, 95)
row_tools = QHBoxLayout()
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addwidget(btn_sharp)
row_tools.addWidget(btn_bw)
row_tools.addWidget(btn_reset)
col2.addLayout(row_tools)

row. addLayout(col1, 20)
row. addLayout(col2, 80)
win.setLayout(row)

workdir = ''

def filter(files, extentions):
    result = []
    for filename in files:
        for ext in extentions
        if filename.endswith(ext):
           result.append(filename)
    return result

def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def showFilenamesList():
    extentions = ['.png', '-jpg', '-jpeg', '.gif', '.bmp']
    chooseWorkdir()
    filenames = filter(os.listdir(workdir), extentions)
    lw_files.clear()
    for filename in filenames:
        lw_files.addItem(filename)

class ImageProcessor():
    def ＿init＿(self):
        self.image = None
        self. dir = None
        self.filename = None
        self.save_dir = "Modified/"
        self.original_image = None

    def loadImage(self, directory, filename):
        self.dir = directory
        self.filename = filename
        image_path = os.path.join(directory, filename)
        self.image = Image.open(image_path)
        self.original_image = self.image.copy()

    def do_bw(self);
        self.image = self,image.convert('L')
        self. SaveImage()
        image_path = 05.path.join(self.dir, self.save_dir, self.filename
        self,showImage(image_path)

    def do_flip(self);
        self,image = self, image, transpose(Image, FLIP_LEFT_RIGHT)
        self, SaveImage()
        image_path = os.path, join(workdir, self, save_dir, self,filename)
        self,showImage(image_path)

    def do_sharpen(self);
        self. image = self,image.filter(SHARPEN)
        self. SaveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename) self showImage(image path)
        ain. py

    def do_left(self):
        self.image = self.image.rotate(90)
        self. SaveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def do_right(self):
        self.image = self.image.rotate(-90)
        self.SaveImage()
        image_path = os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

     def resetImage(self):
        self.image = self.original_image.copy()
        self.showImage(os.path.join(workdir, self.filename))
        def SaveImage(self):
        path = os.path.join(self.dir, self.save_dir)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)

    def showImage(self, path):
        pixmapimage = QPixmap(path)
        label_width, label_height = lb_image.width(), lb_image.height()
        scaled_pixmap = pixmapimage.scaled(label_width, label_height, Qt.Kee;
        lb_image.setPixmap(scaled_pixmap)
        lb_image.setVisible(True)

    def showChosenImage():
        if lw_files.currentRow() >= 0:
            filename = lw_files.currentItem().text()
            workimage.loadImage(workdir, filename)
            image_path = os.path.join(workimage.dir, workimage.filename)
            workimage.showImage(image_path)
            workimage = ImageProcessor()

lw_files.currentRowChanged.connect(showChosenImage)
btn_bw.clicked.connect(workimage.do_bw)
btn_left.clicked.connect(workimage.do_left)
btn_right.clicked.connect(workimage.do_right)
btn_sharp.clicked.connect(workimage.do_sharpen)
btn_reset.clicked.connect(workimage.resetImage)
btn_save.clicked.connect(workimage. SaveImage)
btn_flip.clicked.connect(workimage.do_flip)

win. show()
app.exec()