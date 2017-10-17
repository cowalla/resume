from jinja2 import Environment, FileSystemLoader, select_autoescape
from secret import PHONE_NUMBER, CURRENT_ADDRESS


JINJA_ENV = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

NAME = 'Connor Wallace'
WEBSITE = 'cowalla.me'
