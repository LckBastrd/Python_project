class Developer:
    def __init__(self, name, seniority_level, languages):
        self.name = name
        self.seniority_level = seniority_level
        self.languages = languages

    def add_language(self, language):
        self.languages.append(language)

class Team:
    def __init__(self, name, developers):
        self.name = name
        self.developers = developers

    def add_developer(self, developer):
        self.developers.append(developer)

    def remove_developer(self, developer):
        self.developers.remove(developer)

    def check_developer(self, developer):
        return developer in self.developers

    def get_developers_by_language(self, language):
        return [dev for dev in self.developers if language in dev.languages]

    def list_developers(self):
        return [dev.name for dev in self.developers]

def get_teams_by_developers(dev1, dev2):
    teams = []
    for team in teams:
        if team.check_developer(dev1) and team.check_developer(dev2):
            teams.append(team.name)
    return teams

Dev1 = Developer(name='Anna Smirnova', seniority_level='Junior', language='Python')
Dev1 = Developer(name='Anna Smirnova', seniority_level='Junior', language='Python')
Dev1 = Developer(name='Anna Smirnova', seniority_level='Junior', language='Python')