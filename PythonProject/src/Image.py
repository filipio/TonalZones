import cv2 as cv
from PyQt5.QtGui import QImage
class Image:
  """
  Image is a class responsible for doing operations on an image. Class should be initialized when
  new image from file is required. Every operation that is operating on an image should be contained
  in this class.
  Insert necessery methods below.
  """
  def __init__(self, path):
    self.image = cv.imread(path)
  
  def ui_image(self):
    frame = cv.cvtColor(self.image, cv.COLOR_BGR2RGB)
    return QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format.Format_RGB888)

  def save(self,file):
    cv.imwrite(file,self.image)

  def load(self,path):
    file_name = QFileDialog.getOpenFileName(self, "Open File",
                                "/home",
                                "Images (*.png *.xpm *.jpg)")[0]
    self.image = cv.imread(file_name)
    pass

  def rotate(self):
    pass

  def zoom_in(self):
    pass

  def zoom_out(self):
    pass


  # modify image methods        