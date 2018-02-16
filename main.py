# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Retirement\actual.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from screens import page11, page2, page3, page4, expenses

class Ui_RetirementCalculator(object):
    def setupUi(self, RetirementCalculator):
        RetirementCalculator.setObjectName("RetirementCalculator")
        RetirementCalculator.resize(636, 455)
        RetirementCalculator.setStyleSheet("background-color: rgb(30, 37, 50);")
        self.stackedWidget = QtWidgets.QStackedWidget(RetirementCalculator)
        self.stackedWidget.setGeometry(QtCore.QRect(30, 30, 571, 391))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.form=page11.Ui_Form()
        self.form.Page1Ui(self.page)
        self.form.horizontalSlider_3.setMinimum=0
        self.form.horizontalSlider_3.setMaximum=100
        self.form.horizontalSlider_3.valueChanged.connect(self.valuechange)
        self.form.horizontalSlider_4.setMinimum=0
        self.form.horizontalSlider_4.setMaximum=100
        self.form.horizontalSlider_4.valueChanged.connect(self.valuechange)
        self.form.pushButton_2.clicked.connect(self.onNext)        
        self.stackedWidget.addWidget(self.page)

        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.form2=page2.Ui_Form()
        self.form2.Page2Ui(self.page2)
        self.form2.pushButton_3.clicked.connect(self.onNext_page2)
        self.form2.pushButton_4.clicked.connect(self.onBack)
        self.stackedWidget.addWidget(self.page2)

        self.page3 = QtWidgets.QWidget()
        self.page3.setObjectName("page3")
        self.form3=page3.Ui_Form()
        self.form3.Page3Ui(self.page3)
        self.form3.pushButton_2.clicked.connect(self.onNext_page3)
        self.form3.pushButton_4.clicked.connect(self.onBack)
        self.stackedWidget.addWidget(self.page3)

        self.page4 = QtWidgets.QWidget()
        self.page4.setObjectName("page4")
        self.form4=page4.Ui_Form()
        self.form4.Page4Ui(self.page4)
        self.form4.pushButton_4.clicked.connect(self.onBack)
        self.stackedWidget.addWidget(self.page4)

        self.label = QtWidgets.QLabel(RetirementCalculator)
        self.label.setGeometry(QtCore.QRect(200, 20, 251, 20))
        self.label.setStyleSheet("color: rgb(255, 170, 0);\n"
"font: 75 italic 16pt \"Segoe UI Historic\";")
        self.label.setObjectName("label")

        self.retranslateUi(RetirementCalculator)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(RetirementCalculator)

    def onNext(self):
        if self.stackedWidget.currentIndex()==0:
            self.Age=self.form.lineEdit_6.text()
            self.RetirementAge=self.form.lineEdit_5.text()
            self.Expenses=self.form.lineEdit_7.text()
            self.Inflation_rate=self.form.lineEdit_8.text()
            print(f'Age is {self.Age}')
            print(f'Retirement Age is {self.RetirementAge}')
            print(f'Expenses is {self.Expenses}')
            print(f'Inflation rate is {self.Inflation_rate}')
            if self.Age=="" or self.RetirementAge=="" or self.Expenses=="" or self.Inflation_rate=="" :
                self.form.stackedWidget.setCurrentIndex(0)
                self.stackedWidget.setCurrentIndex(0)
            else:
                self.expensecal=expenses.Expense_Calculator()
                self.Future_Expense=self.expensecal.Expenses(int(self.Age), int(self.RetirementAge), int(self.Inflation_rate), int(self.Expenses))
                self.rowcount=int(self.RetirementAge)-int(self.Age)+1
                self.form2.tableWidget.setColumnCount(2)
                count=0
                self.form2.tableWidget.setRowCount(self.rowcount)
                for x in range(int(self.Age),int(self.RetirementAge)+1):
                    print(f'Age->{x},Expense->{self.Future_Expense[x]}')
                    self.form2.tableWidget.setItem(count, 0, QtWidgets.QTableWidgetItem(str(x)))
                    self.form2.tableWidget.setItem(count, 1, QtWidgets.QTableWidgetItem(str(self.Future_Expense[x])))
                    count+=1
                self.form2.tableWidget.setHorizontalHeaderLabels(('AGE,EXPENSE').split(','))
                self.form2.tableWidget.horizontalHeader().setStretchLastSection(True)
                self.form2.tableWidget.resizeColumnsToContents()
                self.form2.tableWidget.verticalHeader().hide()
                self.stackedWidget.setCurrentIndex(1)
 
    def onNext_page2(self):
        if self.stackedWidget.currentIndex()==1:
            self.stackedWidget.setCurrentIndex(2)

    def onNext_page3(self):
        if self.stackedWidget.currentIndex()==2:
            self.Corpus=self.form3.lineEdit_6.text()
            self.Deposit_rate=self.form3.lineEdit_5.text()
            print(f'Corpus is {self.Corpus}')
            print(f'Interest is {self.Deposit_rate}')
            if self.Corpus=="" or self.Deposit_rate=="" :
                self.form3.tableWidget.setCurrentIndex(1)
            else:
                self.Future_Balance=self.expensecal.Balance(int(self.Corpus), int(self.Age), int(self.RetirementAge), int(self.Deposit_rate), int(self.Inflation_rate), self.Future_Expense)
                self.Min_Balance=self.expensecal.Minimum_Balance(int(self.Age), int(self.RetirementAge), int(self.Deposit_rate), int(self.Inflation_rate), self.Future_Expense)
                self.form4.tableWidget.setColumnCount(2)
                self.form4.tableWidget.setRowCount(self.rowcount)
                count=0
                for x in range(int(self.Age),int(self.RetirementAge)+1):
                    print(f'Age is {x}, Balance->{self.Future_Balance[x]}')
                    self.form4.tableWidget.setItem(count, 0, QtWidgets.QTableWidgetItem(str(x)))
                    self.form4.tableWidget.setItem(count, 1, QtWidgets.QTableWidgetItem(str(self.Future_Balance[x])))
                    count+=1
                if int(self.Future_Balance[int(self.RetirementAge)-1])<int(self.Min_Balance):
                    self.form4.stackedWidget.setCurrentIndex(1)
                    self.form4.label.setText("Min Corpus is {}.Your Corpus is not sufficient to retire now :(".format(self.Min_Balance))
                else:
                    self.form4.stackedWidget.setCurrentIndex(0)
                    self.form4.label3.setText("Min Corpus is {}.You have sufficent funds to retire. COngrats!!".format(self.Min_Balance))
                self.form4.tableWidget.setHorizontalHeaderLabels(('AGE,BALANCE').split(','))
                self.form4.tableWidget.horizontalHeader().setStretchLastSection(True)
                self.form4.tableWidget.resizeColumnsToContents()
                self.form4.tableWidget.verticalHeader().hide()
                self.stackedWidget.setCurrentIndex(3)

    def onBack(self):
        if self.stackedWidget.currentIndex()==1:
            self.stackedWidget.setCurrentIndex(0)
        if self.stackedWidget.currentIndex()==2:
            self.stackedWidget.setCurrentIndex(1)
        if self.stackedWidget.currentIndex()==3:
            self.stackedWidget.setCurrentIndex(2)

    def retranslateUi(self, RetirementCalculator):
        _translate = QtCore.QCoreApplication.translate
        RetirementCalculator.setWindowTitle(_translate("RetirementCalculator", "Form"))
        self.label.setText(_translate("RetirementCalculator", "Retirement Calculator"))

    def valuechange(self):
        self.value4=str(self.form.horizontalSlider_4.value())
        self.value3=str(self.form.horizontalSlider_3.value())
        self.form.lineEdit_6.setText(self.value3)
        self.form.lineEdit_5.setText(self.value4)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RetirementCalculator = QtWidgets.QWidget()
    ui = Ui_RetirementCalculator()
    ui.setupUi(RetirementCalculator)
    RetirementCalculator.show()
    sys.exit(app.exec_())

