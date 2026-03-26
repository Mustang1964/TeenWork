import os
import re

# Update js/script.js
js_code = """
document.addEventListener("DOMContentLoaded", () => {
    // Jobs filtering logic
    const searchInput = document.querySelector('.search-input');
    const filterCheckboxes = document.querySelectorAll('.filter-options input[type="checkbox"]');
    const jobCards = document.querySelectorAll('.job-card');

    if (searchInput && filterCheckboxes.length > 0 && jobCards.length > 0) {
        function filterJobs() {
            const searchTerm = searchInput.value.toLowerCase().trim();
            const activeFilters = {
                type: [],
                format: [],
                category: [],
                experience: []
            };

            // Gather active filters
            filterCheckboxes.forEach(cb => {
                if (cb.checked) {
                    const filterGroup = cb.closest('.filter-group').querySelector('.filter-title').textContent.trim();
                    const value = cb.value;
                    
                    if (filterGroup === 'Тип работы') activeFilters.type.push(value);
                    if (filterGroup === 'Формат') activeFilters.format.push(value);
                    if (filterGroup === 'Категория') activeFilters.category.push(value);
                    if (filterGroup === 'Опыт') activeFilters.experience.push(value);
                }
            });

            // Filter cards
            jobCards.forEach(card => {
                const title = card.getAttribute('data-title').toLowerCase();
                const type = card.getAttribute('data-type');
                const format = card.getAttribute('data-format');
                const category = card.getAttribute('data-category');
                const experience = card.getAttribute('data-experience');

                const matchesSearch = title.includes(searchTerm);
                
                const matchesType = activeFilters.type.length === 0 || activeFilters.type.includes(type);
                const matchesFormat = activeFilters.format.length === 0 || activeFilters.format.includes(format);
                const matchesCategory = activeFilters.category.length === 0 || activeFilters.category.includes(category);
                const matchesExperience = activeFilters.experience.length === 0 || activeFilters.experience.includes(experience);

                if (matchesSearch && matchesType && matchesFormat && matchesCategory && matchesExperience) {
                    card.style.display = 'flex';
                } else {
                    card.style.display = 'none';
                }
            });
        }

        searchInput.addEventListener('input', filterJobs);
        filterCheckboxes.forEach(cb => cb.addEventListener('change', filterJobs));
        
        // Initial filter
        filterJobs();
    }
});
"""
with open(r'd:\TeenWork\js\script.js', 'a', encoding='utf-8') as f:
    f.write(js_code)


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

# Update jobs.html
with open(r'd:\TeenWork\jobs.html', 'r', encoding='utf-8') as f:
    jobs_html = f.read()

# Replace filters
filters_old = '''<div class="filter-options">
                            <label><input type="checkbox" checked> Разовый заказ</label>
                            <label><input type="checkbox" checked> Смены</label>
                            <label><input type="checkbox"> Стажировка</label>
                            <label><input type="checkbox"> Проектная работа</label>
                        </div>'''
filters_new = '''<div class="filter-options">
                            <label><input type="checkbox" value="one-time" checked> Разовый заказ</label>
                            <label><input type="checkbox" value="shifts" checked> Смены</label>
                            <label><input type="checkbox" value="internship"> Стажировка</label>
                            <label><input type="checkbox" value="project"> Проектная работа</label>
                        </div>'''
jobs_html = jobs_html.replace(filters_old, filters_new)

filters_old = '''<div class="filter-options">
                            <label><input type="checkbox" checked> Удаленно</label>
                            <label><input type="checkbox"> В офисе / На месте</label>
                            <label><input type="checkbox"> Гибрид</label>
                        </div>'''
filters_new = '''<div class="filter-options">
                            <label><input type="checkbox" value="remote" checked> Удаленно</label>
                            <label><input type="checkbox" value="office"> В офисе / На месте</label>
                            <label><input type="checkbox" value="hybrid"> Гибрид</label>
                        </div>'''
jobs_html = jobs_html.replace(filters_old, filters_new)

filters_old = '''<div class="filter-options">
                            <label><input type="checkbox"> IT и Программирование</label>
                            <label><input type="checkbox" checked> Дизайн и Арт</label>
                            <label><input type="checkbox" checked> Тексты и Переводы</label>
                            <label><input type="checkbox"> Маркетинг</label>
                            <label><input type="checkbox"> Курьерская доставка</label>
                            <label><input type="checkbox"> Репетиторство</label>
                        </div>'''
filters_new = '''<div class="filter-options">
                            <label><input type="checkbox" value="it"> IT и Программирование</label>
                            <label><input type="checkbox" value="design" checked> Дизайн и Арт</label>
                            <label><input type="checkbox" value="texts" checked> Тексты и Переводы</label>
                            <label><input type="checkbox" value="marketing"> Маркетинг</label>
                            <label><input type="checkbox" value="other" checked> Офлайн / Разное</label>
                        </div>'''
jobs_html = jobs_html.replace(filters_old, filters_new)

filters_old = '''<div class="filter-options">
                            <label><input type="checkbox" checked> Без опыта</label>
                            <label><input type="checkbox"> До 1 года</label>
                            <label><input type="checkbox"> От 1 года до 3 лет</label>
                        </div>'''
filters_new = '''<div class="filter-options">
                            <label><input type="checkbox" value="none" checked> Без опыта</label>
                            <label><input type="checkbox" value="low" checked> До 1 года</label>
                            <label><input type="checkbox" value="mid"> От 1 года до 3 лет</label>
                        </div>'''
jobs_html = jobs_html.replace(filters_old, filters_new)

# Add data attributes to job cards
for job in jobs_data:
    original_card = f'<div class="job-card">'
    # Only replace one by one if we have multiple, but here I can use regex to replace specific cards based on title inside
    # Because we have <div class="job-card">, we can look for the title right after.
    # Actually, easier to regenerate the jobs grid completely!

grid_start = jobs_html.find('<div class="jobs-grid reveal-on-scroll" style="transition-delay: 0.2s;">')
if grid_start != -1:
    grid_start = jobs_html.find('>', grid_start) + 1

grid_end = jobs_html.find('</main>', grid_start)
if grid_end != -1:
    grid_end = jobs_html.rfind('<div class="overlay"', grid_start)
    # Actually just replacing everything inside the grid
    # Let's find the end of the grid specifically.
    grid_end_str = re.search(r'</div>\s*</div>\s*</div>\s*</main>', jobs_html[grid_start:])
    if grid_end_str:
        grid_end = grid_start + grid_end_str.start()

grid_content = ""
for job in jobs_data:
    guarantee = '<span class="guarantee-badge mt-4"><i class="ph-fill ph-shield-check"></i> Гарантия</span>' if "Гарантия" in job.get('meta', '') or job['id'] in [1, 5, 8] else ''
    tag_html = "".join([f'<span class="job-card-tag">{t}</span>' for t in job["tags"]])
    badge = ' <i class="ph-fill ph-seal-check verified" title="Верифицированный работодатель"></i>' if job['id'] in [1, 2, 3, 5, 7, 9, 10] else ''
    star = ' • <span style="margin-left: 4px;"><i class="ph-fill ph-star" style="color:var(--warning)"></i> 4.9</span>' if job['id'] in [1, 6] else ''
    
    card = f'''                    <!-- Job {job['id']} -->
                    <div class="job-card" data-title="{job['title']}" data-type="{job['type']}" data-format="{job['format']}" data-category="{job['category']}" data-experience="{job['experience']}">
                        <div class="job-card-main">
                            <div class="job-card-title"><a href="job-{job['id']}.html">{job['title']}</a></div>
                            <div class="job-card-employer">
                                {job['company']}{badge}{star}
                            </div>
                            <div class="job-card-desc">
                                {job['desc']}
                            </div>
                            <div class="job-card-tags">
                                {tag_html}
                            </div>
                        </div>
                        <div class="job-card-side">
                            <div class="job-card-price">{job['price']}</div>
                            <div class="job-card-meta">{job['meta']}</div>
                            {guarantee}
                        </div>
                    </div>
'''
    grid_content += card

new_jobs_html = jobs_html[:grid_start] + grid_content + jobs_html[grid_end:]

with open(r'd:\TeenWork\jobs.html', 'w', encoding='utf-8') as f:
    f.write(new_jobs_html)


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
    
    with open(f'd:\\TeenWork\\job-{job["id"]}.html', 'w', encoding='utf-8') as f:
        f.write(page_html)

print("Done generating pages and updating files.")
