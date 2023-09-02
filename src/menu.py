from src.exceptions import NotFoundException, StatusException, NoActiveContractsException, NoProjectRelatedException, \
    WrongProjectRelatedException
from src.handlers.contract import ContractHandlersMixin
from src.handlers.project import ProjectHandlersMixin


class Menu(
    ProjectHandlersMixin,
    ContractHandlersMixin,
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
                2: self.project_add_contract,
                3: self.project_close_contract,
                4: self.back,

                11: self.project_list,
                22: self.contract_list,
            },
            2: {
                1: self.contract_create,
                2: self.contract_submit,
                3: self.contract_close,
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
                print('!!!Данные введены некорректно!!!')
            except NotFoundException:
                print('!!!Не удалось найти объект с этим id!!!')
            except StatusException:
                print('!!!Проверьте статус договора!!!')
            except NoActiveContractsException:
                print("!!!У вас нет ни одного активного договора!!!")
            except NoProjectRelatedException:
                print('!!!У договора нет связанного с ним проекта для завершения!!!')
            except WrongProjectRelatedException:
                print('!!!Этот договора не связан с этим проектом!!!')

    def action_handler(self, action):
        if self.position in self.main_switch.keys() and action in self.main_switch[self.position].keys():
            self.main_switch[self.position][action]()
        else:
            raise ValueError

    def back(self):
        self.position = 0

    def set_project_position(self):
        self.position = 1

    def set_contract_position(self):
        self.position = 2
