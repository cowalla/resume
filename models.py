from jinja2 import Template

from settings import JINJA_ENV


DATE_FORMAT = '%B %Y'


class ResumeEntry(object):
    TEMPLATE_NAME = None

    def __init__(self):
        super(ResumeEntry, self).__init__()

        self.template = JINJA_ENV.get_template(self.TEMPLATE_NAME)

    def _start_and_end(self):
        start_formatted = self.start.strftime(DATE_FORMAT)

        if self.end is not None:
            end_formatted = self.end.strftime(DATE_FORMAT)
        else:
            end_formatted = 'Present'

        return start_formatted, end_formatted


class Experience(ResumeEntry):
    TEMPLATE_NAME = 'experience.html'

    def __init__(self, company_name, title, start, end=None, description=None):
        super(Experience, self).__init__()

        self.company_name = company_name
        self.title = title
        self.start = start
        self.end = end
        self.description = description

    def render(self):
        start, end = self._start_and_end()
        template_kwargs = {
            'time_period': '{start} - {end}'.format(start=start, end=end),
            'company_name': self.company_name,
            'title': self.title,
            'description': self.description or '',
        }

        return self.template.render(**template_kwargs)


class Skill(ResumeEntry):
    TEMPLATE_NAME = 'skill.html'

    def __init__(self, skill, *subskills):
        super(Skill, self).__init__()

        self.skill = skill
        self.subskills = subskills

    def render(self):
        return self.template.render(overarching_skill=self.skill, subskills=self.subskills)


class Education(ResumeEntry):
    TEMPLATE_NAME = 'education.html'

    def __init__(self, institution, attained_level, start, end=None, description=None):
        super(Education, self).__init__()

        self.institution = institution
        self.attained_level = attained_level
        self.start = start
        self.end = end
        self.description = description

    def render(self):
        start, end = self._start_and_end()
        template_kwargs = {
            'time_period': '{start} - {end}'.format(start=start, end=end),
            'institution': self.institution,
            'attained_level': self.attained_level,
            'description': self.description or '',
        }

        return self.template.render(**template_kwargs)
