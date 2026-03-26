document.addEventListener('DOMContentLoaded', () => {

    // Header Scroll Effect
    const header = document.querySelector('.header');

    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });

    // Initial animations for Hero section
    setTimeout(() => {
        const animatedElements = document.querySelectorAll('.fade-in-up, .fade-in');
        animatedElements.forEach(el => {
            el.classList.add('visible');
        });
    }, 100);

    // Scroll Reveal Intersection Observer
    const revealElements = document.querySelectorAll('.reveal-on-scroll');

    const revealCallback = (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
            }
        });
    };

    const revealOptions = {
        threshold: 0.15,
        rootMargin: "0px 0px -50px 0px"
    };

    const revealObserver = new IntersectionObserver(revealCallback, revealOptions);

    revealElements.forEach(el => {
        revealObserver.observe(el);
    });

    // Smooth hover effect for cards with tilt (optional lightweight pseudo-tilt)
    const cards = document.querySelectorAll('.feature-card, .glass-card, .cta-box');

    cards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            // Set CSS variables for spotlight effect
            card.style.setProperty('--mouse-x', `${x}px`);
            card.style.setProperty('--mouse-y', `${y}px`);
        });
    });

    // Add spotlight CSS dynamically to cards for the effect
    const style = document.createElement('style');
    style.innerHTML = `
        .feature-card, .glass-card, .cta-box {
            position: relative;
            overflow: hidden;
        }
        .feature-card::after, .glass-card::after, .cta-box::after {
            content: '';
            position: absolute;
            top: var(--mouse-y, -100px);
            left: var(--mouse-x, -100px);
            width: 200px;
            height: 200px;
            background: radial-gradient(circle, rgba(255, 184, 0, 0.15), transparent 70%);
            border-radius: 50%;
            transform: translate(-50%, -50%);
            opacity: 0;
            transition: opacity 0.3s ease;
            pointer-events: none;
            z-index: 0;
        }
        .feature-card:hover::after, .glass-card:hover::after, .cta-box:hover::after {
            opacity: 1;
        }
        .feature-card > *, .glass-card > *, .cta-box > * {
            position: relative;
            z-index: 1;
        }
    `;
    document.head.appendChild(style);

    // ==========================================
    // Mobile Navigation Drawer
    // ==========================================
    const mobileBtn = document.querySelector('.mobile-menu-btn');
    const headerEl = document.querySelector('.header');

    if (mobileBtn && headerEl) {
        // Build mobile drawer if it doesn't already exist
        let drawer = document.querySelector('.mobile-nav-drawer');
        let mobileOverlay = document.querySelector('.mobile-overlay');

        if (!drawer) {
            // Create overlay
            mobileOverlay = document.createElement('div');
            mobileOverlay.className = 'mobile-overlay';
            document.body.appendChild(mobileOverlay);

            // Create drawer
            drawer = document.createElement('div');
            drawer.className = 'mobile-nav-drawer';

            // Copy nav links
            const navLinks = document.querySelectorAll('.nav .nav-link');
            navLinks.forEach(link => {
                const clone = link.cloneNode(true);
                drawer.appendChild(clone);
            });

            // Copy header action buttons
            const headerActions = document.querySelector('.header-actions');
            if (headerActions) {
                const actionsDiv = document.createElement('div');
                actionsDiv.className = 'drawer-actions';
                const actionBtns = headerActions.querySelectorAll('.btn, a');
                actionBtns.forEach(btn => {
                    const clone = btn.cloneNode(true);
                    actionsDiv.appendChild(clone);
                });
                drawer.appendChild(actionsDiv);
            }

            document.body.appendChild(drawer);
        }

        function openDrawer() {
            drawer.classList.add('open');
            mobileOverlay.classList.add('active');
            document.body.style.overflow = 'hidden';
            const icon = mobileBtn.querySelector('i');
            if (icon) icon.classList.replace('ph-list', 'ph-x');
        }

        function closeDrawer() {
            drawer.classList.remove('open');
            mobileOverlay.classList.remove('active');
            document.body.style.overflow = '';
            const icon = mobileBtn.querySelector('i');
            if (icon) icon.classList.replace('ph-x', 'ph-list');
        }

        mobileBtn.addEventListener('click', () => {
            if (drawer.classList.contains('open')) {
                closeDrawer();
            } else {
                openDrawer();
            }
        });

        mobileOverlay.addEventListener('click', closeDrawer);

        // Close drawer on link click
        drawer.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', closeDrawer);
        });

        // Close drawer on resize to desktop
        window.addEventListener('resize', () => {
            if (window.innerWidth >= 1024) {
                closeDrawer();
            }
        });
    }

    // ==========================================
    // Mobile Filters Toggle (Jobs Page)
    // ==========================================
    const filtersToggle = document.querySelector('.filters-toggle-btn');
    const filtersSidebar = document.querySelector('.filters-sidebar');

    if (filtersToggle && filtersSidebar) {
        // Hide filters by default on mobile
        if (window.innerWidth < 768) {
            filtersSidebar.style.display = 'none';
        }

        filtersToggle.addEventListener('click', () => {
            const isVisible = filtersSidebar.style.display !== 'none';
            filtersSidebar.style.display = isVisible ? 'none' : 'block';
            
            const icon = filtersToggle.querySelector('i');
            if (icon) {
                if (isVisible) {
                    icon.classList.replace('ph-funnel-simple', 'ph-funnel-simple');
                    filtersToggle.querySelector('span').textContent = 'Показать фильтры';
                } else {
                    filtersToggle.querySelector('span').textContent = 'Скрыть фильтры';
                }
            }
        });

        // Show filters on resize to tablet+
        window.addEventListener('resize', () => {
            if (window.innerWidth >= 768) {
                filtersSidebar.style.display = '';
            }
        });
    }

    // ==========================================
    // Jobs filtering logic
    // ==========================================
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

        const applyFiltersBtn = document.getElementById('apply-filters-btn');
        if (applyFiltersBtn) {
            applyFiltersBtn.addEventListener('click', filterJobs);
        }

        // Also filter on Enter key in search
        searchInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                filterJobs();
            }
        });

        // Initial filter
        filterJobs();
    }
});
