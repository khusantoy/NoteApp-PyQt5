import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget, 
    QLineEdit,
    QLabel,
    QPushButton,
    QListWidget,
    QHBoxLayout,
    QVBoxLayout,
    QTextEdit
)

class ErrorWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Wrong")
        self.setFixedSize(350, 100)
        self.setStyleSheet("""
            font-family: Arial;
            font-size: 24px;
            color: #FFF;
            background-color: #DC3545;
        """)

        self.error = QLabel(self)
        self.error.setText("⚠️ Something went wrong")
        self.error.setAlignment(Qt.AlignCenter)

        self.h_box = QHBoxLayout()
        self.v_box = QVBoxLayout()

        self.h_box.addWidget(self.error)
        self.v_box.addLayout(self.h_box)

        self.setLayout(self.v_box)

        self.show()

    def change_error(self, text):
        self.error.setText(text)

class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Welcome to Notion")
        self.setFixedSize(400, 500)

        self.title = QLabel(self)
        self.title.setText("Notes:")
        self.title.setStyleSheet("""
            font-family: Arial;
            font-size: 24px;
        """)

        self.notes = QListWidget(self)
        self.notes.setStyleSheet("""
            font-family: Arial;
            font-size: 18px;
            border: 2px solid #343A40;
        """)

        self.add_btn = QPushButton(self)
        self.add_btn.setText("Add Note")
        self.add_btn.setFixedHeight(40)
        self.add_btn.setStyleSheet("""
            QPushButton {
                font-family: Arial;
                font-size: 18px;
                border: 2px solid #0F5132;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #198754;
                color: #FFF;
            }
        """)

        self.view_btn = QPushButton(self)
        self.view_btn.setText("View Note")
        self.view_btn.setFixedHeight(40)
        self.view_btn.setStyleSheet("""
            QPushButton {
                font-family: Arial;
                font-size: 18px;
                border: 2px solid #084298;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #0D6EFD;
                color: #FFF;
            }
        """)

        self.delete_btn = QPushButton(self)
        self.delete_btn.setText("Delete Note")
        self.delete_btn.setFixedHeight(40)
        self.delete_btn.setStyleSheet("""
            QPushButton {
                font-family: Arial;
                font-size: 18px;
                border: 2px solid #842029;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #DC3545;
                color: #FFF;
            }
            QPushButton:pressed {
                opacity: 0.5;
            }
        """)

        self.exit_btn = QPushButton(self)
        self.exit_btn.setText("Exit")
        self.exit_btn.setFixedHeight(40)
        self.exit_btn.setStyleSheet("""
            QPushButton {
                font-family: Arial;
                font-size: 18px;
                border: 2px solid #495057;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #343A40;
                color: #FFF;
            }
            QPushButton:pressed {
                opacity: 0.5;
            }
        """)

        self.h_box1 = QHBoxLayout()
        self.h_box2 = QHBoxLayout()
        self.h_box3 = QHBoxLayout()
        self.h_box4 = QHBoxLayout()
        self.h_box5 = QHBoxLayout()
        self.h_box6 = QHBoxLayout()

        self.v_box = QVBoxLayout()

        self.h_box1.addWidget(self.title)
        self.h_box2.addWidget(self.notes)
        self.h_box3.addWidget(self.add_btn)
        self.h_box4.addWidget(self.view_btn)
        self.h_box5.addWidget(self.delete_btn)
        self.h_box6.addWidget(self.exit_btn)

        self.v_box.addLayout(self.h_box1)
        self.v_box.addLayout(self.h_box2)
        self.v_box.addLayout(self.h_box3)
        self.v_box.addLayout(self.h_box4)
        self.v_box.addLayout(self.h_box5)
        self.v_box.addLayout(self.h_box6)

        self.setLayout(self.v_box)

        self.show()

        try:
            with open("notes.txt", "r") as f:
                self.count = 1
                for i in f.readlines():
                    i = i.split('|')
                    self.notes.addItem(f'{self.count}. {i[0]}')
                    self.count +=1
                f.close()
        except FileNotFoundError:
            self.win = ErrorWindow()
            self.win.change_error("⚠️ Not found notes.txt!")

        self.add_btn.clicked.connect(self.add)
        self.view_btn.clicked.connect(self.view)
        self.delete_btn.clicked.connect(self.delete_line)
        self.exit_btn.clicked.connect(self.exit)

    def add(self):
        self.close()
        self.win = AddWindow()

    def view(self):
        self.close()
        self.win = ViewWindow()
        self.index = self.notes.currentRow()
        self.win.show_content(self.index)

    def delete_line(self):
        def is_file_empty(file_path):
            return os.path.getsize(file_path) == 0

        file_path = 'notes.txt'

        if is_file_empty(file_path):
            self.win = ErrorWindow()
            self.win.change_error("😕 Box is empty")
        else:
            self.index = self.notes.currentRow()
            with open('notes.txt', 'r') as f:
                lines = f.readlines()
                lines.pop(self.index)
    
            with open('notes.txt', 'w') as f:
                f.writelines(lines)
            self.close()
            self.win = MainWindow()

    def exit(self):
        self.close()

class AddWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Add Note")
        self.setFixedSize(400, 500)

        self.title = QLabel(self)
        self.title.setText("Title:")
        self.title.setStyleSheet("""
            font-family: Arial;
            font-size: 24px;
        """)
        self.title_input = QLineEdit(self)
        self.title_input.setFixedHeight(40)
        self.title_input.setStyleSheet("""
            font-family: Arial;
            font-size: 18px;
            border: 2px solid #343A40;
            border-radius: 10px;
        """)

        self.content = QLabel(self)
        self.content.setText("Content:")
        self.content.setStyleSheet("""
            font-family: Arial;
            font-size: 24px;
        """)
        self.content_input = QTextEdit(self)
        self.content_input.setStyleSheet("""
            font-family: Arial;
            font-size: 18px;
            border: 2px solid #343A40;
        """)
        
        self.save_btn = QPushButton(self)
        self.save_btn.setText("Save")
        self.save_btn.setFixedHeight(40)
        self.save_btn.setStyleSheet("""
            QPushButton {
                font-family: Arial;
                font-size: 18px;
                border: 2px solid #0F5132;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #198754;
                color: #FFF;
            }
        """)

        self.back_btn = QPushButton(self)
        self.back_btn.setText("Back")
        self.back_btn.setFixedHeight(40)
        self.back_btn.setStyleSheet("""
            QPushButton {
                font-family: Arial;
                font-size: 18px;
                border: 2px solid #495057;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #343A40;
                color: #FFF;
            }
        """)

        self.h_box1 = QHBoxLayout()
        self.h_box2 = QHBoxLayout()
        self.h_box3 = QHBoxLayout()
        self.h_box4 = QHBoxLayout()
        self.h_box5 = QHBoxLayout()
        self.h_box6 = QHBoxLayout()

        self.v_box = QVBoxLayout()

        self.h_box1.addWidget(self.title)
        self.h_box2.addWidget(self.title_input)
        self.h_box3.addWidget(self.content)
        self.h_box4.addWidget(self.content_input)
        self.h_box5.addWidget(self.save_btn)
        self.h_box6.addWidget(self.back_btn)

        self.v_box.addLayout(self.h_box1)
        self.v_box.addLayout(self.h_box2)
        self.v_box.addLayout(self.h_box3)
        self.v_box.addLayout(self.h_box4)
        self.v_box.addLayout(self.h_box5)
        self.v_box.addLayout(self.h_box6)

        self.setLayout(self.v_box)

        self.show()

        self.save_btn.clicked.connect(self.save)
        self.back_btn.clicked.connect(self.back)

    def save(self):
        f = open("notes.txt", "a")
        title = self.title_input.text()
        content = self.content_input.toPlainText()

        if title and content:
            f.write(f'{title}|{content}\n')
            f.close()
            self.close()
            self.win = MainWindow()
        else:
            self.win = ErrorWindow()
            self.win.change_error("⚠️ Fill empty spaces!")


    def back(self):
        self.close()
        self.win = MainWindow()

class ViewWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("View Note")
        self.setFixedSize(400, 500)

        self.title = QLabel(self)
        self.title.setStyleSheet("""
            font-family: Arial;
            font-size: 24px;
        """)

        self.content = QTextEdit(self)
        self.content.setReadOnly(True)
        self.content.setStyleSheet("""
            font-family: Arial;
            font-size: 18px;
            border: 2px solid #343A40;
        """)

        self.back_btn = QPushButton(self)
        self.back_btn.setFixedHeight(40)
        self.back_btn.setText("Back")
        self.back_btn.setStyleSheet("""
            QPushButton {
                font-family: Arial;
                font-size: 18px;
                border: 2px solid #495057;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #343A40;
                color: #FFF;
            }
        """)

        self.h_box1 = QHBoxLayout()
        self.h_box2 = QHBoxLayout()
        self.h_box3 = QHBoxLayout()

        self.v_box = QVBoxLayout() 

        self.h_box1.addWidget(self.title)
        self.h_box2.addWidget(self.content)
        self.h_box3.addWidget(self.back_btn)

        self.v_box.addLayout(self.h_box1)
        self.v_box.addLayout(self.h_box2)
        self.v_box.addLayout(self.h_box3)

        self.setLayout(self.v_box)

        self.show()

        self.back_btn.clicked.connect(self.back)

    def back(self):
        self.close()
        self.win = MainWindow()

    def show_content(self, index):
        with open('notes.txt', 'r') as f:
            lines = f.readlines()
            text = lines[index].split('|')
            self.title.setText(f"{text[0]}")
            self.content.setText(f"{text[1]}")


app = QApplication([])
main = MainWindow()
# add = AddWindow()
# view = ViewWindow()
# error = ErrorWindow()
app.exec_()