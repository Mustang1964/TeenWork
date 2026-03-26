import re

with open('D:/TeenWork/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Add global touch and image fixes
global_fixes = """
/* Touch and Reset Updates */
img, picture, video, canvas, svg {
    display: block;
    max-width: 100%;
    height: auto;
}
button, a.btn, input, select, textarea {
    min-height: 44px; /* Touch UX */
}
"""
css = css.replace("/* -- VARIABLES & RESET -- */", "/* -- VARIABLES & RESET -- */\n" + global_fixes)

# 2. Refactor grids to mobile first
replacements = [
    # .hero-container
    (r'(\.hero-container\s*{[^}]*?)grid-template-columns:\s*1fr\s+1fr;', r'\1grid-template-columns: 1fr;'),
    
    # .features-grid
    (r'(\.features-grid\s*{[^}]*?)grid-template-columns:\s*repeat\(auto-fit,\s*minmax\(320px,\s*1fr\)\);', r'\1grid-template-columns: 1fr;'),
    
    # .steps-container
    (r'(\.steps-container\s*{[^}]*?)grid-template-columns:\s*1fr\s+1fr;', r'\1grid-template-columns: 1fr;'),
    
    # .footer-grid
    (r'(\.footer-grid\s*{[^}]*?)grid-template-columns:\s*2fr\s+1fr\s+1fr;', r'\1grid-template-columns: 1fr;'),
    
    # .jobs-layout
    (r'(\.jobs-layout\s*{[^}]*?)grid-template-columns:\s*280px\s+1fr;', r'\1grid-template-columns: 1fr;'),
    
    # .job-detail-content
    (r'(\.job-detail-content\s*{[^}]*?)grid-template-columns:\s*2fr\s+1fr;', r'\1grid-template-columns: 1fr;'),
    
    # nav
    (r'(\.nav\s*{[^}]*?)display:\s*flex;', r'\1display: none;'),
    
    # header-actions
    (r'(\.header-actions\s*{[^}]*?)display:\s*flex;', r'\1display: none;'),
    
    # mobile-menu-btn
    (r'(\.mobile-menu-btn\s*{[^}]*?)display:\s*none;', r'\1display: block;'),
    
    # hero-title
    (r'(\.hero-title\s*{[^}]*?)font-size:\s*5rem;', r'\1font-size: clamp(2.5rem, 8vw, 5rem);'),
    
    # section-title
    (r'(\.section-title\s*{[^}]*?)font-size:\s*3rem;', r'\1font-size: clamp(2rem, 5vw, 3rem);'),
    
    # job-detail-title
    (r'(\.job-detail-title\s*{[^}]*?)font-size:\s*2.5rem;', r'\1font-size: clamp(1.8rem, 4vw, 2.5rem);'),
    
    # hero-visual
    (r'(\.hero-visual\s*{[^}]*?)height:\s*650px;', r'\1height: 400px;'),
]

for pattern, repl in replacements:
    css = re.sub(pattern, repl, css, flags=re.DOTALL)

# 3. Strip old max-width media queries entirely
css = re.sub(r'/\* -- RESPONSIVE -- \*/.*$', '', css, flags=re.DOTALL)

new_media_queries = """
/* -- RESPONSIVE (MOBILE FIRST) -- */
/* Mobile Menu Styles */
.header.menu-open .nav {
    display: flex;
    flex-direction: column;
    position: absolute;
    top: 70px;
    left: 0;
    width: 100%;
    background: rgba(255, 255, 255, 0.98);
    backdrop-filter: blur(20px);
    padding: 24px;
    gap: 24px;
    box-shadow: 0 10px 20px rgba(0,0,0,0.05);
}
.header.menu-open .nav-link {
    font-size: 1.25rem;
    padding: 8px 0;
}
.header.menu-open .header-actions {
    display: flex;
    flex-direction: column;
    position: absolute;
    top: 250px;
    left: 0;
    width: 100%;
    padding: 0 24px 24px;
    background: rgba(255, 255, 255, 0.98);
    backdrop-filter: blur(20px);
    box-shadow: 0 10px 20px rgba(0,0,0,0.05);
}

.hero-visual {
    margin-top: 40px;
}
.mockup-profile { left: auto; right: 5%; top: 10%; width: 220px; }
.mockup-job { left: 5%; top: 40%; width: 260px; }
.mockup-course { right: 5%; bottom: 10%; width: 240px; }

.employer-benefits { flex-direction: column; }

.stats { 
    flex-wrap: wrap; 
    justify-content: center; 
}

@media (min-width: 480px) {
    .container { padding: 0 24px; }
    .hero-visual { height: 500px; }
}

@media (min-width: 768px) {
    .hero-buttons {
        flex-direction: row;
        justify-content: flex-start;
    }
    .jobs-grid .job-card {
        flex-direction: row;
        gap: 24px;
    }
    .job-card-side { align-items: flex-end; }
    .features-grid {
        grid-template-columns: repeat(2, 1fr);
    }
    .footer-grid {
        grid-template-columns: 1fr 1fr;
    }
    .employer-benefits {
        flex-direction: row;
    }
    .job-detail-top {
        flex-direction: row;
        align-items: flex-start;
    }
}

@media (min-width: 1024px) {
    /* Header layout */
    .nav {
        display: flex !important;
        position: static;
        flex-direction: row;
        background: transparent;
        padding: 0;
        box-shadow: none;
        width: auto;
    }
    .header-actions {
        display: flex !important;
        position: static;
        flex-direction: row;
        background: transparent;
        padding: 0;
        box-shadow: none;
        width: auto;
    }
    .mobile-menu-btn {
        display: none !important;
    }
    
    /* Layout Grids */
    .hero-container, .steps-container {
        grid-template-columns: 1fr 1fr;
    }
    .hero-content {
        text-align: left;
    }
    .features-grid {
        grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
    }
    .footer-grid {
        grid-template-columns: 2fr 1fr 1fr;
    }
    .jobs-layout {
        grid-template-columns: 280px 1fr;
    }
    .job-detail-content {
        grid-template-columns: 2fr 1fr;
    }
    
    .hero-visual {
        height: 650px;
        margin-top: 0;
    }
    .mockup-profile { top: -25px; right: 50px; width: 280px; }
    .mockup-job { top: 125px; left: 0; width: 320px; }
    .mockup-course { bottom: 185px; right: 220px; width: 310px; }
    .search-header { flex-direction: row; }
}

@media (min-width: 1440px) {
    .container {
        max-width: 1320px;
    }
}
"""

css += "\n" + new_media_queries

with open('D:/TeenWork/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("SUCCESS: Refactored CSS")
