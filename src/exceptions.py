
class NotFoundException(Exception):
    pass


class StatusException(Exception):
    pass


class ContractNotAvailableException(Exception):
    pass


class ActiveContractsLimitException(Exception):
    pass


class NoProjectRelatedException(Exception):
    pass


class WrongProjectRelatedException(Exception):
    pass


class NoActiveContractsException(Exception):
    pass
