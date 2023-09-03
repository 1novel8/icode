from menu import Menu
from src.session import engine, Base


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
    menu = Menu()
    while True:
        menu.start()
