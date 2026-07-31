import os
import shutil
import subprocess
from PIL import Image

INPUT_FILE = "/home/mohammad/Dev/image-for-plugins/screenshoots/smartdashboard/Announcements-Alert.png"
OUTPUT_DIR = "/home/mohammad/Dev/image-for-plugins/improved/smartdashboard"
os.makedirs(OUTPUT_DIR, exist_ok=True)
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "Announcements-Alert.png")
HTML_FILE = os.path.join(OUTPUT_DIR, "Announcements-Alert.png.html")

ITEM = {
    "filename": "Announcements-Alert.png",
    "tagline": "✦ INSTITUTIONAL BROADCAST & ALERTS • LOCAL_SMARTDASHBOARD",
    "title": "Pop-Up <span>Announcements Modal</span>",
    "subtitle": "Broadcast critical course updates, exam schedule changes, and campus alerts directly to students upon login. Features one-click dismissal and course-specific tagging.",
    "img_width": 1380,
    "img_height": 640,
    "callouts": [
        {
            "title": "📢 Instant Pop-Up Notifications",
            "desc": "Displays important course announcements immediately over the dashboard when students log in.",
            "pos": "top: 45px; left: 25px; border-left: 4px solid #38bdf8;"
        },
        {
            "title": "🏷️ Course & Date Tagging",
            "desc": "Clearly identifies which course the update belongs to along with the broadcast timestamp.",
            "pos": "top: 150px; right: 25px; border-left: 4px solid #818cf8;"
        },
        {
            "title": "🔕 User Dismissal Control",
            "desc": "Students can click 'Don't show this again' to dismiss read alerts and keep their workspace distraction-free.",
            "pos": "bottom: 45px; right: 80px; border-left: 4px solid #00C853;"
        }
    ]
}

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
    print(f"Generating HTML for {ITEM['filename']}...")
    html_content = generate_html(ITEM, INPUT_FILE)
    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print(f"Running headless Chrome to render PNG...")
    chrome_out = OUTPUT_FILE if OUTPUT_FILE.endswith(".png") else OUTPUT_FILE + ".png"
    cmd = [
        "google-chrome",
        "--headless",
        "--disable-gpu",
        f"--screenshot={chrome_out}",
        "--window-size=1920,1080",
        "--allow-file-access-from-files",
        HTML_FILE
    ]
    subprocess.run(cmd, check=True)
    if chrome_out != OUTPUT_FILE and os.path.exists(chrome_out):
        shutil.copyfile(chrome_out, OUTPUT_FILE)
    if os.path.exists(OUTPUT_FILE):
        size = os.path.getsize(OUTPUT_FILE)
        print(f"    [OK] Saved {ITEM['filename']} ({size // 1024} KB)")
    if os.path.exists(HTML_FILE):
        os.remove(HTML_FILE)

if __name__ == "__main__":
    run()
