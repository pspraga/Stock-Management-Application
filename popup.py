from PyQt5.QtWidgets import QWidget,QDialog

from ui.pages.popui_ui import Ui_Dialog

class Popup(QWidget):
    def __init__(self):
        dialog = QDialog()
        self.Ui=Ui_Dialog()
        dialog.ui = self.Ui
        dialog.ui.setupUi(dialog)
        
        self.partno=self.Ui.Customer
        self.partno.addItem("select")
        self.ser_no=self.Ui.SerialNo
        self.ser_no.setText("hi")
        self.Prod_Partno=self.Ui.PartNo
        self.okbtn=self.Ui.Okbtn
        self.okbtn.clicked.connect(self.Okbtn)
        self.cancelbtn=self.Ui.CancelBtn
        self.cancelbtn.clicked.connect(self.cancel)
        dialog.exec_()
        dialog.show()
    def cancel(self):
        QDialog.close()
    def Okbtn(self):
        print("ok button pressed")
        pass

        
        