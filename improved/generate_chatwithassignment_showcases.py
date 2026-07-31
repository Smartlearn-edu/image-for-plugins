import os
import subprocess
from PIL import Image

INPUT_DIR = "/home/mohammad/Dev/image-for-plugins/screenshoots/chatwithassignment"
OUTPUT_DIR = "/home/mohammad/Dev/image-for-plugins/improved/chatwithassignment"
os.makedirs(OUTPUT_DIR, exist_ok=True)

SHOWCASES = [
    {
        "filename": "1- assignment with chat with ai .png",
        "tagline": "✦ CHAT WITH ASSIGNMENT AI • LOCAL_CHATWITHASSIGNMENT",
        "title": "Seamless <span>Assignment & Gradebook Integration</span>",
        "subtitle": "Transform assignment feedback from a one-way dead end into an interactive AI learning conversation. Integrates directly into Moodle's native assignment submission view.",
        "img_width": 1380,
        "img_height": 620,
        "callouts": [
            {
                "title": "💬 Ask AI About My Grade Button",
                "desc": "Prominently displayed on graded assignments so students can initiate dialogue immediately.",
                "pos": "top: 40px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "📊 Graded Submission Context",
                "desc": "Automatically links to the student's submission status, rubric scores, and online text.",
                "pos": "top: 140px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🎯 Zero Office-Hour Bottlenecks",
                "desc": "Provides instant 24/7 clarification on rubric scores and teacher comments.",
                "pos": "bottom: 40px; right: 80px; border-left: 4px solid #c084fc;"
            }
        ]
    },
    {
        "filename": "2 start.png",
        "tagline": "✦ SOCRATIC TUTORING DIALOGUE",
        "title": "Interactive <span>Grade & Rubric Discussion</span>",
        "subtitle": "Instead of passively reading feedback, students enter an active, Socratic dialogue about their submission. The AI tutor answers questions using exact grading criteria and points scored.",
        "img_width": 1150,
        "img_height": 600,
        "callouts": [
            {
                "title": "🤖 Rubric-Grounded Reasoning",
                "desc": "Explains exact criterion deductions and teacher comments from mod_assign.",
                "pos": "top: 50px; left: 35px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "💬 Conversational Clarification",
                "desc": "Students can ask follow-up questions like 'Why did I lose points?' or 'How can I improve?'",
                "pos": "top: 160px; right: 35px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🎓 Supportive Pedagogical Coach",
                "desc": "Guides student reflection without giving away answers or rewriting assignments.",
                "pos": "bottom: 50px; left: 90px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "chat 1.png",
        "tagline": "✦ PRECISION RUBRIC BREAKDOWN",
        "title": "Rubric-Aware <span>Reasoning & Prompts</span>",
        "subtitle": "Pre-configured Socratic prompt buttons encourage active reflection. The tutor helps students understand exactly why points were deducted and how to achieve full marks on future submissions.",
        "img_width": 1380,
        "img_height": 600,
        "callouts": [
            {
                "title": "⚡ Quick-Action Socratic Buttons",
                "desc": "Pre-configured prompt buttons ('Explain my rubric scores', 'How can I improve?', 'Review teacher feedback').",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🔍 Granular Score Explanation",
                "desc": "Breaks down criterion-by-criterion performance with transparent pedagogical feedback.",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🎯 Actionable Next Steps",
                "desc": "Provides tailored recommendations to help students master future assignments.",
                "pos": "bottom: 45px; right: 80px; border-left: 4px solid #c084fc;"
            }
        ]
    },
    {
        "filename": "chat 2.png",
        "tagline": "✦ DEEP SUBMISSION ANALYSIS",
        "title": "Deep Critique <span>& Learning Guidance</span>",
        "subtitle": "Engage in multi-turn discussions where the AI analyzes student submissions against course learning objectives, offering constructive guidance that deepens comprehension.",
        "img_width": 1380,
        "img_height": 600,
        "callouts": [
            {
                "title": "📚 Personalized Learning Conversation",
                "desc": "Turns static gradebook entries into an interactive tutoring session tailored to the student.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "💡 Concrete Improvement Examples",
                "desc": "Offers illustrative examples of how to strengthen arguments, structure, or evidence.",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "⚡ 24/7 Academic Support",
                "desc": "Empowers students to resolve confusion instantly, improving retention and learning outcomes.",
                "pos": "bottom: 45px; left: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "setting -13.png",
        "tagline": "✦ 5-LEVEL INTELLIGENT CONTEXT ENGINE",
        "title": "Granular <span>Context Level Control</span>",
        "subtitle": "Administrators and teachers can choose from 5 levels of context sharing (None, Minimal, Summary, Standard, Full) to determine exactly how much submission data is shared with the LLM per assignment.",
        "img_width": 1380,
        "img_height": 580,
        "callouts": [
            {
                "title": "🎛️ 5-Level Context Hierarchy",
                "desc": "Configure Level 1 (None) through Level 5 (Full Online Text) to balance depth and privacy.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "💸 First-Message Context Injection",
                "desc": "Sends heavy rubric and assignment context only on the initial turn, reducing token usage by up to 70%.",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🔒 Privacy & Budget Guardrails",
                "desc": "Prevent unnecessary data sharing while tailoring context depth to specific course needs.",
                "pos": "bottom: 45px; right: 80px; border-left: 4px solid #c084fc;"
            }
        ]
    },
    {
        "filename": "4 setting 2.png",
        "tagline": "✦ COST-EFFECTIVE AI PROVIDER ROUTING",
        "title": "AI Hub BYOK <span>& Fallback Policies</span>",
        "subtitle": "Maintain complete budgetary control. Connects with local_aihub so students can use their own API keys or allocated token balances, with granular administrative fallback policies.",
        "img_width": 1380,
        "img_height": 560,
        "callouts": [
            {
                "title": "🔑 Student-Funded Usage (BYOK)",
                "desc": "Integrates with local_aihub so students can power tutoring using personal API keys or tokens.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🛡️ Granular Fallback Policies",
                "desc": "Choose Strict Mode, Capability-Based Fallback, or Enabled for All for institutional Core AI routing.",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "⚙️ Complete Admin Visibility",
                "desc": "Track real-time token spend, latency, and model configuration across your Moodle site.",
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
    print(f"Starting showcase generation for {len(SHOWCASES)} chatwithassignment screenshots...")
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

    print("\nAll 6 chatwithassignment showcase images generated successfully!")

if __name__ == "__main__":
    run()
