import sys

from PyQt5.QtWidgets import QApplication

from frame import MajorDialog
from frame.login.login_dialog import LoginDialog

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_dialog = MajorDialog()
    login_dialog.show()
    sys.exit(app.exec_())
