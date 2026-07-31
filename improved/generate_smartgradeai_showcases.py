import os
import shutil
import subprocess
from PIL import Image

INPUT_DIR = "/home/mohammad/Dev/image-for-plugins/screenshoots/smartgradeai"
OUTPUT_DIR = "/home/mohammad/Dev/image-for-plugins/improved/smartgradeai"
os.makedirs(OUTPUT_DIR, exist_ok=True)

ITEMS = [
    {
        "filename": "1setting-1.png",
        "tagline": "✦ UNIFIED AI ARCHITECTURE & FALLBACKS • LOCAL_SMARTGRADEAI",
        "title": "Enterprise <span>AI Provider Engine</span>",
        "subtitle": "Connect natively to Google Gemini 3.0 Pro, OpenAI GPT-4o, Claude 3.5, and local Ollama models. Features automatic fallback to Moodle Core AI during rate limits.",
        "img_width": 1360,
        "img_height": 600,
        "callouts": [
            {
                "title": "🌐 Multi-Provider Support",
                "desc": "Choose between Gemini, OpenAI, Claude, DeepSeek, Azure, Ollama, or Moodle Core AI.",
                "pos": "top: 40px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🔄 Automatic Failover Protection",
                "desc": "Automatically switches providers if API rate limits (429) or outages occur.",
                "pos": "top: 40px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🛡️ Human-in-the-Loop Toggle",
                "desc": "Enforce teacher draft review so AI never modifies official grades without explicit approval.",
                "pos": "bottom: 40px; right: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "2- student .png",
        "tagline": "✦ STUDENT ACADEMIC GROWTH • LOCAL_SMARTGRADEAI",
        "title": "Formative <span>AI Tutor Feedback</span>",
        "subtitle": "Empower students to trigger self-check evaluations on draft submissions before the final due date. Actionable tips align with your Moodle rubric without grading.",
        "img_width": 1360,
        "img_height": 600,
        "callouts": [
            {
                "title": "✨ On-Demand Rubric Check",
                "desc": "Students click 'Check AI Feedback' to get instant preliminary advice on their draft.",
                "pos": "top: 40px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "💡 Strengths & Growth Areas",
                "desc": "Provides constructive praise and highlights missing criteria based on teacher rubrics.",
                "pos": "top: 40px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🔒 Zero Gradebook Impact",
                "desc": "Formative tutor advice stays private to the student and does not alter official scores.",
                "pos": "bottom: 40px; right: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "3 teacher.png",
        "tagline": "✦ SEAMLESS ASSIGNMENT INTEGRATION • LOCAL_SMARTGRADEAI",
        "title": "One-Click <span>AI Grading Trigger</span>",
        "subtitle": "Integrates natively into Moodle's assignment grading table and summary view. Educators can trigger batch AI rubric evaluations with a single click.",
        "img_width": 1360,
        "img_height": 560,
        "callouts": [
            {
                "title": "⚡ Instant AI Evaluation Button",
                "desc": "Launch AI assessment directly from the standard Moodle assignment interface.",
                "pos": "top: 40px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "📊 Native Grading Table Sync",
                "desc": "Tracks submitted, needs-grading, and participant metrics seamlessly.",
                "pos": "top: 40px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🎯 100% Core Moodle Harmony",
                "desc": "No external popups required—works within Moodle's familiar grading workflow.",
                "pos": "bottom: 40px; right: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "4.png",
        "tagline": "✦ ASYNC BACKGROUND PROCESSING • LOCAL_SMARTGRADEAI",
        "title": "Instant <span>Grading Trigger Confirmation</span>",
        "subtitle": "Submissions are queued immediately into Moodle's resilient Adhoc Task engine. Guarantees non-blocking performance even for massive cohorts.",
        "img_width": 1050,
        "img_height": 740,
        "callouts": [
            {
                "title": "🚀 Instant Trigger Response",
                "desc": "Confirms immediately that the AI assessment task has been queued.",
                "pos": "top: 50px; left: 35px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "⚙️ Background Adhoc Tasks",
                "desc": "Uses Moodle task\\ai_grade_submission with teacher impersonation restoration.",
                "pos": "top: 50px; right: 35px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "📦 Zero Timeout Risk",
                "desc": "Handles complex PDF, DOCX, and source code document extraction in background threads.",
                "pos": "bottom: 50px; right: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "5 - grade waiting teacher review.png",
        "tagline": "✦ HUMAN-IN-THE-LOOP SAFETY • LOCAL_SMARTGRADEAI",
        "title": "Draft Status <span>Review Indicator</span>",
        "subtitle": "Submissions evaluated by AI are automatically flagged as 'Waiting teacher review' in the grading table. Ensures zero unapproved grades reach students.",
        "img_width": 1400,
        "img_height": 380,
        "callouts": [
            {
                "title": "⏳ Waiting Teacher Review Badge",
                "desc": "Clear visual status showing that AI has completed grading and is awaiting approval.",
                "pos": "top: 30px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "📋 Draft Grade Protection",
                "desc": "Scores remain in draft review state until an instructor explicitly signs off.",
                "pos": "top: 30px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🔍 Side-by-Side Verification",
                "desc": "Teachers can click into any submission to inspect rubric criteria before publishing.",
                "pos": "bottom: 25px; right: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "6 approve or not.png",
        "tagline": "✦ COMPLETE TEACHER AUTHORITY • LOCAL_SMARTGRADEAI",
        "title": "Human-in-the-Loop <span>Rubric Review</span>",
        "subtitle": "Inspect AI-proposed rubric criterion scores and detailed remarks. Teachers retain complete power to approve, reject, or adjust any score before saving.",
        "img_width": 1380,
        "img_height": 520,
        "callouts": [
            {
                "title": "📊 Criterion-by-Criterion Evaluation",
                "desc": "AI maps submission content to specific rubric achievement levels with custom remarks.",
                "pos": "top: 35px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "✅ One-Click Grade Approval",
                "desc": "Click 'Approve & Save to Gradebook' to publish scores and feedback to Moodle.",
                "pos": "top: 35px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "📝 Full Editorial Control",
                "desc": "Educators can reject drafts or override individual scores anytime.",
                "pos": "bottom: 30px; right: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "7.png",
        "tagline": "✦ GRADEBOOK SYNCHRONIZATION • LOCAL_SMARTGRADEAI",
        "title": "Approved Grade <span>Gradebook Publish</span>",
        "subtitle": "Upon approval, final rubric scores and teacher-endorsed feedback are automatically written to Moodle Gradebook with full Privacy API compliance.",
        "img_width": 1400,
        "img_height": 420,
        "callouts": [
            {
                "title": "🎉 Instant Gradebook Save",
                "desc": "Confirmation alert showing the grade has been successfully written to Moodle Gradebook.",
                "pos": "top: 30px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "✨ Empty Queue Confirmation",
                "desc": "Clear 'No pending reviews found' message when all submissions are reviewed.",
                "pos": "top: 30px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🔐 GDPR & Privacy Compliance",
                "desc": "All student data and grading logs adhere strictly to Moodle Privacy API.",
                "pos": "bottom: 25px; right: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "8grading wait task .png",
        "tagline": "✦ RESILIENT BATCH ORCHESTRATION • LOCAL_SMARTGRADEAI",
        "title": "Queued <span>Adhoc Grading Tasks</span>",
        "subtitle": "Monitor scheduled AI grading jobs directly in Moodle's task queue. Built for enterprise reliability across large enrollments and complex attachments.",
        "img_width": 1400,
        "img_height": 480,
        "callouts": [
            {
                "title": "📥 Queued Task Monitoring",
                "desc": "System administrators and teachers can track active batch grading processes.",
                "pos": "top: 35px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🔄 Automatic Retry Logic",
                "desc": "Built-in resilience automatically retries transient AI provider timeouts.",
                "pos": "top: 35px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "📄 Multi-Format Extraction",
                "desc": "Processes PDFs, Microsoft Word DOCX, source code, and plain text effortlessly.",
                "pos": "bottom: 30px; right: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "9 garding task completed.png",
        "tagline": "✦ BATCH ASSESSMENT COMPLETION • LOCAL_SMARTGRADEAI",
        "title": "Completed <span>AI Grading Task Queue</span>",
        "subtitle": "All queued student submissions are processed with criterion-level rubric feedback and draft scores, ready for immediate instructor inspection.",
        "img_width": 1400,
        "img_height": 520,
        "callouts": [
            {
                "title": "✅ 100% Task Completion",
                "desc": "All scheduled assignment submissions successfully evaluated against the rubric.",
                "pos": "top: 35px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "⚡ Massive Time Savings",
                "desc": "Reduces hours of manual rubric evaluation down to minutes of review.",
                "pos": "top: 35px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🎯 High-Confidence Scoring",
                "desc": "Delivers consistent, unbiased criterion scoring across the entire cohort.",
                "pos": "bottom: 30px; right: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "access to pending ai review.png",
        "tagline": "✦ DEDICATED TEACHER PORTAL • LOCAL_SMARTGRADEAI",
        "title": "Pending AI Reviews <span>Dashboard Hub</span>",
        "subtitle": "Access all draft reviews across your courses from a single centralized dashboard (reviews.php). Streamline your grading queue with intuitive filters.",
        "img_width": 1100,
        "img_height": 660,
        "callouts": [
            {
                "title": "🎯 Centralized Review Hub",
                "desc": "One-click access to view every submission waiting for teacher sign-off.",
                "pos": "top: 45px; left: 35px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🔍 Side-by-Side Document View",
                "desc": "Preview student files right next to AI rubric evaluations.",
                "pos": "top: 45px; right: 35px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "⚡ Quick Batch Actions",
                "desc": "Filter by assignment, course, or student to clear grading queues fast.",
                "pos": "bottom: 45px; right: 80px; border-left: 4px solid #00C853;"
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
    padding-top: 48px;
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
    print(f"Starting showcase generation for {len(ITEMS)} smartgradeai screenshots...")
    for i, item in enumerate(ITEMS, 1):
        print(f"[{i}/{len(ITEMS)}] Generating: {item['filename']}")
        in_path = os.path.join(INPUT_DIR, item['filename'])
        out_path = os.path.join(OUTPUT_DIR, item['filename'])
        html_path = os.path.join(OUTPUT_DIR, f"temp_{i}.html")
        
        html_content = generate_html(item, in_path)
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)
            
        chrome_out = out_path if out_path.endswith(".png") else out_path + ".png"
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
        if chrome_out != out_path and os.path.exists(chrome_out):
            shutil.copyfile(chrome_out, out_path)
        if os.path.exists(out_path):
            size = os.path.getsize(out_path)
            print(f"    [OK] Saved {item['filename']} ({size // 1024} KB)")
        if os.path.exists(html_path):
            os.remove(html_path)
            
    print("\nAll 10 smartgradeai showcase images generated successfully!")

if __name__ == "__main__":
    run()
