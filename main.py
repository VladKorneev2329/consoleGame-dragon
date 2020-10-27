class Dragon:
    """Объект дракона"""

    def __init__(self, name: str):
        """
        Инициализация основных характеристик дракона
        :param name:str Имя дракона
        """
        self.health = 100  # Здоровье дракона
        self.name = name.title()

    def get_info(self):
        """Информация о драконе, количество жизнией, имя"""
        print(self.name, ': ', self.health, ' Здоровья', sep='')

    def get_damage(self, damage: int):
        """
         Получение урона по дракону
        :param damage:int  Колличество нанесенного урона Дракону
        :return: None
        """
        if damage < 0:  # Защита от добавления здоровья Дракону путем ввода отрицательного урона
            damage = -damage

        if self.health - damage <= 0:
            self.health = 0
            print(self.name, 'Побежден')
        else:
            self.health -= damage

    @property
    def is_alive(self):
        """Проверка на то, жив ли дракон"""
        return self.health > 0


def main():
    enemy_list = [Dragon('hydra'), Dragon('kali')]

    flag_game_end = False
    while not flag_game_end:

        enemy_list[0].get_info()
        damage = int(input('Урон: '))
        enemy_list[0].get_damage(damage)

        if not enemy_list[0].is_alive:
            enemy_list.pop(0)

        if not enemy_list:
            print('-'*25)
            print('Все драконы побеждены')
            print('-'*25)
            flag_game_end = True


if __name__ == '__main__':
    main()
