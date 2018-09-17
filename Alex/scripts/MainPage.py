from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
import sys
import Item
import ChatPage

class MainPage(QDialog):
    close_signal = pyqtSignal()
    def __init__(self, mc,parent=None):
        # super这个用法是调用父类的构造函数
        # parent=None表示默认没有父Widget，如果指定父亲Widget，则调用之
        super(MainPage, self).__init__(parent)
        loadUi('UI/mainPage.ui',self)
        self.mc = mc
        self.mc.mainPage = self
        self.itemWidget = QWidget()
        self.sca.setWidget(self.itemWidget)
        self.vLayout = QVBoxLayout(self.itemWidget)
        self.btn_state1.clicked.connect(self.toState1)
        self.btn_state2.clicked.connect(self.toState2)
        self.btn_state3.clicked.connect(self.toState3)
        self.btn_state4.clicked.connect(self.toState4)
        self.btn_logout.clicked.connect(self.logout)
        self.btn_addMoney.clicked.connect(self.addMoney)
        self.btn_startChat.clicked.connect(self.startChat)


    def toState1(self):
        self.mc.searchState = 1
        self.getState()

    def toState2(self):
        self.mc.searchState = 2
        self.getState()

    def toState3(self):
        self.mc.searchState = 3
        self.getState()

    def toState4(self):
        self.mc.searchState = 4
        self.getState()


    def getItemInfo(self):
        self.mc.items = []
        if self.mc.searchState == 1:
            for i in range(5):
                tmp = {}
                tmp['itemName'] = '商品'+str(i)
                tmp['seller'] = '卖家'+str(i)
                tmp['startTime'] = '开始时间'+str(i)
                tmp['startPrice'] = str(i*100)
                self.mc.items.append(tmp)

    def getState(self):
        self.setLine()
        self.getItemInfo()

        self.itemWidget.destroy()
        self.itemWidget = QWidget()
        self.sca.setWidget(self.itemWidget)
        self.vLayout = QVBoxLayout(self.itemWidget)
        self.vLayout.setContentsMargins(0, 0, 0, 0)
        self.vLayout.setSpacing(0)
        for i in range(len(self.mc.items)):
            item = Item.Item1(self.mc,i)
            item.setMinimumSize(521, 100)
            self.vLayout.addWidget(item, alignment=Qt.AlignTop)
        self.vLayout.addStretch(1)

    def setLine(self):
        self.lin.setGeometry(290 + (self.mc.searchState-1)*140,170,20,31)

    def logout(self):
        self.mc.username = None
        self.mc.nextPage = 'loginPage'
        self.close()

    def addMoney(self):
        if self.lie_addMoney.text().isdigit():
            self.mc.money += int(self.lie_addMoney.text())
        else:
            QMessageBox.information(self, "错误", "请输入正确金额！\n（目前只支持整数金额）",QMessageBox.Yes)
        self.lie_addMoney.setText('')
        self.lbl_money.setText(str(self.mc.money) + ' 元')

    def startChat(self):
        if not self.lwg_other.selectedItems():
            QMessageBox.information(self, "错误", "请选择一个用户!",QMessageBox.Yes)
            return
        other = self.lwg_other.selectedItems()[0].text()
        #########################################
        #开始p2p
        #########################################
        self.mc.chatOther = other
        ChatPage.ChatPage(self.mc).run()
        # self.mc.nextPage = 'chatPage'
        # self.close()

    def closeEvent(self, event):
        if not self.mc.nextPage:
            sys.exit()

    def run(self):
        self.mc.nextPage = None
        self.lbl_username.setText(self.mc.username)
        r = ''
        for x in self.mc.roles:
            r += x + '\n'
        self.lbl_roles.setText(r)
        if not '商品管理员' in self.mc.roles:
            self.btn_state4.setEnabled(False)
        self.lbl_money.setText(str(self.mc.money) + ' 元')
        for i in range(100):
            self.lwg_other.addItem(str(i))

        self.exec_()

