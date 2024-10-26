def single_root_words(root_word, *other_words):
    # Приводим root_word к нижнему регистру и создаем пустой список для совпадений
    root_word_lower = root_word.lower()
    same_words = []

    # Проходимся по каждому слову в other_words
    for word in other_words:
        word_lower = word.lower()
        # Проверяем, содержится ли root_word в слове или наоборот
        if root_word_lower in word_lower or word_lower in root_word_lower:
            same_words.append(word)

    # Возвращаем список совпадений
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)
