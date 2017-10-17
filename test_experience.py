from datetime import date

from models import Experience


most_recent_experience = Experience(
    company_name='BetterWorks',
    title='Software Engineer II',
    start=date(2016, 10, 30),
    description='Full stack feature development in two week sprints.'
)

print most_recent_experience.render()