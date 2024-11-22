import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QSizePolicy
from PyQt5.QtGui import QFont
from converter import convert_md_to_anki, convert_anki_to_md
import pyperclip

class PlainTextEdit(QTextEdit):
    def insertFromMimeData(self, source):
        """重写粘贴功能，只保留纯文本"""
        if source.hasText():
            self.insertPlainText(source.text())  # 仅插入纯文本

class MarkdownToAnkiConverter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Markdown to Anki Converter')
        self.setGeometry(100, 100, 1000, 1030)  # 设置窗口大小

        self.setStyleSheet('background-color: #f0f0f0;')

        font_label = QFont('Microsoft YaHei', 14)
        font_textedit = QFont('Arial', 14)

        # 输入Markdown文本部分
        label_input = QLabel('输入Markdown文本:')
        label_input.setFont(font_label)
        self.text_input = PlainTextEdit()  # 替换为自定义类
        self.text_input.setFont(font_textedit)
        self.text_input.setStyleSheet('background-color: #FAFAFA; border: 1px solid #000000;')
        self.text_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  # 设置大小策略，高度固定，宽度扩展

        # 输出Anki格式文本部分
        label_output = QLabel('转换后的Anki格式:')
        label_output.setFont(font_label)
        self.text_output = PlainTextEdit()  # 替换为自定义类
        self.text_output.setFont(font_textedit)
        self.text_output.setStyleSheet('background-color: #FAFAFA; border: 1px solid #000000;')
        self.text_output.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # 设置大小策略，宽高都扩展

        # 按钮部分
        button_convert = QPushButton('转换')
        button_convert.setFont(font_label)
        button_convert.setStyleSheet('QPushButton { background-color: #dddddd; color: #000000; border: 1px solid #808080; padding: 10px; border-radius: 5px; }'
                                     'QPushButton:hover { background-color: #999999; color: #ffffff; }')
        button_convert.clicked.connect(self.convert_button_clicked)

        button_reverse_convert = QPushButton('反向转换')
        button_reverse_convert.setFont(font_label)
        button_reverse_convert.setStyleSheet('QPushButton { background-color: #dddddd; color: #000000; border: 1px solid #808080; padding: 10px; border-radius: 5px; }'
                                             'QPushButton:hover { background-color: #999999; color: #ffffff; }')
        button_reverse_convert.clicked.connect(self.reverse_convert_button_clicked)

        button_clear = QPushButton('清空输入')
        button_clear.setFont(font_label)
        button_clear.setStyleSheet('QPushButton { background-color: #dddddd; color: #000000; border: 1px solid #808080; padding: 10px; border-radius: 5px; }'
                                   'QPushButton:hover { background-color: #999999; color: #ffffff; }')
        button_clear.clicked.connect(self.clear_button_clicked)

        button_copy = QPushButton('复制输出')
        button_copy.setFont(font_label)
        button_copy.setStyleSheet('QPushButton { background-color: #dddddd; color: #000000; border: 1px solid #808080; padding: 10px; border-radius: 5px; }'
                                  'QPushButton:hover { background-color: #999999; color: #ffffff; }')
        button_copy.clicked.connect(self.copy_button_clicked)

        # 按钮布局
        button_layout = QHBoxLayout()
        button_layout.addWidget(button_convert)
        button_layout.addWidget(button_reverse_convert)
        button_layout.addWidget(button_clear)
        button_layout.addWidget(button_copy)

        # 使用GridLayout进行布局
        grid_layout = QGridLayout()
        grid_layout.addWidget(label_input, 0, 0)  
        grid_layout.addWidget(self.text_input, 1, 0)
        grid_layout.addLayout(button_layout, 2, 0)
        grid_layout.addWidget(label_output, 3, 0)
        grid_layout.addWidget(self.text_output, 4, 0)
        grid_layout.setSpacing(20)

        self.setLayout(grid_layout)

    def convert_button_clicked(self):
        md_content = self.text_input.toPlainText()
        anki_content = convert_md_to_anki(md_content)
        self.text_output.setPlainText(anki_content)

    def reverse_convert_button_clicked(self):
        anki_content = self.text_input.toPlainText()
        md_content = convert_anki_to_md(anki_content)
        self.text_output.setPlainText(md_content)

    def clear_button_clicked(self):
        self.text_input.clear()

    def copy_button_clicked(self):
        anki_content = self.text_output.toPlainText()
        pyperclip.copy(anki_content)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter = MarkdownToAnkiConverter()
    converter.show()
    sys.exit(app.exec_())
