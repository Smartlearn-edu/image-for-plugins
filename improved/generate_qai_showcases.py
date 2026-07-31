import os
import shutil
import subprocess
from PIL import Image

INPUT_DIR = "/home/mohammad/Dev/image-for-plugins/screenshoots/qai"
OUTPUT_DIR = "/home/mohammad/Dev/image-for-plugins/improved/qai"
os.makedirs(OUTPUT_DIR, exist_ok=True)

SHOWCASES = [
    {
        "filename": "0 - startchat with quiz .png",
        "tagline": "✦ MOODLE QUIZ AI CHAT • LOCAL_QAI",
        "title": "Seamless <span>Quiz Review Integration</span>",
        "subtitle": "Empower students with context-aware, on-demand AI quiz tutoring while mastering token economics. Integrates Moodle's native AI Subsystem directly into quiz attempt reviews.",
        "img_width": 1380,
        "img_height": 600,
        "callouts": [
            {
                "title": "💬 Ask AI about Quiz Button",
                "desc": "Offers an interactive button on the quiz review summary for holistic performance discussions.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "📊 Attempt & Gradebook Sync",
                "desc": "Automatically connects to the student's marks, duration, and individual question statuses.",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🚀 Zero Navigation Breakage",
                "desc": "Students initiate dialogue directly from their finished quiz review page.",
                "pos": "bottom: 45px; right: 80px; border-left: 4px solid #c084fc;"
            }
        ]
    },
    {
        "filename": "1  chat with question.png",
        "tagline": "✦ PER-QUESTION SOCRATIC AI TUTOR",
        "title": "Interactive <span>Per-Question Guidance</span>",
        "subtitle": "Students reviewing their attempts see an Ask AI to Explain button attached natively to each quiz question. The tutor explains underlying concepts without simply revealing answers.",
        "img_width": 1150,
        "img_height": 620,
        "callouts": [
            {
                "title": "🎯 Per-Question AI Tutoring (askai)",
                "desc": "Attaches an interactive Ask AI to Explain button directly to individual quiz questions.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🤖 Socratic Tutoring Mode",
                "desc": "Explains concepts and reasoning step-by-step, encouraging deeper critical thinking.",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "💡 Actionable Conceptual Hints",
                "desc": "Helps students understand why their answer was incorrect and how to master the topic.",
                "pos": "bottom: 45px; left: 60px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "2 chat with quiz",
        "tagline": "✦ HOLISTIC PERFORMANCE TUTORING",
        "title": "Quiz-Level <span>Performance Discussion</span>",
        "subtitle": "Discuss overall quiz performance, score breakdowns, and study strategies in an interactive modal. Helps students identify broader learning gaps across the entire quiz.",
        "img_width": 1380,
        "img_height": 600,
        "callouts": [
            {
                "title": "📈 Holistic Score & Attempt Analysis",
                "desc": "Reviews the student's complete score across all quiz questions and topics.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "💬 Conversational Study Guidance",
                "desc": "Students can ask follow-up questions like 'What should I focus on next?' or 'Why did I miss question 5?'",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "⚡ Instant Glassmorphism Modal",
                "desc": "Opens immediately without navigating away from the review screen.",
                "pos": "bottom: 45px; left: 80px; border-left: 4px solid #c084fc;"
            }
        ]
    },
    {
        "filename": "3-setting 1.png",
        "tagline": "✦ 5 GRANULAR CONTEXT LEVELS",
        "title": "Granular <span>AI Context Control</span>",
        "subtitle": "Teachers choose exactly how much data (questions, choices, answers, feedback, scores) is transmitted to the LLM to optimize helpfulness and token usage.",
        "img_width": 1380,
        "img_height": 620,
        "callouts": [
            {
                "title": "🎛️ 5 Context Level Hierarchy",
                "desc": "Configure Level 1 (Free chat) through Level 5 (Full Detail with Choices & Feedback).",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "💸 Token Efficiency Optimization",
                "desc": "Send first only setting transmits question context on initial prompt only, saving up to 70% tokens.",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🛡️ Complete Pedagogical Guardrails",
                "desc": "Prevent answers from being revealed prematurely while maximizing instructional depth.",
                "pos": "bottom: 45px; right: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "4-setting 2.png",
        "tagline": "✦ FAIR BYOK TOKEN ARCHITECTURE",
        "title": "BYOK Token Hub <span>& Fallback Engine</span>",
        "subtitle": "Eliminate unpredictable AI bills with a Fair Bring-Your-Own-Token (BYOK) architecture. Natively prioritizes student tokens via local_aihub with customizable institutional fallback.",
        "img_width": 1380,
        "img_height": 640,
        "callouts": [
            {
                "title": "🔑 BYOK AI Hub Integration",
                "desc": "Works natively with local_aihub so students can plug in their own personal API keys or allocated tokens.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🛡️ 3-Tier Fallback Provider Engine",
                "desc": "Choose Strict Mode (AI Hub only), Capability-Based, or Enabled for All for institutional Core AI routing.",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🔒 100% GDPR & Privacy Compliant",
                "desc": "Fully integrates with Moodle's Privacy API for complete personal chat history export and erasure.",
                "pos": "bottom: 45px; right: 80px; border-left: 4px solid #c084fc;"
            }
        ]
    },
    {
        "filename": "5-setting 3.png",
        "tagline": "✦ ACCESS MANAGER & PEDAGOGICAL PROMPTS",
        "title": "Access Manager <span>& Custom Prompts</span>",
        "subtitle": "Dedicated administrative interface (manage_users.php) to search users and grant explicit fallback permissions, plus custom teacher prompts to guide tutoring tone.",
        "img_width": 1380,
        "img_height": 620,
        "callouts": [
            {
                "title": "👥 Built-in Access Manager UI",
                "desc": "Dedicated interface to search users and grant explicit fallback permissions (local/qai:usecoreai).",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "✍️ Custom Pedagogical Prompts",
                "desc": "Teachers can define custom Question Prompts and Quiz Prompts to guide tone and style.",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "📦 Backup & Restore Ready",
                "desc": "Custom AI settings for each quiz are preserved automatically during Moodle course backups.",
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
    print(f"Starting showcase generation for {len(SHOWCASES)} qai screenshots...")
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

    print("\nAll 6 qai showcase images generated successfully!")

if __name__ == "__main__":
    run()
