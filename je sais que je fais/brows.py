
class Sasha:
    def __init__(self):
        self.ultimate_goal = "мидлом к 19"
        self.a_group_to_die_for = "Twenty one pilots"
        self.personal_boundaries = None
        self.bible = "Медиум"
        self.worst_group_ever = "(G)I-DLE"
        self.response = ""

    def conversation(self, trigger):
        if "цель" in trigger:
            self.response = "А вот моя цель - стать " + self.ultimate_goal
        elif "I could take the high road, but I know..." in trigger:
            self.response = f"Да, я еду на концерт {self.a_group_to_die_for} в июне."
        elif "курсач" in trigger:
            self.response = f"{self.bible} рулит"
        elif "успокой" in trigger:
            raise AttributeError()



