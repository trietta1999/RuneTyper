from PyQt5 import QtCore, QtGui, QtWidgets
import sys, form
import keyboard_monitor, keyboard_control

MainWindow = tray_icon = None

def hide():
	MainWindow.hide()
	tray_icon.showMessage(
		"Rune Typer",
		"Chương trình đã ẩn",
		QtWidgets.QSystemTrayIcon.Information,
		2000
	)
	
def setup():
	global MainWindow, tray_icon
	
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = form.Ui_MainWindow()
	ui.setupUi(MainWindow)
	ui.button.clicked.connect(hide)

	tray_icon = QtWidgets.QSystemTrayIcon(MainWindow)
	icon = QtGui.QIcon()
	icon.addPixmap(QtGui.QPixmap(":/icon/runes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	tray_icon.setIcon(icon)

	show_action = QtWidgets.QAction("Hiện cửa sổ")
	quit_action = QtWidgets.QAction("Thoát")
	show_action.triggered.connect(lambda: MainWindow.show())
	quit_action.triggered.connect(app.quit)

	tray_menu = QtWidgets.QMenu()
	tray_menu.addAction(show_action)
	tray_menu.addAction(quit_action)
	tray_icon.setContextMenu(tray_menu)
	tray_icon.show()

	MainWindow.show()
	sys.exit(app.exec_())
	
keyboard_monitor.setup()
setup()
