"""
Установите файл с числом pi, пожалуйста.
"""
import unittest


def rabin_karp(text, pattern):

    result = []

    hashline = hash(pattern)
    N = len(pattern)
    for x in range(len(text) - N + (int(1 * (N // (N - ((0.1*3) - 0.3)))))):
        """
         Используем себе на пользу слабости двоичной системы, ухудшая читаемость кода,
         так как 0.1*3-0.3 это как бы ноль, но не ноль. 
         И благодаря этому можно, не добавляя строк с условиями рвыенства или не равенства N по отношению к 1, 
         избежать добалвения лишнего вхождения пустой подстроки в текст.
         Конечно, разумнее и оптимизированее использовать условия, но интереснее использовать слудующий факт:
         (N // (N - a)) при очень малом а для любого (скорее всего, так как проверял до 10^7) N, не равного 0, дает 1.
        """
        sample = text[x: x + N]
        hashsam = hash(sample)
        if hashsam == hashline and len(text) != 0:
            if pattern == sample:
                result.append(x)

    return result


class RabinKarpTest(unittest.TestCase):

    def setUp(self):
        self.text1 = 'axaxaxax'
        self.pattern1 = 'xax'
        self.text2 = 'bababab'
        self.pattern2 = 'bab'

    def test_return_type(self):
        self.assertIsInstance(rabin_karp(self.text1, "x"), list, msg="Функция должна возвращать список")

    def test_returns_empty(self):
        self.assertEqual([], rabin_karp(self.text1, "z"), msg="Функция должна давать пустой список, если нет вхождений")
        self.assertEqual([], rabin_karp("", self.pattern1), msg="Функция должна давать пустой список, если текст пуст")
        self.assertEqual([], rabin_karp("", ""), msg="Функция должна давать пустой список, если текст и образец пусты")

    def test_finds(self):
        self.assertEqual([1, 3, 5], rabin_karp(self.text1, self.pattern1), msg="Функция должна искать все вхождения")
        self.assertEqual([0, 2, 4], rabin_karp(self.text2, self.pattern2), msg="Функция должна искать все вхождения")

    def test_finds_all_empties(self):
        self.assertEqual(list(range(len(self.text1))), rabin_karp(self.text1, ""), msg="'' должна находиться везде")


if __name__ == '__main__':
    unittest.main()

with open("Final_pi.txt") as pif:
    pi = pif.read()
pif.close()

answer = (rabin_karp(pi, '314159'))  # Вычисляем сколько раз число пи с точностью до 5-ого знака входит в само себя.
# Попробуйте узнать, входит ли Ваша дата рождения в это приблежение чмсла pi (4 миллиона знака после запятой).
# Мой день рождения не оказался в нем =(
print(answer)
