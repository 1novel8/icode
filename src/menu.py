from src.services.contract import ContractService
from src.services.project import ProjectService
from src.settings import get_session


class ProjectActions:
    @get_session
    def project_create(self, session):
        name = input('Input project name:')
        service = ProjectService(session=session)
        project = service.create(name=name)
        return project

    @get_session
    def project_list(self, session):
        service = ProjectService(session=session)
        service.print_projects()

    @get_session
    def add_contract(self, session):
        contract_service = ContractService(session=session)
        project_service = ProjectService(session=session)
        contract_service.print_contracts()
        project_service.print_projects()

        print('Adding contract to project')
        try:
            contract_id = int(input('Enter contract id'))
            project_id = int(input('Enter project id'))

            contract = contract_service.get_by_id(contract_id)
            project = project_service.get_by_id(project_id)

            project_service.add_contract(contract, project)
        except ValueError:
            print('Данные введены некорректно')

        contract = contract_service.get_by_id(contract_id)
        project = project_service.get_by_id(project_id)





class ContractActions:
    @get_session
    def contract_create(self, session):
        name = input('Input project name:')
        service = ContractService(session=session)
        contract = service.create(name=name)
        return contract

    @get_session
    def contract_list(self, session):
        service = ContractService(session=session)
        service.print_contracts()


class Menu(
    ProjectActions,
    ContractActions
):
    def __init__(self):
        self.position = 0
        self.actions = {
            0: 'Waiting for action:\n'
               '1 - Project\n'
               '2 - Contract\n'
               '3 - Exit\n'
               '11 - project list\n'
               '22 - contract list\n',
            1: 'Project. Waiting for action:\n'
               '1 - create\n'
               '2 - add contract\n'
               '3 - close contract\n'
               '4 - back\n'
               '11 - project list\n'
               '22 - contract list\n',
            2: 'Contract. Waiting for action:\n'
               '1 - create\n'
               '2 - submit contract\n'
               '3 - close contract\n'
               '4 - back\n'               
               '11 - project list\n'
               '22 - contract list\n',
        }
        self.main_switch = {
            0: {
                1: self.set_project_position,
                2: self.set_contract_position,
                3: exit,

                11: self.project_list,
                22: self.contract_list,
            },
            1: {
                1: self.project_create,
                2: self.add_contract,
                4: self.back,

                11: self.project_list,
                22: self.contract_list,
            },
            2: {
                1: self.contract_create,
                4: self.back,

                11: self.project_list,
                22: self.contract_list,
            },
        }

    def start(self):
        while True:
            try:
                print(self.actions[self.position])
                action = int(input())
                self.action_handler(action)
            except ValueError:
                print('данные введены некорректно')

    def action_handler(self, action):
        if self.position in self.main_switch.keys() and action in self.main_switch[self.position].keys():
            self.main_switch[self.position][action]()
        else:
            print('Данные введены некорректно')

    def back(self):
        self.position = 0

    def set_project_position(self):
        self.position = 1

    def set_contract_position(self):
        self.position = 2

    def stop(self):
        exit()
