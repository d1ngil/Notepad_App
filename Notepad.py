import sys

from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QLineEdit, QPushButton,
                             QVBoxLayout, QTextEdit, QHBoxLayout, QFileDialog, QMessageBox, QRadioButton)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt


class NotepadApp(QWidget):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Enter your note", self)
        self.textbox = QTextEdit(self)
        self.textbox.setPlaceholderText("Today i washed my hand..")
        self.save_button = QPushButton("Save", self)
        self.new_button = QPushButton("New", self)
        self.open_button = QPushButton("Open", self)
        self.toggle_button = QRadioButton("Dark Mode", self)
        self.dark_mode = False
        self.initUI()

    def initUI(self):
        self.setGeometry(700, 300, 600, 400)
        self.setWindowTitle("Notepad")
        self.setWindowIcon(QIcon("notepad.png"))


        hbox = QHBoxLayout()
        hbox.addWidget(self.new_button)
        hbox.addWidget(self.save_button)
        hbox.addWidget(self.open_button)

        vbox = QVBoxLayout()


        vbox.addWidget(self.label)
        vbox.addWidget(self.textbox)
        vbox.addWidget(self.toggle_button, alignment=Qt.AlignTop | Qt.AlignRight)
        vbox.addLayout(hbox)


        self.setLayout(vbox)

        self.label.setObjectName("note")
        self.save_button.setObjectName("save")
        self.open_button.setObjectName("open")
        self.new_button.setObjectName("new")
        self.toggle_button.setObjectName("toggle")

        self.setStyleSheet("""
            QLabel#note{
                font-size: 25px;
                font-style: italic;
            }
            QPushButton#save{
                font-size: 25px;
            }
            QPushButton#open{
                font-size: 25px;
            }
            QPushButton#new{
                font-size: 25px;
            }
            QTextEdit{
                font-size: 20px;
            }
            QPushButton{
                font-size: 20px;
            }
        """)

        self.new_button.clicked.connect(self.new)
        self.save_button.clicked.connect(self.save)
        self.open_button.clicked.connect(self.open)
        self.toggle_button.toggled.connect(self.toggle)


    def new(self):
        reply = QMessageBox.question(self, "Save the file",
                            "Do you want to save the changes?",
                            QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)

        if reply == QMessageBox.Yes:
            self.save()
            self.textbox.clear()
        elif reply == QMessageBox.No:
            self.textbox.clear()
        else:
            pass

    def save(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save file", "", "Text Files (*.txt);;All Files (*)")

        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(self.textbox.toPlainText())


    def open(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Text Files (*.txt);;All Files (*)")

        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    data = file.read()
                self.textbox.setText(data)
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Could not open file:\n{e} ")

    def toggle(self):
            if self.dark_mode:
                # Dark mode enabled
                self.setStyleSheet("""
                    QWidget {
                        background-color: white;
                        color: black;
                    }
                    QTextEdit {
                        background-color: white;
                        color: black;
                        font-size: 20px;
                    }
                    QPushButton {
                        font-size: 20px;
                    }
                    QLabel#Note {
                        font-size: 25px;
                        font-style: italic;
                    }
                """)
            else:
                # Light mode enabled
                self.setStyleSheet("""
                    QWidget {
                        background-color: #121212;
                        color: #e0e0e0;
                    }
                    QTextEdit {
                        background-color: #1e1e1e;
                        color: #ffffff;
                        font-size: 20px;
                    }
                    QPushButton {
                        font-size: 20px;
                    }
                    QLabel#Note {
                        font-size: 25px;
                        font-style: italic;
                    }
                """)
            self.dark_mode = not self.dark_mode

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NotepadApp()
    window.show()
    sys.exit(app.exec_())
