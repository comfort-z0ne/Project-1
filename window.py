# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QStackedWidget,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 452)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 641, 431))
        self.login = QWidget()
        self.login.setObjectName(u"login")
        self.gridLayoutWidget = QWidget(self.login)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(200, 290, 239, 141))
        self.keypadLayout = QGridLayout(self.gridLayoutWidget)
        self.keypadLayout.setObjectName(u"keypadLayout")
        self.keypadLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_six = QPushButton(self.gridLayoutWidget)
        self.pushButton_six.setObjectName(u"pushButton_six")

        self.keypadLayout.addWidget(self.pushButton_six, 1, 2, 1, 1)

        self.pushButton_five = QPushButton(self.gridLayoutWidget)
        self.pushButton_five.setObjectName(u"pushButton_five")

        self.keypadLayout.addWidget(self.pushButton_five, 1, 1, 1, 1)

        self.pushButton_two = QPushButton(self.gridLayoutWidget)
        self.pushButton_two.setObjectName(u"pushButton_two")

        self.keypadLayout.addWidget(self.pushButton_two, 2, 1, 1, 1)

        self.pushButton_four = QPushButton(self.gridLayoutWidget)
        self.pushButton_four.setObjectName(u"pushButton_four")

        self.keypadLayout.addWidget(self.pushButton_four, 1, 0, 1, 1)

        self.pushButton_nine = QPushButton(self.gridLayoutWidget)
        self.pushButton_nine.setObjectName(u"pushButton_nine")

        self.keypadLayout.addWidget(self.pushButton_nine, 0, 2, 1, 1)

        self.pushButton_seven = QPushButton(self.gridLayoutWidget)
        self.pushButton_seven.setObjectName(u"pushButton_seven")

        self.keypadLayout.addWidget(self.pushButton_seven, 0, 0, 1, 1)

        self.pushButton_eight = QPushButton(self.gridLayoutWidget)
        self.pushButton_eight.setObjectName(u"pushButton_eight")

        self.keypadLayout.addWidget(self.pushButton_eight, 0, 1, 1, 1)

        self.pushButton_one = QPushButton(self.gridLayoutWidget)
        self.pushButton_one.setObjectName(u"pushButton_one")

        self.keypadLayout.addWidget(self.pushButton_one, 2, 0, 1, 1)

        self.pushButton_three = QPushButton(self.gridLayoutWidget)
        self.pushButton_three.setObjectName(u"pushButton_three")

        self.keypadLayout.addWidget(self.pushButton_three, 2, 2, 1, 1)

        self.pushButton_zero = QPushButton(self.gridLayoutWidget)
        self.pushButton_zero.setObjectName(u"pushButton_zero")

        self.keypadLayout.addWidget(self.pushButton_zero, 3, 0, 1, 1)

        self.pushButton_confirm = QPushButton(self.gridLayoutWidget)
        self.pushButton_confirm.setObjectName(u"pushButton_confirm")

        self.keypadLayout.addWidget(self.pushButton_confirm, 3, 2, 1, 1)

        self.pushButton_backspace = QPushButton(self.gridLayoutWidget)
        self.pushButton_backspace.setObjectName(u"pushButton_backspace")

        self.keypadLayout.addWidget(self.pushButton_backspace, 3, 1, 1, 1)

        self.inputLine = QLineEdit(self.login)
        self.inputLine.setObjectName(u"inputLine")
        self.inputLine.setGeometry(QRect(260, 270, 113, 20))
        self.inputLine.setInputMethodHints(Qt.ImhNone)
        self.inputLine.setReadOnly(True)
        self.inputNotice = QLabel(self.login)
        self.inputNotice.setObjectName(u"inputNotice")
        self.inputNotice.setGeometry(QRect(0, 250, 641, 20))
        self.inputNotice.setAlignment(Qt.AlignCenter)
        self.welcomeTitle = QLabel(self.login)
        self.welcomeTitle.setObjectName(u"welcomeTitle")
        self.welcomeTitle.setGeometry(QRect(0, 150, 641, 21))
        self.welcomeTitle.setAlignment(Qt.AlignCenter)
        self.errorLabel = QLabel(self.login)
        self.errorLabel.setObjectName(u"errorLabel")
        self.errorLabel.setGeometry(QRect(10, 210, 621, 21))
        self.errorLabel.setLayoutDirection(Qt.LeftToRight)
        self.errorLabel.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.login)
        self.main = QWidget()
        self.main.setObjectName(u"main")
        self.label_L1 = QLabel(self.main)
        self.label_L1.setObjectName(u"label_L1")
        self.label_L1.setGeometry(QRect(90, 80, 46, 13))
        self.label_R1 = QLabel(self.main)
        self.label_R1.setObjectName(u"label_R1")
        self.label_R1.setGeometry(QRect(510, 80, 46, 13))
        self.label_L2 = QLabel(self.main)
        self.label_L2.setObjectName(u"label_L2")
        self.label_L2.setGeometry(QRect(90, 170, 46, 13))
        self.label_R2 = QLabel(self.main)
        self.label_R2.setObjectName(u"label_R2")
        self.label_R2.setGeometry(QRect(510, 170, 46, 13))
        self.verticalLayoutWidget_2 = QWidget(self.main)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(560, 15, 77, 411))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_R1 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_R1.setObjectName(u"pushButton_R1")

        self.verticalLayout_2.addWidget(self.pushButton_R1)

        self.pushButton_R2 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_R2.setObjectName(u"pushButton_R2")

        self.verticalLayout_2.addWidget(self.pushButton_R2)

        self.pushButton_R3 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_R3.setObjectName(u"pushButton_R3")

        self.verticalLayout_2.addWidget(self.pushButton_R3)

        self.pushButton_R4 = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_R4.setObjectName(u"pushButton_R4")

        self.verticalLayout_2.addWidget(self.pushButton_R4)

        self.verticalLayoutWidget = QWidget(self.main)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 15, 77, 411))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_L1 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_L1.setObjectName(u"pushButton_L1")

        self.verticalLayout.addWidget(self.pushButton_L1)

        self.pushButton_L2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_L2.setObjectName(u"pushButton_L2")

        self.verticalLayout.addWidget(self.pushButton_L2)

        self.pushButton_L3 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_L3.setObjectName(u"pushButton_L3")

        self.verticalLayout.addWidget(self.pushButton_L3)

        self.pushButton_L4 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_L4.setObjectName(u"pushButton_L4")

        self.verticalLayout.addWidget(self.pushButton_L4)

        self.label_L4 = QLabel(self.main)
        self.label_L4.setObjectName(u"label_L4")
        self.label_L4.setGeometry(QRect(90, 340, 46, 13))
        self.label_R4 = QLabel(self.main)
        self.label_R4.setObjectName(u"label_R4")
        self.label_R4.setGeometry(QRect(510, 340, 46, 13))
        self.label_top = QLabel(self.main)
        self.label_top.setObjectName(u"label_top")
        self.label_top.setGeometry(QRect(90, 125, 461, 20))
        self.label_top.setAlignment(Qt.AlignCenter)
        self.label_bottom = QLabel(self.main)
        self.label_bottom.setObjectName(u"label_bottom")
        self.label_bottom.setGeometry(QRect(90, 145, 461, 20))
        self.label_bottom.setAlignment(Qt.AlignCenter)
        self.pageLabel = QLabel(self.main)
        self.pageLabel.setObjectName(u"pageLabel")
        self.pageLabel.setGeometry(QRect(0, 0, 46, 13))
        self.label_L3 = QLabel(self.main)
        self.label_L3.setObjectName(u"label_L3")
        self.label_L3.setGeometry(QRect(90, 260, 46, 13))
        self.label_R3 = QLabel(self.main)
        self.label_R3.setObjectName(u"label_R3")
        self.label_R3.setGeometry(QRect(510, 260, 46, 13))
        self.stackedWidget.addWidget(self.main)
        self.withdraw = QWidget()
        self.withdraw.setObjectName(u"withdraw")
        self.verticalLayoutWidget_3 = QWidget(self.withdraw)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(560, 15, 77, 411))
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pushButton_R1_w = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_R1_w.setObjectName(u"pushButton_R1_w")

        self.verticalLayout_7.addWidget(self.pushButton_R1_w)

        self.pushButton_R2_w = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_R2_w.setObjectName(u"pushButton_R2_w")

        self.verticalLayout_7.addWidget(self.pushButton_R2_w)

        self.pushButton_R3_w = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_R3_w.setObjectName(u"pushButton_R3_w")

        self.verticalLayout_7.addWidget(self.pushButton_R3_w)

        self.pushButton_R4_w = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_R4_w.setObjectName(u"pushButton_R4_w")

        self.verticalLayout_7.addWidget(self.pushButton_R4_w)

        self.verticalLayoutWidget_4 = QWidget(self.withdraw)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(0, 15, 77, 411))
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton_L1_w = QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_L1_w.setObjectName(u"pushButton_L1_w")

        self.verticalLayout_8.addWidget(self.pushButton_L1_w)

        self.pushButton_L2_w = QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_L2_w.setObjectName(u"pushButton_L2_w")

        self.verticalLayout_8.addWidget(self.pushButton_L2_w)

        self.pushButton_L3_w = QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_L3_w.setObjectName(u"pushButton_L3_w")

        self.verticalLayout_8.addWidget(self.pushButton_L3_w)

        self.pushButton_L4_w = QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_L4_w.setObjectName(u"pushButton_L4_w")

        self.verticalLayout_8.addWidget(self.pushButton_L4_w)

        self.label_L3_w = QLabel(self.withdraw)
        self.label_L3_w.setObjectName(u"label_L3_w")
        self.label_L3_w.setGeometry(QRect(90, 260, 46, 13))
        self.label_R4_w = QLabel(self.withdraw)
        self.label_R4_w.setObjectName(u"label_R4_w")
        self.label_R4_w.setGeometry(QRect(510, 340, 46, 13))
        self.label_R2_w = QLabel(self.withdraw)
        self.label_R2_w.setObjectName(u"label_R2_w")
        self.label_R2_w.setGeometry(QRect(510, 170, 46, 13))
        self.label_R1_w = QLabel(self.withdraw)
        self.label_R1_w.setObjectName(u"label_R1_w")
        self.label_R1_w.setGeometry(QRect(510, 80, 46, 13))
        self.label_L4_w = QLabel(self.withdraw)
        self.label_L4_w.setObjectName(u"label_L4_w")
        self.label_L4_w.setGeometry(QRect(90, 340, 46, 13))
        self.label_bottom_w = QLabel(self.withdraw)
        self.label_bottom_w.setObjectName(u"label_bottom_w")
        self.label_bottom_w.setGeometry(QRect(90, 145, 461, 20))
        self.label_bottom_w.setAlignment(Qt.AlignCenter)
        self.label_top_w = QLabel(self.withdraw)
        self.label_top_w.setObjectName(u"label_top_w")
        self.label_top_w.setGeometry(QRect(90, 120, 461, 20))
        self.label_top_w.setAlignment(Qt.AlignCenter)
        self.label_R3_w = QLabel(self.withdraw)
        self.label_R3_w.setObjectName(u"label_R3_w")
        self.label_R3_w.setGeometry(QRect(510, 260, 46, 13))
        self.label_L2_w = QLabel(self.withdraw)
        self.label_L2_w.setObjectName(u"label_L2_w")
        self.label_L2_w.setGeometry(QRect(90, 170, 46, 13))
        self.label_L1_w = QLabel(self.withdraw)
        self.label_L1_w.setObjectName(u"label_L1_w")
        self.label_L1_w.setGeometry(QRect(90, 80, 46, 13))
        self.pageLabel_w = QLabel(self.withdraw)
        self.pageLabel_w.setObjectName(u"pageLabel_w")
        self.pageLabel_w.setGeometry(QRect(0, 0, 46, 13))
        self.inputLine_w = QLineEdit(self.withdraw)
        self.inputLine_w.setObjectName(u"inputLine_w")
        self.inputLine_w.setGeometry(QRect(260, 270, 113, 20))
        self.inputLine_w.setReadOnly(True)
        self.gridLayoutWidget_2 = QWidget(self.withdraw)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(200, 290, 239, 141))
        self.keypadLayout_w = QGridLayout(self.gridLayoutWidget_2)
        self.keypadLayout_w.setObjectName(u"keypadLayout_w")
        self.keypadLayout_w.setContentsMargins(0, 0, 0, 0)
        self.pushButton_six_w = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_six_w.setObjectName(u"pushButton_six_w")

        self.keypadLayout_w.addWidget(self.pushButton_six_w, 1, 2, 1, 1)

        self.pushButton_five_w = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_five_w.setObjectName(u"pushButton_five_w")

        self.keypadLayout_w.addWidget(self.pushButton_five_w, 1, 1, 1, 1)

        self.pushButton_two_w = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_two_w.setObjectName(u"pushButton_two_w")

        self.keypadLayout_w.addWidget(self.pushButton_two_w, 2, 1, 1, 1)

        self.pushButton_four_w = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_four_w.setObjectName(u"pushButton_four_w")

        self.keypadLayout_w.addWidget(self.pushButton_four_w, 1, 0, 1, 1)

        self.pushButton_nine_w = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_nine_w.setObjectName(u"pushButton_nine_w")

        self.keypadLayout_w.addWidget(self.pushButton_nine_w, 0, 2, 1, 1)

        self.pushButton_seven_w = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_seven_w.setObjectName(u"pushButton_seven_w")

        self.keypadLayout_w.addWidget(self.pushButton_seven_w, 0, 0, 1, 1)

        self.pushButton_eight_w = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_eight_w.setObjectName(u"pushButton_eight_w")

        self.keypadLayout_w.addWidget(self.pushButton_eight_w, 0, 1, 1, 1)

        self.pushButton_one_w = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_one_w.setObjectName(u"pushButton_one_w")

        self.keypadLayout_w.addWidget(self.pushButton_one_w, 2, 0, 1, 1)

        self.pushButton_three_w = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_three_w.setObjectName(u"pushButton_three_w")

        self.keypadLayout_w.addWidget(self.pushButton_three_w, 2, 2, 1, 1)

        self.pushButton_zero_w = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_zero_w.setObjectName(u"pushButton_zero_w")

        self.keypadLayout_w.addWidget(self.pushButton_zero_w, 3, 0, 1, 1)

        self.pushButton_point_w = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_point_w.setObjectName(u"pushButton_point_w")

        self.keypadLayout_w.addWidget(self.pushButton_point_w, 3, 2, 1, 1)

        self.pushButton_backspace_w = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_backspace_w.setObjectName(u"pushButton_backspace_w")

        self.keypadLayout_w.addWidget(self.pushButton_backspace_w, 3, 1, 1, 1)

        self.inputNotice_w = QLabel(self.withdraw)
        self.inputNotice_w.setObjectName(u"inputNotice_w")
        self.inputNotice_w.setGeometry(QRect(90, 250, 461, 20))
        self.inputNotice_w.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.withdraw)
        self.deposit = QWidget()
        self.deposit.setObjectName(u"deposit")
        self.verticalLayoutWidget_5 = QWidget(self.deposit)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(560, 15, 77, 411))
        self.verticalLayout_9 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.pushButton_R1_d = QPushButton(self.verticalLayoutWidget_5)
        self.pushButton_R1_d.setObjectName(u"pushButton_R1_d")

        self.verticalLayout_9.addWidget(self.pushButton_R1_d)

        self.pushButton_R2_d = QPushButton(self.verticalLayoutWidget_5)
        self.pushButton_R2_d.setObjectName(u"pushButton_R2_d")

        self.verticalLayout_9.addWidget(self.pushButton_R2_d)

        self.pushButton_R3_d = QPushButton(self.verticalLayoutWidget_5)
        self.pushButton_R3_d.setObjectName(u"pushButton_R3_d")

        self.verticalLayout_9.addWidget(self.pushButton_R3_d)

        self.pushButton_R4_d = QPushButton(self.verticalLayoutWidget_5)
        self.pushButton_R4_d.setObjectName(u"pushButton_R4_d")

        self.verticalLayout_9.addWidget(self.pushButton_R4_d)

        self.verticalLayoutWidget_6 = QWidget(self.deposit)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(0, 15, 77, 411))
        self.verticalLayout_10 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.pushButton_L1_d = QPushButton(self.verticalLayoutWidget_6)
        self.pushButton_L1_d.setObjectName(u"pushButton_L1_d")

        self.verticalLayout_10.addWidget(self.pushButton_L1_d)

        self.pushButton_L2_d = QPushButton(self.verticalLayoutWidget_6)
        self.pushButton_L2_d.setObjectName(u"pushButton_L2_d")

        self.verticalLayout_10.addWidget(self.pushButton_L2_d)

        self.pushButton_L3_d = QPushButton(self.verticalLayoutWidget_6)
        self.pushButton_L3_d.setObjectName(u"pushButton_L3_d")

        self.verticalLayout_10.addWidget(self.pushButton_L3_d)

        self.pushButton_L4_d = QPushButton(self.verticalLayoutWidget_6)
        self.pushButton_L4_d.setObjectName(u"pushButton_L4_d")

        self.verticalLayout_10.addWidget(self.pushButton_L4_d)

        self.label_L4_d = QLabel(self.deposit)
        self.label_L4_d.setObjectName(u"label_L4_d")
        self.label_L4_d.setGeometry(QRect(90, 340, 46, 13))
        self.label_R3_d = QLabel(self.deposit)
        self.label_R3_d.setObjectName(u"label_R3_d")
        self.label_R3_d.setGeometry(QRect(510, 260, 46, 13))
        self.pageLabel_d = QLabel(self.deposit)
        self.pageLabel_d.setObjectName(u"pageLabel_d")
        self.pageLabel_d.setGeometry(QRect(0, 0, 46, 13))
        self.label_bottom_d = QLabel(self.deposit)
        self.label_bottom_d.setObjectName(u"label_bottom_d")
        self.label_bottom_d.setGeometry(QRect(90, 145, 461, 20))
        self.label_bottom_d.setAlignment(Qt.AlignCenter)
        self.label_L2_d = QLabel(self.deposit)
        self.label_L2_d.setObjectName(u"label_L2_d")
        self.label_L2_d.setGeometry(QRect(90, 170, 46, 13))
        self.label_top_d = QLabel(self.deposit)
        self.label_top_d.setObjectName(u"label_top_d")
        self.label_top_d.setGeometry(QRect(90, 120, 461, 20))
        self.label_top_d.setAlignment(Qt.AlignCenter)
        self.label_R4_d = QLabel(self.deposit)
        self.label_R4_d.setObjectName(u"label_R4_d")
        self.label_R4_d.setGeometry(QRect(510, 340, 46, 13))
        self.label_R2_d = QLabel(self.deposit)
        self.label_R2_d.setObjectName(u"label_R2_d")
        self.label_R2_d.setGeometry(QRect(510, 170, 46, 13))
        self.label_L3_d = QLabel(self.deposit)
        self.label_L3_d.setObjectName(u"label_L3_d")
        self.label_L3_d.setGeometry(QRect(90, 260, 46, 13))
        self.label_L1_d = QLabel(self.deposit)
        self.label_L1_d.setObjectName(u"label_L1_d")
        self.label_L1_d.setGeometry(QRect(90, 80, 46, 13))
        self.label_R1_d = QLabel(self.deposit)
        self.label_R1_d.setObjectName(u"label_R1_d")
        self.label_R1_d.setGeometry(QRect(510, 80, 46, 13))
        self.inputNotice_d = QLabel(self.deposit)
        self.inputNotice_d.setObjectName(u"inputNotice_d")
        self.inputNotice_d.setGeometry(QRect(90, 250, 461, 20))
        self.inputNotice_d.setAlignment(Qt.AlignCenter)
        self.inputLine_d = QLineEdit(self.deposit)
        self.inputLine_d.setObjectName(u"inputLine_d")
        self.inputLine_d.setGeometry(QRect(260, 270, 113, 20))
        self.inputLine_d.setReadOnly(True)
        self.gridLayoutWidget_3 = QWidget(self.deposit)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(200, 290, 239, 141))
        self.keypadLayout_d = QGridLayout(self.gridLayoutWidget_3)
        self.keypadLayout_d.setObjectName(u"keypadLayout_d")
        self.keypadLayout_d.setContentsMargins(0, 0, 0, 0)
        self.pushButton_six_d = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_six_d.setObjectName(u"pushButton_six_d")

        self.keypadLayout_d.addWidget(self.pushButton_six_d, 1, 2, 1, 1)

        self.pushButton_five_d = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_five_d.setObjectName(u"pushButton_five_d")

        self.keypadLayout_d.addWidget(self.pushButton_five_d, 1, 1, 1, 1)

        self.pushButton_two_d = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_two_d.setObjectName(u"pushButton_two_d")

        self.keypadLayout_d.addWidget(self.pushButton_two_d, 2, 1, 1, 1)

        self.pushButton_four_d = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_four_d.setObjectName(u"pushButton_four_d")

        self.keypadLayout_d.addWidget(self.pushButton_four_d, 1, 0, 1, 1)

        self.pushButton_nine_d = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_nine_d.setObjectName(u"pushButton_nine_d")

        self.keypadLayout_d.addWidget(self.pushButton_nine_d, 0, 2, 1, 1)

        self.pushButton_seven_d = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_seven_d.setObjectName(u"pushButton_seven_d")

        self.keypadLayout_d.addWidget(self.pushButton_seven_d, 0, 0, 1, 1)

        self.pushButton_eight_d = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_eight_d.setObjectName(u"pushButton_eight_d")

        self.keypadLayout_d.addWidget(self.pushButton_eight_d, 0, 1, 1, 1)

        self.pushButton_one_d = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_one_d.setObjectName(u"pushButton_one_d")

        self.keypadLayout_d.addWidget(self.pushButton_one_d, 2, 0, 1, 1)

        self.pushButton_three_d = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_three_d.setObjectName(u"pushButton_three_d")

        self.keypadLayout_d.addWidget(self.pushButton_three_d, 2, 2, 1, 1)

        self.pushButton_zero_d = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_zero_d.setObjectName(u"pushButton_zero_d")

        self.keypadLayout_d.addWidget(self.pushButton_zero_d, 3, 0, 1, 1)

        self.pushButton_point_d = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_point_d.setObjectName(u"pushButton_point_d")

        self.keypadLayout_d.addWidget(self.pushButton_point_d, 3, 2, 1, 1)

        self.pushButton_backspace_d = QPushButton(self.gridLayoutWidget_3)
        self.pushButton_backspace_d.setObjectName(u"pushButton_backspace_d")

        self.keypadLayout_d.addWidget(self.pushButton_backspace_d, 3, 1, 1, 1)

        self.stackedWidget.addWidget(self.deposit)
        self.transfer = QWidget()
        self.transfer.setObjectName(u"transfer")
        self.verticalLayoutWidget_7 = QWidget(self.transfer)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(560, 15, 77, 411))
        self.verticalLayout_11 = QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.pushButton_R1_t = QPushButton(self.verticalLayoutWidget_7)
        self.pushButton_R1_t.setObjectName(u"pushButton_R1_t")

        self.verticalLayout_11.addWidget(self.pushButton_R1_t)

        self.pushButton_R2_t = QPushButton(self.verticalLayoutWidget_7)
        self.pushButton_R2_t.setObjectName(u"pushButton_R2_t")

        self.verticalLayout_11.addWidget(self.pushButton_R2_t)

        self.pushButton_R3_t = QPushButton(self.verticalLayoutWidget_7)
        self.pushButton_R3_t.setObjectName(u"pushButton_R3_t")

        self.verticalLayout_11.addWidget(self.pushButton_R3_t)

        self.pushButton_R4_t = QPushButton(self.verticalLayoutWidget_7)
        self.pushButton_R4_t.setObjectName(u"pushButton_R4_t")

        self.verticalLayout_11.addWidget(self.pushButton_R4_t)

        self.verticalLayoutWidget_8 = QWidget(self.transfer)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(0, 15, 77, 411))
        self.verticalLayout_12 = QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.pushButton_L1_t = QPushButton(self.verticalLayoutWidget_8)
        self.pushButton_L1_t.setObjectName(u"pushButton_L1_t")

        self.verticalLayout_12.addWidget(self.pushButton_L1_t)

        self.pushButton_L2_t = QPushButton(self.verticalLayoutWidget_8)
        self.pushButton_L2_t.setObjectName(u"pushButton_L2_t")

        self.verticalLayout_12.addWidget(self.pushButton_L2_t)

        self.pushButton_L3_t = QPushButton(self.verticalLayoutWidget_8)
        self.pushButton_L3_t.setObjectName(u"pushButton_L3_t")

        self.verticalLayout_12.addWidget(self.pushButton_L3_t)

        self.pushButton_L4_t = QPushButton(self.verticalLayoutWidget_8)
        self.pushButton_L4_t.setObjectName(u"pushButton_L4_t")

        self.verticalLayout_12.addWidget(self.pushButton_L4_t)

        self.label_L4_t = QLabel(self.transfer)
        self.label_L4_t.setObjectName(u"label_L4_t")
        self.label_L4_t.setGeometry(QRect(90, 340, 46, 13))
        self.label_R3_t = QLabel(self.transfer)
        self.label_R3_t.setObjectName(u"label_R3_t")
        self.label_R3_t.setGeometry(QRect(510, 260, 46, 13))
        self.pageLabel_t = QLabel(self.transfer)
        self.pageLabel_t.setObjectName(u"pageLabel_t")
        self.pageLabel_t.setGeometry(QRect(0, 0, 46, 13))
        self.label_bottom_t = QLabel(self.transfer)
        self.label_bottom_t.setObjectName(u"label_bottom_t")
        self.label_bottom_t.setGeometry(QRect(90, 145, 461, 20))
        self.label_bottom_t.setAlignment(Qt.AlignCenter)
        self.label_L2_t = QLabel(self.transfer)
        self.label_L2_t.setObjectName(u"label_L2_t")
        self.label_L2_t.setGeometry(QRect(90, 170, 46, 13))
        self.label_top_t = QLabel(self.transfer)
        self.label_top_t.setObjectName(u"label_top_t")
        self.label_top_t.setGeometry(QRect(90, 120, 461, 20))
        self.label_top_t.setAlignment(Qt.AlignCenter)
        self.label_R4_t = QLabel(self.transfer)
        self.label_R4_t.setObjectName(u"label_R4_t")
        self.label_R4_t.setGeometry(QRect(510, 340, 46, 13))
        self.label_R2_t = QLabel(self.transfer)
        self.label_R2_t.setObjectName(u"label_R2_t")
        self.label_R2_t.setGeometry(QRect(510, 170, 46, 13))
        self.label_L3_t = QLabel(self.transfer)
        self.label_L3_t.setObjectName(u"label_L3_t")
        self.label_L3_t.setGeometry(QRect(90, 260, 46, 13))
        self.label_L1_t = QLabel(self.transfer)
        self.label_L1_t.setObjectName(u"label_L1_t")
        self.label_L1_t.setGeometry(QRect(90, 80, 46, 13))
        self.label_R1_t = QLabel(self.transfer)
        self.label_R1_t.setObjectName(u"label_R1_t")
        self.label_R1_t.setGeometry(QRect(510, 80, 46, 13))
        self.inputNotice_t = QLabel(self.transfer)
        self.inputNotice_t.setObjectName(u"inputNotice_t")
        self.inputNotice_t.setGeometry(QRect(90, 250, 461, 20))
        self.inputNotice_t.setAlignment(Qt.AlignCenter)
        self.inputLine_t = QLineEdit(self.transfer)
        self.inputLine_t.setObjectName(u"inputLine_t")
        self.inputLine_t.setGeometry(QRect(260, 270, 113, 20))
        self.inputLine_t.setReadOnly(True)
        self.gridLayoutWidget_4 = QWidget(self.transfer)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(200, 290, 239, 141))
        self.keypadLayout_t = QGridLayout(self.gridLayoutWidget_4)
        self.keypadLayout_t.setObjectName(u"keypadLayout_t")
        self.keypadLayout_t.setContentsMargins(0, 0, 0, 0)
        self.pushButton_six_t = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_six_t.setObjectName(u"pushButton_six_t")

        self.keypadLayout_t.addWidget(self.pushButton_six_t, 1, 2, 1, 1)

        self.pushButton_five_t = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_five_t.setObjectName(u"pushButton_five_t")

        self.keypadLayout_t.addWidget(self.pushButton_five_t, 1, 1, 1, 1)

        self.pushButton_two_t = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_two_t.setObjectName(u"pushButton_two_t")

        self.keypadLayout_t.addWidget(self.pushButton_two_t, 2, 1, 1, 1)

        self.pushButton_four_t = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_four_t.setObjectName(u"pushButton_four_t")

        self.keypadLayout_t.addWidget(self.pushButton_four_t, 1, 0, 1, 1)

        self.pushButton_nine_t = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_nine_t.setObjectName(u"pushButton_nine_t")

        self.keypadLayout_t.addWidget(self.pushButton_nine_t, 0, 2, 1, 1)

        self.pushButton_seven_t = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_seven_t.setObjectName(u"pushButton_seven_t")

        self.keypadLayout_t.addWidget(self.pushButton_seven_t, 0, 0, 1, 1)

        self.pushButton_eight_t = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_eight_t.setObjectName(u"pushButton_eight_t")

        self.keypadLayout_t.addWidget(self.pushButton_eight_t, 0, 1, 1, 1)

        self.pushButton_one_t = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_one_t.setObjectName(u"pushButton_one_t")

        self.keypadLayout_t.addWidget(self.pushButton_one_t, 2, 0, 1, 1)

        self.pushButton_three_t = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_three_t.setObjectName(u"pushButton_three_t")

        self.keypadLayout_t.addWidget(self.pushButton_three_t, 2, 2, 1, 1)

        self.pushButton_zero_t = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_zero_t.setObjectName(u"pushButton_zero_t")

        self.keypadLayout_t.addWidget(self.pushButton_zero_t, 3, 0, 1, 1)

        self.pushButton_point_t = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_point_t.setObjectName(u"pushButton_point_t")

        self.keypadLayout_t.addWidget(self.pushButton_point_t, 3, 2, 1, 1)

        self.pushButton_backspace_t = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_backspace_t.setObjectName(u"pushButton_backspace_t")

        self.keypadLayout_t.addWidget(self.pushButton_backspace_t, 3, 1, 1, 1)

        self.acctnumLine_t = QLineEdit(self.transfer)
        self.acctnumLine_t.setObjectName(u"acctnumLine_t")
        self.acctnumLine_t.setGeometry(QRect(260, 210, 113, 20))
        self.acctnumLine_t.setReadOnly(False)
        self.acctnumNotice_t = QLabel(self.transfer)
        self.acctnumNotice_t.setObjectName(u"acctnumNotice_t")
        self.acctnumNotice_t.setGeometry(QRect(90, 190, 461, 20))
        self.acctnumNotice_t.setAlignment(Qt.AlignCenter)
        self.errorLabel_t = QLabel(self.transfer)
        self.errorLabel_t.setObjectName(u"errorLabel_t")
        self.errorLabel_t.setGeometry(QRect(80, 230, 481, 21))
        self.errorLabel_t.setLayoutDirection(Qt.LeftToRight)
        self.errorLabel_t.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.transfer)
        self.balance = QWidget()
        self.balance.setObjectName(u"balance")
        self.verticalLayoutWidget_9 = QWidget(self.balance)
        self.verticalLayoutWidget_9.setObjectName(u"verticalLayoutWidget_9")
        self.verticalLayoutWidget_9.setGeometry(QRect(560, 15, 77, 411))
        self.verticalLayout_13 = QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.pushButton_R1_b = QPushButton(self.verticalLayoutWidget_9)
        self.pushButton_R1_b.setObjectName(u"pushButton_R1_b")

        self.verticalLayout_13.addWidget(self.pushButton_R1_b)

        self.pushButton_R2_b = QPushButton(self.verticalLayoutWidget_9)
        self.pushButton_R2_b.setObjectName(u"pushButton_R2_b")

        self.verticalLayout_13.addWidget(self.pushButton_R2_b)

        self.pushButton_R3_b = QPushButton(self.verticalLayoutWidget_9)
        self.pushButton_R3_b.setObjectName(u"pushButton_R3_b")

        self.verticalLayout_13.addWidget(self.pushButton_R3_b)

        self.pushButton_R4_b = QPushButton(self.verticalLayoutWidget_9)
        self.pushButton_R4_b.setObjectName(u"pushButton_R4_b")

        self.verticalLayout_13.addWidget(self.pushButton_R4_b)

        self.verticalLayoutWidget_10 = QWidget(self.balance)
        self.verticalLayoutWidget_10.setObjectName(u"verticalLayoutWidget_10")
        self.verticalLayoutWidget_10.setGeometry(QRect(0, 15, 77, 411))
        self.verticalLayout_14 = QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.pushButton_L1_b = QPushButton(self.verticalLayoutWidget_10)
        self.pushButton_L1_b.setObjectName(u"pushButton_L1_b")

        self.verticalLayout_14.addWidget(self.pushButton_L1_b)

        self.pushButton_L2_b = QPushButton(self.verticalLayoutWidget_10)
        self.pushButton_L2_b.setObjectName(u"pushButton_L2_b")

        self.verticalLayout_14.addWidget(self.pushButton_L2_b)

        self.pushButton_L3_b = QPushButton(self.verticalLayoutWidget_10)
        self.pushButton_L3_b.setObjectName(u"pushButton_L3_b")

        self.verticalLayout_14.addWidget(self.pushButton_L3_b)

        self.pushButton_L4_b = QPushButton(self.verticalLayoutWidget_10)
        self.pushButton_L4_b.setObjectName(u"pushButton_L4_b")

        self.verticalLayout_14.addWidget(self.pushButton_L4_b)

        self.label_L4_b = QLabel(self.balance)
        self.label_L4_b.setObjectName(u"label_L4_b")
        self.label_L4_b.setGeometry(QRect(90, 340, 46, 13))
        self.label_R3_b = QLabel(self.balance)
        self.label_R3_b.setObjectName(u"label_R3_b")
        self.label_R3_b.setGeometry(QRect(510, 260, 46, 13))
        self.pageLabel_b = QLabel(self.balance)
        self.pageLabel_b.setObjectName(u"pageLabel_b")
        self.pageLabel_b.setGeometry(QRect(0, 0, 46, 13))
        self.label_bottom_b = QLabel(self.balance)
        self.label_bottom_b.setObjectName(u"label_bottom_b")
        self.label_bottom_b.setGeometry(QRect(80, 145, 481, 20))
        self.label_bottom_b.setAlignment(Qt.AlignCenter)
        self.label_L2_b = QLabel(self.balance)
        self.label_L2_b.setObjectName(u"label_L2_b")
        self.label_L2_b.setGeometry(QRect(90, 170, 46, 13))
        self.label_top_b = QLabel(self.balance)
        self.label_top_b.setObjectName(u"label_top_b")
        self.label_top_b.setGeometry(QRect(80, 120, 481, 20))
        self.label_top_b.setAlignment(Qt.AlignCenter)
        self.label_R4_b = QLabel(self.balance)
        self.label_R4_b.setObjectName(u"label_R4_b")
        self.label_R4_b.setGeometry(QRect(510, 340, 46, 13))
        self.label_R2_b = QLabel(self.balance)
        self.label_R2_b.setObjectName(u"label_R2_b")
        self.label_R2_b.setGeometry(QRect(510, 170, 46, 13))
        self.label_L3_b = QLabel(self.balance)
        self.label_L3_b.setObjectName(u"label_L3_b")
        self.label_L3_b.setGeometry(QRect(90, 260, 46, 13))
        self.label_L1_b = QLabel(self.balance)
        self.label_L1_b.setObjectName(u"label_L1_b")
        self.label_L1_b.setGeometry(QRect(90, 80, 46, 13))
        self.label_R1_b = QLabel(self.balance)
        self.label_R1_b.setObjectName(u"label_R1_b")
        self.label_R1_b.setGeometry(QRect(510, 80, 46, 13))
        self.stackedWidget.addWidget(self.balance)
        self.account = QWidget()
        self.account.setObjectName(u"account")
        self.verticalLayoutWidget_11 = QWidget(self.account)
        self.verticalLayoutWidget_11.setObjectName(u"verticalLayoutWidget_11")
        self.verticalLayoutWidget_11.setGeometry(QRect(560, 15, 77, 411))
        self.verticalLayout_15 = QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.pushButton_R1_a = QPushButton(self.verticalLayoutWidget_11)
        self.pushButton_R1_a.setObjectName(u"pushButton_R1_a")

        self.verticalLayout_15.addWidget(self.pushButton_R1_a)

        self.pushButton_R2_a = QPushButton(self.verticalLayoutWidget_11)
        self.pushButton_R2_a.setObjectName(u"pushButton_R2_a")

        self.verticalLayout_15.addWidget(self.pushButton_R2_a)

        self.pushButton_R3_a = QPushButton(self.verticalLayoutWidget_11)
        self.pushButton_R3_a.setObjectName(u"pushButton_R3_a")

        self.verticalLayout_15.addWidget(self.pushButton_R3_a)

        self.pushButton_R4_a = QPushButton(self.verticalLayoutWidget_11)
        self.pushButton_R4_a.setObjectName(u"pushButton_R4_a")

        self.verticalLayout_15.addWidget(self.pushButton_R4_a)

        self.verticalLayoutWidget_12 = QWidget(self.account)
        self.verticalLayoutWidget_12.setObjectName(u"verticalLayoutWidget_12")
        self.verticalLayoutWidget_12.setGeometry(QRect(0, 15, 77, 411))
        self.verticalLayout_16 = QVBoxLayout(self.verticalLayoutWidget_12)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.pushButton_L1_a = QPushButton(self.verticalLayoutWidget_12)
        self.pushButton_L1_a.setObjectName(u"pushButton_L1_a")

        self.verticalLayout_16.addWidget(self.pushButton_L1_a)

        self.pushButton_L2_a = QPushButton(self.verticalLayoutWidget_12)
        self.pushButton_L2_a.setObjectName(u"pushButton_L2_a")

        self.verticalLayout_16.addWidget(self.pushButton_L2_a)

        self.pushButton_L3_a = QPushButton(self.verticalLayoutWidget_12)
        self.pushButton_L3_a.setObjectName(u"pushButton_L3_a")

        self.verticalLayout_16.addWidget(self.pushButton_L3_a)

        self.pushButton_L4_a = QPushButton(self.verticalLayoutWidget_12)
        self.pushButton_L4_a.setObjectName(u"pushButton_L4_a")

        self.verticalLayout_16.addWidget(self.pushButton_L4_a)

        self.label_L4_a = QLabel(self.account)
        self.label_L4_a.setObjectName(u"label_L4_a")
        self.label_L4_a.setGeometry(QRect(90, 340, 46, 13))
        self.label_R3_a = QLabel(self.account)
        self.label_R3_a.setObjectName(u"label_R3_a")
        self.label_R3_a.setGeometry(QRect(510, 260, 46, 13))
        self.pageLabel_a = QLabel(self.account)
        self.pageLabel_a.setObjectName(u"pageLabel_a")
        self.pageLabel_a.setGeometry(QRect(0, 0, 46, 13))
        self.label_bottom_a = QLabel(self.account)
        self.label_bottom_a.setObjectName(u"label_bottom_a")
        self.label_bottom_a.setGeometry(QRect(80, 145, 481, 20))
        self.label_bottom_a.setAlignment(Qt.AlignCenter)
        self.label_L2_a = QLabel(self.account)
        self.label_L2_a.setObjectName(u"label_L2_a")
        self.label_L2_a.setGeometry(QRect(90, 170, 46, 13))
        self.label_top_a = QLabel(self.account)
        self.label_top_a.setObjectName(u"label_top_a")
        self.label_top_a.setGeometry(QRect(80, 120, 481, 20))
        self.label_top_a.setAlignment(Qt.AlignCenter)
        self.label_R4_a = QLabel(self.account)
        self.label_R4_a.setObjectName(u"label_R4_a")
        self.label_R4_a.setGeometry(QRect(510, 340, 46, 13))
        self.label_R2_a = QLabel(self.account)
        self.label_R2_a.setObjectName(u"label_R2_a")
        self.label_R2_a.setGeometry(QRect(510, 170, 46, 13))
        self.label_L3_a = QLabel(self.account)
        self.label_L3_a.setObjectName(u"label_L3_a")
        self.label_L3_a.setGeometry(QRect(90, 260, 46, 13))
        self.label_L1_a = QLabel(self.account)
        self.label_L1_a.setObjectName(u"label_L1_a")
        self.label_L1_a.setGeometry(QRect(90, 80, 46, 13))
        self.label_R1_a = QLabel(self.account)
        self.label_R1_a.setObjectName(u"label_R1_a")
        self.label_R1_a.setGeometry(QRect(510, 80, 46, 13))
        self.stackedWidget.addWidget(self.account)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Example Bank ATM System", None))
        self.pushButton_six.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_five.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_two.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_four.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_nine.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_seven.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_eight.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_one.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_three.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_zero.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_confirm.setText(QCoreApplication.translate("MainWindow", u"O", None))
        self.pushButton_backspace.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.inputLine.setInputMask("")
        self.inputLine.setText("")
        self.inputNotice.setText(QCoreApplication.translate("MainWindow", u"Please log in (PIN):", None))
        self.welcomeTitle.setText(QCoreApplication.translate("MainWindow", u"Welcome to the Example Bank ATM System!", None))
        self.errorLabel.setText("")
        self.label_L1.setText(QCoreApplication.translate("MainWindow", u"Withdraw", None))
        self.label_R1.setText(QCoreApplication.translate("MainWindow", u"Deposit", None))
        self.label_L2.setText(QCoreApplication.translate("MainWindow", u"Transfer", None))
        self.label_R2.setText(QCoreApplication.translate("MainWindow", u"Balance", None))
        self.pushButton_R1.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_R2.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_R3.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_R4.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_L1.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.pushButton_L2.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.pushButton_L3.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.pushButton_L4.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_L4.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.label_R4.setText(QCoreApplication.translate("MainWindow", u"Account", None))
        self.label_top.setText(QCoreApplication.translate("MainWindow", u"Welcome (user)!", None))
        self.label_bottom.setText(QCoreApplication.translate("MainWindow", u"Please select an option.", None))
        self.pageLabel.setText(QCoreApplication.translate("MainWindow", u"Main", None))
        self.label_L3.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_R3.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_R1_w.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_R2_w.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_R3_w.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_R4_w.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_L1_w.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.pushButton_L2_w.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.pushButton_L3_w.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.pushButton_L4_w.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_L3_w.setText(QCoreApplication.translate("MainWindow", u"$60", None))
        self.label_R4_w.setText(QCoreApplication.translate("MainWindow", u"Custom", None))
        self.label_R2_w.setText(QCoreApplication.translate("MainWindow", u"$100", None))
        self.label_R1_w.setText(QCoreApplication.translate("MainWindow", u"$80", None))
        self.label_L4_w.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_bottom_w.setText(QCoreApplication.translate("MainWindow", u"Please select an option.", None))
        self.label_top_w.setText(QCoreApplication.translate("MainWindow", u"You are now withdrawing.", None))
        self.label_R3_w.setText(QCoreApplication.translate("MainWindow", u"$120", None))
        self.label_L2_w.setText(QCoreApplication.translate("MainWindow", u"$40", None))
        self.label_L1_w.setText(QCoreApplication.translate("MainWindow", u"$20", None))
        self.pageLabel_w.setText(QCoreApplication.translate("MainWindow", u"Withdraw", None))
        self.inputLine_w.setText("")
        self.pushButton_six_w.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_five_w.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_two_w.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_four_w.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_nine_w.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_seven_w.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_eight_w.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_one_w.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_three_w.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_zero_w.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_point_w.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.pushButton_backspace_w.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.inputNotice_w.setText(QCoreApplication.translate("MainWindow", u"Custom amount:", None))
        self.pushButton_R1_d.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_R2_d.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_R3_d.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_R4_d.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_L1_d.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.pushButton_L2_d.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.pushButton_L3_d.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.pushButton_L4_d.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_L4_d.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_R3_d.setText(QCoreApplication.translate("MainWindow", u"$120", None))
        self.pageLabel_d.setText(QCoreApplication.translate("MainWindow", u"Deposit", None))
        self.label_bottom_d.setText(QCoreApplication.translate("MainWindow", u"Please select an option.", None))
        self.label_L2_d.setText(QCoreApplication.translate("MainWindow", u"$40", None))
        self.label_top_d.setText(QCoreApplication.translate("MainWindow", u"You are now depositing.", None))
        self.label_R4_d.setText(QCoreApplication.translate("MainWindow", u"Custom", None))
        self.label_R2_d.setText(QCoreApplication.translate("MainWindow", u"$100", None))
        self.label_L3_d.setText(QCoreApplication.translate("MainWindow", u"$60", None))
        self.label_L1_d.setText(QCoreApplication.translate("MainWindow", u"$20", None))
        self.label_R1_d.setText(QCoreApplication.translate("MainWindow", u"$80", None))
        self.inputNotice_d.setText(QCoreApplication.translate("MainWindow", u"Custom amount:", None))
        self.inputLine_d.setText("")
        self.pushButton_six_d.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_five_d.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_two_d.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_four_d.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_nine_d.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_seven_d.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_eight_d.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_one_d.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_three_d.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_zero_d.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_point_d.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.pushButton_backspace_d.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_R1_t.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_R2_t.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_R3_t.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_R4_t.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_L1_t.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.pushButton_L2_t.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.pushButton_L3_t.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.pushButton_L4_t.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_L4_t.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_R3_t.setText(QCoreApplication.translate("MainWindow", u"$120", None))
        self.pageLabel_t.setText(QCoreApplication.translate("MainWindow", u"Transfer", None))
        self.label_bottom_t.setText(QCoreApplication.translate("MainWindow", u"Please select an option.", None))
        self.label_L2_t.setText(QCoreApplication.translate("MainWindow", u"$40", None))
        self.label_top_t.setText(QCoreApplication.translate("MainWindow", u"You are now transferring.", None))
        self.label_R4_t.setText(QCoreApplication.translate("MainWindow", u"Custom", None))
        self.label_R2_t.setText(QCoreApplication.translate("MainWindow", u"$100", None))
        self.label_L3_t.setText(QCoreApplication.translate("MainWindow", u"$60", None))
        self.label_L1_t.setText(QCoreApplication.translate("MainWindow", u"$20", None))
        self.label_R1_t.setText(QCoreApplication.translate("MainWindow", u"$80", None))
        self.inputNotice_t.setText(QCoreApplication.translate("MainWindow", u"Custom amount:", None))
        self.inputLine_t.setText("")
        self.pushButton_six_t.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.pushButton_five_t.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.pushButton_two_t.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.pushButton_four_t.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.pushButton_nine_t.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.pushButton_seven_t.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.pushButton_eight_t.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.pushButton_one_t.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton_three_t.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.pushButton_zero_t.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_point_t.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.pushButton_backspace_t.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.acctnumLine_t.setInputMask(QCoreApplication.translate("MainWindow", u"9999", None))
        self.acctnumLine_t.setText("")
        self.acctnumNotice_t.setText(QCoreApplication.translate("MainWindow", u"Destination acct #:", None))
        self.errorLabel_t.setText("")
        self.pushButton_R1_b.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_R2_b.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_R3_b.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_R4_b.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_L1_b.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.pushButton_L2_b.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.pushButton_L3_b.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.pushButton_L4_b.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_L4_b.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_R3_b.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pageLabel_b.setText(QCoreApplication.translate("MainWindow", u"Balance", None))
        self.label_bottom_b.setText(QCoreApplication.translate("MainWindow", u"(balance)", None))
        self.label_L2_b.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_top_b.setText(QCoreApplication.translate("MainWindow", u"Your current balance is:", None))
        self.label_R4_b.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_R2_b.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_L3_b.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_L1_b.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_R1_b.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_R1_a.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_R2_a.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_R3_a.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_R4_a.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_L1_a.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.pushButton_L2_a.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.pushButton_L3_a.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.pushButton_L4_a.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_L4_a.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_R3_a.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pageLabel_a.setText(QCoreApplication.translate("MainWindow", u"Account", None))
        self.label_bottom_a.setText(QCoreApplication.translate("MainWindow", u"Acct #/PIN: (PIN)", None))
        self.label_L2_a.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_top_a.setText(QCoreApplication.translate("MainWindow", u"Owner: (owner)", None))
        self.label_R4_a.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_R2_a.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_L3_a.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_L1_a.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_R1_a.setText(QCoreApplication.translate("MainWindow", u"...", None))
    # retranslateUi

