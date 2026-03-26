import re

jobs_data = [
    {
        "id": 1,
        "title": "Создание презентации для IT-стартапа",
        "company": 'ООО "ТехНова"',
        "desc": "Ищем креативного специалиста для создания современной презентации продукта (10-12 слайдов). Есть готовый текст и логотип. Нужно продумать визуальную концепцию, подобрать иллюстрации, сверстать в Figma или PowerPoint так, чтобы это выглядело дорого.",
        "tags": ["Дизайн", "Figma", "PowerPoint", "Удаленно"],
        "price": "2 500 ₽",
        "meta": "Разовый заказ • 2 дня",
        "type": "one-time", "format": "remote", "category": "design", "experience": "low"
    },
    {
        "id": 2,
        "title": "Написать 5 статей для блога о технологиях",
        "company": 'Digital Agency "Peak"',
        "desc": "Требуется копирайтер для написания статей на тему гаджетов и IT-новинок. Объем каждой статьи 3000-4000 символов. Уникальность от 90%. Важно писать понятным языком, без воды.",
        "tags": ["Копирайтинг", "IT", "Удаленно"],
        "price": "5 000 ₽",
        "meta": "Проект • 1 неделя",
        "type": "project", "format": "remote", "category": "texts", "experience": "low"
    },
    {
        "id": 3,
        "title": "Бариста выходного дня",
        "company": 'Кофейня "Зерно"',
        "desc": "Ищем бариста на субботу и воскресенье. Опыт не обязателен — всему научим за 2 дня стажировки. Главное — любовь к кофе и умение общаться с гостями. Гибкие смены.",
        "tags": ["Офлайн", "Смены", "Без опыта"],
        "price": "2 000 ₽",
        "meta": "Постоянная работа",
        "type": "shifts", "format": "office", "category": "other", "experience": "none"
    },
    {
        "id": 4,
        "title": "Помощник SMM-специалиста (Стажировка)",
        "company": 'Социальное медиа агенство',
        "desc": "Стажировка для тех, кто хочет развиваться в SMM. Задачи: поиск референсов, помощь в составлении контент-планов, написание коротких постов для соцсетей. При успешном прохождении стажировки берем в штат.",
        "tags": ["SMM", "Стажировка", "Удаленно"],
        "price": "10 000 ₽",
        "meta": "Стажировка • 1 мес",
        "type": "internship", "format": "remote", "category": "marketing", "experience": "none"
    },
    {
        "id": 5,
        "title": "Монтаж коротких видео (Reels, TikTok)",
        "company": 'Блогер Иван С.',
        "desc": "Нужно смонтировать 10 коротких видеороликов из предоставленных исходников. Наложить субтитры, добавить эффекты и музыку из трендов.",
        "tags": ["Видеомонтаж", "CapCut / Premiere Pro", "Удаленно"],
        "price": "3 500 ₽",
        "meta": "Разовый заказ",
        "type": "one-time", "format": "remote", "category": "design", "experience": "mid"
    },
    {
        "id": 6,
        "title": "Перевод субтитров с английского языка на русский",
        "company": 'Студия "VoiceOver"',
        "desc": "Ищем студента-лингвиста для перевода субтитров к познавательному 20-минутному видео на YouTube. Тематика — космос. Требуется знание английского от B2.",
        "tags": ["Переводы", "Английский", "Удаленно"],
        "price": "1 500 ₽",
        "meta": "Разовый заказ • 1 день",
        "type": "one-time", "format": "remote", "category": "texts", "experience": "mid"
    },
    {
        "id": 7,
        "title": "Провести опрос на улице (Промоутер)",
        "company": 'Маркетинговое агенство "Сфера"',
        "desc": "Нужно провести социологический опрос среди молодежи (18-25 лет) в центре города. Каждый опрос занимает 2-3 минуты. За 4 часа нужно собрать минимум 40 анкет.",
        "tags": ["Офлайн", "Промоутер", "Без опыта"],
        "price": "1 200 ₽",
        "meta": "Разовый заказ • 4 часа",
        "type": "one-time", "format": "office", "category": "marketing", "experience": "none"
    },
    {
        "id": 8,
        "title": "Оформить группу ВКонтакте",
        "company": 'Магазин "SneakerShop"',
        "desc": "Нужен дизайн для сообщества ВК магазина кроссовок. Требуется обложка, аватар, 3 виджета и шаблон для постов.",
        "tags": ["Дизайн", "Photoshop/Figma", "Удаленно"],
        "price": "3 000 ₽",
        "meta": "Разовый заказ • 3 дня",
        "type": "one-time", "format": "remote", "category": "design", "experience": "low"
    },
    {
        "id": 9,
        "title": "Тестировщик мобильного приложения (Бета-тест)",
        "company": 'AppDev Studio',
        "desc": "Приглашаем на бета-тестирование нового приложения для тайм-менеджмента. Нужно пройтись по всем функциям и написать развернутый фидбек + зафиксировать баги, если они есть.",
        "tags": ["Тестирование", "QA", "Удаленно"],
        "price": "1 000 ₽",
        "meta": "Разовый заказ",
        "type": "one-time", "format": "remote", "category": "it", "experience": "none"
    },
    {
        "id": 10,
        "title": "Сборщик заказов в выходные",
        "company": 'Супермаркет "Быстро"',
        "desc": "Ищем активных ребят для сборки онлайн-заказов в супермаркете. Работа через удобное приложение. Можно выбирать удобные смены от 4 часов.",
        "tags": ["Смены", "Офлайн", "Без опыта"],
        "price": "300 ₽",
        "meta": "Постоянная работа",
        "type": "shifts", "format": "office", "category": "other", "experience": "none"
    }
]

# Generate job detail pages
with open(r'd:\TeenWork\job-details.html', 'r', encoding='utf-8') as f:
    template_html = f.read()

for job in jobs_data:
    page_html = template_html
    # Title
    page_html = re.sub(r'<title>.*?</title>', f'<title>{job["title"]} | TeenWork</title>', page_html)
    page_html = re.sub(r'<h1 class="job-detail-title">.*?</h1>', f'<h1 class="job-detail-title">{job["title"]}</h1>', page_html)
    page_html = re.sub(r'<div class="job-detail-price">.*?</div>', f'<div class="job-detail-price">{job["price"]}</div>', page_html)
    
    tags = "".join([f'<span class="job-card-tag">{t}</span>' for t in job["tags"]])
    page_html = re.sub(r'<div class="job-detail-tags">.*?</div>', f'<div class="job-detail-tags">\n                            {tags}\n                        </div>', page_html, flags=re.DOTALL)
    
    # Description
    desc_html = f'''<div class="job-detail-section">
                        <h3>Описание задачи</h3>
                        <p>{job["desc"]}</p>
                    </div>'''
    page_html = re.sub(r'<div class="job-detail-section">\s*<h3>Описание задачи</h3>.*?</div>', desc_html, page_html, flags=re.DOTALL)
    
    page_html = page_html.replace('ООО "ТехНова"', job["company"])
    page_html = page_html.replace('data-category="design"', f'data-category="{job["category"]}"')
    
    with open(f'd:\\TeenWork\\job-{job["id"]}.html', 'w', encoding='utf-8') as f:
        f.write(page_html)

print("job pages generated.")
