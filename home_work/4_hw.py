#задание 1
class rectangle:
    def __init__(self, length=None, width=None):
        self.length = length
        self.width = width

    def area(self):
        print('площадь прямоугольника:', self.length * self.width)
        print('периметр прямоугольника:', self.length * 2 + self.width * 2 )

rectangle_1 = rectangle(length=4, width=5)
#rectangle_1.area()

rectangle_2 = rectangle(length=6, width=8)
rectangle_3 = rectangle(length=9, width=7)
rectangle_4 = rectangle(length=2, width=20)
#rectangle_2.area()
#rectangle_3.area()
#rectangle_4.area()

#задание 2
class math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def methods(self):
        print('сложение:', self.a + self.b )
        print('вычитание:', self.a - self.b )
        print('умножение:', self.a * self.b )
        print('деление:', self.a / self.b )

math_1 = math(a=3, b=9)
#math_1.methods()

#задание 3
class Button:

    type: str = 'Кнопка'

    def __init__(self, text, loc=None):
        self.text = text
        self.loc = loc

    def click(self):
        return 'Клик по кнопке {}'.format(self.text)

textbox = Button('Text Box')
checkbox = Button('Check Box')
radiobutton = Button('Radio Button')
webtables = Button('Web Tables')
buttons = Button('Buttons')
links = Button('Links')
brokenlinksimages = Button('Broken Links - Images')
uploadanddownload = Button('Upload and Download')
dynamicproperties = Button('Dynamic Properties')
practiceform = Button('Practice Form')
browserwindows = Button('Browser Windows')
alerts = Button('Alerts')
frames = Button('Frames')
nestedframes = Button('Nested Frames')
modaldialogs = Button('Modal Dialogs')
accordian = Button('Accordian')
autocomplete = Button('Auto Complete')
datepicker = Button('Date Picker')
slider = Button('Slider')
progressbar = Button('Progress Bar')
tabs = Button('Tabs')
tooltips = Button('Tool Tips')
menu = Button('Menu')
selectmenu = Button('Select Menu')
sortable = Button('Sortable')
selectable = Button('Selectable')
resizable = Button('Resizable')
droppable = Button('Droppable')
dragabble = Button('Dragabble')
login = Button('Login')
bookstore = Button('Book Store')
profile = Button('Profile')
bookstoreapi = Button('Book Store API')


print(textbox.text)
print(textbox.click())

print(checkbox.text)
print(checkbox.click())

print(radiobutton.text)
print(radiobutton.click())

print(webtables.text)
print(webtables.click())

print(buttons.text)
print(buttons.click())

print(links.text)
print(links.click())

print(brokenlinksimages.text)
print(brokenlinksimages.click())

print(uploadanddownload.text)
print(uploadanddownload.click())

print(dynamicproperties.text)
print(dynamicproperties.click())

print(practiceform.text)
print(practiceform.click())

print(browserwindows.text)
print(browserwindows.click())

print(alerts.text)
print(alerts.click())

print(frames.text)
print(frames.click())

print(nestedframes.text)
print(nestedframes.click())

print(modaldialogs.text)
print(modaldialogs.click())

print(accordian.text)
print(accordian.click())

print(autocomplete.text)
print(autocomplete.click())

print(datepicker.text)
print(datepicker.click())

print(slider.text)
print(slider.click())

print(progressbar.text)
print(progressbar.click())

print(tabs.text)
print(tabs.click())

print(tooltips.text)
print(tooltips.click())

print(menu.text)
print(menu.click())

print(selectmenu.text)
print(selectmenu.click())

print(sortable.text)
print(sortable.click())

print(selectable.text)
print(selectable.click())

print(resizable.text)
print(resizable.click())

print(droppable.text)
print(droppable.click())

print(dragabble.text)
print(dragabble.click())

print(login.text)
print(login.click())

print(bookstore.text)
print(bookstore.click())

print(profile.text)
print(profile.click())

print(bookstoreapi.text)
print(bookstoreapi.click())
