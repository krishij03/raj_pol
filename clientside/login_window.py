from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.uic import loadUi
import webbrowser
import requests
import json
from settings_window import SettingsWindow


class LoginWindow(QMainWindow):
	def __init__(self):
		super(LoginWindow, self).__init__()
		loadUi('UI/login_window.ui', self)

		self.register_button.clicked.connect(self.go_to_register_page)
		self.login_button.clicked.connect(self.login)

		self.popup = QMessageBox()
		self.popup.setWindowTitle("Failed")

		self.show()

	
	def go_to_register_page(self):
		webbrowser.open('http://127.0.0.1:8000/register/')

	
	def login(self):
		try:
			url = 'http://127.0.0.1:8000/api/get_auth_token/'
			response = requests.post(url, data={'username': self.username_input.text(),'password': self.password_input.text()})
			json_response = json.loads(response.text)

			
			if response.ok:
				
				self.open_settings_window(json_response['token'])
			
			else:
				
				self.popup.setText("Username or Password is not correct")
				self.popup.exec_()
		except:
			
			self.popup.setText("Unable to access server")
			self.popup.exec_()
	
	
	def open_settings_window(self, token):
		self.settings_window = SettingsWindow(token)
		self.settings_window.displayInfo()
		self.close()
