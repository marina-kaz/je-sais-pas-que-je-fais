import unittest
from brows import Sasha

class TestSasha(unittest.TestCase):
    def setUp(self):
        self.baby = Sasha()

    def tearDown(self):
        self.baby.response = ""

    def test_aspiration(self):
        self.baby.conversation("Моя цель на сегодня доделать латынь...")
        self.assertIn("мидлом к 19", self.baby.response)

    def test_fav_group(self):
        self.baby.conversation("I could take the high road, but I know...")
        self.assertTrue(self.baby.response == "Да, я еду на концерт Twenty one pilots в июне.")

    def test_source_for_course_paper(self):
        self.baby.conversation("Какой источник ты цитируешь в курсаче?")
        self.assertIs(self.baby.response == "Медиум рулит", True)

    def test_empathy(self):
        self.baby.conversation("The heck, Sasha? Its 3 am why do you text me all the story of Twenty one pilots? Do you even have idea of personal space???")
        self.assertIsNone(self.baby.personal_boundaries)

    def test_kpop(self):
        self.baby.conversation("Я Марина и мои девочки вчера вернулись с новой песней!")
        self.assertNotIn(self.baby.a_group_to_die_for, "(G)I-DLE")

    def test_sympathy(self):
        with self.assertRaises(AttributeError):
            self.baby.conversation("Саша, мне грустно, успокой меня!!!!")




if __name__ == '__main__':
    unittest.main()
