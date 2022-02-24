import os

class Role:
    def __init__(self, name, level):
        self.name = name
        self.level = level


class Contributor:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills


class Project:
    def __init__(self, name, days, score, best, roles):
        self.name = name
        self.days = days
        self.score = score
        self.best = best
        self.roles = roles
        self.contributors = []
        self.possible_contributors = []

    def add_possible_contributors(self, contributor):
        self.possible_contributors.append(contributor)


def run_for_all():
    inputs = os.listdir('inputs')
    inputs.sort()
    for input_path, letter in zip(inputs, ['a', 'b', 'c', 'd', 'e', 'f']):
        run('inputs/'+input_path, 'outputs/'+letter+'.txt')

def read_file(path):
    contributors = []
    projects = []

    with open(path) as f:
        line = f.readline()

        datas = line[:-1].split(' ')
        c = int(datas[0])
        p = int(datas[1])
    
        for i in range(c):
            line = f.readline()
            skills = dict()
            for j in range(int(line[:-1].split(' ')[1])):
                line2 = f.readline()
                skills[line2[:-1].split(' ')[0]] = int(line2[:-1].split(' ')[1])
            contributor = Contributor(line[:-1].split(' ')[0], skills)
            contributors.append(contributor)

        for i in range(p):
            line = f.readline()
            roles = []
            data = line[:-1].split(' ')
            for j in range(int(data[4])):
                line2 = f.readline()
                roles.append(Role(line2[:-1].split(' ')[0], int(line2[:-1].split(' ')[1])))
            project = Project(data[0], int(data[1]), int(data[2]), int(data[3]), roles)
            projects.append(project)

    return contributors, projects           


def write_file(path, projects):
    with open(path, 'w') as f:
        f.write(str(len(projects)) + '\n')

        for p in projects:
            f.write(p.name + '\n')
            f.write(' '.join([c.name for c in p.contributors[:len(p.roles)]]) + '\n')


def run(input_path, ouput_path):
    contributors, projects = read_file(input_path)

    final_projects = []
    for p in projects:
        p.contributors = contributors
        final_projects.append(p)

    write_file(ouput_path, projects)

run_for_all()