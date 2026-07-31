import os
import shutil
import subprocess
from PIL import Image

INPUT_DIR = "/home/mohammad/Dev/image-for-plugins/screenshoots/cataloge"
OUTPUT_DIR_PRIMARY = "/home/mohammad/Dev/image-for-plugins/cataloge"
OUTPUT_DIR_SECONDARY = "/home/mohammad/Dev/image-for-plugins/improved/cataloge"
os.makedirs(OUTPUT_DIR_PRIMARY, exist_ok=True)
os.makedirs(OUTPUT_DIR_SECONDARY, exist_ok=True)

ITEMS = [
    {
        "filename": "1.png",
        "tagline": "✦ MODERN E-COMMERCE COURSE MARKETPLACE • LOCAL_SMARTCATALOG",
        "title": "Interactive <span>Storefront Catalog</span>",
        "subtitle": "Transform Moodle's course list into an attractive eCommerce storefront. Features real-time keyword search, instructor filtering, and responsive grid layouts.",
        "img_width": 1420,
        "img_height": 620,
        "callouts": [
            {
                "title": "⚡ Instant Course Search",
                "desc": "Filter courses in real-time by keyword, instructor name, and custom sort criteria.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🎯 Extended Search Mode",
                "desc": "Deep search through course titles, descriptions, and custom tags simultaneously.",
                "pos": "top: 45px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🎨 Clean Grid Marketplace",
                "desc": "Presents courses in a visually stunning card grid with instant category switching.",
                "pos": "bottom: 40px; right: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "by teacher.png",
        "tagline": "✦ INSTRUCTOR DIRECTORY & NAVIGATION • LOCAL_SMARTCATALOG",
        "title": "Browse by <span>Teacher Directory</span>",
        "subtitle": "Empower students to discover courses grouped by their favorite instructors. Showcases faculty profiles, course portfolios, and teaching expertise.",
        "img_width": 1420,
        "img_height": 620,
        "callouts": [
            {
                "title": "👨‍🏫 Faculty & Instructor Hub",
                "desc": "Dedicated view grouping educational offerings by individual course creators.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "📋 Clean Faculty Listings",
                "desc": "Students can easily filter and browse courses taught by specific mentors.",
                "pos": "top: 45px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🔄 Seamless Mode Switching",
                "desc": "One-click toggle between Course catalog, Program pathways, and Teacher directory.",
                "pos": "bottom: 40px; right: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "course quizck info.png",
        "tagline": "✦ INTERACTIVE COURSE PREVIEWS • LOCAL_SMARTCATALOG",
        "title": "Quick Info <span>Preview Popover</span>",
        "subtitle": "Give prospective students an instant sneak peek into course details without leaving the catalog page. Displays learning outcomes, activity counts, and enrollment stats.",
        "img_width": 780,
        "img_height": 650,
        "callouts": [
            {
                "title": "💡 'What You'll Learn' Outcomes",
                "desc": "Highlights key skills and competencies covered in the course curriculum.",
                "pos": "top: 45px; left: 60px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "📊 Instant Enrollment Stats",
                "desc": "Shows live student enrollment counts, activity totals, and last-updated timestamps.",
                "pos": "top: 45px; right: 60px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🚀 One-Click Enrollment Jump",
                "desc": "Direct 'View Course' button launches students into their learning journey immediately.",
                "pos": "bottom: 45px; right: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "filter.png",
        "tagline": "✦ GRANULAR SIDEBAR FILTERING • LOCAL_SMARTCATALOG",
        "title": "Dynamic <span>Sidebar Filter Engine</span>",
        "subtitle": "Help learners find their exact course match using faceted filters. Filter by category, subject, difficulty level, certificate availability, and custom Moodle fields.",
        "img_width": 1420,
        "img_height": 620,
        "callouts": [
            {
                "title": "🎛️ Multi-Faceted Filter Sidebar",
                "desc": "Refine course listings instantly by difficulty Level, Category, or Certificate status.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🏷️ Custom Field Filter Support",
                "desc": "Administrators can enable custom Moodle dropdown or checkbox fields as filters.",
                "pos": "top: 45px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "⚡ Real-Time Query Updating",
                "desc": "Course cards refresh immediately as users check and uncheck sidebar options.",
                "pos": "bottom: 40px; right: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "program.png",
        "tagline": "✦ CURRICULUM & LEARNING PATHWAYS • LOCAL_SMARTCATALOG",
        "title": "Structured <span>Program Discovery</span>",
        "subtitle": "Showcase multi-course programs, degree tracks, and professional certificates in a clean, unified view. Guides students through structured learning roadmaps.",
        "img_width": 1420,
        "img_height": 600,
        "callouts": [
            {
                "title": "🎓 Unified Program Pathways",
                "desc": "Group individual courses into cohesive programs and professional certificates.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🗺️ Structured Learning Roadmaps",
                "desc": "Provides students with a clear progression path across multiple milestones.",
                "pos": "top: 45px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "✨ Premium Storefront Aesthetics",
                "desc": "Consistent eCommerce design language across Courses, Programs, and Teachers.",
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
    padding-top: 50px;
    position: relative;
    overflow: hidden;
  }}
  .hero-top {{
    text-align: center;
    max-width: 1050px;
    margin-bottom: 30px;
  }}
  .tagline {{
    display: inline-block;
    background: linear-gradient(135deg, rgba(56,189,248,0.2), rgba(139,92,246,0.2));
    border: 1px solid rgba(56,189,248,0.45);
    color: #38bdf8;
    padding: 7px 20px;
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
    font-size: 44px;
    font-weight: 800;
    line-height: 1.15;
    margin-bottom: 14px;
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
    font-size: 17px;
    color: #94a3b8;
    line-height: 1.55;
    font-weight: 400;
  }}
  .showcase-wrapper {{
    position: relative;
    width: 1560px;
    height: 680px;
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
    width: 290px;
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
    print(f"Starting showcase generation for {len(ITEMS)} cataloge screenshots...")
    for i, item in enumerate(ITEMS, 1):
        print(f"[{i}/{len(ITEMS)}] Generating: {item['filename']}")
        in_path = os.path.join(INPUT_DIR, item['filename'])
        out_path_1 = os.path.join(OUTPUT_DIR_PRIMARY, item['filename'])
        out_path_2 = os.path.join(OUTPUT_DIR_SECONDARY, item['filename'])
        html_path = os.path.join(OUTPUT_DIR_PRIMARY, f"temp_{i}.html")
        
        html_content = generate_html(item, in_path)
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)
            
        chrome_out = out_path_1 if out_path_1.endswith(".png") else out_path_1 + ".png"
        cmd = [
            "google-chrome",
            "--headless",
            "--disable-gpu",
            f"--screenshot={chrome_out}",
            "--window-size=1920,1080",
            "--allow-file-access-from-files",
            html_path
        ]
        subprocess.run(cmd, check=True)
        if chrome_out != out_path_1 and os.path.exists(chrome_out):
            shutil.copyfile(chrome_out, out_path_1)
        if os.path.exists(out_path_1):
            shutil.copyfile(out_path_1, out_path_2)
            size = os.path.getsize(out_path_1)
            print(f"    [OK] Saved {item['filename']} ({size // 1024} KB)")
        if os.path.exists(html_path):
            os.remove(html_path)
            
    print("\nAll 5 cataloge showcase images generated successfully!")

if __name__ == "__main__":
    run()
