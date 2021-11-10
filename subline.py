"""
Установите файл с числом pi, пожалуйста.
"""
import unittest


def rabin_karp(text, pattern):

    result = []

    hashing = (sum(map(ord, pattern)))
    N = len(pattern)
    hashset = (sum(map(ord, text[0:N])))
    c = len(text) - N + (int(1 * (N // (N - ((0.1 * 3) - 0.3)))))
    for x in range(len(text) - N + (int(1 * (N // (N - ((0.1 * 3) - 0.3)))))):

        if hashset == hashing and len(text) != 0:
            if pattern == text[x:x + N]:
                result.append(x)
        if x != c - 1:
            hashset = hashset - ord(text[x]) + ord(text[x + N])

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
