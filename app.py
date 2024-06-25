from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def resume():
    personal_info = {
        "name": "Полянский Александр Константинович",
        "address": "улица Памяти Чернобыльцев, 8, микрорайон Солнечный, Фестивальный микрорайон, Краснодар, 350078",
        "phone": "+7 (988) 000-57-86",
        "email": "ak.polyanskiy@gmail.com",
        "linkedin": "https://t.me/ak_gek",
        "github": "https://github.com/Alexsandr52"
    }
    
    skills = ["Python", "Flask", "SQL", "Git", "Docker", "Linux", "Web (Js, HTML, CSS)"]
    
    experience = [
        {
            "title": "Стажер разработчик.",
            "company": "Компания \"Старт Эксперт\"",
            "location": "Краснодар, ул. Северная, д. 405 оф. 203",
            "dates": "Февраль 2024 – Июнь 2024",
            "description": [
                "Изучение работы основного проекта.",
                "Тестирование и внедрение нового функционала.",
                "Изучение и поиск новых технологий и функций для улучшения работы основного проекта.",
                "Оптимизация производительности приложений и обеспечение безопасности.",
                "Основные технологии node.js, firebase."
            ]
        },
    ]
    
    education = [
        {
            "degree": "Среднее специальное образование",
            "institution": """Институт среднего профессионального образования кубанского государственного университета. 
            Программирование в компьютерных системах, Техник программист в компьютерных системах""",
            "dates": "Сентябрь 2020 – Июнь 2024"
        }
    ]
    
    projects = [
        {
            "name": "Поиск переломов на рентгеновском снимке Python.",
            "description": "Этот проект содержит код для обучения и развёртывания модели обнаружения переломов на основе архитектуры YOLOv8 с использованием Flask для вывода результатов."
        },
        {
            "name": "Bot Speech To Text On Yandex Cloud. (@speech2text_prac_bot)",
            "description": "Бот, который умеет транскрибировать текст из аудио сообщений, сам бот работает и доступен в телеграмм. Интересные технологии в разработке, это облако яндекса и его функции, а так же APIGetWay."
        }
    ]
    
    certificates = [
        "Алгоритмы и структуры данных на Python. [GeekBrains]",
        "Машинное обучение в бизнесе. [GeekBrains]",
        "PyTorch для разработкиы нейронных сетей. [GeekBrains]",
        "Математический анализ. [GeekBrains]",
    ]
    
    languages = [
        "Русский – Родной",
        "Английский – Средний уровень"
    ]
    
    additional_info = [
        "Принимаю участие в хакатонах и соревнованиях на kaggel, в свободное время разрабатываю различные инструменты, для автоматизации рутинных задач.",
        "Активно изучаю машинное обучение и нейронные сети, получаю опыт используя различие рецепты и участвуя в соревнованиях на kaggel."
    ]
    
    return render_template('resume.html', personal_info=personal_info, skills=skills, experience=experience, education=education, projects=projects, certificates=certificates, languages=languages, additional_info=additional_info)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
