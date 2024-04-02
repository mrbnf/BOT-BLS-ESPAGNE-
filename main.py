from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic 
from blsFacilateWork import BlsFacilateWork
import sys
import os
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton
from PyQt5.QtWidgets import QApplication, QMainWindow
import json
import threading
from mygui import Ui_Dialog
with open('data.json','r') as f:
    data = json.loads(f.read())
with open('cookies.json','r') as f2:
    cookies = json.loads(f2.read())
user_session = BlsFacilateWork()
user_session=BlsFacilateWork()
class MyGUI(QMainWindow,QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.startButton.clicked.connect(self.start_auto)
        self.ui.addButton.clicked.connect(self.add_new)
        self.ui.deleteButton.clicked.connect(self.delete_row)
        self.ui.saveButton.clicked.connect(self.save_table)
        self.ui.loginAllCheckBox.stateChanged.connect(self.on_loginAllCheckBox_state_changed)
        self.ui.manualCheckBox.stateChanged.connect(self.on_manualCheckBox_state_changed)
        self.ui.selfieCheckBox.stateChanged.connect(self.on_selfieCheckBox_state_changed)
        self.ui.paymentCheckBox.stateChanged.connect(self.on_paymentCheckBox_state_changed)
        self.ui.calenderBox.addItem('3 times only')
        self.ui.calenderBox.addItem('all green')
        self.ui.calenderBox.addItem('30 days')
        self.ui.calenderBox.currentIndexChanged.connect(self.on_combo_box_index_changed)

        self.load_emails()
    
    def on_selfieCheckBox_state_changed(self, state):
        if state == 2:  # Qt.Checked
            user_session.selfieFill = True
            # Perform actions when checkbox is checked
        else:
            user_session.selfieFill = False
    def on_paymentCheckBox_state_changed(self, state):
        if state == 2:  # Qt.Checked
            user_session.paymentFill = True
            # Perform actions when checkbox is checked
        else:
            user_session.paymentFill = False
    def on_combo_box_index_changed(self, index):
        # Access the selected item's text
        selected_item = self.ui.calenderBox.currentText()
        if selected_item == '3 times only':
            user_session.dateGetType = 0
        elif selected_item == 'all green':
            user_session.dateGetType = 1
        elif selected_item == '30 days':
            user_session.dateGetType = 2
    def on_loginAllCheckBox_state_changed(self, state):
        if state == 2:  # Qt.Checked
            user_session.login_all = True
            # Perform actions when checkbox is checked
        else:
            user_session.login_all = False
    def on_manualCheckBox_state_changed(self, state):
        if state == 2:  # Qt.Checked
            user_session.all_manual = True
            # Perform actions when checkbox is checked
        else:
            user_session.all_manual = False

    def delete_row(self):
        selected_items = self.ui.tableWidget.selectedItems()
        selected_rows = set()

        # Get the row indexes of the selected cells
        for item in selected_items:
            selected_rows.add(item.row())

        # Remove selected rows from the table
        for row in sorted(selected_rows, reverse=True):
            del data[self.ui.tableWidget.item(row, 0).text()]
            self.ui.tableWidget.removeRow(row)
        with open('data.json', 'w') as f3:
            json.dump(data, f3)
    def save_table(self):
        row_count = self.ui.tableWidget.rowCount()
        for i in range(row_count):
            data[self.ui.tableWidget.item(i, 0).text()]=[self.ui.tableWidget.item(i, 0).text(),self.ui.tableWidget.item(i, 1).text(),self.ui.tableWidget.item(i, 2).text(),  self.ui.tableWidget.item(i, 3).text(), self.ui.tableWidget.item(i, 4).text(), self.ui.tableWidget.item(i, 5).text(), self.ui.tableWidget.item(i, 6).text()]
        with open('data.json', 'w') as f3:
            json.dump(data, f3)
    def add_new(self):
        row_count = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row_count)
        for i in range(7):
            if self.ui.addTable.item(0, i)== None:
                self.ui.tableWidget.setItem(row_count,i,QTableWidgetItem(""))
            else:
                self.ui.tableWidget.setItem(row_count,i,QTableWidgetItem(self.ui.addTable.item(0, i).text()))
        #self.ui.tableWidget.setItem(row_count,0,QTableWidgetItem(self.ui.addTable.item(0, 0).text()))
        #self.ui.tableWidget.setItem(row_count,1,QTableWidgetItem(self.ui.addTable.item(0, 1).text()))
        #self.ui.tableWidget.setItem(row_count,2,QTableWidgetItem(self.ui.addTable.item(0, 2).text()))
        #self.ui.tableWidget.setItem(row_count,3,QTableWidgetItem(self.ui.addTable.item(0, 3).text()))
        #self.ui.tableWidget.setItem(row_count,4,QTableWidgetItem(self.ui.addTable.item(0, 4).text()))
        #self.ui.tableWidget.setItem(row_count,5,QTableWidgetItem(self.ui.addTable.item(0, 5).text()))
        #self.ui.tableWidget.setItem(row_count,6,QTableWidgetItem(self.ui.addTable.item(0, 6).text()))
        button = QPushButton("Open")
        button.clicked.connect(lambda checked, idx=row_count,btn=button: self.handle_button_clicked(idx,btn))
        self.ui.tableWidget.setCellWidget(row_count, 7, button)
        data[self.ui.addTable.item(0, 0).text()]=[self.ui.addTable.item(0, 0).text(),self.ui.addTable.item(0, 1).text(),self.ui.addTable.item(0, 2).text(), "" if self.ui.addTable.item(0, 3) == None else self.ui.addTable.item(0, 3).text(),"" if self.ui.addTable.item(0, 4) == None else self.ui.addTable.item(0, 4).text(),"" if self.ui.addTable.item(0, 5) == None else self.ui.addTable.item(0, 5).text(),"" if self.ui.addTable.item(0, 6) == None else self.ui.addTable.item(0, 6).text()]
        cookies[self.ui.addTable.item(0, 0).text()]= None
        print(data)
        with open('data.json', 'w') as f3:
            json.dump(data, f3)
        with open('cookies.json', 'w') as f4:
            json.dump(cookies, f4)
    def start_auto(self):
        if self.ui.startButton.text() == "Start Notifications":  # Check button text
            self.ui.startButton.setText("Stop Notifications")
            self.ui.startButton.repaint()
            thread1 = threading.Thread(target=user_session.go_auto, args=())
            thread1.start()
            #user_session.go_auto()
            
        else:
            self.ui.startButton.setText("Start Notifications")
            self.ui.startButton.repaint()
            user_session.stop_auto =True
    def load_emails(self):
        self.ui.tableWidget.setRowCount(len(data))    
        self.ui.tableWidget.setColumnCount(8)
        self.ui.tableWidget.setHorizontalHeaderLabels(('Email','place','member','N carte','CVV','Nom Carte','Expiry','open/close'))
        self.ui.addTable.setRowCount(1)    
        self.ui.addTable.setColumnCount(7)
        self.ui.addTable.setHorizontalHeaderLabels(('Email','place','member','N carte','CVV','Nom Carte','Expiry'))
        index = 0
        for d in data :
            self.ui.tableWidget.setItem(index,0,QTableWidgetItem(data[d][0]))
            self.ui.tableWidget.setItem(index,1,QTableWidgetItem(data[d][1]))
            self.ui.tableWidget.setItem(index,2,QTableWidgetItem(data[d][2]))
            self.ui.tableWidget.setItem(index,3,QTableWidgetItem(data[d][3]))
            self.ui.tableWidget.setItem(index,4,QTableWidgetItem(data[d][4]))
            self.ui.tableWidget.setItem(index,5,QTableWidgetItem(data[d][5]))
            self.ui.tableWidget.setItem(index,6,QTableWidgetItem(data[d][6]))
            button = QPushButton("Open")
            button.clicked.connect(lambda checked, idx=data[d][0],btn=button: self.handle_button_clicked(idx,btn))
            self.ui.tableWidget.setCellWidget(index, 7, button)
            index+=1
    def handle_button_clicked(self,index,button):
        #user_session.make_session(index,False)
        
        if button.text() == "Open":  # Check button text
            button.setText("Close")
            button.repaint()
            thread = threading.Thread(target=user_session.make_session, args=(index,False))
            thread.start()
            #thread = threading.Thread(target=user_session.go_auto, args=())
            #thread.start()
            #user_session.go_auto()
            
        else:
            button.setText("Open")
            button.repaint()
            user_session.session_chrome[index].close()
            user_session.session_chrome[index]=None

        #print(f"Button clicked!")

def main():
    app = QApplication(sys.argv)
    window = MyGUI()
    window.show()
    app.exec_()
if __name__=='__main__':
    main()
