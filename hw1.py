#Сделайте функцию, которая будет печатать читаемое имя переданной ей функции
# и значений аргументов.
from inspect import getfullargspec


def function_name(func):
    name = func.__name__
    args = getfullargspec(func)
    print(f"The function name is {name}.\nThe function arguments are {args[0]}")

def open_browser(browser_name):
    pass

def go_to_companyname_homepage(page_url):
    pass

def find_registration_button_on_login_page(page_url, button_text):
    pass


function_name(open_browser)
function_name(find_registration_button_on_login_page)
