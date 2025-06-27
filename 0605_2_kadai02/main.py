# 課題02 クラス基礎
import textwrap
class Monster:
    def __init__(self, name, hp, mp):
        self.__name = name
        self.__hp = hp
        self.__mp = mp

    def show_status(self):
        print(textwrap.dedent(f'''\
            名前:{self.__name}
            HP:{self.__hp}
            MP:{self.__mp}'''))

    def cure(self):
        self.__hp += 100

    def get_name(self):
        return self.__name

monster = Monster('スライム', 100, 50)
monster.show_status()

# monster.cure()
# monster.show_status()
# print(monster.get_name())