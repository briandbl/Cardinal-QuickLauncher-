# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Setbox.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Setbox(object):
    def setupUi(self, Setbox):
        if not Setbox.objectName():
            Setbox.setObjectName(u"Setbox")
        Setbox.resize(800, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Setbox.sizePolicy().hasHeightForWidth())
        Setbox.setSizePolicy(sizePolicy)
        Setbox.setMinimumSize(QSize(400, 500))
        Setbox.setMaximumSize(QSize(800, 500))
        self.SaveConfig_action = QAction(Setbox)
        self.SaveConfig_action.setObjectName(u"SaveConfig_action")
        self.centralwidget = QWidget(Setbox)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setPointSize(9)
        self.tabWidget.setFont(font)
        self.BasicSet_tab = QWidget()
        self.BasicSet_tab.setObjectName(u"BasicSet_tab")
        self.verticalLayout = QVBoxLayout(self.BasicSet_tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Show_groupBox = QGroupBox(self.BasicSet_tab)
        self.Show_groupBox.setObjectName(u"Show_groupBox")
        self.ImgSize_text = QLabel(self.Show_groupBox)
        self.ImgSize_text.setObjectName(u"ImgSize_text")
        self.ImgSize_text.setGeometry(QRect(10, 20, 31, 21))
        self.ImgSize_control = QSlider(self.Show_groupBox)
        self.ImgSize_control.setObjectName(u"ImgSize_control")
        self.ImgSize_control.setGeometry(QRect(40, 20, 191, 22))
        self.ImgSize_control.setMaximum(100)
        self.ImgSize_control.setPageStep(0)
        self.ImgSize_control.setValue(0)
        self.ImgSize_control.setSliderPosition(0)
        self.ImgSize_control.setOrientation(Qt.Horizontal)
        self.ImgSize_text_percent = QLabel(self.Show_groupBox)
        self.ImgSize_text_percent.setObjectName(u"ImgSize_text_percent")
        self.ImgSize_text_percent.setGeometry(QRect(240, 20, 31, 21))
        self.TopWindow_checkBox = QCheckBox(self.Show_groupBox)
        self.TopWindow_checkBox.setObjectName(u"TopWindow_checkBox")
        self.TopWindow_checkBox.setGeometry(QRect(10, 50, 81, 16))
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.TopWindow_checkBox.sizePolicy().hasHeightForWidth())
        self.TopWindow_checkBox.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(9)
        font1.setKerning(True)
        self.TopWindow_checkBox.setFont(font1)
        self.TopWindow_checkBox.setChecked(True)
        self.WindowIconbox_checkBox = QCheckBox(self.Show_groupBox)
        self.WindowIconbox_checkBox.setObjectName(u"WindowIconbox_checkBox")
        self.WindowIconbox_checkBox.setGeometry(QRect(90, 50, 121, 16))
        self.WindowIconbox_checkBox.setChecked(False)
        self.SetBox_Go_with_Person_checkBox = QCheckBox(self.Show_groupBox)
        self.SetBox_Go_with_Person_checkBox.setObjectName(u"SetBox_Go_with_Person_checkBox")
        self.SetBox_Go_with_Person_checkBox.setGeometry(QRect(10, 80, 181, 16))
        self.SetBox_Go_with_Person_checkBox.setChecked(True)

        self.verticalLayout.addWidget(self.Show_groupBox)

        self.ImagePackageInfo_groupBox = QGroupBox(self.BasicSet_tab)
        self.ImagePackageInfo_groupBox.setObjectName(u"ImagePackageInfo_groupBox")
        self.Name_show = QLineEdit(self.ImagePackageInfo_groupBox)
        self.Name_show.setObjectName(u"Name_show")
        self.Name_show.setGeometry(QRect(40, 20, 241, 20))
        self.Name_show.setReadOnly(True)
        self.Name_text = QLabel(self.ImagePackageInfo_groupBox)
        self.Name_text.setObjectName(u"Name_text")
        self.Name_text.setGeometry(QRect(10, 21, 31, 21))
        self.Introduction_text = QLabel(self.ImagePackageInfo_groupBox)
        self.Introduction_text.setObjectName(u"Introduction_text")
        self.Introduction_text.setGeometry(QRect(10, 50, 31, 21))
        self.Introduction_show = QPlainTextEdit(self.ImagePackageInfo_groupBox)
        self.Introduction_show.setObjectName(u"Introduction_show")
        self.Introduction_show.setGeometry(QRect(40, 50, 241, 141))
        self.Introduction_show.setReadOnly(True)

        self.verticalLayout.addWidget(self.ImagePackageInfo_groupBox)

        self.tabWidget.addTab(self.BasicSet_tab, "")
        self.Animation_tab = QWidget()
        self.Animation_tab.setObjectName(u"Animation_tab")
        self.verticalLayout_2 = QVBoxLayout(self.Animation_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.AnimationValueSet_groupBox = QGroupBox(self.Animation_tab)
        self.AnimationValueSet_groupBox.setObjectName(u"AnimationValueSet_groupBox")
        self.Skip_frame_lineEdit = QLineEdit(self.AnimationValueSet_groupBox)
        self.Skip_frame_lineEdit.setObjectName(u"Skip_frame_lineEdit")
        self.Skip_frame_lineEdit.setGeometry(QRect(40, 20, 31, 20))
        self.Skip_frame_lineEdit.setStyleSheet(u"QLineEdit{qproperty-alignment:AlignHCenter;}\n"
"")
        self.Skip_frame_label = QLabel(self.AnimationValueSet_groupBox)
        self.Skip_frame_label.setObjectName(u"Skip_frame_label")
        self.Skip_frame_label.setGeometry(QRect(10, 20, 31, 20))
        self.Skip_frame_pushButton = QPushButton(self.AnimationValueSet_groupBox)
        self.Skip_frame_pushButton.setObjectName(u"Skip_frame_pushButton")
        self.Skip_frame_pushButton.setGeometry(QRect(80, 20, 91, 21))

        self.verticalLayout_2.addWidget(self.AnimationValueSet_groupBox)

        self.AnimationChoicegroupBox = QGroupBox(self.Animation_tab)
        self.AnimationChoicegroupBox.setObjectName(u"AnimationChoicegroupBox")
        self.Animation_Mirror_checkBox = QCheckBox(self.AnimationChoicegroupBox)
        self.Animation_Mirror_checkBox.setObjectName(u"Animation_Mirror_checkBox")
        self.Animation_Mirror_checkBox.setGeometry(QRect(10, 20, 51, 16))
        self.Animation_Mirror_checkBox.setChecked(False)
        self.Animation_Cache_checkBox = QCheckBox(self.AnimationChoicegroupBox)
        self.Animation_Cache_checkBox.setObjectName(u"Animation_Cache_checkBox")
        self.Animation_Cache_checkBox.setGeometry(QRect(10, 40, 71, 16))
        self.Animation_Cache_checkBox.setChecked(False)

        self.verticalLayout_2.addWidget(self.AnimationChoicegroupBox)

        self.tabWidget.addTab(self.Animation_tab, "")
        self.Debug_tab = QWidget()
        self.Debug_tab.setObjectName(u"Debug_tab")
        self.horizontalLayout = QHBoxLayout(self.Debug_tab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Debug_tabWidget = QTabWidget(self.Debug_tab)
        self.Debug_tabWidget.setObjectName(u"Debug_tabWidget")
        self.Debug_Animation_tab = QWidget()
        self.Debug_Animation_tab.setObjectName(u"Debug_Animation_tab")
        self.Debug_Animation_Actions_listWidget = QListWidget(self.Debug_Animation_tab)
        self.Debug_Animation_Actions_listWidget.setObjectName(u"Debug_Animation_Actions_listWidget")
        self.Debug_Animation_Actions_listWidget.setGeometry(QRect(10, 110, 231, 81))
        self.Debug_Animation_GetActions_pushButton = QPushButton(self.Debug_Animation_tab)
        self.Debug_Animation_GetActions_pushButton.setObjectName(u"Debug_Animation_GetActions_pushButton")
        self.Debug_Animation_GetActions_pushButton.setGeometry(QRect(10, 360, 61, 23))
        self.Debug_Animation_PlayAction_pushButton = QPushButton(self.Debug_Animation_tab)
        self.Debug_Animation_PlayAction_pushButton.setObjectName(u"Debug_Animation_PlayAction_pushButton")
        self.Debug_Animation_PlayAction_pushButton.setGeometry(QRect(70, 360, 81, 23))
        self.Debug_Animation_CoreInfo_groupBox = QGroupBox(self.Debug_Animation_tab)
        self.Debug_Animation_CoreInfo_groupBox.setObjectName(u"Debug_Animation_CoreInfo_groupBox")
        self.Debug_Animation_CoreInfo_groupBox.setGeometry(QRect(10, 10, 231, 91))
        self.Debug_Animation_CoreInfo_Usualyplay_label = QLabel(self.Debug_Animation_CoreInfo_groupBox)
        self.Debug_Animation_CoreInfo_Usualyplay_label.setObjectName(u"Debug_Animation_CoreInfo_Usualyplay_label")
        self.Debug_Animation_CoreInfo_Usualyplay_label.setGeometry(QRect(10, 20, 61, 16))
        self.Debug_Animation_CoreInfo_Usualyplay_lineEdit = QLineEdit(self.Debug_Animation_CoreInfo_groupBox)
        self.Debug_Animation_CoreInfo_Usualyplay_lineEdit.setObjectName(u"Debug_Animation_CoreInfo_Usualyplay_lineEdit")
        self.Debug_Animation_CoreInfo_Usualyplay_lineEdit.setGeometry(QRect(90, 20, 131, 16))
        self.Debug_Animation_CoreInfo_Usualyplay_lineEdit.setStyleSheet(u"QLineEdit{qproperty-alignment:AlignHCenter;}")
        self.Debug_Animation_CoreInfo_Usualyplay_lineEdit.setReadOnly(True)
        self.Debug_Animation_CoreInfo_ImageSize_label = QLabel(self.Debug_Animation_CoreInfo_groupBox)
        self.Debug_Animation_CoreInfo_ImageSize_label.setObjectName(u"Debug_Animation_CoreInfo_ImageSize_label")
        self.Debug_Animation_CoreInfo_ImageSize_label.setGeometry(QRect(10, 40, 71, 16))
        self.Debug_Animation_CoreInfo_ImageSize_x_lineEdit = QLineEdit(self.Debug_Animation_CoreInfo_groupBox)
        self.Debug_Animation_CoreInfo_ImageSize_x_lineEdit.setObjectName(u"Debug_Animation_CoreInfo_ImageSize_x_lineEdit")
        self.Debug_Animation_CoreInfo_ImageSize_x_lineEdit.setEnabled(True)
        self.Debug_Animation_CoreInfo_ImageSize_x_lineEdit.setGeometry(QRect(90, 40, 51, 16))
        self.Debug_Animation_CoreInfo_ImageSize_x_lineEdit.setFocusPolicy(Qt.StrongFocus)
        self.Debug_Animation_CoreInfo_ImageSize_x_lineEdit.setStyleSheet(u"QLineEdit{qproperty-alignment:AlignHCenter;}")
        self.Debug_Animation_CoreInfo_ImageSize_x_lineEdit.setReadOnly(True)
        self.Debug_Animation_CoreInfo_ImageSize_y_lineEdit = QLineEdit(self.Debug_Animation_CoreInfo_groupBox)
        self.Debug_Animation_CoreInfo_ImageSize_y_lineEdit.setObjectName(u"Debug_Animation_CoreInfo_ImageSize_y_lineEdit")
        self.Debug_Animation_CoreInfo_ImageSize_y_lineEdit.setGeometry(QRect(170, 40, 51, 16))
        self.Debug_Animation_CoreInfo_ImageSize_y_lineEdit.setStyleSheet(u"QLineEdit{qproperty-alignment:AlignHCenter;}")
        self.Debug_Animation_CoreInfo_ImageSize_y_lineEdit.setReadOnly(True)
        self.Debug_Animation_CoreInfo_ImageSize_connect_label = QLabel(self.Debug_Animation_CoreInfo_groupBox)
        self.Debug_Animation_CoreInfo_ImageSize_connect_label.setObjectName(u"Debug_Animation_CoreInfo_ImageSize_connect_label")
        self.Debug_Animation_CoreInfo_ImageSize_connect_label.setGeometry(QRect(150, 40, 16, 16))
        self.Debug_Animation_CoreInfo_Change_label = QLabel(self.Debug_Animation_CoreInfo_groupBox)
        self.Debug_Animation_CoreInfo_Change_label.setObjectName(u"Debug_Animation_CoreInfo_Change_label")
        self.Debug_Animation_CoreInfo_Change_label.setGeometry(QRect(10, 60, 71, 16))
        self.Debug_Animation_CoreInfo_Change_lineEdit = QLineEdit(self.Debug_Animation_CoreInfo_groupBox)
        self.Debug_Animation_CoreInfo_Change_lineEdit.setObjectName(u"Debug_Animation_CoreInfo_Change_lineEdit")
        self.Debug_Animation_CoreInfo_Change_lineEdit.setGeometry(QRect(90, 60, 131, 16))
        self.Debug_Animation_CoreInfo_Change_lineEdit.setStyleSheet(u"QLineEdit{qproperty-alignment:AlignHCenter;}")
        self.Debug_Animation_CoreInfo_Change_lineEdit.setReadOnly(True)
        self.Animation_Information_groupBox = QGroupBox(self.Debug_Animation_tab)
        self.Animation_Information_groupBox.setObjectName(u"Animation_Information_groupBox")
        self.Animation_Information_groupBox.setGeometry(QRect(10, 200, 231, 151))
        self.Animation_Information_path_label = QLabel(self.Animation_Information_groupBox)
        self.Animation_Information_path_label.setObjectName(u"Animation_Information_path_label")
        self.Animation_Information_path_label.setGeometry(QRect(10, 20, 31, 16))
        self.Animation_Information_path_lineEdit = QLineEdit(self.Animation_Information_groupBox)
        self.Animation_Information_path_lineEdit.setObjectName(u"Animation_Information_path_lineEdit")
        self.Animation_Information_path_lineEdit.setGeometry(QRect(40, 20, 181, 16))
        self.Animation_Information_path_lineEdit.setReadOnly(True)
        self.Animation_Information_front_label = QLabel(self.Animation_Information_groupBox)
        self.Animation_Information_front_label.setObjectName(u"Animation_Information_front_label")
        self.Animation_Information_front_label.setGeometry(QRect(10, 40, 81, 16))
        self.Animation_Information_end_label = QLabel(self.Animation_Information_groupBox)
        self.Animation_Information_end_label.setObjectName(u"Animation_Information_end_label")
        self.Animation_Information_end_label.setGeometry(QRect(10, 60, 81, 16))
        self.Animation_Information_front_lineEdit = QLineEdit(self.Animation_Information_groupBox)
        self.Animation_Information_front_lineEdit.setObjectName(u"Animation_Information_front_lineEdit")
        self.Animation_Information_front_lineEdit.setGeometry(QRect(90, 40, 131, 16))
        self.Animation_Information_front_lineEdit.setReadOnly(True)
        self.Animation_Information_end_lineEdit = QLineEdit(self.Animation_Information_groupBox)
        self.Animation_Information_end_lineEdit.setObjectName(u"Animation_Information_end_lineEdit")
        self.Animation_Information_end_lineEdit.setGeometry(QRect(90, 60, 131, 16))
        self.Animation_Information_end_lineEdit.setReadOnly(True)
        self.Animation_Information_start_label = QLabel(self.Animation_Information_groupBox)
        self.Animation_Information_start_label.setObjectName(u"Animation_Information_start_label")
        self.Animation_Information_start_label.setGeometry(QRect(10, 80, 61, 16))
        self.Animation_Information_start_lineEdit = QLineEdit(self.Animation_Information_groupBox)
        self.Animation_Information_start_lineEdit.setObjectName(u"Animation_Information_start_lineEdit")
        self.Animation_Information_start_lineEdit.setGeometry(QRect(90, 80, 131, 16))
        self.Animation_Information_start_lineEdit.setReadOnly(True)
        self.Animation_Information_last_label = QLabel(self.Animation_Information_groupBox)
        self.Animation_Information_last_label.setObjectName(u"Animation_Information_last_label")
        self.Animation_Information_last_label.setGeometry(QRect(10, 100, 61, 16))
        self.Animation_Information_last_lineEdit = QLineEdit(self.Animation_Information_groupBox)
        self.Animation_Information_last_lineEdit.setObjectName(u"Animation_Information_last_lineEdit")
        self.Animation_Information_last_lineEdit.setGeometry(QRect(90, 100, 131, 16))
        self.Animation_Information_last_lineEdit.setReadOnly(True)
        self.Animation_Information_fps_label = QLabel(self.Animation_Information_groupBox)
        self.Animation_Information_fps_label.setObjectName(u"Animation_Information_fps_label")
        self.Animation_Information_fps_label.setGeometry(QRect(10, 120, 71, 16))
        self.Animation_Information_fps_lineEdit = QLineEdit(self.Animation_Information_groupBox)
        self.Animation_Information_fps_lineEdit.setObjectName(u"Animation_Information_fps_lineEdit")
        self.Animation_Information_fps_lineEdit.setGeometry(QRect(90, 120, 131, 16))
        self.Animation_Information_fps_lineEdit.setReadOnly(True)
        self.Debug_Animation_Set_usually_play_pushButton = QPushButton(self.Debug_Animation_tab)
        self.Debug_Animation_Set_usually_play_pushButton.setObjectName(u"Debug_Animation_Set_usually_play_pushButton")
        self.Debug_Animation_Set_usually_play_pushButton.setGeometry(QRect(150, 360, 91, 23))
        self.Debug_tabWidget.addTab(self.Debug_Animation_tab, "")
        self.Debug_sound_tab = QWidget()
        self.Debug_sound_tab.setObjectName(u"Debug_sound_tab")
        self.label = QLabel(self.Debug_sound_tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 111, 41))
        self.label.setTextFormat(Qt.MarkdownText)
        self.Debug_tabWidget.addTab(self.Debug_sound_tab, "")

        self.horizontalLayout.addWidget(self.Debug_tabWidget)

        self.tabWidget.addTab(self.Debug_tab, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)

        Setbox.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Setbox)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        Setbox.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.SaveConfig_action)

        self.retranslateUi(Setbox)
        self.ImgSize_control.valueChanged.connect(Setbox.ImgSize_control_valueChange)
        self.TopWindow_checkBox.toggled.connect(Setbox.TopWindow_checkBox_valueChange)
        self.WindowIconbox_checkBox.toggled.connect(Setbox.WindowIconbox_checkBox_valueChange)
        self.SetBox_Go_with_Person_checkBox.toggled.connect(Setbox.SetBox_Go_with_Person_checkBox_valueChange)
        self.Skip_frame_lineEdit.textChanged.connect(Setbox.Change_Skip_frame)
        self.Animation_Mirror_checkBox.toggled.connect(Setbox.Mirror_Image)
        self.Skip_frame_pushButton.clicked.connect(Setbox.Skip_frame_GetBestConfig)
        self.Debug_Animation_GetActions_pushButton.clicked.connect(Setbox.Debug_Animation_GetActions)
        self.Debug_Animation_Actions_listWidget.itemClicked.connect(Setbox.Animation_Information_Get)
        self.Debug_Animation_PlayAction_pushButton.clicked.connect(Setbox.Animation_Test_Play)
        self.Animation_Cache_checkBox.clicked.connect(Setbox.Cache_Image)
        self.Debug_Animation_Set_usually_play_pushButton.clicked.connect(Setbox.SetUsuallyPlay)

        self.tabWidget.setCurrentIndex(0)
        self.Debug_tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Setbox)
    # setupUi

    def retranslateUi(self, Setbox):
        Setbox.setWindowTitle(QCoreApplication.translate("Setbox", u"\u4eba\u7269\u8bbe\u7f6e", None))
        self.SaveConfig_action.setText(QCoreApplication.translate("Setbox", u"\u4fdd\u5b58\u914d\u7f6e", None))
        self.Show_groupBox.setTitle(QCoreApplication.translate("Setbox", u"\u663e\u793a", None))
        self.ImgSize_text.setText(QCoreApplication.translate("Setbox", u"\u7f29\u653e", None))
        self.ImgSize_text_percent.setText(QCoreApplication.translate("Setbox", u"0", None))
        self.TopWindow_checkBox.setText(QCoreApplication.translate("Setbox", u"\u7a97\u53e3\u7f6e\u9876", None))
        self.WindowIconbox_checkBox.setText(QCoreApplication.translate("Setbox", u"\u663e\u793a\u56fe\u6807\u680f\u56fe\u6807", None))
        self.SetBox_Go_with_Person_checkBox.setText(QCoreApplication.translate("Setbox", u"\u8bbe\u7f6e\u9762\u677f\u4e0e\u4eba\u7269\u4f4d\u7f6e\u7ed1\u5b9a", None))
        self.ImagePackageInfo_groupBox.setTitle(QCoreApplication.translate("Setbox", u"\u56fe\u5305\u53c2\u6570", None))
        self.Name_text.setText(QCoreApplication.translate("Setbox", u"\u540d\u79f0", None))
        self.Introduction_text.setText(QCoreApplication.translate("Setbox", u"\u4ecb\u7ecd", None))
        self.Introduction_show.setPlainText("")
        self.Introduction_show.setPlaceholderText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.BasicSet_tab), QCoreApplication.translate("Setbox", u"\u57fa\u672c\u53c2\u6570", None))
        self.AnimationValueSet_groupBox.setTitle(QCoreApplication.translate("Setbox", u"\u53c2\u6570\u8bbe\u7f6e\u7c7b", None))
#if QT_CONFIG(tooltip)
        self.Skip_frame_lineEdit.setToolTip(QCoreApplication.translate("Setbox", u"\u66f4\u6539\u5355\u5e27\u4f11\u7720\u65f6\u95f4\u6765\u8df3\u5e27\uff08\u6b64\u5904\u586b\u5199\u7684\u662f\u539ffps\u5355\u5e27\u4f11\u7720\u65f6\u95f4\u7684\u500d\u6570\uff09\uff08\u4e0d\u8981\u5f97\u5bf8\u8fdb\u5c3a\uff09", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.Skip_frame_lineEdit.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.Skip_frame_lineEdit.setText(QCoreApplication.translate("Setbox", u"1", None))
        self.Skip_frame_lineEdit.setPlaceholderText("")
        self.Skip_frame_label.setText(QCoreApplication.translate("Setbox", u"\u8df3\u5e27", None))
        self.Skip_frame_pushButton.setText(QCoreApplication.translate("Setbox", u"\u9002\u914d\u6700\u4f73\u53c2\u6570", None))
        self.AnimationChoicegroupBox.setTitle(QCoreApplication.translate("Setbox", u"\u9009\u62e9\u9879\u76ee", None))
        self.Animation_Mirror_checkBox.setText(QCoreApplication.translate("Setbox", u"\u955c\u50cf", None))
        self.Animation_Cache_checkBox.setText(QCoreApplication.translate("Setbox", u"\u56fe\u50cf\u7f13\u5b58", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Animation_tab), QCoreApplication.translate("Setbox", u"\u52a8\u753b\u53c2\u6570", None))
        self.Debug_Animation_GetActions_pushButton.setText(QCoreApplication.translate("Setbox", u"\u83b7\u53d6\u6570\u636e", None))
        self.Debug_Animation_PlayAction_pushButton.setText(QCoreApplication.translate("Setbox", u"\u64ad\u653e\u9009\u4e2d\u52a8\u753b", None))
        self.Debug_Animation_CoreInfo_groupBox.setTitle(QCoreApplication.translate("Setbox", u"\u6838\u5fc3\u53c2\u6570[\u53ea\u8bfb]", None))
        self.Debug_Animation_CoreInfo_Usualyplay_label.setText(QCoreApplication.translate("Setbox", u"\u5e38\u6001\u6027\u52a8\u4f5c", None))
        self.Debug_Animation_CoreInfo_ImageSize_label.setText(QCoreApplication.translate("Setbox", u"\u6e32\u67d3\u533a\u57df\u5c3a\u5bf8", None))
        self.Debug_Animation_CoreInfo_ImageSize_connect_label.setText(QCoreApplication.translate("Setbox", u"\u00d7", None))
        self.Debug_Animation_CoreInfo_Change_label.setText(QCoreApplication.translate("Setbox", u"\u7f29\u653e\u7cfb\u6570", None))
        self.Animation_Information_groupBox.setTitle(QCoreApplication.translate("Setbox", u"\u52a8\u753b\u4fe1\u606f[\u9009\u62e9\u540e\u663e\u793a][\u53ea\u8bfb]", None))
        self.Animation_Information_path_label.setText(QCoreApplication.translate("Setbox", u"\u8def\u5f84", None))
        self.Animation_Information_front_label.setText(QCoreApplication.translate("Setbox", u"\u6587\u4ef6\u540d\u79f0\u524d\u5bfc", None))
        self.Animation_Information_end_label.setText(QCoreApplication.translate("Setbox", u"\u6587\u4ef6\u540d\u79f0\u540e\u5bfc", None))
        self.Animation_Information_start_label.setText(QCoreApplication.translate("Setbox", u"\u6587\u4ef6\u8d77\u59cb\u5e27", None))
        self.Animation_Information_last_label.setText(QCoreApplication.translate("Setbox", u"\u6587\u4ef6\u7ec8\u6b62\u5e27", None))
        self.Animation_Information_fps_label.setText(QCoreApplication.translate("Setbox", u"\u52a8\u753b\u8bbe\u5b9afps", None))
        self.Debug_Animation_Set_usually_play_pushButton.setText(QCoreApplication.translate("Setbox", u"\u8bbe\u4e3a\u5e38\u6001\u6027\u52a8\u4f5c", None))
        self.Debug_tabWidget.setTabText(self.Debug_tabWidget.indexOf(self.Debug_Animation_tab), QCoreApplication.translate("Setbox", u"\u52a8\u753b", None))
        self.label.setText(QCoreApplication.translate("Setbox", u"# \u656c\u8bf7\u671f\u5f85", None))
        self.Debug_tabWidget.setTabText(self.Debug_tabWidget.indexOf(self.Debug_sound_tab), QCoreApplication.translate("Setbox", u"\u8bed\u97f3", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Debug_tab), QCoreApplication.translate("Setbox", u"\u8c03\u8bd5\u5668", None))
        self.menu.setTitle(QCoreApplication.translate("Setbox", u"\u83dc\u5355", None))
    # retranslateUi

