import os
import shutil
import subprocess
from PIL import Image

INPUT_DIR = "/home/mohammad/Dev/image-for-plugins/screenshoots/smartdashboard"
OUTPUT_DIR = "/home/mohammad/Dev/image-for-plugins/improved/smartdashboard"
os.makedirs(OUTPUT_DIR, exist_ok=True)

SHOWCASES = [
    {
        "filename": "admin 1.png",
        "tagline": "✦ ADMIN ROLE REDIRECTION • LOCAL_SMARTDASHBOARD",
        "title": "Seamless <span>Role-Based Redirection</span>",
        "subtitle": "Configure whether Smart Dashboard replaces the default Moodle dashboard for specific user roles. Support granular role selection for Managers, Teachers, Students, and Parents.",
        "img_width": 1380,
        "img_height": 640,
        "callouts": [
            {
                "title": "🔄 Granular Role Selection",
                "desc": "Select exact roles (Teacher, Student, Manager, Parent) to redirect automatically.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🛡️ Admin Override Control",
                "desc": "Optionally exempt or redirect Site Administrators with a single checkbox toggle.",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "⚡ Zero Core Code Modifications",
                "desc": "Works natively via Moodle navigation hooks without altering any core LMS files.",
                "pos": "bottom: 45px; right: 80px; border-left: 4px solid #c084fc;"
            }
        ]
    },
    {
        "filename": "admin 2.png",
        "tagline": "✦ ADVANCED RULE CONFIGURATION",
        "title": "Modular <span>At-Risk Alert Rules</span>",
        "subtitle": "Manage modular at-risk warning subplugins such as Login Recency, Course Completion, Low Average Grades, and Overdue Assignments from a unified admin console.",
        "img_width": 1380,
        "img_height": 640,
        "callouts": [
            {
                "title": "⚠️ Modular Subplugin Engine",
                "desc": "Enable or tune individual smartdashboardrule plugins to match school retention policies.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🎯 Custom Risk Thresholds",
                "desc": "Set exact numeric thresholds for login inactivity, passing grades, and deadline grace periods.",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🔔 Automated Webhook Triggers",
                "desc": "Configure external n8n webhook notifications when student risk scores exceed safety limits.",
                "pos": "bottom: 45px; left: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "admin 3.png",
        "tagline": "✦ ENTERPRISE DASHBOARD SETTINGS",
        "title": "Customizable <span>UI & Feature Toggles</span>",
        "subtitle": "Take full control over dashboard widgets, custom branding, layout options, and student shortcut icons directly from Site Administration.",
        "img_width": 1380,
        "img_height": 640,
        "callouts": [
            {
                "title": "🎨 Dark Mode Glassmorphism",
                "desc": "Manage premium visual themes, custom color palettes, and responsive container styles.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "📌 Custom Shortcuts Grid",
                "desc": "Define up to 10 custom icon links and badges for institutional tools and resources.",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "⚡ High-Performance Caching",
                "desc": "Built-in query optimization ensures instant dashboard load times even for large universities.",
                "pos": "bottom: 45px; right: 80px; border-left: 4px solid #c084fc;"
            }
        ]
    },
    {
        "filename": "mentor 1.png",
        "tagline": "✦ PARENT & MENTOR CONNECTIVITY",
        "title": "Unified <span>Parent & Mentor Hub</span>",
        "subtitle": "Give parents and academic mentors a dedicated portal to monitor all assigned mentees in one place. Features real-time KPI cards, progress buttons, and instant deadline alerts.",
        "img_width": 1380,
        "img_height": 640,
        "callouts": [
            {
                "title": "👥 Multi-Mentee Card Grid",
                "desc": "View all assigned children or mentees with avatars, names, and average performance scores.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "📈 Overall Performance KPI",
                "desc": "Instant visual snapshot of each mentee's average grade and course standing.",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🚨 Urgent Deadline Monitor",
                "desc": "Highlights upcoming deadlines and recent quiz/assignment results for proactive support.",
                "pos": "bottom: 45px; right: 80px; border-left: 4px solid #c084fc;"
            }
        ]
    },
    {
        "filename": "mentor 2.png",
        "tagline": "✦ MENTEE ACTIVITY TRACKING",
        "title": "Granular <span>Mentee Course Drill-Down</span>",
        "subtitle": "Inspect detailed course progress for any selected mentee. View exact completion percentages across individual courses and track active learning streaks.",
        "img_width": 1380,
        "img_height": 640,
        "callouts": [
            {
                "title": "🔍 Interactive Mentee Selector",
                "desc": "Switch between different mentees from a smooth dropdown selector at the top of the page.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "📊 Per-Course Completion Bars",
                "desc": "Visual progress bars show percentage completed for each enrolled subject.",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🔥 Engagement & Streak Badges",
                "desc": "Motivates consistent learning by tracking daily login streaks and active coursework.",
                "pos": "bottom: 45px; left: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "mentor 3.png",
        "tagline": "✦ ACADEMIC STANDING & GRADES",
        "title": "Comprehensive <span>Mentee Grade Overview</span>",
        "subtitle": "Empower mentors and parents with full visibility into mentee grades across all courses, quizzes, assignments, and interactive learning activities.",
        "img_width": 1380,
        "img_height": 640,
        "callouts": [
            {
                "title": "📑 Course Grade Summary Table",
                "desc": "Itemizes overall course scores and letter grades across every enrolled subject.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "⭐ Recent Assessment Results",
                "desc": "Shows immediate feedback on recently submitted quizzes, rubrics, and exams.",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "💬 Proactive Guidance Support",
                "desc": "Allows mentors to identify academic drop-offs early and intervene before end-of-term.",
                "pos": "bottom: 45px; right: 80px; border-left: 4px solid #c084fc;"
            }
        ]
    },
    {
        "filename": "mentor 4.png",
        "tagline": "✦ PARENTAL DEADLINE AWARENESS",
        "title": "Color-Coded <span>Mentee Deadline Alerts</span>",
        "subtitle": "Never miss an important school due date again. Groups upcoming assignments and quizzes by urgency so mentors can help students prioritize their workload.",
        "img_width": 1380,
        "img_height": 640,
        "callouts": [
            {
                "title": "🔴 Critical & Urgent Alerts",
                "desc": "Highlights items due within 24–48 hours in high-visibility alert cards.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🟡 Due Soon Notifications",
                "desc": "Categorizes upcoming assessments for balanced weekly study planning.",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "✅ Caught-Up Status Confirmation",
                "desc": "Provides positive visual reinforcement when all coursework is completed on schedule.",
                "pos": "bottom: 45px; left: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "mentor 5.png",
        "tagline": "✦ HOLISTIC MENTEE ANALYTICS",
        "title": "Mentee <span>Engagement KPI Dashboard</span>",
        "subtitle": "Track overall attendance, login frequency, GPA trends, and completion metrics from an executive-style analytics interface designed for mentors.",
        "img_width": 1380,
        "img_height": 640,
        "callouts": [
            {
                "title": "📈 Longitudinal GPA Trends",
                "desc": "Monitors academic progress over time to ensure consistent student development.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "⏱️ Activity & Time Tracking",
                "desc": "Summarizes total active learning hours and course participation metrics.",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🔗 One-Click Teacher Communication",
                "desc": "Streamlines collaboration between parents, mentors, and course instructors.",
                "pos": "bottom: 45px; right: 80px; border-left: 4px solid #c084fc;"
            }
        ]
    },
    {
        "filename": "mr.png",
        "tagline": "✦ AI MAGIC REPORTS • NATURAL LANGUAGE SQL",
        "title": "AI-Powered <span>Magic Reports Hub</span>",
        "subtitle": "Stop writing manual SQL queries. Ask questions in plain English and let AI generate complex Moodle database queries and custom reports automatically.",
        "img_width": 1380,
        "img_height": 640,
        "callouts": [
            {
                "title": "🪄 Plain English Query Builder",
                "desc": "Type requests like 'Show top 10 students by grade' and let AI write accurate SQL.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🛡️ Built-In Security Guardrails",
                "desc": "Prevents unauthorized data access and ensures read-only database execution.",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "💾 One-Click Report Library",
                "desc": "Save, name, and categorize frequently run AI reports for instant future re-execution.",
                "pos": "bottom: 45px; left: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "mr1.png",
        "tagline": "✦ VISUAL DATA EXPLORATION",
        "title": "Interactive <span>SQL Query Visualizer</span>",
        "subtitle": "Transform raw SQL report results into stunning interactive charts, revenue graphs, and sortable data tables without exporting to Excel.",
        "img_width": 1380,
        "img_height": 640,
        "callouts": [
            {
                "title": "📊 Dynamic Chart Generation",
                "desc": "Instantly convert query output into bar, line, and pie charts with custom legends.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "📥 One-Click Export & Sharing",
                "desc": "Export report results to CSV or share executive summaries across your institution.",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "⚡ Real-Time Database Querying",
                "desc": "Executes optimized read-only queries directly against live Moodle tables.",
                "pos": "bottom: 45px; right: 80px; border-left: 4px solid #c084fc;"
            }
        ]
    },
    {
        "filename": "student 2.png",
        "tagline": "✦ CROSS-COURSE PROGRESS TRACKING",
        "title": "Interactive <span>Course Progress Cards</span>",
        "subtitle": "Keep students motivated with a beautiful, centralized overview of all enrolled courses featuring progress bars, student counts, and direct jump-in links.",
        "img_width": 1380,
        "img_height": 640,
        "callouts": [
            {
                "title": "🚀 Instant Course Jump-In",
                "desc": "One-click navigation directly to the latest unfinished course activity.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "📊 Visual Completion Bars",
                "desc": "Displays exact progress percentages across every active course.",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "👥 Cohort & Student Statistics",
                "desc": "Shows total enrolled classmates and live course activity indicators.",
                "pos": "bottom: 45px; left: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "student 3.png",
        "tagline": "✦ SMART WORKLOAD MANAGEMENT",
        "title": "Color-Coded <span>Deadline Timeline</span>",
        "subtitle": "Eliminate missed assignments with an intuitive deadline timeline that categorizes tasks by Critical, Due Soon, and Upcoming status.",
        "img_width": 1380,
        "img_height": 640,
        "callouts": [
            {
                "title": "🔴 Critical Urgency Highlighting",
                "desc": "Immediate red badges for assignments and quizzes due within 24 hours.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🟡 Balanced 'Due Soon' View",
                "desc": "Helps students plan their weekly study schedule without feeling overwhelmed.",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "✅ Instant Submission Verification",
                "desc": "Automatically checks off completed assignments once submitted.",
                "pos": "bottom: 45px; right: 80px; border-left: 4px solid #c084fc;"
            }
        ]
    },
    {
        "filename": "student 5.png",
        "tagline": "✦ PERSONALIZED STUDY PLANNING",
        "title": "Daily <span>Study Agenda & Calendar</span>",
        "subtitle": "Give students a clean daily agenda that aggregates upcoming lectures, quiz deadlines, and study goals into an actionable daily schedule.",
        "img_width": 1380,
        "img_height": 640,
        "callouts": [
            {
                "title": "📅 Daily & Weekly Agenda View",
                "desc": "Presents an organized chronological feed of all course events and tasks.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🔥 Daily Streak & Goal Tracking",
                "desc": "Encourages daily login habits with interactive streak counters and badges.",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🎨 Premium Glassmorphic Layout",
                "desc": "A sleek dark-mode aesthetic that students love using every day.",
                "pos": "bottom: 45px; left: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "student1.png",
        "tagline": "✦ STUDENT DASHBOARD HERO",
        "title": "Welcome Banner & <span>Shortcuts Grid</span>",
        "subtitle": "A stunning dark-mode landing experience featuring a personalized student greeting, live KPI metrics, and a customizable 10-icon shortcuts grid.",
        "img_width": 1380,
        "img_height": 640,
        "callouts": [
            {
                "title": "👋 Personalized Welcome Header",
                "desc": "Displays student avatar, name, current date, and live academic streak.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "📌 Institutional Shortcuts Grid",
                "desc": "Quick links to campus resources, libraries, email, and frequently used tools.",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "⚡ Clean Zero-Clutter Navigation",
                "desc": "Replaces Moodle's cluttered default dashboard with a modern executive portal.",
                "pos": "bottom: 45px; right: 80px; border-left: 4px solid #c084fc;"
            }
        ]
    },
    {
        "filename": "student4.png",
        "tagline": "✦ ACADEMIC PERFORMANCE SNAPSHOT",
        "title": "Centralized <span>My Grades Summary</span>",
        "subtitle": "Provide students with immediate visibility into their GPA and individual course grades without navigating deep into the Moodle gradebook.",
        "img_width": 1380,
        "img_height": 640,
        "callouts": [
            {
                "title": "🏆 Overall GPA & Standing",
                "desc": "Displays aggregated grade point average prominently at the top of the page.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "📑 Course-by-Course Score Breakdown",
                "desc": "Clear tabular view of percentage scores and letter grades for every course.",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🎯 Goal Tracking & Feedback",
                "desc": "Helps students see where they stand and where to focus their study efforts.",
                "pos": "bottom: 45px; left: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "teacher 1.png",
        "tagline": "✦ EARLY WARNING & RETENTION SYSTEM",
        "title": "Detailed <span>Student Progress Drill-Down</span>",
        "subtitle": "Empower teachers to inspect individual student activity completion, filter by activity type, and monitor engagement across every lesson and quiz.",
        "img_width": 1380,
        "img_height": 640,
        "callouts": [
            {
                "title": "🔍 Instant Student Dropdown",
                "desc": "Select any student in the course to see their complete activity tracking history.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🏷️ Activity Type Filtering",
                "desc": "Filter between Quizzes, Assignments, Forums, and Books with a single click.",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🟢 Real-Time Completion Badges",
                "desc": "Color-coded badges (Completed, Pending, No Tracking) make auditing effortless.",
                "pos": "bottom: 45px; right: 80px; border-left: 4px solid #c084fc;"
            }
        ]
    },
    {
        "filename": "teacher 2.png",
        "tagline": "✦ PROACTIVE AT-RISK MONITORING",
        "title": "Teacher <span>At-Risk Student Alerts</span>",
        "subtitle": "Identify struggling students before they drop out using automated risk scores based on login recency, course completion, and grade thresholds.",
        "img_width": 1380,
        "img_height": 640,
        "callouts": [
            {
                "title": "⚠️ Modular Risk Score Calculation",
                "desc": "Aggregates multiple risk factors into a clear, actionable warning score.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🚨 Instant Intervention Alerts",
                "desc": "Highlight students who need tutoring, emails, or guidance check-ins.",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "⚡ Webhook & Automation Support",
                "desc": "Connects with external messaging tools to alert advisors automatically.",
                "pos": "bottom: 45px; left: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "teacher 3.png",
        "tagline": "✦ CENTRALIZED TEACHER WORKFLOW",
        "title": "Unified <span>Grading Queue & Analytics</span>",
        "subtitle": "Stop clicking through dozens of courses to find ungraded work. Grade pending assignments and analyze cohort performance from one central screen.",
        "img_width": 1380,
        "img_height": 640,
        "callouts": [
            {
                "title": "📥 Centralized Grading Queue",
                "desc": "Aggregates all pending submissions across all courses into a single actionable list.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "📊 Cohort Performance Analytics",
                "desc": "Visual charts highlight grade distributions and common learning bottlenecks.",
                "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "⏱️ Massive Time Savings",
                "desc": "Reduces teacher grading administrative time by hours every week.",
                "pos": "bottom: 45px; right: 80px; border-left: 4px solid #c084fc;"
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
    print(f"Starting showcase generation for {len(SHOWCASES)} smartdashboard screenshots...")
    for index, item in enumerate(SHOWCASES, 1):
        in_file = os.path.join(INPUT_DIR, item["filename"])
        out_file = os.path.join(OUTPUT_DIR, item["filename"])
        html_file = os.path.join(OUTPUT_DIR, item["filename"] + ".html")
        
        if not os.path.exists(in_file):
            print(f"[{index}/{len(SHOWCASES)}] ERROR: Input file not found: {in_file}")
            continue
            
        print(f"[{index}/{len(SHOWCASES)}] Generating: {item['filename']}")
        html_content = generate_html(item, in_file)
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(html_content)
            
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

    print("\nAll 18 smartdashboard showcase images generated successfully!")

if __name__ == "__main__":
    run()
