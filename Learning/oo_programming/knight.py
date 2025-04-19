class Knight:
    count = 0

    def __init__(self, name):
        self.__name = name
        self.__title = None
        self.__favorite_color = None
        self.__quest = None
        self.__comment = None
        Knight.count += 1

    def __repr__(self):
        return f"{self.__title} {self.__name} -- {self.__quest} -- {self.__favorite_color} -- {self.__comment}"

    def __str__(self):
        return f"{self.__title} {self.__name} -- {self.__quest} -- {self.__favorite_color} -- {self.__comment}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_k):
        self.__name = name_k

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title_k):
        self.__title = title_k

    @property
    def favorite_color(self):
        return self._title_color(self.__favorite_color)

    @favorite_color.setter
    def favorite_color(self, favorite_color_k):
        self.__favorite_color = favorite_color_k

    @property
    def quest(self):
        return self.__quest

    @quest.setter
    def quest(self, quest_k):
        self.__quest = quest_k

    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, comment_k):
        self.__comment = comment_k

    @classmethod
    def number_kings(cls):
        return cls.count

    @staticmethod
    def _title_color(string: str) -> str:
        return string.title()

    @staticmethod
    def _static_method():
        print("This is a static method")
        test_var = Knight._title_color("test") # Calling a static method
        print(test_var)
        Knight.number_kings() # Calling a class method


if __name__ == "__main__":
    knight = Knight("Arthur")
    knight.title = "King"
    knight.favorite_color = "red"
    knight.quest = "Ruler of the kingdom"
    knight.comment = "Going medieval"
    print(
        f"This is {knight.title} {knight.name} the {knight.quest}, who likes color {knight.favorite_color} is {knight.comment}!")
    print(repr(knight)) # using the __repr___() call
    print(f"Hash = {knight.__hash__()}")
    knight.name = "Carlos V"
    knight.title = "Rey"
    knight.favorite_color = "blue"
    knight.quest = "Ruler of the chocolate kingdom"
    knight.comment = "Going sweet"
    print(f"Number of kings: {Knight.number_kings()}")
    print(
        f"This is {knight.title} {knight.name} the {knight.quest}, who likes color {knight.favorite_color} is {knight.comment}!")
    print(f"Hash = {hash(knight)}")
    knight2 = Knight("Edward")
    print(knight) # using the __str__() call
    print(f"Number of kings: {Knight.number_kings()}")
    print(f"Hash = {knight2.__hash__()}")
    print(f"Bool = {bool(knight2)}")
