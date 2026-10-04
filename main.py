import random
import os
from faker import Faker
from file_operations import render_template

# Папка, в которой лежит этот скрипт
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

letters_mapping = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
}

fake = Faker('ru_RU')

SKILLS = [
    'Стремительный прыжок',
    'Электрический выстрел',
    'Ледяной удар',
    'Стремительный удар',
    'Кислотный взгляд',
    'Тайный побег',
    'Ледяной выстрел',
    'Огненный заряд'
]


def stylize_skill(skill):
    """Принимает навык и возвращает его в руническом виде."""
    stylized_skill = ''
    for letter in skill:
        if letter in letters_mapping:
            stylized_skill += letters_mapping[letter]
        else:
            stylized_skill += letter
    return stylized_skill


def main():
    """Генерирует 10 карточек персонажей."""
    output_dir = os.path.join(BASE_DIR, 'карточки')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i in range(10):
        # Генерация данных
        first_name = fake.first_name()
        last_name = fake.last_name()
        city = fake.city()
        job = fake.job()

        strength = random.randint(3, 18)
        agility = random.randint(3, 18)
        endurance = random.randint(3, 18)
        intelligence = random.randint(3, 18)
        luck = random.randint(3, 18)

        # Выбор и стилизация навыков
        selected_skills = random.sample(SKILLS, 3)
        skill_1 = stylize_skill(selected_skills[0])
        skill_2 = stylize_skill(selected_skills[1])
        skill_3 = stylize_skill(selected_skills[2])

        # Создание словаря context
        context = {
            'first_name': first_name,
            'last_name': last_name,
            'strength': strength,
            'agility': agility,
            'endurance': endurance,
            'intelligence': intelligence,
            'luck': luck,
            'job': job,
            'town': city,
            'skill_1': skill_1,
            'skill_2': skill_2,
            'skill_3': skill_3
        }

        # Уникальное имя файла в папке 'карточки'
        output_filename = os.path.join(
            output_dir,
            'my_card_{}_{}_{}.txt'.format(i, first_name, last_name)
        )

        # Путь к шаблону относительно скрипта
        template_path = os.path.join(BASE_DIR, 'template.txt')

        render_template(template_path, output_filename, context)
        


if __name__ == '__main__':
    main()
    