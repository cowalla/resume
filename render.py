from datetime import date

from models import Education, Experience, Skill, Resume


# Education
app_academy = Education(
    institution='App Academy',
    attained_level='Graduate',
    start=date(2013, 11, 1),
    end=date(2014, 2, 1),
    description='Less than 3% acceptance rate.'
)
college = Education(
    institution='Reed College',
    attained_level='BA Physics',
    start=date(2009, 8, 1),
    end=date(2013, 5, 1),
    description='Senior thesis subsequently published -- Jones-Smith, K. & Wallace, C. Int J Theor Phys (2015) 54: 219.'
)

#  Experiences
nuro = Experience(
    company_name='Nuro',
    title='Fleet Connectivity Engineer',
    start=date(2021, 1, 1),
    description='Full stack feature development in two week sprints.'
)
ike = Experience(
    company_name='Ike (acquired by Nuro)',
    title='Infrastructure Engineer',
    start=date(2020, 3, 1),
    end=date(2020, 12, 31),
    description='Full stack feature development in two week sprints.'
)
granular = Experience(
    company_name='Granular',
    title='Senior Software Engineer',
    start=date(2018, 2, 1),
    end=date(2019, 5, 1),
    description='Full stack feature development in two week sprints.'
)
betterworks = Experience(
    company_name='BetterWorks',
    title='Software Engineer II',
    start=date(2016, 10, 1),
    end=date(2018, 2, 1),
    description='Full stack feature development in two week sprints.'
)
urban_airship = Experience(
    company_name='Urban Airship',
    title='Web Engineer',
    start=date(2014, 2, 1),
    end=date(2013, 5, 1),
    description='Customer-facing feature development and Web API platform work.'
)

#  Skills
web_engineering = Skill(
    'Web Engineering',
    'Django',
    'React',
    'Angular',
)
cloud_infra = Skill(
    'Cloud Infrastructure / CICD',
    'AWS',
    'GCP',
    'Jenkins',
    'Buildkite',
)
embedded = Skill(
    'C++'
    'Arduino',
    'Particle',
    'Bazel',
)

educations = [college, app_academy]
experiences = [nuro, ike, granular, betterworks, urban_airship]
skills = [cloud_infra, web_engineering, embedded]

#  Resume
resume = Resume(
    full_name="Connor Wallace",
    contact_info="Seattle, WA",
    experiences=experiences,
    educations=educations,
    skills=skills
)


if __name__ == "__main__":
    print(resume.render())
