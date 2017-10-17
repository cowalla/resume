from datetime import date

from models import Education


college = Education(
    institution='Reed College',
    attained_level='BA Physics',
    start=date(2009, 8, 30),
    end=date(2013, 5, 16),
    description='Senior thesis subsequently published -- Jones-Smith, K. & Wallace, C. Int J Theor Phys (2015) 54: 219.'
)

print college.render()