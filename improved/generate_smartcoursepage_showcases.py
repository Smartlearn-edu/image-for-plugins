import os
import shutil
import subprocess
from PIL import Image

INPUT_DIR = "/home/mohammad/Dev/image-for-plugins/screenshoots/smartcoursepage"
OUTPUT_DIR = "/home/mohammad/Dev/image-for-plugins/improved/smartcoursepage"
os.makedirs(OUTPUT_DIR, exist_ok=True)

SHOWCASES = [
    {
        "filename": "0- banner.png",
        "tagline": "✦ SMART COURSE LANDING PAGE • LOCAL_SMARTCOURSEPAGE",
        "title": "Modern <span>eCommerce Hero Header</span>",
        "subtitle": "Transform standard Moodle enrollment pages into a high-converting, modern course landing page. Renders automatically at /enrol/index.php with rich badges, live ratings, and instructor metadata.",
        "img_width": 1380,
        "img_height": 600,
        "callouts": [
            {
                "title": "🏷️ Dynamic Course Badges & Info",
                "desc": "Displays custom course badges (e.g. 'New'), title, subtitle, student count, and last updated date.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "⭐ Live Star Rating Integration",
                "desc": "Pulls aggregated star ratings and student reviews directly into the header banner.",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "📺 Sticky Video Enrollment Sidebar",
                "desc": "Features an embedded preview video, Enrol Now CTA, and structured course metadata.",
                "pos": "bottom: 45px; right: 80px; border-left: 4px solid #c084fc;"
            }
        ]
    },
    {
        "filename": "1- coursr statistics .png",
        "tagline": "✦ REAL-TIME COURSE ANALYTICS",
        "title": "Interactive <span>Activity Distribution</span>",
        "subtitle": "Provide prospective students with transparent course composition before enrolling. Displays clean visual charts summarizing the exact mix of videos, quizzes, books, and assignments.",
        "img_width": 1380,
        "img_height": 640,
        "callouts": [
            {
                "title": "📊 Donut & Bar Distribution Charts",
                "desc": "Visualizes the balance of course activities (Pages, Quizzes, Interactive Videos, Assignments).",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "📦 Sticky 'Course Includes' Summary",
                "desc": "Sidebar itemizes total counts for every activity type included in the curriculum.",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "⚙️ Custom Field Data Mapping",
                "desc": "Seamlessly maps course custom fields (Level, Length, Effort, Delivery Mode) without code edits.",
                "pos": "bottom: 45px; left: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "2- course info - what will student learn.png",
        "tagline": "✦ CONVERSION-OPTIMIZED OVERVIEW",
        "title": "Structured <span>Course Curriculum Specs</span>",
        "subtitle": "Showcase clear learning outcomes, requirements, and subject tags to boost student enrollment confidence. Formatted cleanly inside an intuitive multi-tab navigation interface.",
        "img_width": 1380,
        "img_height": 640,
        "callouts": [
            {
                "title": "🎯 What You'll Learn & Outcomes",
                "desc": "Highlights core competencies and key takeaways mapped from course custom fields.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "📋 Prerequisites & Requirements",
                "desc": "Clearly states entry requirements so students know if they are prepared to start.",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🏷️ Subjects Covered Taxonomy",
                "desc": "Displays interactive subject badges and tags for easy catalog scanning.",
                "pos": "bottom: 45px; right: 80px; border-left: 4px solid #c084fc;"
            }
        ]
    },
    {
        "filename": "3- list course content 0without access - just show sections and activities names.png",
        "tagline": "✦ TRANSPARENT SYLLABUS PREVIEW",
        "title": "Unenrolled <span>Course Content Preview</span>",
        "subtitle": "Allow prospective students to inspect the full course structure, section titles, and activity names without granting access to protected course materials.",
        "img_width": 1380,
        "img_height": 640,
        "callouts": [
            {
                "title": "📑 Expandable Section Accordions",
                "desc": "Displays all course sections with accurate activity counts ('10 sections • 35 activities').",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🔒 Content Protection Guardrails",
                "desc": "Showcases the syllabus structure while keeping actual activity content securely locked.",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "📅 Optional Live Booking Sub-Section",
                "desc": "Includes a dedicated Booking tab for scheduled sessions, seat availability, and dates.",
                "pos": "bottom: 45px; right: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "5 - about instructor.png",
        "tagline": "✦ INSTRUCTOR CREDENTIALS & TRUST",
        "title": "Dedicated <span>Instructor Profiles</span>",
        "subtitle": "Build authority and student trust by highlighting instructor biographies, qualifications, and teaching backgrounds directly on the course landing page.",
        "img_width": 1380,
        "img_height": 640,
        "callouts": [
            {
                "title": "👨‍🏫 Rich Instructor Bio & Avatar",
                "desc": "Displays the course teacher's name, profile picture, and detailed professional summary.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🌟 Authority & Social Proof",
                "desc": "Helps students connect with their instructors before making an enrollment decision.",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🔗 Seamless Multi-Tab Navigation",
                "desc": "Students switch between Overview, Content, Certificate, Instructors, and Reviews instantly.",
                "pos": "bottom: 45px; right: 80px; border-left: 4px solid #c084fc;"
            }
        ]
    },
    {
        "filename": "6 course review.png",
        "tagline": "✦ STUDENT REVIEWS & SOCIAL PROOF",
        "title": "Authentic <span>Student Rating Reviews</span>",
        "subtitle": "Showcase verified student feedback and rating breakdowns to maximize course conversions. Displays overall score badges along with detailed individual review commentary.",
        "img_width": 1380,
        "img_height": 640,
        "callouts": [
            {
                "title": "⭐ Aggregated Score Breakdowns",
                "desc": "Displays total review count and star rating score prominently (e.g. '5.0 out of 5').",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "💬 Verified Student Testimonials",
                "desc": "Renders clean HTML student reviews mapped directly from custom course fields.",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🛡️ 100% Native Moodle Integration",
                "desc": "No third-party SaaS subscriptions required—all reviews and data stay within your Moodle DB.",
                "pos": "bottom: 45px; right: 80px; border-left: 4px solid #00C853;"
            }
        ]
    }
]

def generate_html(item, img_path):
    callout_html = ""
    for i, c in enumerate(item["callouts"], 1):
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
    margin-bottom: 34px;
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
    margin-bottom: 16px;
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
    print(f"Starting showcase generation for {len(SHOWCASES)} smartcoursepage screenshots...")
    for item in SHOWCASES:
        in_file = os.path.join(INPUT_DIR, item["filename"])
        out_file = os.path.join(OUTPUT_DIR, item["filename"])
        html_file = os.path.join(OUTPUT_DIR, item["filename"] + ".html")
        
        if not os.path.exists(in_file):
            print(f"ERROR: Input file not found: {in_file}")
            continue
            
        print(f" -> Generating HTML for: {item['filename']}")
        html_content = generate_html(item, in_file)
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(html_content)
            
        print(f" -> Running headless Chrome to render PNG: {item['filename']}")
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
            print(f"    [OK] Saved {item['filename']} ({size // 1024} KB)")
        if os.path.exists(html_file):
            os.remove(html_file)

    print("\nAll 6 smartcoursepage showcase images generated successfully!")

if __name__ == "__main__":
    run()
