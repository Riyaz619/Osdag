# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'svg_image.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_WizardPage(object):
    def setupUi(self, WizardPage):
        WizardPage.setObjectName(_fromUtf8("WizardPage"))
        WizardPage.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(WizardPage)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.btn_svg_save = QtGui.QPushButton(WizardPage)
        self.btn_svg_save.setObjectName(_fromUtf8("btn_svg_save"))
        self.gridLayout.addWidget(self.btn_svg_save, 0, 0, 1, 1)
        self.lbl_svg = QtGui.QLabel(WizardPage)
        self.lbl_svg.setText(_fromUtf8(""))
        self.lbl_svg.setObjectName(_fromUtf8("lbl_svg"))
        self.gridLayout.addWidget(self.lbl_svg, 1, 0, 1, 1)

        self.retranslateUi(WizardPage)
        QtCore.QMetaObject.connectSlotsByName(WizardPage)

    def retranslateUi(self, WizardPage):
        WizardPage.setWindowTitle(_translate("WizardPage", "WizardPage", None))
        self.btn_svg_save.setText(_translate("WizardPage", "Save", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    WizardPage = QtGui.QWizardPage()
    ui = Ui_WizardPage()
    ui.setupUi(WizardPage)
    WizardPage.show()
    sys.exit(app.exec_())

