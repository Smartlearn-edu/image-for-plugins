import os
import subprocess
from PIL import Image

INPUT_DIR = "/home/mohammad/Dev/image-for-plugins/screenshoots/airubricgenerator"
OUTPUT_DIR = "/home/mohammad/Dev/image-for-plugins/improved/airubricgenerator"
os.makedirs(OUTPUT_DIR, exist_ok=True)

SHOWCASES = [
    {
        "filename": "1 start.png",
        "tagline": "✦ AI RUBRIC GENERATOR FOR MOODLE • LOCAL_RUBRICGENERATOR",
        "title": "Seamless <span>Moodle Assignment Entry Point</span>",
        "subtitle": "Create production-ready, multi-level grading rubrics directly inside any Moodle assignment in seconds. Fully integrated into Moodle's native Advanced Grading navigation.",
        "img_width": 1380,
        "img_height": 600,
        "callouts": [
            {
                "title": "⚡ One-Click Access",
                "desc": "Launch the AI Rubric Generator directly from the Assignment More dropdown menu or Advanced Grading tab.",
                "pos": "top: 40px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🤖 Core AI Powered",
                "desc": "Natively built on Moodle 4.5+ Core AI subsystem without external database bloat.",
                "pos": "top: 140px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🎯 Direct Form Integration",
                "desc": "Seamlessly replaces manual rubric creation with intelligent, course-aware automation.",
                "pos": "bottom: 40px; right: 80px; border-left: 4px solid #c084fc;"
            }
        ]
    },
    {
        "filename": "2 options-1.png",
        "tagline": "✦ PEDAGOGICAL FRAMEWORK ALIGNMENT",
        "title": "Generation Parameters — <span>Criteria & Taxonomies</span>",
        "subtitle": "Aligned with established pedagogical taxonomies (Bloom's Taxonomy, SOLO Taxonomy, and Constructive Alignment), the generator structures evaluation criteria across rigorous academic levels.",
        "img_width": 1380,
        "img_height": 560,
        "callouts": [
            {
                "title": "🔢 Custom Criterion & Level Counts",
                "desc": "Specify the exact number of evaluation criteria (4-8) and achievement levels (3-5) for your assignment.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🎓 Pedagogical Frameworks",
                "desc": "Choose between Bloom's Taxonomy, SOLO Taxonomy, Constructive Alignment, or General evaluation.",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "📚 Course-Aware Context",
                "desc": "Automatically tailors rubric criteria to match your specific assignment prompt and course learning objectives.",
                "pos": "bottom: 45px; left: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "3-options -2.png",
        "tagline": "✦ TONE & CUSTOM PROMPTING",
        "title": "Generation Parameters — <span>Tone & Custom Instructions</span>",
        "subtitle": "Fine-tune the AI's grading language and focus. Select your preferred tone (Academic, Professional, Encouraging, Direct) and provide custom natural language instructions.",
        "img_width": 1150,
        "img_height": 620,
        "callouts": [
            {
                "title": "🎭 Professional Tone Selection",
                "desc": "Set the grading language to Academic, Professional, Encouraging, or Direct to match institutional standards.",
                "pos": "top: 50px; left: 40px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "💬 Custom Prompt Instructions",
                "desc": "Inject specific grading rules or emphasis areas directly into the generation prompt.",
                "pos": "top: 170px; right: 40px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "⚡ Instant AI Execution",
                "desc": "Leverages configured Moodle Core AI providers (OpenAI, Gemini, Azure) for rapid rubric creation.",
                "pos": "bottom: 50px; left: 100px; border-left: 4px solid #c084fc;"
            }
        ]
    },
    {
        "filename": "4 rubric preview -1.png",
        "tagline": "✦ INTERACTIVE RUBRIC PREVIEW",
        "title": "Generated Criteria <span>& Multi-Level Matrix</span>",
        "subtitle": "Review the AI-generated rubric matrix before publishing. Automatically structures grading criteria across Bloom's or SOLO taxonomy levels with clear point allocations.",
        "img_width": 1380,
        "img_height": 620,
        "callouts": [
            {
                "title": "📊 Structured Multi-Level Criteria",
                "desc": "Presents detailed performance descriptors for each achievement level from mastery to developing.",
                "pos": "top: 40px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🎯 Balanced Point Allocations",
                "desc": "Automatically calculates and assigns fair point weighting across all evaluation dimensions.",
                "pos": "top: 140px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🔍 Pedagogical Rigor",
                "desc": "Ensures every descriptor uses clear, objective, and observable grading criteria.",
                "pos": "bottom: 40px; right: 80px; border-left: 4px solid #c084fc;"
            }
        ]
    },
    {
        "filename": "5 rubric preview -2 and .png",
        "tagline": "✦ PRE-PILOT SUBMISSION TESTING",
        "title": "Pre-Pilot Rubric <span>Submission Testing</span>",
        "subtitle": "Don't just generate—test-drive your rubric before assigning it to students. Upload sample student submissions (PDF or plain text) to see predicted grades and criterion-by-criterion level matching.",
        "img_width": 1380,
        "img_height": 600,
        "callouts": [
            {
                "title": "🧪 Test-Drive Before Assigning",
                "desc": "Verify that your draft rubric evaluates student work fairly before publishing it to live grading.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "📄 Client-Side PDF & Text Extraction",
                "desc": "Upload sample student essays or text submissions for instant AI evaluation against draft criteria.",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🎯 Predicted Scoring Insights",
                "desc": "Displays detailed criterion-by-criterion level matching and feedback rationales.",
                "pos": "bottom: 45px; right: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "6option to modify by ai chat.png",
        "tagline": "✦ INTERACTIVE NATURAL LANGUAGE REFINEMENT",
        "title": "Conversational <span>Rubric Refinement</span>",
        "subtitle": "Refine draft rubrics effortlessly using natural language prompts without starting over (e.g., 'Make the scoring stricter for citations' or 'Add a criterion for critical analysis').",
        "img_width": 1380,
        "img_height": 540,
        "callouts": [
            {
                "title": "💬 Natural Language Editing",
                "desc": "Type conversational prompts directly into the chat box to modify criteria, point weights, or wording.",
                "pos": "top: 40px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "⚡ Iterative Criteria Tuning",
                "desc": "Instantly updates achievement descriptors and level definitions based on your feedback.",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🔄 Zero Scratch Rebuilds",
                "desc": "Preserves your approved criteria while selectively adjusting targeted areas.",
                "pos": "bottom: 40px; left: 80px; border-left: 4px solid #c084fc;"
            }
        ]
    },
    {
        "filename": "7.png",
        "tagline": "✦ ONE-CLICK DEPLOYMENT & EXPORT",
        "title": "Production-Ready <span>Rubric Deployment</span>",
        "subtitle": "Instantly save generated rubrics directly into Moodle's native Advanced Grading rubric tables (grading_form_rubric), or export to Word (.docx) and PDF for offline review.",
        "img_width": 1380,
        "img_height": 560,
        "callouts": [
            {
                "title": "🚀 One-Click Moodle Deployment",
                "desc": "Directly saves the approved rubric into Moodle's native Advanced Grading tables.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "📄 Export to Word & PDF",
                "desc": "Download formatted rubrics (.docx or PDF) for syllabus documentation and department archives.",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🔒 Native Gradebook Sync",
                "desc": "Fully compatible with Moodle Assignment grading, student feedback views, and gradebook calculation.",
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
    print(f"Starting showcase generation for {len(SHOWCASES)} airubricgenerator screenshots...")
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

    print("\nAll 7 airubricgenerator showcase images generated successfully!")

if __name__ == "__main__":
    run()
