import os
import subprocess
from PIL import Image

INPUT_DIR = "/home/mohammad/Dev/image-for-plugins/screenshoots/adaptiveplan"
OUTPUT_DIR = "/home/mohammad/Dev/image-for-plugins/improved/adaptiveplan"
os.makedirs(OUTPUT_DIR, exist_ok=True)

SHOWCASES = [
    {
        "filename": "1- student plan statitstic.png",
        "tagline": "✦ ADAPTIVE STUDY PLAN FOR MOODLE • V0.1.0",
        "title": "Student AI Roadmap <span>& Progress Hub</span>",
        "subtitle": "An intelligent, personalized dashboard that tracks real-time completion progress, total study activities, hours invested, and target completion dates from a centralized view.",
        "img_width": 1380,
        "img_height": 590,
        "callouts": [
            {
                "title": "📊 Live Progress Tracking",
                "desc": "Real-time completion circle graph reflecting finished activities and overall course momentum.",
                "pos": "top: 40px; left: 15px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "⚡ Activity & Time Metrics",
                "desc": "Instant breakdown of completed modules (4 / 41) and total study hours invested (15 Hours-50 min).",
                "pos": "top: 130px; right: 15px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🎯 Goal & Deadline Sync",
                "desc": "Clear visibility into remaining study workload and target course end dates (9 July).",
                "pos": "bottom: 40px; right: 60px; border-left: 4px solid #c084fc;"
            }
        ]
    },
    {
        "filename": "2-plane details- activities per day.png",
        "tagline": "✦ SMART SCHEDULE ORCHESTRATION",
        "title": "Chronological <span>Study Roadmap</span>",
        "subtitle": "Eliminate cognitive overload. Activities are dynamically organized into manageable study blocks (Today, Tomorrow, Upcoming) with direct hyperlinks to every Moodle resource.",
        "img_width": 1280,
        "img_height": 620,
        "callouts": [
            {
                "title": "📅 Structured Daily Blocks",
                "desc": "Automatically breaks long course curricula into bite-sized daily tasks to prevent burnout.",
                "pos": "top: 50px; left: 20px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "⏱️ Smart Duration Detection",
                "desc": "Displays estimated completion minutes for Quizzes, Readings, and Videos (15 min, 30 min).",
                "pos": "top: 160px; right: 20px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🔗 One-Click Activity Launch",
                "desc": "Click any roadmap item to jump directly to the Moodle Quiz, Assignment, or SCORM module.",
                "pos": "bottom: 40px; left: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "3reset- and add to calender option.png",
        "tagline": "✦ SEAMLESS LMS INTEGRATION",
        "title": "Instant Schedule <span>Reset & Calendar Sync</span>",
        "subtitle": "Empower students to adapt when life happens. Rebuild the entire study plan with one click or export scheduled study sessions directly to the native Moodle Calendar.",
        "img_width": 1250,
        "img_height": 580,
        "callouts": [
            {
                "title": "🔄 One-Click Plan Reset",
                "desc": "Recalculate and rebuild your study schedule instantly whenever your weekly availability changes.",
                "pos": "top: 45px; left: 30px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "📅 Add to Moodle Calendar",
                "desc": "Synchronize study sessions into your personal calendar with automatic reminder alerts.",
                "pos": "top: 150px; right: 30px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "⚡ Dynamic Availability Sync",
                "desc": "Updates target completion dates without losing track of completed coursework.",
                "pos": "bottom: 45px; right: 100px; border-left: 4px solid #c084fc;"
            }
        ]
    },
    {
        "filename": "4.create paln options -1png",
        "tagline": "✦ CONVERSATIONAL ONBOARDING COACH",
        "title": "Interactive AI Coach — <span>Step 1: Availability</span>",
        "subtitle": "A conversational onboarding wizard that guides students to specify weekly study availability, prior subject knowledge, and planning preferences.",
        "img_width": 980,
        "img_height": 650,
        "callouts": [
            {
                "title": "⏱️ Flexible Availability Input",
                "desc": "Specify study hours per day or per week so the schedule matches your personal routine.",
                "pos": "top: 60px; left: 60px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🎓 Prior Knowledge Calibration",
                "desc": "Tailors schedule pacing based on whether you are a Beginner, Intermediate, or Advanced learner.",
                "pos": "top: 200px; right: 60px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "💬 Custom Learning Goals",
                "desc": "Provide natural language instructions and weak spots directly to the AI Study Coach.",
                "pos": "bottom: 50px; left: 120px; border-left: 4px solid #c084fc;"
            }
        ]
    },
    {
        "filename": "5.create paln options -2png",
        "tagline": "✦ MODULAR TOPIC FOCUS",
        "title": "Interactive AI Coach — <span>Step 2: Target Focus</span>",
        "subtitle": "Students can choose to generate a study roadmap for the entire course or target specific sections and modules where they need extra help.",
        "img_width": 980,
        "img_height": 650,
        "callouts": [
            {
                "title": "🎯 Selective Section Focus",
                "desc": "Choose 'Select Specific Sections' to isolate difficult chapters or upcoming exam topics.",
                "pos": "top: 70px; left: 60px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "📅 Granular Planning Mode",
                "desc": "Toggle between detailed Day-by-Day tasks or high-level Weekly overview roadmaps.",
                "pos": "top: 220px; right: 60px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🚀 Instant AI Generation",
                "desc": "Create an AI-optimized schedule or opt for a quick algorithmic plan without AI delay.",
                "pos": "bottom: 50px; right: 100px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "6choos hours per day.png",
        "tagline": "✦ SMART WORKLOAD BALANCING",
        "title": "Workload Balancing <span>& Daily Hours</span>",
        "subtitle": "Automatically prevents burnout by distributing study hours evenly across available days and synchronizing with institutional deadlines.",
        "img_width": 980,
        "img_height": 650,
        "callouts": [
            {
                "title": "🔢 Custom Hour Selector",
                "desc": "Fine-tune daily study limits from 1 hour up to full intensive study sessions.",
                "pos": "top: 60px; left: 60px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "📊 Realistic Pacing Engine",
                "desc": "Prevents cramming by mathematically balancing activity durations across available days.",
                "pos": "top: 200px; right: 60px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "⚡ Instant Recalibration",
                "desc": "Automatically adjusts remaining activities when study hours are modified.",
                "pos": "bottom: 50px; left: 100px; border-left: 4px solid #c084fc;"
            }
        ]
    },
    {
        "filename": "7 start chat with ai to crate paln .png",
        "tagline": "✦ CORE AI & LOCAL_AIHUB COMPLIANT",
        "title": "Conversational AI <span>Coach Dialogue</span>",
        "subtitle": "Natively integrated with Moodle Core AI and local_aihub. The AI coach receives structured preferences and dynamically crafts a customized study path.",
        "img_width": 980,
        "img_height": 650,
        "callouts": [
            {
                "title": "💬 Structured AI Prompting",
                "desc": "Automatically translates student availability and focus areas into clear AI instructions.",
                "pos": "top: 60px; left: 60px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "⚡ Real-Time Coach Inference",
                "desc": "Engages the student with responsive feedback and progress indicators while building the plan.",
                "pos": "top: 200px; right: 60px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🧠 Personalized Learning Path",
                "desc": "Ensures every student receives a unique roadmap tailored to their exact background.",
                "pos": "bottom: 50px; right: 100px; border-left: 4px solid #c084fc;"
            }
        ]
    },
    {
        "filename": "8 start chat with ai to crate paln -2 .png",
        "tagline": "✦ DYNAMIC ROADMAP GENERATION",
        "title": "AI Study Coach — <span>Roadmap Delivery</span>",
        "subtitle": "The AI Study Coach delivers an actionable, chronologically structured study plan with instant feedback and continuous adjustment options.",
        "img_width": 950,
        "img_height": 650,
        "callouts": [
            {
                "title": "📋 Actionable Study Blocks",
                "desc": "Presents recommended study tasks organized clearly by date and estimated effort.",
                "pos": "top: 60px; left: 60px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🔄 Continuous Refinement",
                "desc": "Students can ask follow-up questions to tweak pacing or reschedule specific modules.",
                "pos": "top: 200px; right: 60px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🚀 One-Click Plan Activation",
                "desc": "Apply the AI-generated schedule directly to your dashboard and Moodle Calendar.",
                "pos": "bottom: 50px; left: 100px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "9 add to calnder.png",
        "tagline": "✦ NATIVE MOODLE CALENDAR SYNC",
        "title": "Seamless Moodle <span>Calendar Integration</span>",
        "subtitle": "Bridge the gap between course activities and daily life. With one click, export all scheduled study blocks into Moodle's native Calendar.",
        "img_width": 1150,
        "img_height": 450,
        "callouts": [
            {
                "title": "📅 Instant Calendar Export",
                "desc": "Synchronizes all study plan deadlines directly into the student's personal Moodle Calendar.",
                "pos": "top: 40px; left: 40px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "⏰ Automated Reminder Alerts",
                "desc": "Leverages Moodle's native notification system to alert students before study sessions start.",
                "pos": "top: 140px; right: 40px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🔄 Zero Double-Booking",
                "desc": "Intelligently aligns study blocks around existing course deadlines and institutional events.",
                "pos": "bottom: 40px; right: 100px; border-left: 4px solid #c084fc;"
            }
        ]
    },
    {
        "filename": "10 setting .png",
        "tagline": "✦ ADMINISTRATOR & TEACHER CONTROL",
        "title": "Instance Settings <span>& AI Configuration</span>",
        "subtitle": "Full administrative control. Teachers can toggle the conversational AI coach, set default activity durations, and configure core AI backend providers.",
        "img_width": 1380,
        "img_height": 600,
        "callouts": [
            {
                "title": "🤖 AI Coach Toggle",
                "desc": "Enable or disable conversational AI onboarding per activity instance (allowchat).",
                "pos": "top: 40px; left: 20px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "⏱️ Default Duration Fallbacks",
                "desc": "Set global baseline completion minutes for activities without custom tags or limits.",
                "pos": "top: 150px; right: 20px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🔒 Core AI & AIHub Routing",
                "desc": "Select between Moodle Core AI (\\core_ai\\manager) or enterprise local_aihub backends.",
                "pos": "bottom: 40px; left: 100px; border-left: 4px solid #c084fc;"
            }
        ]
    },
    {
        "filename": "11-setting 2.png",
        "tagline": "✦ BUILT-IN MEMORY RETENTION ENGINE",
        "title": "Spaced Repetition <span>Intensity Controls</span>",
        "subtitle": "Apply cognitive science directly to your Moodle course. Define spaced repetition intensity (#Repetition=Aggressive#) and automated review schedules.",
        "img_width": 1380,
        "img_height": 450,
        "callouts": [
            {
                "title": "🧠 Automated Review Scheduling",
                "desc": "Orchestrates Day 1, Day 3, and Day 7 review sessions without database bloat.",
                "pos": "top: 40px; left: 30px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🏷️ Hashtag & Custom Field Tags",
                "desc": "Configure repetition intensity using #Repetition=Aggressive#, Normal, or Light tags.",
                "pos": "top: 140px; right: 30px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "📊 Cognitive Retention Boosting",
                "desc": "Dramatically increases long-term memory retention and exam performance across all subjects.",
                "pos": "bottom: 40px; right: 100px; border-left: 4px solid #00C853;"
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
    print(f"Starting showcase generation for {len(SHOWCASES)} adaptiveplan screenshots...")
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

    print("\nAll 11 adaptiveplan showcase images generated successfully!")

if __name__ == "__main__":
    run()
