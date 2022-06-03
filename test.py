import unittest
from ror import wror
import re


class TestWikipediaROR(unittest.TestCase):

    def test_up(self):
        self.assertEqual(wror.upper("hello"), "Hello")

    def word(self, eq):
        m = re.compile("(.*)\s=\s(.*)").match(eq).groups()
        self.assertEqual(len(m), 2)
        self.assertEqual(wror.word(m[0]), m[1])

    def words(self, eq):
        m = re.compile("(.*)\s=\s(.*)").match(eq).groups()
        self.assertEqual(len(m), 2)
        return
        self.assertEqual((" ").join(list(map(word, m[0].split(" ")))), m[1])

    def test_а(self):
        self.word("Аликово = Alikovo")
        self.word("Поганкино = Pogankino")

    def test_б(self):
        self.word("Болотин = Bolotin")
        self.word("Колбасин = Kolbasin")

    def test_в(self):
        self.word("Воронин = Voronin")
        self.word("Привалин = Privalin")

    def test_г(self):
        self.word("Галкин = Galkin")
        self.word("Луговой = Lugovoy")

    def test_д(self):
        self.word("Дровяное = Drovyanoye")
        self.word("Подгорск = Podgorsk")

    def test_е(self):
        self.word("Белкин = Belkin")
        self.word("Ельцин = Yeltsin")
        self.word("Раздольное = Razdolnoye")
        # self.word("Юрьев = Yuryev (ь omitted; see ь below)")
        self.word("Подъездной = Podyezdnoy")

    def test_ё(self):
        self.word("Ёлкино = Yolkino")
        self.word("Озёрск = Ozyorsk")

    def test_ж(self):
        self.word("Жиров = Zhirov")
        self.word("Приволжское = Privolzhskoye")

    def test_з(self):
        self.word("Зорин = Zorin")
        self.word("Обозов = Obozov")

    def test_и(self):
        self.word("Иркутск = Irkutsk")
        self.word("Владивосток = Vladivostok")

    def test_й(self):
        self.word("Йошкар-Ола = Yoshkar-Ola")
        self.word("Бийск = Biysk")

    def test_к(self):
        self.word("Киров = Kirov")
        self.word("Галкин = Galkin")

    def test_л(self):
        self.word("Лапинск = Lapinsk")
        self.word("Комсомольск = Komsomolsk")

    def test_м(self):
        self.word("Мичурин = Michurin")
        self.word("Колыма = Kolyma")

    def test_н(self):
        self.word("Нальчик = Nalchik")
        self.word("Савино = Savino")

    def test_о(self):
        self.word("Оха = Okha")
        self.word("Грозный = Grozny")

    def test_п(self):
        self.word("Петроград = Petrograd")
        self.word("Ставрополь = Stavropol")

    def test_р(self):
        self.word("Родниковое = Rodnikovoye")
        self.word("Высокогорск = Vysokogorsk")

    def test_с(self):
        self.word("Ступино = Stupino")
        self.word("Бирск = Birsk")

    def test_т(self):
        self.word("Тавричанка = Tavrichanka")
        self.word("Ростов = Rostov")

    def test_у(self):
        self.word("Улетайск = Uletaysk")
        self.word("Шушенское = Shushenskoye")

    def test_ф(self):
        self.word("Фёдоровка = Fyodorovka")
        self.word("Уфа = Ufa")

    def test_х(self):
        self.word("Хабаровск = Khabarovsk")
        self.word("Оха = Okha")

    def test_ц(self):
        self.word("Царское = Tsarskoye")
        self.word("Зарецкий = Zaretsky")

    def test_ч(self):
        self.word("Черемшаны = Cheremshany")
        self.word("Зареченск = Zarechensk")

    def test_ш(self):
        self.word("Шадрин = Shadrin")
        self.word("Моршанск = Morshansk")

    def test_щ(self):
        self.word("Щукино = Shchukino")
        self.word("Рощинский = Roshchinsky")

    def test_ъ(self):
        self.word("Подъярский = Podyarsky")
        self.word("Мусийкъонгийкоте = Musiykyongiykote")

    def test_ы(self):
        self.word("Ытык-Кюёль = Ytyk-Kyuyol")
        self.word("Давыдов = Davydov")

    def test_ь(self):
        self.word("Усолье = Usolye")
        self.word("Выхухоль = Vykhukhol")
        self.word("Дальнегорск = Dalnegorsk")
        self.word("Ильинский = Ilyinsky")

    def test_э(self):
        self.word("Элиста = Elista")
        self.word("Тетраэдральный = Tetraedralny")

    def test_ю(self):
        self.word("Южный = Yuzhny")
        self.word("Вилючинск = Vilyuchinsk")

    def test_я(self):
        self.word("Ярославль = Yaroslavl")
        self.word("Бурянск = Buryansk")

    def test_ый(self):
        self.word("Красный = Krasny")

    def test_ий_1(self):
        self.word("Синий = Siny")
        self.word("Великий = Veliky")

    def test_ий_2(self):
        self.word("Рыркайпий = Ryrkaypiy")

    def test_ые(self):
        self.words("Набережные Челны = Naberezhnye Chelny")
