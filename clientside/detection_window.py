from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtCore import QThread, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap
import cv2
import numpy as np
import time
import requests
from detection import Detection #,PoseDetection


class DetectionWindow(QMainWindow):
	def __init__(self):
		super(DetectionWindow, self).__init__()	
		loadUi('UI/detection_window.ui', self)

		self.stop_detection_button.clicked.connect(self.close)

	
	def create_detection_instance(self, token, location, receiver):
		
		#change below to Detection if using normal yolo.
		self.detection = Detection(token, location, receiver)
	
	@pyqtSlot(QImage)
	def setImage(self, image):
		self.label_detection.setPixmap(QPixmap.fromImage(image))

	
	def start_detection(self):
		self.detection.changePixmap.connect(self.setImage)
		self.detection.start()
		self.show()

	
	def closeEvent(self, event):
		self.detection.running = False
		event.accept()

