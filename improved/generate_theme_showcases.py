import os
import shutil
import subprocess
from PIL import Image

INPUT_DIR = "/home/mohammad/Dev/image-for-plugins/screenshoots/smartlearn theme"
OUTPUT_DIR = "/home/mohammad/Dev/image-for-plugins/improved/theme"
os.makedirs(OUTPUT_DIR, exist_ok=True)

SHOWCASES = [
    {
        "filename": "0.png",
        "tagline": "✦ NEXT-GEN MOODLE 4.5+ / 5.X THEME • THEME_SMARTLEARN",
        "title": "Flagship <span>Glassmorphic Landing Page</span>",
        "subtitle": "Transform Moodle into a breathtaking modern learning portal. Features glassmorphism aesthetics, live search hero, course grids, stats counters, and seamless dual light/dark modes.",
        "img_width": 1420,
        "img_height": 620,
        "callouts": [
            {
                "title": "✨ Modern Glassmorphism UI",
                "desc": "Frosted glass blur effects, smooth micro-interactions, and responsive layout.",
                "pos": "top: 40px; left: 20px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🔍 Interactive Hero & Search",
                "desc": "Instant course discovery bar and curated subject badges right on the frontpage.",
                "pos": "top: 40px; right: 20px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🌓 Instant Dual-Mode Switcher",
                "desc": "Seamless one-click toggle between 27 curated light and dark aesthetic themes.",
                "pos": "bottom: 40px; right: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "1-setting.png",
        "tagline": "✦ ENTERPRISE THEME ADMINISTRATION • THEME_SMARTLEARN",
        "title": "Unified <span>Brand Identity & General Settings</span>",
        "subtitle": "Centralized configuration panel for logos, favicons, custom branding colors, and institutional presets directly within Site Administration.",
        "img_width": 1400,
        "img_height": 610,
        "callouts": [
            {
                "title": "🎨 Brand Color Engine",
                "desc": "Configure primary brand accents, dark/light contrast ratios, and secondary hues.",
                "pos": "top: 40px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🖼️ Dynamic Logo & Favicon",
                "desc": "Multi-format logo upload supporting standard, compact mobile, and SVG brand assets.",
                "pos": "top: 40px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "⚡ Instant Cacheless Live Preview",
                "desc": "Review visual branding changes in real time before publishing site-wide.",
                "pos": "bottom: 40px; right: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "2-select style.png",
        "tagline": "✦ 27 CURATED DESIGN PRESETS & PALETTES • THEME_SMARTLEARN",
        "title": "Visual <span>Style & Palette Selector</span>",
        "subtitle": "Choose from 27 expertly designed color presets (Cyberpunk, Neon Tokyo, Deep Space, Nordic Clean, Aurora, Obsidian, Emerald) with automatic light and dark mode pairing.",
        "img_width": 1400,
        "img_height": 610,
        "callouts": [
            {
                "title": "🎭 27 Pre-Built Presets",
                "desc": "Instant modern themes ranging from ultra-clean minimalist to vibrant dark futuristic.",
                "pos": "top: 40px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🌓 Dual-Mode Pairing",
                "desc": "Define specific light and dark theme complements with one-click user switching.",
                "pos": "top: 40px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🔒 Homepage Preset Lock",
                "desc": "Option to enforce a signature theme on the frontpage while allowing user choice inside courses.",
                "pos": "bottom: 40px; right: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "3- login page option.png",
        "tagline": "✦ HIGH-CONVERTING AUTHENTICATION EXPERIENCES • THEME_SMARTLEARN",
        "title": "AI-Powered <span>Login Page Customizer</span>",
        "subtitle": "Elevate first impressions with customizable login layouts. Choose between Split-Screen, Fullscreen Immersive Hero, or generate brand-new layouts with AI prompt assistance.",
        "img_width": 1400,
        "img_height": 610,
        "callouts": [
            {
                "title": "🖼️ Split & Fullscreen Layouts",
                "desc": "Switch between modern split-card and full-bleed high-impact background styles.",
                "pos": "top: 40px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🤖 AI Layout Generator",
                "desc": "Generate custom login hero sections and branding copy using integrated AI prompts.",
                "pos": "top: 40px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🔒 Fully Secure Core Auth",
                "desc": "100% compliant with Moodle core authentication, OAuth2, SAML, and SSO plugins.",
                "pos": "bottom: 40px; right: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "4- coveride style.png",
        "tagline": "✦ GRANULAR CSS & TYPOGRAPHY CONTROL • THEME_SMARTLEARN",
        "title": "Deep <span>Style Overrides & CSS Engine</span>",
        "subtitle": "Fine-tune typography, Google Fonts pairings, border radiuses, container shadows, and inject custom CSS variables without ever modifying source files.",
        "img_width": 1400,
        "img_height": 610,
        "callouts": [
            {
                "title": "🔤 Google Fonts Integration",
                "desc": "Select modern font pairings (Inter, Outfit, Plus Jakarta Sans) for headings and body.",
                "pos": "top: 40px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🎛️ CSS Variable Overrides",
                "desc": "Tweak border-radius, card elevation, and backdrop blur strength on the fly.",
                "pos": "top: 40px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🛡️ Upgrade-Safe Custom Code",
                "desc": "Injected SCSS/CSS rules remain untouched across Moodle and theme version updates.",
                "pos": "bottom: 40px; right: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "5- navbar.png",
        "tagline": "✦ ADAPTIVE HEADER NAVIGATION • THEME_SMARTLEARN",
        "title": "Dynamic <span>Navbar & Header Canvas</span>",
        "subtitle": "Configure responsive navigation bars with custom menu items, quick search bar, role-based link toggles, and customizable logo placements.",
        "img_width": 1400,
        "img_height": 600,
        "callouts": [
            {
                "title": "🧭 Quick Nav Link Toggles",
                "desc": "Easily show or hide Home, My Courses, and Dashboard links with one click.",
                "pos": "top: 40px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🔍 Inline Course Search",
                "desc": "Built-in search input in the navigation bar for rapid course and activity lookup.",
                "pos": "top: 40px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "📱 Fully Responsive Drawer",
                "desc": "Flawless sticky header experience optimized for desktop, tablet, and mobile displays.",
                "pos": "bottom: 40px; right: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "6- sections-1.png",
        "tagline": "✦ VISUAL DRAG-AND-DROP PAGE COMPOSER • THEME_SMARTLEARN",
        "title": "Smart Canvas <span>Frontpage Section Builder</span>",
        "subtitle": "Build engaging homepage layouts by stacking, re-ordering, and toggling modular Canvas sections without writing a single line of HTML or PHP.",
        "img_width": 1420,
        "img_height": 580,
        "callouts": [
            {
                "title": "🧱 Modular Canvas Architecture",
                "desc": "Enable Hero banners, features, course grids, stats counters, and testimonials.",
                "pos": "top: 40px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "↕️ Drag-and-Drop Ordering",
                "desc": "Effortlessly rearrange the visual hierarchy of your LMS homepage in seconds.",
                "pos": "top: 40px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "👁️ Instant Visibility Controls",
                "desc": "Toggle individual sections on or off for seasonal campaigns or promotions.",
                "pos": "bottom: 40px; right: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "7- sections-selection.png",
        "tagline": "✦ PRE-BUILT UI COMPONENT GALLERY • THEME_SMARTLEARN",
        "title": "Extensive <span>Section Template Library</span>",
        "subtitle": "Browse a rich catalog of ready-to-use Canvas sections. Select from hero banners, instructor spotlights, category sliders, and dynamic CTA blocks.",
        "img_width": 1080,
        "img_height": 640,
        "callouts": [
            {
                "title": "📚 Rich Template Variety",
                "desc": "Choose from dozens of professionally crafted section designs and variations.",
                "pos": "top: 45px; left: 35px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "⚡ One-Click Section Addition",
                "desc": "Insert new section templates directly into your page layout with a single click.",
                "pos": "top: 45px; right: 35px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🎨 Auto-Themed Aesthetics",
                "desc": "All sections automatically adapt to your active color palette and dark/light modes.",
                "pos": "bottom: 45px; right: 90px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "8- section -live editor.png",
        "tagline": "✦ REAL-TIME WYSIWYG CUSTOMIZATION • THEME_SMARTLEARN",
        "title": "Interactive <span>Live Section Visual Editor</span>",
        "subtitle": "Customize section headings, subtitle copy, button labels, CTA links, and background images directly in an intuitive visual sidebar editor.",
        "img_width": 1400,
        "img_height": 620,
        "callouts": [
            {
                "title": "✏️ Live Content Form Fields",
                "desc": "Update headlines, badges, call-to-action buttons, and rich descriptions effortlessly.",
                "pos": "top: 40px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🖼️ Media & Icon Picker",
                "desc": "Upload custom section banners or select from modern SVG and FontAwesome icons.",
                "pos": "top: 40px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "⚡ Real-Time Instant Preview",
                "desc": "See changes rendered live before saving to your production homepage.",
                "pos": "bottom: 40px; right: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "9- section code editor.png",
        "tagline": "✦ ADVANCED DEVELOPER WORKSPACE • THEME_SMARTLEARN",
        "title": "Section <span>Mustache & Code Editor</span>",
        "subtitle": "Full code-level control for developers and designers. Edit Mustache templates, custom HTML structure, and localized styles directly from the admin panel.",
        "img_width": 1400,
        "img_height": 610,
        "callouts": [
            {
                "title": "💻 Built-In Code Editor",
                "desc": "Syntax-highlighted editor with auto-indenting for HTML, Mustache, and CSS.",
                "pos": "top: 40px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🔄 Dynamic Mustache Tags",
                "desc": "Utilize context variables like {{sitename}}, {{user_name}}, and course data tokens.",
                "pos": "top: 40px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🛡️ Safe Sandbox Execution",
                "desc": "Code edits are validated and stored safely in the database without touching core files.",
                "pos": "bottom: 40px; right: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "10-custompages.png",
        "tagline": "✦ UNLIMITED LANDING PAGES • THEME_SMARTLEARN",
        "title": "Unlimited <span>Custom Pages Manager</span>",
        "subtitle": "Create standalone marketing pages, course bundles, event portals, or organizational about pages at dedicated clean URLs like /theme/smartlearn/page.php?id=...",
        "img_width": 1400,
        "img_height": 600,
        "callouts": [
            {
                "title": "📄 Unlimited Dedicated URLs",
                "desc": "Generate clean, standalone landing pages for marketing, partnerships, or info hubs.",
                "pos": "top: 40px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🗂️ Page Status & SEO Controls",
                "desc": "Manage drafts, published states, custom slugs, and individual meta tags.",
                "pos": "top: 40px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "⚡ Lightning-Fast Routing",
                "desc": "High-performance internal routing optimized for maximum page load speeds.",
                "pos": "bottom: 40px; right: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "11- custom page edit by select sections.png",
        "tagline": "✦ BESPOKE LANDING PAGE COMPOSITION • THEME_SMARTLEARN",
        "title": "Custom Page <span>Visual Section Composer</span>",
        "subtitle": "Assemble bespoke landing pages using the same modular Smart Canvas section library. Mix and match hero headers, pricing tables, and curriculum overviews.",
        "img_width": 1400,
        "img_height": 600,
        "callouts": [
            {
                "title": "🧩 Modular Page Stacking",
                "desc": "Select and stack pre-built sections to construct high-converting custom pages.",
                "pos": "top: 40px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🎯 Targeted Landing Pages",
                "desc": "Build specific landing experiences for corporate clients, departments, or campaigns.",
                "pos": "top: 40px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🔄 Reusable Section Assets",
                "desc": "Share customized sections across both the homepage and custom pages.",
                "pos": "bottom: 40px; right: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "12- custom apge code editor.png",
        "tagline": "✦ FULL-PAGE DEVELOPER FLEXIBILITY • THEME_SMARTLEARN",
        "title": "Custom Page <span>Direct Template & Code Editor</span>",
        "subtitle": "Developer-grade IDE for complete custom page design. Inject bespoke JavaScript, custom CSS frameworks, or tailored Mustache layouts.",
        "img_width": 1020,
        "img_height": 650,
        "callouts": [
            {
                "title": "🛠️ Full Page Template Control",
                "desc": "Override complete page layouts with custom HTML/Mustache scaffolding.",
                "pos": "top: 45px; left: 35px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "💉 Scoped CSS & JS Injection",
                "desc": "Add page-specific stylesheets and interactive scripts safely.",
                "pos": "top: 45px; right: 35px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "📦 Asset Mapping & Bundling",
                "desc": "Access theme asset paths and dynamic Moodle web service helpers directly.",
                "pos": "bottom: 45px; right: 90px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "13-1- seo.png",
        "tagline": "✦ GOOGLE RICH SNIPPETS & SOCIAL SHARING • THEME_SMARTLEARN",
        "title": "Enterprise <span>SEO & Schema.org JSON-LD</span>",
        "subtitle": "Boost organic search rankings and course discovery. Automatically outputs Schema.org Course, FAQ, and Breadcrumb JSON-LD structured data alongside OpenGraph and Twitter cards.",
        "img_width": 1400,
        "img_height": 610,
        "callouts": [
            {
                "title": "🎓 Schema.org/Course JSON-LD",
                "desc": "Automatic Google Rich Snippet markup displaying course names, providers, and prices.",
                "pos": "top: 40px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "📱 Open Graph & Twitter Cards",
                "desc": "Beautiful rich preview thumbnails when sharing course links on social media.",
                "pos": "top: 40px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "❓ FAQ & Breadcrumb Markup",
                "desc": "Enhances Google SERP listings with expandable FAQ snippets and clear site hierarchy.",
                "pos": "bottom: 40px; right: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "13-2-seo.png",
        "tagline": "✦ AI AGENT & LLM DISCOVERY PROTOCOL • THEME_SMARTLEARN",
        "title": "AI Agent-Readiness <span>& LLMs.txt Feed</span>",
        "subtitle": "Future-proof your LMS for the AI era. Generates standardized /llms.txt and /llms-full.txt feeds compliant with llmstxt.org for ChatGPT Search, Claude, Perplexity, and Gemini.",
        "img_width": 1400,
        "img_height": 610,
        "callouts": [
            {
                "title": "🤖 llmstxt.org Compliance",
                "desc": "Automatically exposes clean, token-efficient Markdown feeds of your course catalog.",
                "pos": "top: 40px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🔍 AI Crawler Optimization",
                "desc": "Enables seamless indexing by ChatGPT Search, Perplexity AI, Claude, and Gemini.",
                "pos": "top: 40px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "⚙️ Dynamic Feed Regeneration",
                "desc": "Keeps course titles, summaries, and enrollment links synchronized in real time.",
                "pos": "bottom: 40px; right: 80px; border-left: 4px solid #00C853;"
            }
        ]
    }
]

def generate_html(item, img_path):
    callout_html = ""
    for c in item["callouts"]:
        callout_html += f"""
        <div class="callout" style="{c['pos']}">
          <div class="callout-title">{c['title']}</div>
          <div class="callout-desc">{c['desc']}</div>
        </div>
        """
    
    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@600;700;800&display=swap');
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1920px;
    height: 1080px;
    background: #070a12;
    background-image: radial-gradient(circle at 50% 0%, rgba(56, 189, 248, 0.22), transparent 50%),
                      radial-gradient(circle at 80% 30%, rgba(139, 92, 246, 0.18), transparent 40%),
                      radial-gradient(rgba(255, 255, 255, 0.04) 1px, transparent 1px);
    background-size: 100% 100%, 100% 100%, 32px 32px;
    font-family: 'Inter', system-ui, -apple-system, sans-serif;
    color: white;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding-top: 46px;
    position: relative;
    overflow: hidden;
  }}
  .hero-top {{
    text-align: center;
    max-width: 1100px;
    margin-bottom: 30px;
  }}
  .tagline {{
    display: inline-block;
    background: linear-gradient(135deg, rgba(56,189,248,0.2), rgba(139,92,246,0.2));
    border: 1px solid rgba(56,189,248,0.45);
    color: #38bdf8;
    padding: 7px 22px;
    border-radius: 99px;
    font-size: 13px;
    font-weight: 700;
    margin-bottom: 14px;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    box-shadow: 0 0 20px rgba(56,189,248,0.2);
  }}
  .hero-title {{
    font-family: 'Outfit', sans-serif;
    font-size: 42px;
    font-weight: 800;
    line-height: 1.15;
    margin-bottom: 12px;
    background: linear-gradient(to right, #ffffff, #e2e8f0, #94a3b8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }}
  .hero-title span {{
    background: linear-gradient(to right, #38bdf8, #818cf8, #c084fc);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }}
  .hero-sub {{
    font-size: 16.5px;
    color: #94a3b8;
    line-height: 1.5;
    font-weight: 400;
    max-width: 980px;
    margin: 0 auto;
  }}
  .showcase-wrapper {{
    position: relative;
    width: 1580px;
    height: 690px;
    display: flex;
    justify-content: center;
    align-items: center;
  }}
  .main-screenshot {{
    width: {item['img_width']}px;
    height: {item['img_height']}px;
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.22);
    box-shadow: 0 40px 90px rgba(0,0,0,0.85), 0 0 60px rgba(99,102,241,0.18);
    object-fit: cover;
    object-position: top center;
    background: #0f172a;
  }}
  .callout {{
    position: absolute;
    background: rgba(15, 23, 42, 0.95);
    backdrop-filter: blur(14px);
    border: 1px solid rgba(255, 255, 255, 0.22);
    border-radius: 16px;
    padding: 16px 20px;
    width: 300px;
    box-shadow: 0 25px 50px rgba(0,0,0,0.75), 0 0 30px rgba(139,92,246,0.25);
    z-index: 10;
  }}
  .callout-title {{
    font-size: 15px;
    font-weight: 700;
    color: #38bdf8;
    margin-bottom: 5px;
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  .callout-desc {{
    font-size: 13px;
    color: #cbd5e1;
    line-height: 1.45;
  }}
</style>
</head>
<body>
  <div class="hero-top">
    <div class="tagline">{item['tagline']}</div>
    <div class="hero-title">{item['title']}</div>
    <div class="hero-sub">{item['subtitle']}</div>
  </div>
  <div class="showcase-wrapper">
    <img class="main-screenshot" src="file://{img_path}">
    {callout_html}
  </div>
</body>
</html>
"""
    return html

def run():
    print(f"Starting showcase generation for {len(SHOWCASES)} smartlearn theme screenshots...")
    for idx, item in enumerate(SHOWCASES, 1):
        in_file = os.path.join(INPUT_DIR, item["filename"])
        out_file = os.path.join(OUTPUT_DIR, item["filename"])
        html_file = os.path.join(OUTPUT_DIR, item["filename"] + ".html")
        
        if not os.path.exists(in_file):
            print(f"[{idx}/{len(SHOWCASES)}] ERROR: Input file not found: {in_file}")
            continue
            
        print(f"[{idx}/{len(SHOWCASES)}] -> Generating HTML for: {item['filename']}")
        html_content = generate_html(item, in_file)
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(html_content)
            
        print(f"[{idx}/{len(SHOWCASES)}] -> Rendering 1920x1080 PNG via headless Chrome...")
        chrome_out = out_file if out_file.endswith(".png") else out_file + ".png"
        cmd = [
            "google-chrome",
            "--headless",
            "--disable-gpu",
            f"--screenshot={chrome_out}",
            "--window-size=1920,1080",
            "--allow-file-access-from-files",
            html_file
        ]
        subprocess.run(cmd, check=True)
        if chrome_out != out_file and os.path.exists(chrome_out):
            shutil.copyfile(chrome_out, out_file)
        if os.path.exists(out_file):
            size = os.path.getsize(out_file)
            print(f"      [OK] Saved: {out_file} ({size // 1024} KB)")
        if os.path.exists(html_file):
            os.remove(html_file)

    print("\nAll 15 SmartLearn theme showcase images generated successfully in:")
    print(f"{OUTPUT_DIR}")

if __name__ == "__main__":
    run()
