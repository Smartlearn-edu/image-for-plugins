import os
import subprocess
from PIL import Image

INPUT_DIR = "/home/mohammad/Dev/image-for-plugins/screenshoots/gapcloser"
OUTPUT_DIR = "/home/mohammad/Dev/image-for-plugins/improved/gapcloser"
os.makedirs(OUTPUT_DIR, exist_ok=True)

SHOWCASES = [
    {
        "filename": "1start.png",
        "tagline": "✦ AUTOMATIC KNOWLEDGE GAP DETECTION • MOD_GAPCLOSER",
        "title": "Automatic <span>Course-Wide Gap Detection</span>",
        "subtitle": "Transform past quiz mistakes into an interactive remedial review session. Automatically scans all visible quizzes in a course and aggregates incorrectly answered questions into a focused practice activity.",
        "img_width": 1380,
        "img_height": 560,
        "callouts": [
            {
                "title": "🔍 Whole-Course Quiz Aggregation",
                "desc": "Scans every visible quiz across the course for questions answered incorrectly (fraction < 1.0).",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "📊 Real-Time Question Pool",
                "desc": "Displays exactly how many unmastered questions were found ('13 question(s) found to review').",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🚀 One-Click Remedial Launch",
                "desc": "Students can start a targeted review session immediately without manual question hunting.",
                "pos": "bottom: 45px; right: 80px; border-left: 4px solid #c084fc;"
            }
        ]
    },
    {
        "filename": "2 gap closer quiz.png",
        "tagline": "✦ INTERACTIVE REMEDIAL REVIEW SESSION",
        "title": "Interactive <span>Remedial Practice Quiz</span>",
        "subtitle": "Powered by Moodle's native Question Engine with interactive behaviour. Students answer previously missed questions and receive immediate hints and feedback on every attempt.",
        "img_width": 1380,
        "img_height": 600,
        "callouts": [
            {
                "title": "🎯 Native Question Engine Integration",
                "desc": "Uses core Moodle Question Engine (interactive mode) for instant feedback and scoring.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🧩 Dynamic Quiz Navigation",
                "desc": "Clear visual status for each question (~ partially correct, x incorrect, ✓ mastered).",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "💡 Immediate Formative Feedback",
                "desc": "Students learn from their mistakes in real-time with step-by-step guidance.",
                "pos": "bottom: 45px; left: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "3results and ateempts and review.png",
        "tagline": "✦ FORMATIVE ANALYTICS & RESTARTABILITY",
        "title": "Remedial Session <span>History & Restart</span>",
        "subtitle": "Sessions are automatically saved so students can pause and resume at any time. A single click on Restart clears the current session and re-scans the course for fresh gaps after completing new quizzes.",
        "img_width": 1380,
        "img_height": 600,
        "callouts": [
            {
                "title": "🔄 One-Click Course Re-Scanning",
                "desc": "Clicking Restart clears completed questions and scans for newly missed items in recent quizzes.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "📈 Complete Attempt Tracking",
                "desc": "Stores remedial session history in mdl_gapcloser_attempts linked to core question_usages.",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🛡️ Zero Gradebook Overhead",
                "desc": "Designed purely for adaptive learning with zero gradebook entries or grading stress.",
                "pos": "bottom: 45px; right: 80px; border-left: 4px solid #c084fc;"
            }
        ]
    },
    {
        "filename": "setting.png",
        "tagline": "✦ SMART FILTERING & ZERO OVERHEAD",
        "title": "Smart Filtering <span>& Activity Configuration</span>",
        "subtitle": "Effortless setup for instructors with zero question bank duplication. Features an intelligent filtering engine that automatically respects course visibility and ignores deleted quiz questions.",
        "img_width": 1380,
        "img_height": 560,
        "callouts": [
            {
                "title": "🧹 Smart Structure-Aware Filtering",
                "desc": "Automatically excludes hidden quizzes, hidden question bank items, and deleted quiz questions.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "⚡ Zero Quiz Bank Duplication",
                "desc": "Questions remain dynamically synchronized with your existing course quizzes and question bank.",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🔒 Moodle 4.0+ Compatible",
                "desc": "Built cleanly on modern Moodle question_references and question_versions APIs.",
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
    print(f"Starting showcase generation for {len(SHOWCASES)} gapcloser screenshots...")
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
            import shutil
            shutil.copyfile(chrome_out, out_file)
        if os.path.exists(out_file):
            size = os.path.getsize(out_file)
            print(f"    [OK] Saved {item['filename']} ({size // 1024} KB)")
        if os.path.exists(html_file):
            os.remove(html_file)

    print("\nAll 4 gapcloser showcase images generated successfully!")

if __name__ == "__main__":
    run()
