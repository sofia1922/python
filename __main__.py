from reverse_words_package.reverse_words import reverse_text

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    text_input = input("Введіть текст: ")
    result = reverse_text(text_input)
    print("Результат:", result)
