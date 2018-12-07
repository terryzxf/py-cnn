# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MW_zxf.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtGui import QFont
from info_get import info_get as ptinfo
from PyQt5 import QtCore, QtWidgets #QtGui,
#from PyQt5.QtGui import QIcon

from action_class import doc_mk, dose_cal, ad_rec_style, rec_mk,first_mk
import sys
from docxtpl import DocxTemplate


class Ui_MainWindow(object):



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.infoLbl = QtWidgets.QLabel(self.centralwidget)
        self.infoLbl.setGeometry(QtCore.QRect(10, 10, 561, 111))
        self.infoLbl.setLineWidth(12)
        self.infoLbl.setText("")
        self.infoLbl.setOpenExternalLinks(False)
        self.infoLbl.setObjectName("infoLbl")

        self.rtidEdt = QtWidgets.QLineEdit(self.centralwidget)
        self.rtidEdt.setGeometry(QtCore.QRect(580, 20, 89, 24))
        self.rtidEdt.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.rtidEdt.setObjectName("rtidEdt")

        self.chkBtn = QtWidgets.QPushButton(self.centralwidget)
        self.chkBtn.setGeometry(QtCore.QRect(680, 20, 89, 24))
        self.chkBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.chkBtn.setObjectName("chkBtn")

        self.cureBtn = QtWidgets.QPushButton(self.centralwidget)
        self.cureBtn.setGeometry(QtCore.QRect(680, 50, 89, 24))
        self.cureBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.cureBtn.setObjectName("cureBtn")

        self.beamNumE = QtWidgets.QLineEdit(self.centralwidget)
        self.beamNumE.setGeometry(QtCore.QRect(10, 170, 61, 24))
        self.beamNumE.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.beamNumE.setObjectName("beamNumE")

        self.TdoseE = QtWidgets.QLineEdit(self.centralwidget)
        self.TdoseE.setGeometry(QtCore.QRect(90, 170, 61, 24))
        self.TdoseE.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.TdoseE.setObjectName("TdoseE")

        self.startDateE = QtWidgets.QLineEdit(self.centralwidget)
        self.startDateE.setGeometry(QtCore.QRect(170, 170, 61, 24))
        self.startDateE.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.startDateE.setObjectName("startDateE")



        self.docBtn = QtWidgets.QPushButton(self.centralwidget)
        self.docBtn.setGeometry(QtCore.QRect(610, 170, 83, 24))
        self.docBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.docBtn.setObjectName("docBtn")

        self.recBtn = QtWidgets.QPushButton(self.centralwidget)
        self.recBtn.setGeometry(QtCore.QRect(700, 170, 83, 24))
        self.recBtn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.recBtn.setObjectName("recBtn")

        self.sectNumE = QtWidgets.QLineEdit(self.centralwidget)
        self.sectNumE.setGeometry(QtCore.QRect(350, 170, 61, 24))
        self.sectNumE.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.sectNumE.setObjectName("sectNumE")

        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(550, 170, 47, 23))
        self.toolButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.toolButton.setObjectName("toolButton")

        self.firmStyl = QtWidgets.QComboBox(self.centralwidget)
        self.firmStyl.setGeometry(QtCore.QRect(250, 170, 86, 24))
        self.firmStyl.setCurrentText("")
        self.firmStyl.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.firmStyl.setObjectName("firmStyl")
        self.firmStyl.addItem("U型面膜+体架")
        self.firmStyl.addItem("S型面膜+体架")
        self.firmStyl.addItem("真空负压袋")
        self.firmStyl.setCurrentIndex(2)

        self.aim = QtWidgets.QComboBox(self.centralwidget)
        self.aim.setGeometry(QtCore.QRect(610, 75, 55, 24))  #680, 50, 89, 24
        self.aim.setCurrentText("")
        self.aim.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.aim.setObjectName("aim")
        self.aim.addItem("根治")
        self.aim.addItem("姑息")
        self.aim.addItem("术前")
        self.aim.addItem("术后")
        self.aim.addItem("预防")
        self.aim.addItem("其它")
        self.aim.setCurrentIndex(1)

        self.part = QtWidgets.QComboBox(self.centralwidget)
        self.part.setGeometry(QtCore.QRect(680, 75, 70, 24))
        self.part.setCurrentText("")
        self.part.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.part.setObjectName("part")
        self.part.addItem("头颈部")
        self.part.addItem("胸部")
        self.part.addItem("腹部")
        self.part.addItem("盆腔")
        self.part.addItem("四肢")
        self.part.addItem("其他")
        self.part.setCurrentIndex(2)

        self.pose = QtWidgets.QComboBox(self.centralwidget)
        self.pose.setGeometry(QtCore.QRect(610, 109, 55, 24))
        self.pose.setCurrentText("")
        self.pose.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pose.setObjectName("pose")
        self.pose.addItem("仰卧")
        self.pose.addItem("俯卧")
        self.pose.addItem("其他")
        self.pose.setCurrentIndex(0)

        self.beamaim = QtWidgets.QComboBox(self.centralwidget)
        self.beamaim.setGeometry(QtCore.QRect(610, 138, 75, 24))
        self.beamaim.setCurrentText("")
        self.beamaim.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.beamaim.setObjectName("beamaim")
        self.beamaim.addItem("原发灶")
        self.beamaim.addItem("淋巴引流区")
        self.beamaim.addItem("转移灶")
        self.beamaim.setCurrentIndex(0)


        self.tech = QtWidgets.QComboBox(self.centralwidget)
        self.tech.setGeometry(QtCore.QRect(680, 109, 75, 24))
        self.tech.setCurrentText("")
        self.tech.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tech.setObjectName("tech")
        self.tech.addItem("3DCRT")
        self.tech.addItem("2D")
        self.tech.addItem("IGRT")
        self.tech.addItem("IMRT")
        self.tech.setCurrentIndex(0)

        self.infoLst = QtWidgets.QTableView(self.centralwidget)
        self.infoLst.setGeometry(QtCore.QRect(10, 200, 781, 341))
        self.infoLst.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.infoLst.setObjectName("infoLst")



        self.BeamNumlbl = QtWidgets.QLabel(self.centralwidget)
        self.BeamNumlbl.setGeometry(QtCore.QRect(10, 140, 68, 16))
        self.BeamNumlbl.setObjectName("BeamNumlbl")

        self.Tdoselbl = QtWidgets.QLabel(self.centralwidget)
        self.Tdoselbl.setGeometry(QtCore.QRect(100, 140, 68, 16))
        self.Tdoselbl.setObjectName("Tdoselbl")

        self.startDatelbl = QtWidgets.QLabel(self.centralwidget)
        self.startDatelbl.setGeometry(QtCore.QRect(170, 140, 80, 16))
        self.startDatelbl.setObjectName("startDatelbl")

        self.secNumlbl = QtWidgets.QLabel(self.centralwidget)
        self.secNumlbl.setGeometry(QtCore.QRect(350, 140, 68, 16))
        self.secNumlbl.setObjectName("secNumlbl")

        self.stylelbl = QtWidgets.QLabel(self.centralwidget)
        self.stylelbl.setGeometry(QtCore.QRect(260, 140, 68, 16))
        self.stylelbl.setObjectName("stylelbl")

        self.ExdoseE = QtWidgets.QLineEdit(self.centralwidget)
        self.ExdoseE.setGeometry(QtCore.QRect(430, 170, 51, 24))
        self.ExdoseE.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.ExdoseE.setObjectName("ExdoseE")

        self.Exdoselbl = QtWidgets.QLabel(self.centralwidget)
        self.Exdoselbl.setGeometry(QtCore.QRect(430, 140, 160, 16))
        self.Exdoselbl.setObjectName("Exdoselbl")

        self.LdoseE = QtWidgets.QLineEdit(self.centralwidget)
        self.LdoseE.setGeometry(QtCore.QRect(490, 170, 51, 24))
        self.LdoseE.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.LdoseE.setObjectName("LdoseE")

        self.Ldoselbl = QtWidgets.QLabel(self.centralwidget)
        self.Ldoselbl.setGeometry(QtCore.QRect(430, 122, 160, 16))
        self.Ldoselbl.setObjectName("Ldoselbl")

        self.statusbar = QtWidgets.QStatusBar(self.centralwidget)
        self.statusbar.setGeometry(QtCore.QRect(5, 566, 800, 32))
        font =QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)


        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        self.Ldoselbl.setVisible(False)
        self.Exdoselbl.setVisible(False)
        self.ExdoseE.setVisible(False)
        self.LdoseE.setVisible(False)

        # 信号槽位置
        self.retranslateUi(MainWindow)
        self.chkBtn.clicked.connect(self.chkBtn_Clk)
        self.docBtn.clicked.connect(self.docBtn_Clk)
        self.recBtn.clicked.connect(self.recBtn_Clk)
        self.cureBtn.clicked.connect(self.cureBtn_Clk)
        self.sectNumE.textEdited.connect(self.sectNumE_endEdt)
        self.beamNumE.textEdited.connect(self.beamNumE_endEdt)
        self.TdoseE.textEdited.connect(self.TdoseE_endEdt)
        self.startDateE.textEdited.connect(self.startDateE_endEdt)
        #self.firmStyl.currentIndexChanged.connect(self.firmStyl_change)

        MainWindow.setTabOrder(self.rtidEdt, self.chkBtn)
        MainWindow.setTabOrder(self.chkBtn, self.beamNumE)
        MainWindow.setTabOrder(self.TdoseE, self.startDateE)
        MainWindow.setTabOrder(self.sectNumE, self.firmStyl)
        MainWindow.setTabOrder(self.firmStyl, self.docBtn)
        MainWindow.setTabOrder(self.docBtn, self.recBtn)
        #MainWindow.setTabOrder(self.recBtn, self.rtidEdt)


    def chkBtn_Clk(self):
            if self.rtidEdt.text() != '':
                rtid = self.rtidEdt.text()  #path = '/home/zxf/病人登记/Data.xlsx'
                pt_S, pt_info, pt_infoTbl= ptinfo.info_get(rtid)
                err = pt_S is None
                self.statusbar.showMessage('查询 %s !' % ('error'if err else rtid ))
                self.infoLbl.setText(pt_info)
            else:
                self.statusbar.showMessage('rdid is null, input again! stupid!')

    # docBtn() 功能:生成病程
    #  子过程:
    # 1.需要完成的动作: BeamNum Tdose startDose secNum firmStyle Exdose Ldose 的获取存储           done
    #   动作 secNum change动作  secNum=2 Exdose Ldose可见  secNum=1 Exdose可见 secNum='' Exdose   done
    # 2. 传入的变量 其中secNum 为空 Exdose Ldose 为0 可不传递不计算
    #                 secNum ==1  Exdose 传递计算
    #                 secNum ==2  Exdose Ldose 传递计算
    # BeamNum野数 首次病程中的野数
    # Tdose首次计划总剂量 格式为 xxGY/yyF  根据xx/yy计算出分割单次剂量 由此推算出每次中间病程的累加剂量mdose
    # yy为次数 yy/5计算出中间病程数 mRecNum
    # startDose 和yy 协同计算出结束日期和中间病程的日期
    # secNum 首次计划结束病程后 是否有追加再次病程 后续中间 Exdose  xxGY/yyF 计算出 yy/5 后续追加中间病程数 ExmRecNum
    # firmStyle 固定方式 首次病程和追加病程中的固定方式
    # Exdose 追加计划的剂量  secNum <1时不输入和计算
    # Ldose 最后追加计划的剂量 secNum <2时不输入和计算

    def docBtn_Clk(self):
        #firmStyle = self.firmStyl.currentText()
        #startDat = self.startDateE.text()
        #self.statusbar.showMessage('生成doc! '+ startDat)
        #if self.format_chk():
        #else:
        #self.format_chk()
        if self.rtidEdt.text() != '':
            rtid = self.rtidEdt.text()  # path = '/home/zxf/病人登记/Data.xlsx'
            pt_S, pt_info, pt_infoTbl = ptinfo.info_get(rtid)
            err = pt_S is None
            self.statusbar.showMessage('查询 %s !' % ('error' if err else rtid))
            self.infoLbl.setText(pt_info)

            beamNum = self.beamNumE.text()
            Tdose = self.TdoseE.text()
            firmStyle = self.firmStyl.currentText()
            startdate = self.startDateE.text()
            diagnosisT =''
            sectNum = self.sectNumE.text()
            Exdose = self.ExdoseE.text()
            Ldose = self.LdoseE.text()

            doc_mk(pt_S, beamNum, firmStyle, Tdose, startdate, diagnosisT, sectNum, Exdose, Ldose)
        else:
            self.statusbar.showMessage('rdid is null')



    def recBtn_Clk(self):

        rtid = self.rtidEdt.text()
        #print(isinstance((eval(rtid)),int))
        if rtid != '' and eval(rtid) and eval(rtid) in range(2574,9999):

            startDate = self.startDateE.text()
            pt_S, pt_info, pt_infoTbl = ptinfo.info_get(rtid)
            self.infoLbl.setText(pt_info)

            #first_mk(pt_S)
            rec_mk(pt_S, startDate, rtid)
            self.statusbar.showMessage('生成rec!')


    def cureBtn_Clk(self): #生成治疗前小结

        gerpath = str(sys.path[0])

        rtid = self.rtidEdt.text()
        pt_S, pt_info, pt_infoTbl = ptinfo.info_get(rtid)

        dose = self.TdoseE.text()
        startdate = self.startDateE.text()
        tdose, dosesplit, dose_t =dose_cal(dose)

        aimC= str(self.aim.currentIndex())
        partC =str(self.part.currentIndex())
        firmC =str(self.firmStyl.currentIndex())
        #techC = str(self.tech.currentIndex())
        beamaimC =str(self.beamaim.currentIndex())
        poseC = str(self.pose.currentIndex())

        aim = {'aim0': '□', 'aim1': '□', 'aim2': '□', 'aim3': '□', 'aim4': '□', 'aim5': '□'}
        part = {'part0':'□', 'part1':'□', 'part2':'□', 'part3':'□', 'part4':'□'}
        firm = {'firm0':'□', 'firm1':'□', 'firm2':'□', 'firm3':'□', 'firm4':'□'}
        #tech = {'tech0':'□', 'tech1':'□', 'tech2':'□', 'tech3':'□'}
        pose = {'pose0':'□', 'pose1':'□', 'pose2':'□'}
        ndose = {'dose':dose_t*dosesplit,'splite':dosesplit, 'days':int(dosesplit/5*7) }
        beamaim ={'tar0':' ','tar1':' ', 'tar2':' '}

        context = {
            'name': pt_S.Names, 'sex': pt_S.sex, 'age': pt_S.age, 'nid': pt_S.id, 'dignose': pt_S.dignose,
            'firmdate': startdate, 'plandate': startdate, 'confirmdate': startdate}

        aim['aim'+aimC] = 'R'
        part['part'+partC] ='R'
        firm['firm'+firmC] ='R'
        #tech['tech'+techC] ='R'
        beamaim['tar'+beamaimC] = pt_S.bodyPart
        pose['pose'+poseC] = 'R'

        context.update(aim)
        context.update(part)
        context.update(firm)
        #context.update(tech)
        context.update(ndose)
        context.update(beamaim)
        context.update(pose)

        #print(context.keys())
        Adoc = DocxTemplate(gerpath+'/模板doc/Adoc_bk.docx')


        Adoc.render(context)

        filepath = gerpath + '/record/放疗前小结记录/'+pt_S.Names+'_放疗前小结.doc'
        Adoc.save(filepath)

        ad_rec_style(filepath)


    def sectNumE_endEdt(self): #完成的动作: 检验格式合法性  变量传递 设置追加剂量input 和label的可视性

        secNum = self.sectNumE.text()
        if secNum == '':
            self.Ldoselbl.setVisible(False)
            self.Exdoselbl.setVisible(False)
            self.ExdoseE.setVisible(False)
            self.LdoseE.setVisible(False)
            self.statusbar.showMessage("")
        elif secNum == '1':
            self.Ldoselbl.setVisible(False)
            self.Exdoselbl.setVisible(True)
            self.ExdoseE.setVisible(True)
            self.LdoseE.setVisible(False)
            self.statusbar.showMessage("")
        elif secNum == '2':
            self.Ldoselbl.setVisible(True)
            self.Exdoselbl.setVisible(True)
            self.ExdoseE.setVisible(True)
            self.LdoseE.setVisible(True)
            self.statusbar.showMessage("")
        else:
            self.Ldoselbl.setVisible(False)
            self.Exdoselbl.setVisible(False)
            self.ExdoseE.setVisible(False)
            self.LdoseE.setVisible(False)
            self.ExdoseE.setVisible(False)
            self.LdoseE.setVisible(False)
            self.statusbar.showMessage("secNum get an unexpect input, check ur mind.")

    def beamNumE_endEdt(self): #完成的动作: 检验格式合法性  变量传递

        beamNum = self.beamNumE.text()
        if not beamNum.isalnum() and int(beamNum) in range (15):
            self.statusbar.showMessage("!!! (BeaNu) illegal input !!!")

    def TdoseE_endEdt(self): #完成的动作: 检验格式合法性  变量传递

        Tdose = self.TdoseE.text()


    def startDateE_endEdt(self): #完成的动作: 检验格式合法性  变量传递

        startDate = self.startDateE.text()

    def format_chk(self):
        self.statusbar.showMessage('')
        error = 0
        beamstatus =''
        Tdosestatus = ''
        sectNumEstatus =''
        startDateEstatus = ''
        firmStylestatus = ''
        if self.beamNumE.text() == '' or eval(self.beamNumE.text())<0 or not type(eval(self.beamNumE.text()))==int:
            error = 1
            beamstatus = 'beamnum unexpect!'
        if not self.TdoseE.text().find('/') or self.TdoseE.text() =='':
            error = 1
            Tdosestatus = 'unexpect Tdo!'
        if self.startDateE.text() =='' or not type(eval(self.startDateE.text())) == int or eval(self.startDateE.text()) not in range(10000101,99991231):
            error =1
            startDateEstatus = 'stD unexpect!'
        #if (self.sectNumE.text() == '') and not type(eval(self.sectNumE.text()))==int or eval(self.sectNumE.text())<=2:
         #   error =1
          #  sectNumEstatus = 'unexpect sec!'
        if self.firmStyl.currentText() =='':
            error =1
            firmStylestatus = 'unexpect firmStyle!'

        if error == 1:
            self.statusbar.showMessage(beamstatus+Tdosestatus+sectNumEstatus+startDateEstatus+firmStylestatus)
        return error




    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Soul"))
        self.chkBtn.setText(_translate("MainWindow", "OK"))
        self.docBtn.setText(_translate("MainWindow", "DM"))
        self.recBtn.setText(_translate("MainWindow", "BM"))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.BeamNumlbl.setText(_translate("MainWindow", "BeaNu"))
        self.Tdoselbl.setText(_translate("MainWindow", "Tdo(G/F)"))
        self.startDatelbl.setText(_translate("MainWindow", "StD(Y4-M2-D2)"))
        self.secNumlbl.setText(_translate("MainWindow", "sec"))
        self.stylelbl.setText(_translate("MainWindow", "style"))
        self.Exdoselbl.setText(_translate("MainWindow", "Ed(G/F/yyyy-mm-dd/beaN)"))
        self.Ldoselbl.setText(_translate("MainWindow", "Ld(G/F/yyyy-mm-dd/beaN)"))
        self.cureBtn.setText(_translate("MainWindow", "Adoc"))

    def __init__(self):
        super().__init__()

        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        #ui = Ui_MainWindow()
        self.setupUi(MainWindow)
        #MainWindow.setWindowIcon(QIcon('icon.png'))  #增加icon图标
        MainWindow.show()
        sys.exit(app.exec_())



"""
if __name__ == "__main__":


    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    #MainWindow.setWindowIcon(QIcon('icon.png'))  #增加icon图标
    MainWindow.show()
    sys.exit(app.exec_())
"""