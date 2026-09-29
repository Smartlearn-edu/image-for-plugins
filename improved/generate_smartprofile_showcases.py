import os
import shutil
import subprocess
from PIL import Image

INPUT_DIR = "/home/mohammad/Dev/image-for-plugins/screenshoots/smartprofile"
OUTPUT_DIR_PRIMARY = "/home/mohammad/Dev/image-for-plugins/improved/smartprofile"
OUTPUT_DIR_SECONDARY = "/home/mohammad/Dev/image-for-plugins/readmefiles-generated images/smartprofile"

os.makedirs(OUTPUT_DIR_PRIMARY, exist_ok=True)
os.makedirs(OUTPUT_DIR_SECONDARY, exist_ok=True)

SHOWCASES = [
    {
        "filename": "0-main banner.png",
        "tagline": "✦ STUDENT ACADEMIC IDENTITY • LOCAL_SMARTPROFILE",
        "title": "Dynamic <span>Academic Profile & Wallet Hub</span>",
        "subtitle": "Transform Moodle student profiles into a modern verified academic passport. Features comprehensive department credit hour breakdowns, verified digital badges, and 1-tap Apple Wallet export.",
        "img_width": 1380,
        "img_height": 590,
        "callouts": [
            {
                "title": "🎓 Verified Academic Passport",
                "desc": "Displays student avatar, verified badge, bio, academic discipline, and joined date.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "📊 Department Credit Breakdown",
                "desc": "Categorizes earned credit hours organized by academic department & subject.",
                "pos": "top: 45px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "📱 Apple Wallet Pass Integration",
                "desc": "Instantly export student credentials and credit summaries to Apple Wallet.",
                "pos": "bottom: 40px; right: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "1- performance.png",
        "tagline": "✦ LEARNING ANALYTICS & ACTIVITY ENGINE",
        "title": "Real-Time <span>Learning Performance & Feed</span>",
        "subtitle": "Provide students with crystal-clear visibility into their academic momentum. Tracks overall completion percentage, interactive activity metrics, recent course activity, and earned badges.",
        "img_width": 1380,
        "img_height": 590,
        "callouts": [
            {
                "title": "📈 73% Overall Progress KPI",
                "desc": "Real-time calculation of overall learning performance and course activity completion.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "⚡ Live Activity Stream",
                "desc": "Chronological audit trail of recently completed courses, lessons, and assignments.",
                "pos": "top: 45px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🏆 Gamified Achievements",
                "desc": "Displays unlocked Moodle open badges, milestone awards, and certificates.",
                "pos": "bottom: 40px; right: 80px; border-left: 4px solid #c084fc;"
            }
        ]
    },
    {
        "filename": "2- completed courses.png",
        "tagline": "✦ VERIFIED ACADEMIC ACHIEVEMENTS",
        "title": "Interactive <span>Completed Courses Grid</span>",
        "subtitle": "Showcase a rich portfolio of successfully completed courses with final scores, completion dates, and direct links to digital certificates across programming, medical sciences, and pharmacy.",
        "img_width": 1380,
        "img_height": 590,
        "callouts": [
            {
                "title": "📦 Structured Course Cards",
                "desc": "Clean visual cards displaying course title, subject tags, and completion timestamps.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "💯 100% Mastery Grade Tracking",
                "desc": "Transparent grade badges showing perfect completion and course mastery scores.",
                "pos": "top: 45px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "📜 1-Click Certificate Access",
                "desc": "Direct download and verification links attached to each completed curriculum.",
                "pos": "bottom: 40px; right: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "3- lerning progress.png",
        "tagline": "✦ ACTIVE ENROLLMENT TRACKER",
        "title": "Transparent <span>Curriculum & Module Progress</span>",
        "subtitle": "Empower learners to manage their ongoing studies across all active enrollments. Features visual progress bars, detailed module breakdown, and immediate certificate unlocking upon 100% completion.",
        "img_width": 1380,
        "img_height": 610,
        "callouts": [
            {
                "title": "📊 Multi-Course Progress Bars",
                "desc": "Live percentage meters for Web Design, PHP, Python, and Clinical Pharmacy.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🔄 In-Progress vs Completed Status",
                "desc": "Clear distinction between actively studied subjects and certified modules.",
                "pos": "top: 45px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🔓 Instant Certificate Unlocking",
                "desc": "Automatic credential issuance as soon as course requirements reach 100%.",
                "pos": "bottom: 40px; right: 80px; border-left: 4px solid #f59e0b;"
            }
        ]
    },
    {
        "filename": "4- academic endorsment.png",
        "tagline": "✦ FACULTY CREDENTIALS & TRUST",
        "title": "Verifiable <span>Faculty Endorsements</span>",
        "subtitle": "Enable professors and instructors to attach official academic recommendations and clinical commendations directly to student profiles, building high-value credibility for graduate applications.",
        "img_width": 1440,
        "img_height": 465,
        "callouts": [
            {
                "title": "👨‍🏫 Official Instructor Letters",
                "desc": "Direct academic recommendations from course leaders and university professors.",
                "pos": "top: 35px; left: 35px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🩺 Clinical & Analytical Precision",
                "desc": "Highlights diagnostic reasoning, case analysis skills, and practical achievements.",
                "pos": "top: 35px; right: 35px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🛡️ Cryptographic Trust Link",
                "desc": "Official course date and faculty verification stamp prevent credential fraud.",
                "pos": "bottom: 30px; right: 75px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "5- generated pf.png",
        "tagline": "✦ OFFICIAL VERIFIED ACADEMIC TRANSCRIPT",
        "title": "1-Click <span>Exportable Academic CV (PDF)</span>",
        "subtitle": "Generate an official, tamper-evident Academic CV and verified record in PDF format with a single click. Bundles verified contact details, biography, and complete certified coursework for employers.",
        "img_width": 1380,
        "img_height": 610,
        "callouts": [
            {
                "title": "📄 Official Verified Record",
                "desc": "Standardized academic transcript header with official Smart Learn branding.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "📚 Complete Coursework Transcript",
                "desc": "Itemizes every completed curriculum, grade percentage, and academic track.",
                "pos": "top: 45px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "⚡ Instant PDF Generation",
                "desc": "One-click export ready for job applications, scholarship reviews, and admissions.",
                "pos": "bottom: 40px; right: 80px; border-left: 4px solid #c084fc;"
            }
        ]
    },
    {
        "filename": "6- linkedin share.png",
        "tagline": "✦ CAREER READINESS & SOCIAL PROOF",
        "title": "Seamless <span>1-Click LinkedIn Credential Sync</span>",
        "subtitle": "Bridge the gap between LMS learning and career opportunities. Seamlessly connects to LinkedIn's Certification API to pre-fill credentials, issuing organization, issue dates, and verification links.",
        "img_width": 860,
        "img_height": 640,
        "callouts": [
            {
                "title": "🔗 Native LinkedIn Integration",
                "desc": "Opens the official LinkedIn 'Add license or certification' modal pre-filled instantly.",
                "pos": "top: 45px; left: 40px; border-left: 4px solid #0077b5;"
            },
            {
                "title": "🏷️ Auto-Filled Credential ID",
                "desc": "Populates official Credential ID (SL-CE...) and issuing organization automatically.",
                "pos": "top: 45px; right: 40px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🚀 Instant Professional Credibility",
                "desc": "Empowers students to showcase verified 26.5 credit hours directly on their profile.",
                "pos": "bottom: 45px; left: 40px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "7- Privacy.png",
        "tagline": "✦ GRANULAR PRIVACY ARCHITECTURE",
        "title": "Student-Centric <span>Contact & Profile Privacy</span>",
        "subtitle": "Put students in complete control of their personal information. Granular toggle switches allow students to configure public vs private visibility for email, phone, timezone, and personal details.",
        "img_width": 1380,
        "img_height": 580,
        "callouts": [
            {
                "title": "🔒 Granular Visibility Toggles",
                "desc": "Switch individual fields between Public and Private with real-time saving.",
                "pos": "top: 40px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "📍 Contact & Location Protection",
                "desc": "Safeguard personal contact details, location data, and timezone information.",
                "pos": "top: 40px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🛡️ Zero Accidental Data Exposure",
                "desc": "Default privacy safeguards prevent sensitive student data from leaking publicly.",
                "pos": "bottom: 35px; right: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "7- Privacy-2.png",
        "tagline": "✦ ACADEMIC VISIBILITY GOVERNANCE",
        "title": "Granular <span>Academic & KPI Privacy Controls</span>",
        "subtitle": "Full control over the visibility of academic records. Students can independently configure whether GPA, credit hours, completed courses, badges, and endorsements appear on their public profile.",
        "img_width": 1380,
        "img_height": 590,
        "callouts": [
            {
                "title": "🎓 Academic Credit Visibility",
                "desc": "Toggle public/private status for earned credit hours and department breakdowns.",
                "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🏅 Badge & Endorsement Privacy",
                "desc": "Choose which recommendations and achievements are shared with external visitors.",
                "pos": "top: 45px; right: 25px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "⚖️ GDPR & FERPA Compliance",
                "desc": "Complies strictly with international student privacy laws and data protection standards.",
                "pos": "bottom: 40px; right: 80px; border-left: 4px solid #00C853;"
            }
        ]
    },
    {
        "filename": "8- certificate.png",
        "tagline": "✦ HIGH-SECURITY DIGITAL CREDENTIALS",
        "title": "Verifiable <span>Digital Certificate & QR ID</span>",
        "subtitle": "Issue tamper-proof certificates equipped with unique verification hashes and scannable QR / barcodes. Employers and institutions can instantly authenticate certificate validity online.",
        "img_width": 1440,
        "img_height": 420,
        "callouts": [
            {
                "title": "📜 High-Resolution Certificate",
                "desc": "Official course completion credential for Python for Beginners & Language Basics.",
                "pos": "top: 30px; left: 35px; border-left: 4px solid #38bdf8;"
            },
            {
                "title": "🔍 Scannable QR & Barcode",
                "desc": "Embedded digital verification codes for instantaneous third-party authentication.",
                "pos": "top: 30px; right: 35px; border-left: 4px solid #818cf8;"
            },
            {
                "title": "🏛️ Official Institutional Stamp",
                "desc": "Signed credential with unique certificate serial number (1348610882SM).",
                "pos": "bottom: 25px; right: 75px; border-left: 4px solid #00C853;"
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
    width: 300px;
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
    print(f"Starting showcase generation for {len(SHOWCASES)} smartprofile screenshots...")
    for i, item in enumerate(SHOWCASES, 1):
        in_file = os.path.join(INPUT_DIR, item["filename"])
        out_file_1 = os.path.join(OUTPUT_DIR_PRIMARY, item["filename"])
        out_file_2 = os.path.join(OUTPUT_DIR_SECONDARY, item["filename"])
        html_file = os.path.join(OUTPUT_DIR_PRIMARY, f"temp_sp_{i}.html")
        
        if not os.path.exists(in_file):
            print(f"[{i}/{len(SHOWCASES)}] ERROR: Input file not found: {in_file}")
            continue
            
        print(f"[{i}/{len(SHOWCASES)}] Processing: {item['filename']}")
        html_content = generate_html(item, in_file)
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(html_content)
            
        chrome_out = out_file_1 if out_file_1.endswith(".png") else out_file_1 + ".png"
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
        if chrome_out != out_file_1 and os.path.exists(chrome_out):
            shutil.copyfile(chrome_out, out_file_1)
        if os.path.exists(out_file_1):
            shutil.copyfile(out_file_1, out_file_2)
            size = os.path.getsize(out_file_1)
            print(f"    [OK] Saved {item['filename']} ({size // 1024} KB)")
        if os.path.exists(html_file):
            os.remove(html_file)

    print("\nAll 10 smartprofile showcase images generated and synchronized successfully!")

if __name__ == "__main__":
    run()
