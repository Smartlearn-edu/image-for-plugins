import os
import shutil
import subprocess
from PIL import Image

INPUT_DIR = "/home/mohammad/Dev/image-for-plugins/screenshoots/airubricgenerator"
OUTPUT_DIR = "/home/mohammad/Dev/image-for-plugins/improved/airubricgenerator"
os.makedirs(OUTPUT_DIR, exist_ok=True)

ITEMS = [
    {
        "filename": "8- options.png",
        "tagline": "✦ ADVANCED AI CUSTOMIZATION • LOCAL_AIRUBRICGENERATOR",
        "title": "Granular <span>Generation Control</span>",
        "subtitle": "Tailor AI-generated assignments and rubrics with custom writing tones, learning objective inclusions, and explicit teacher instructions.",
        "img_width": 1420,
        "img_height": 580,
        "callouts": [
            {
                "title": "🎨 Writing Tone Selection",
                "desc": "Choose from Academic, Professional, Encouraging, or Strict pedagogical tones.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "✅ Structural Checkboxes",
                "desc": "Automatically include course learning objectives and submission requirements.",
                "pos": "top: 45px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "📝 Custom AI Prompts",
                "desc": "Add custom notes and pedagogical guidelines to steer the AI's generation.",
                "pos": "bottom: 40px; right: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "9- description geneertaor.png",
        "tagline": "✦ INSTANT ASSIGNMENT CREATION • LOCAL_AIRUBRICGENERATOR",
        "title": "AI Description <span>Generator Menu</span>",
        "subtitle": "Access powerful generative AI directly from any Moodle assignment menu. Generate complete, structured assignment briefs in seconds.",
        "img_width": 1420,
        "img_height": 600,
        "callouts": [
            {
                "title": "⚡ Instant Menu Access",
                "desc": "Seamlessly integrated into Moodle's native 'More' assignment navigation menu.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "✨ One-Click Description AI",
                "desc": "Generate comprehensive assignment instructions without leaving your course page.",
                "pos": "top: 45px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🎯 Unified Tool Suite",
                "desc": "Access Description AI, Rubric AI, and AI Grader settings all from one menu.",
                "pos": "bottom: 40px; right: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "10- option -1- generator mode whole course or selected sections.png",
        "tagline": "✦ CURRICULUM CONTEXT SCOPING • LOCAL_AIRUBRICGENERATOR",
        "title": "Course & Section <span>Context Scoping</span>",
        "subtitle": "Provide the AI with precise curriculum context. Choose whether to analyze the entire course or focus on specific chapters and sections.",
        "img_width": 1440,
        "img_height": 500,
        "callouts": [
            {
                "title": "🎯 Flexible Content Scope",
                "desc": "Switch effortlessly between Full Course analysis and Selected Sections.",
                "pos": "top: 40px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "📚 Section & Activity Picker",
                "desc": "Select exact chapters so AI rubrics align directly with covered materials.",
                "pos": "top: 40px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🧠 Context-Aware AI",
                "desc": "Ensures generated criteria reflect the specific difficulty of chosen topics.",
                "pos": "bottom: 35px; right: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "11- tone.png",
        "tagline": "✦ PEDAGOGICAL VOICE & STYLE • LOCAL_AIRUBRICGENERATOR",
        "title": "Pedagogical <span>Tone Selection</span>",
        "subtitle": "Match the assessment language to your teaching style. Choose Academic, Professional, Encouraging, or Strict tones for your generated rubrics.",
        "img_width": 1400,
        "img_height": 380,
        "callouts": [
            {
                "title": "🎓 Academic & Rigorous",
                "desc": "Ideal for formal research papers, university essays, and scientific evaluations.",
                "pos": "top: 35px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "💼 Professional & Practical",
                "desc": "Industry-focused tone tailored for practical exercises and vocational tasks.",
                "pos": "top: 35px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🌟 Encouraging & Supportive",
                "desc": "Growth-oriented language designed to motivate students and guide improvement.",
                "pos": "bottom: 30px; right: 60px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "12-assignment type.png",
        "tagline": "✦ SPECIALIZED ASSESSMENT TEMPLATES • LOCAL_AIRUBRICGENERATOR",
        "title": "Assignment Type <span>Templates</span>",
        "subtitle": "Select from 9 specialized pedagogical templates including Final Projects, Case Studies, Research Papers, and Practical Exercises.",
        "img_width": 1420,
        "img_height": 480,
        "callouts": [
            {
                "title": "📋 9 Pedagogical Templates",
                "desc": "Pre-configured prompt structures for essays, exams, case studies, and more.",
                "pos": "top: 40px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🎯 Purpose-Driven Criteria",
                "desc": "Automatically adapts rubric dimensions to fit the specific assignment genre.",
                "pos": "top: 40px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "⚙️ Fully Custom Option",
                "desc": "Use the Custom template option for unique or unconventional assignment formats.",
                "pos": "bottom: 35px; right: 70px; border-left: 4px solid #00C853;"
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
    print(f"Starting showcase generation for {len(ITEMS)} extra airubricgenerator screenshots...")
    for i, item in enumerate(ITEMS, 1):
        print(f"[{i}/{len(ITEMS)}] Generating: {item['filename']}")
        in_path = os.path.join(INPUT_DIR, item['filename'])
        out_path = os.path.join(OUTPUT_DIR, item['filename'])
        html_path = os.path.join(OUTPUT_DIR, f"temp_extra_{i}.html")
        
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
            
    print("\nAll 5 extra airubricgenerator showcase images generated successfully!")

if __name__ == "__main__":
    run()
