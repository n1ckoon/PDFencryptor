from PyPDF2 import PdfWriter, PdfReader
from getpass import getpass
from reportlab.pdfgen import canvas

# Создаём PDF
c = canvas.Canvas("test.pdf")
c.drawString(100, 750, "Это тестовый PDF файл.")
c.save()

print("PDF успешно создан.")

# Открытие существующего PDF файла
pdfwriter = PdfWriter()
pdf = PdfReader('test.pdf')

# Добавление страниц из исходного PDF в новый
for page in pdf.pages:
    pdfwriter.add_page(page)

# Установка пароля для защиты файла
password = getpass(prompt='Введите пароль: ')
pdfwriter.encrypt(password)

# Сохранение защищенного PDF файла
with open('protected.pdf', 'wb') as file:
    pdfwriter.write(file)
