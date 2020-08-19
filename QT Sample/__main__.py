import numpy as np
import cv2 # pip install opencv-python

#GUI Libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QKeySequence, QPalette, QColor,QPixmap,QImage
from PyQt5.QtCore import Qt

from PIL import Image, ImageQt

app = QApplication([])

# Force the style to be the same on all OSs:
app.setStyle("Fusion")

# Now use a palette to switch to dark colors:
palette = QPalette()
palette.setColor(QPalette.Window, QColor(53, 53, 53))
palette.setColor(QPalette.WindowText, Qt.white)
palette.setColor(QPalette.Base, QColor(25, 25, 25))
palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
palette.setColor(QPalette.ToolTipBase, Qt.white)
palette.setColor(QPalette.ToolTipText, Qt.white)
palette.setColor(QPalette.Text, Qt.white)
palette.setColor(QPalette.Button, QColor(53, 53, 53))
palette.setColor(QPalette.ButtonText, Qt.white)
palette.setColor(QPalette.BrightText, Qt.red)
palette.setColor(QPalette.Link, QColor(42, 130, 218))
palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
palette.setColor(QPalette.HighlightedText, Qt.black)
app.setPalette(palette)

# The rest of the code is the same as for the "normal" text editor.

app.setApplicationName("Filmmmmh")
text = QPlainTextEdit()
x, y, w, h = 100, 100, 200, 200
label = QLabel()
label.setGeometry(x, y, w, h)


class MainWindow(QMainWindow):
    def closeEvent(self, e):
        if not text.document().isModified():
            return
        answer = QMessageBox.question(
            window, None,
            "You have unsaved changes. Save before closing?",
            QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel
        )
        if answer & QMessageBox.Save:
            save()
        elif answer & QMessageBox.Cancel:
            e.ignore()

window = MainWindow()
window.setCentralWidget(text)

file_path = None

menu = window.menuBar().addMenu("&File")
open_action = QAction("&Open")
def open_file():
    global file_path
    path = QFileDialog.getOpenFileName(window, "Open")[0]
    if path:
        #text.setPlainText(open(path).read())
        file_path = path
        pixmap = pil2pixmap(file_path)
        label.setPixmap(pixmap)
        label.move(10, 10)
        label.show()
open_action.triggered.connect(open_file)
open_action.setShortcut(QKeySequence.Open)
menu.addAction(open_action)

save_action = QAction("&Save")
def save():
    if file_path is None:
        save_as()
    else:
        with open(file_path, "w") as f:
            f.write(text.toPlainText())
        text.document().setModified(False)
save_action.triggered.connect(save)
save_action.setShortcut(QKeySequence.Save)
menu.addAction(save_action)

save_as_action = QAction("Save &As...")
def save_as():
    global file_path
    path = QFileDialog.getSaveFileName(window, "Save As")[0]
    if path:
        file_path = path
        save()
save_as_action.triggered.connect(save_as)
menu.addAction(save_as_action)

close = QAction("&Close")
close.triggered.connect(window.close)
menu.addAction(close)

#Remove Scratches
image_menu = window.menuBar().addMenu("&Image")
remove_scratches_action = QAction("&Remove Scratches")
image_menu.addAction(remove_scratches_action)
def removes_scratches():
    #https://docs.opencv.org/3.3.1/df/d3d/tutorial_py_inpainting.html
    img = cv2.imread('messi_2.jpg')
    mask = cv2.imread('mask2.png',0)
    dst = cv2.inpaint(img,mask,3,cv2.INPAINT_TELEA)
    cv2.imshow('dst',dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
remove_scratches_action.triggered.connect(removes_scratches)


#About Box
help_menu = window.menuBar().addMenu("&Help")
about_action = QAction("&About")
help_menu.addAction(about_action)
def show_about_dialog():
    text = "<center>" \
           "<h1>Filmmmh Utility</h1>" \
           "&#8291;" \
           "<img src=icon.svg>" \
           "</center>" \
           "<p>Version 31.4.159.265358<br/>" \
           "Copyright &copy; Company Inc.</p>"
    QMessageBox.about(window, "About Text Editor", text)
about_action.triggered.connect(show_about_dialog)


def pil2pixmap(file_path):
    im = Image.open(fp = file_path)
    imageqt = ImageQt.ImageQt(im)
    #if im.mode == "RGB":
   #     pass
   # elif im.mode == "L":
    #    im = im.convert("RGBA")
   # data = im.tostring('raw', "RGBA")
    #qim = QtGui.QImage(data, im.size[0], im.size[1], QtGui.QImage.Format_ARGB32)
    pixmap = QPixmap.fromImage(imageqt,Qt.AutoColor)
    return pixmap 

window.show()
app.exec_()