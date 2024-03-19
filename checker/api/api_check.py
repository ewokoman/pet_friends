def compare_dicts_by_key_values(dict1, dict2):
    # Получаем множество ключей, общих для обоих словарей
    common_keys = set(dict1.keys()) & set(dict2.keys())

    # Проверяем значения для общих ключей
    for key in common_keys:
        assert dict1[key] == dict2[key], f"Значения для ключа '{key}' не одинаковые: {dict1[key]} != {dict2[key]}"