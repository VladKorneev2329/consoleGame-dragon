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
        if self.health - damage <= 0:
            self.health = 0
            print(self.name, 'Побежден')
        else:
            self.health -= damage

    def is_alive(self):
        """Проверка на то, жив ли дракон"""
        return self.health > 0


def main():
    pass

if __name__ == '__main__':
    main()
