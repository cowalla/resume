from datetime import date

from models import Skill


web_engineering = Skill(
    'Web Engineering',
    'Django',
    'Angular',
    'Rails',
    'Ractive',
    'Chef',
    'Jenkins',
    'AWS',
    'Protractor'
)

print web_engineering.render()