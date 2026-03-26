import os

# Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract header and footer
header_end = content.find('<main>') + len('<main>')
footer_start = content.find('</main>')

header = content[:header_end]
footer = content[footer_start:]

# Fix active navigation links in header (simple approach - replace # with actual links)
header = header.replace('href="#features"', 'href="index.html#features"')
header = header.replace('href="#how-it-works"', 'href="index.html#how-it-works"')
header = header.replace('href="#education"', 'href="knowledge-base.html"')
header = header.replace('href="#employers"', 'href="employers.html"')

pages = {
    'jobs-one-time.html': {
        'title': 'Разовые заказы | TeenWork',
        'content': '''
        <section class="hero" style="min-height: 50vh; padding-top: 120px;">
            <div class="bg-glow-container">
                <div class="glow-orb orb-1"></div>
            </div>
            <div class="container text-center">
                <div class="badge badge-dark">Работа для тебя</div>
                <h1 class="section-title">Разовые <span class="text-gradient">заказы</span></h1>
                <p class="section-subtitle mx-auto" style="max-width: 600px;">Выполняй простые поручения, зарабатывай карманные деньги и прокачивай профиль.</p>
            </div>
        </section>
        <section class="section pt-0">
            <div class="container">
                <div class="features-grid">
                    <div class="glass-card mockup-card" style="position: static; width: auto; animation: none; transform: none; box-shadow: var(--glass-shadow);">
                        <div class="job-tag">Дизайн</div>
                        <div class="job-title">Сделать превью для YouTube</div>
                        <div class="job-price">500 ₽ <span class="guarantee-badge"><i class="ph-fill ph-shield-check"></i> Гарантия</span></div>
                        <p class="text-muted mb-4">Нужно яркое превью для игрового ролика. Исходники предоставлю.</p>
                        <button class="btn btn-primary btn-sm btn-block mt-4">Откликнуться</button>
                    </div>
                    <div class="glass-card mockup-card" style="position: static; width: auto; animation: none; transform: none; box-shadow: var(--glass-shadow);">
                        <div class="job-tag">Тексты</div>
                        <div class="job-title">Написать 3 поста для Telegram</div>
                        <div class="job-price">900 ₽ <span class="guarantee-badge"><i class="ph-fill ph-shield-check"></i> Гарантия</span></div>
                        <p class="text-muted mb-4">Тематика: технологии и гаджеты. Объем около 1000 символов каждый.</p>
                        <button class="btn btn-primary btn-sm btn-block mt-4">Откликнуться</button>
                    </div>
                    <div class="glass-card mockup-card" style="position: static; width: auto; animation: none; transform: none; box-shadow: var(--glass-shadow);">
                        <div class="job-tag">Офлайн</div>
                        <div class="job-title">Выгулять собаку (Хаски)</div>
                        <div class="job-price">300 ₽ / час <span class="guarantee-badge"><i class="ph-fill ph-shield-check"></i> Гарантия</span></div>
                        <p class="text-muted mb-4">Район Центр. Собака активная, нужна прогулка минимум 1.5 часа.</p>
                        <button class="btn btn-primary btn-sm btn-block mt-4">Откликнуться</button>
                    </div>
                </div>
            </div>
        </section>
        '''
    },
    'jobs-shifts.html': {
        'title': 'Посменная работа | TeenWork',
        'content': '''
        <section class="hero" style="min-height: 50vh; padding-top: 120px;">
            <div class="bg-glow-container">
                <div class="glow-orb orb-2"></div>
            </div>
            <div class="container text-center">
                <div class="badge badge-dark">Стабильный доход</div>
                <h1 class="section-title">Посменная <span class="text-gradient">работа</span></h1>
                <p class="section-subtitle mx-auto" style="max-width: 600px;">Найди работу, которую легко совмещать с учебой благодаря гибкому графику.</p>
            </div>
        </section>
        <section class="section pt-0">
            <div class="container">
                <div class="features-grid">
                    <div class="glass-card mockup-card" style="position: static; width: auto; animation: none; transform: none; box-shadow: var(--glass-shadow);">
                        <div class="job-tag">Бариста</div>
                        <div class="job-title">CoffeSpace: Смены по выходным</div>
                        <div class="job-price">от 15 000 ₽/мес <span class="guarantee-badge"><i class="ph-fill ph-shield-check"></i> Оформление</span></div>
                        <p class="text-muted mb-4">Ищем бариста выходного дня. Обучим с нуля, оплата за смену + чаевые.</p>
                        <button class="btn btn-primary btn-sm btn-block mt-4">Откликнуться</button>
                    </div>
                    <div class="glass-card mockup-card" style="position: static; width: auto; animation: none; transform: none; box-shadow: var(--glass-shadow);">
                        <div class="job-tag">Курьер</div>
                        <div class="job-title">Доставка документов (Офис)</div>
                        <div class="job-price">от 2000 ₽/смена <span class="guarantee-badge"><i class="ph-fill ph-shield-check"></i> Оформление</span></div>
                        <p class="text-muted mb-4">Развоз бумаг по городу. Гибкий график, оплата проезда.</p>
                        <button class="btn btn-primary btn-sm btn-block mt-4">Откликнуться</button>
                    </div>
                </div>
            </div>
        </section>
        '''
    },
    'internships.html': {
        'title': 'Стажировки | TeenWork',
        'content': '''
        <section class="hero" style="min-height: 50vh; padding-top: 120px;">
            <div class="bg-glow-container">
                <div class="glow-orb orb-3"></div>
            </div>
            <div class="container text-center">
                <div class="badge badge-dark">Карьерный старт</div>
                <h1 class="section-title">Оплачиваемые <span class="text-gradient">стажировки</span></h1>
                <p class="section-subtitle mx-auto" style="max-width: 600px;">Получи первый оффер от крутых компаний и развивайся в IT, маркетинге или дизайне.</p>
            </div>
        </section>
        <section class="section pt-0">
            <div class="container">
                <div class="glass-panel" style="padding: 40px; margin-bottom: 24px;">
                    <div style="display: flex; gap: 24px; align-items: flex-start; flex-wrap: wrap;">
                        <img src="https://ui-avatars.com/api/?name=Tech+Corp&background=random" style="width: 80px; height: 80px; border-radius: 16px;">
                        <div style="flex: 1; min-width: 300px;">
                            <h3 style="font-size: 1.5rem; margin-bottom: 8px;">Junior Frontend Разработчик (Стажер)</h3>
                            <p style="color: var(--text-muted); margin-bottom: 16px;">IT Company "TechNova" • Удаленно</p>
                            <p>3-х месячная стажировка с ментором. Изучение React, создание компонентов для внутреннего портала. Оплата 25 000 руб/мес.</p>
                        </div>
                        <button class="btn btn-primary">Подать заявку</button>
                    </div>
                </div>
                <div class="glass-panel" style="padding: 40px; margin-bottom: 24px;">
                    <div style="display: flex; gap: 24px; align-items: flex-start; flex-wrap: wrap;">
                        <img src="https://ui-avatars.com/api/?name=Media&background=random" style="width: 80px; height: 80px; border-radius: 16px;">
                        <div style="flex: 1; min-width: 300px;">
                            <h3 style="font-size: 1.5rem; margin-bottom: 8px;">Стажер SMM / Контент-мейкер</h3>
                            <p style="color: var(--text-muted); margin-bottom: 16px;">Агентство "Buzz" • Гибрид</p>
                            <p>Помощь в создании Reels, генерации идей для постов. Отличный старт для креативных ребят. Оплата 15 000 руб/мес.</p>
                        </div>
                        <button class="btn btn-primary">Подать заявку</button>
                    </div>
                </div>
            </div>
        </section>
        '''
    },
    'employers.html': {
        'title': 'Для работодателей | TeenWork',
        'content': '''
        <section class="hero" style="min-height: 50vh; padding-top: 120px;">
            <div class="bg-glow-container">
                <div class="glow-orb orb-1"></div>
            </div>
            <div class="container text-center">
                <h1 class="section-title">Нанимайте <span class="text-gradient">энергичных</span> сотрудников</h1>
                <p class="section-subtitle mx-auto" style="max-width: 600px;">Молодые таланты готовы к выполнению ваших задач уже сегодня. Легально, быстро и безопасно.</p>
                <div class="hero-buttons justify-center mt-4" style="margin-top: 32px; justify-content: center;">
                    <button class="btn btn-primary btn-lg">Опубликовать вакансию (200 ₽)</button>
                    <button class="btn btn-outline btn-lg">Связаться с нами</button>
                </div>
            </div>
        </section>
        <section class="section pt-0">
            <div class="container">
                <div class="features-grid">
                    <div class="feature-card glass-panel" style="text-align: center;">
                        <div class="feature-icon mx-auto"><i class="ph-duotone ph-lightning"></i></div>
                        <h3 class="feature-title">Быстрое закрытие задач</h3>
                        <p class="feature-desc">Разовые поручения забирают в течение 10 минут после публикации.</p>
                    </div>
                    <div class="feature-card glass-panel" style="text-align: center;">
                        <div class="feature-icon mx-auto"><i class="ph-duotone ph-wallet"></i></div>
                        <h3 class="feature-title">Экономия средств</h3>
                        <p class="feature-desc">Ставки стажеров и джуниоров ниже рыночных, а мотивация зачастую выше.</p>
                    </div>
                    <div class="feature-card glass-panel" style="text-align: center;">
                        <div class="feature-icon mx-auto"><i class="ph-duotone ph-files"></i></div>
                        <h3 class="feature-title">Юридическая чистота</h3>
                        <p class="feature-desc">Помогаем с договорами ГПХ, статусом самозанятого и закрывающими документами.</p>
                    </div>
                </div>
            </div>
        </section>
        '''
    },
    'pro.html': {
        'title': 'TeenWork Pro | TeenWork',
        'content': '''
        <section class="hero" style="min-height: 50vh; padding-top: 120px;">
            <div class="bg-glow-container">
                <div class="glow-orb orb-3"></div>
            </div>
            <div class="container text-center">
                <div class="badge badge-dark" style="background: var(--primary); color: var(--secondary);">Премиум</div>
                <h1 class="section-title">TeenWork <span class="text-gradient">PRO</span></h1>
                <p class="section-subtitle mx-auto" style="max-width: 600px;">Получай больше заказов, выделяйся среди откликов и прокачивай навыки быстрее всего за 350 ₽ в месяц.</p>
            </div>
        </section>
        <section class="section pt-0">
            <div class="container" style="max-width: 800px;">
                <div class="glass-panel" style="padding: 48px; text-align: center; border: 2px solid var(--primary); box-shadow: 0 20px 40px rgba(255, 184, 0, 0.2);">
                    <h2 style="font-size: 2.5rem; margin-bottom: 24px;">350 ₽ <span style="font-size: 1rem; color: var(--text-muted);">/ месяц</span></h2>
                    <ul class="benefit-list" style="text-align: left; max-width: 400px; margin: 0 auto 32px auto;">
                        <li><i class="ph-fill ph-check-circle"></i><div><strong>PRO-статус в профиле</strong><p>Заказчики видят вас в топе поиска.</p></div></li>
                        <li><i class="ph-fill ph-check-circle"></i><div><strong>Сниженная комиссия</strong><p>Комиссия сервиса ниже на 2%.</p></div></li>
                        <li><i class="ph-fill ph-check-circle"></i><div><strong>Безлимитные отклики</strong><p>Откликайся на любое количество заданий.</p></div></li>
                    </ul>
                    <button class="btn btn-primary btn-lg btn-block" style="max-width: 400px; margin: 0 auto;">Оформить подписку</button>
                </div>
            </div>
        </section>
        '''
    },
    'knowledge-base.html': {
        'title': 'База знаний | TeenWork',
        'content': '''
        <section class="hero" style="min-height: 40vh; padding-top: 120px;">
            <div class="bg-glow-container">
                <div class="glow-orb orb-2"></div>
            </div>
            <div class="container text-center">
                <h1 class="section-title">База <span class="text-gradient">знаний</span></h1>
                <p class="section-subtitle mx-auto" style="max-width: 600px;">Все, что нужно знать о первой работе, правах и фрилансе.</p>
            </div>
        </section>
        <section class="section pt-0">
            <div class="container">
                <div class="features-grid">
                    <div class="glass-card mockup-course" style="position: static; width: auto; animation: none; transform: none; box-shadow: var(--glass-shadow);">
                        <i class="ph-duotone ph-book-open course-icon"></i>
                        <div style="flex:1;">
                            <div class="course-title">Как стать самозанятым?</div>
                            <div class="course-meta">Статья • 5 мин чтения</div>
                        </div>
                        <button class="btn btn-outline btn-sm">Читать</button>
                    </div>
                    <div class="glass-card mockup-course" style="position: static; width: auto; animation: none; transform: none; box-shadow: var(--glass-shadow);">
                        <i class="ph-duotone ph-shield-check course-icon"></i>
                        <div style="flex:1;">
                            <div class="course-title">Трудовые права до 18 лет</div>
                            <div class="course-meta">Видео • 12 мин</div>
                        </div>
                        <button class="btn btn-outline btn-sm">Смотреть</button>
                    </div>
                    <div class="glass-card mockup-course" style="position: static; width: auto; animation: none; transform: none; box-shadow: var(--glass-shadow);">
                        <i class="ph-duotone ph-pencil-line course-icon"></i>
                        <div style="flex:1;">
                            <div class="course-title">Как составить резюме без опыта</div>
                            <div class="course-meta">Статья • 7 мин чтения</div>
                        </div>
                        <button class="btn btn-outline btn-sm">Читать</button>
                    </div>
                </div>
            </div>
        </section>
        '''
    },
    'rules.html': {
        'title': 'Правила платформы | TeenWork',
        'content': '''
        <section class="hero" style="min-height: 30vh; padding-top: 120px;">
            <div class="container text-center">
                <h1 class="section-title">Правила <span class="text-gradient">платформы</span></h1>
            </div>
        </section>
        <section class="section pt-0">
            <div class="container" style="max-width: 800px;">
                <div class="glass-panel" style="padding: 40px; font-size: 1.1rem; line-height: 1.8;">
                    <h2>1. Общие положения</h2>
                    <p class="mb-4">Платформа TeenWork предназначена для безопасного взаимодействия между заказчиками и исполнителями в возрасте от 14 до 25 лет.</p>
                    <h2 class="mt-4">2. Запрещенный контент</h2>
                    <p class="mb-4">Запрещается публикация заданий, нарушающих законодательство РФ, а также заданий, связанных с рисками для жизни и здоровья.</p>
                    <h2 class="mt-4">3. Ответственность</h2>
                    <p class="mb-4">Обе стороны обязаны соблюдать договоренности. В случае споров администрация платформы выступает арбитром.</p>
                </div>
            </div>
        </section>
        '''
    },
    'insurance.html': {
        'title': 'Страховой фонд | TeenWork',
        'content': '''
        <section class="hero" style="min-height: 40vh; padding-top: 120px;">
            <div class="bg-glow-container">
                <div class="glow-orb orb-1" style="background: radial-gradient(circle, rgba(16, 185, 129, 0.3), transparent 70%);"></div>
            </div>
            <div class="container text-center">
                <h1 class="section-title">Страховой <span class="text-gradient">фонд</span></h1>
                <p class="section-subtitle mx-auto" style="max-width: 600px;">Твоя гарантия оплаты труда. Мы возвращаем деньги, если заказчик оказался недобросовестным.</p>
            </div>
        </section>
        <section class="section pt-0">
            <div class="container" style="max-width: 800px;">
                <div class="features-grid">
                    <div class="glass-panel" style="padding: 32px; text-align: center;">
                        <span style="font-size: 3rem; font-weight: 800; color: var(--success);">5%</span>
                        <p>С каждой транзакции отчисляется в фонд платформы</p>
                    </div>
                    <div class="glass-panel" style="padding: 32px; text-align: center;">
                        <span style="font-size: 3rem; font-weight: 800; color: var(--success);">100%</span>
                        <p>Компенсация в случае доказанного обмана со стороны заказчика</p>
                    </div>
                </div>
            </div>
        </section>
        '''
    },
    'terms.html': {
        'title': 'Пользовательское соглашение | TeenWork',
        'content': '''
        <section class="hero" style="min-height: 30vh; padding-top: 120px;">
            <div class="container text-center">
                <h1 class="section-title">Пользовательское <span class="text-gradient">соглашение</span></h1>
            </div>
        </section>
        <section class="section pt-0">
            <div class="container" style="max-width: 800px;">
                <div class="glass-panel" style="padding: 40px; font-size: 1rem; line-height: 1.8; color: var(--text-muted);">
                    <p>Настоящее Соглашение определяет условия использования сервиса TeenWork...</p>
                    <p>1. Термины и определения...</p>
                    <p>2. Предмет соглашения...</p>
                    <p>3. Права и обязанности сторон...</p>
                    <p><em>(Типовой текст пользовательского соглашения)</em></p>
                </div>
            </div>
        </section>
        '''
    }
}

for filename, data in pages.items():
    # Update title in header
    page_header = header.replace('<title>TeenWork | Безопасная работа и стажировки для молодежи</title>', f'<title>{data["title"]}</title>')
    
    # Assemble page
    full_html = page_header + '<main>\n' + data['content'] + '\n    </main>' + footer
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(full_html)
    print(f"Created {filename}")
