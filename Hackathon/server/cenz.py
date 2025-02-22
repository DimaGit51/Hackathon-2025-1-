class ProfanityFilter:
    def __init__(self):
        self.words  = ["мудила", "ебан", "пизд", "долбоеб", "чмо", "дроч", "бля", "шлюха", "мудак", "фашист", "ебать",
            "сука", "еблан", "хуй", "пизда", "мудак", "мудила", "шлюха", "ахуел", "охуел", "аухе", "охуе", "херня",
            "мразь", "пидор", "пидарас", "ебать", "долбоеб", "уебан", "чмо","хер","ёбан","ёба" ,"еблет","ебка","ебак","ебо",
            "залупа", "гандон", "блядь", "бля", "ебись", "выебок", "ебло","нихуя","похуи","проёб","хуе",
            "ебнутый", "заебок", "заебал", "заебать", "заебись", "наебал",
            "наебать", "наебнулся", "отъебись", "подъеб", "подъебать",
            "поебать", "проебать", "разъебай", "съебать", "уебок", "уебище",
            "хуесос", "хуйня", "хуйло", "какашка", "говно"
]
        self.d =  {'а' : ['а', 'a', '@','4'],
  'б' : ['б', '6', 'b'],
  'в' : ['в', 'b', 'v','\/'],
  'г' : ['г', 'r', 'g'],
  'д' : ['д', 'd'],
  'е' : ['е', 'e','3'],
  'ё' : ['ё', 'e','3'],
  'ж' : ['ж', 'zh', '*'],
  'з' : ['з', '3', 'z'],
  'и' : ['и', 'u', 'i'],
  'й' : ['й', 'u', 'i'],
  'к' : ['к', 'k', 'i{', '|{'],
  'л' : ['л', 'l', 'ji'],
  'м' : ['м', 'm'],
  'н' : ['н', 'h', 'n'],
  'о' : ['о', 'o', '0'],
  'п' : ['п', 'n', 'p'],
  'р' : ['р', 'r', 'p'],
  'с' : ['с', 'c', 's'],
  'т' : ['т', 'm', 't'],
  'у' : ['у', 'y', 'u'],
  'ф' : ['ф', 'f'],
  'х' : ['х', 'x', 'h' , '}{','kh'],
  'ц' : ['ц', 'c', 'u,'],
  'ч' : ['ч', 'ch'],
  'ш' : ['ш', 'sh'],
  'щ' : ['щ', 'sch'],
  'ь' : ['ь', 'b'],
  'ы' : ['ы', 'bi'],
  'ъ' : ['ъ'],
  'э' : ['э', 'e'],
  'ю' : ['ю', 'io'],
  'я' : ['я', 'ya']
}

    def distance(self, a, b):
        """Calculates the Levenshtein distance between a and b."""
        n, m = len(a), len(b)
        if n > m:
            a, b = b, a
            n, m = m, n

        current_row = range(n + 1)
        for i in range(1, m + 1):
            previous_row, current_row = current_row, [i] + [0] * n
            for j in range(1, n + 1):
                add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
                if a[j - 1] != b[i - 1]:
                    change += 1
                current_row[j] = min(add, delete, change)

        return current_row[n]

    def replace_chars(self, phrase):
        """Replaces characters in the phrase according to the dictionary."""
        for key, value in self.d.items():
            for letter in value:
                phrase = phrase.replace(letter, key)
        return phrase

    def filter_profanity(self, phrase):
        """Filters profanity in the phrase."""
        phrase = phrase.lower().replace(" ", "")
        phrase = self.replace_chars(phrase)
        for word in self.words:
            for part in range(len(phrase)):
                fragment = phrase[part: part + len(word)]
                if self.distance(fragment, word) <= len(word) * 0.25:
                    return True  # Найдено нецензурное слово
        return False  # Нецензурных слов не найдено