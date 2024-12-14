def reverse_text(text):
    """
    Розвертає всі слова у вхідному рядку text, зберігаючи небуквенні символи на місці.

    Приклади:
    >>> reverse_text("abcd efgh")
    'dcba hgfe'
    >>> reverse_text("a1bcd efg!h")
    'd1cba hgf!e'
    """
    words = text.split()
    reversed_words = []

    for word in words:
        letters = [char for char in word if char.isalpha()]
        reversed_letters = iter(letters[::-1])

        result_word = [
            next(reversed_letters) if char.isalpha() else char
            for char in word
        ]
        reversed_words.append("".join(result_word))

    return " ".join(reversed_words)
