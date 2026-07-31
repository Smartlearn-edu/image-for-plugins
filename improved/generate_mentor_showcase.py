import os
import subprocess
from PIL import Image

OUTPUT_DIR = "/home/mohammad/Dev/image-for-plugins/improved"
SCREENSHOT_PATH = "/home/mohammad/Dev/image-for-plugins/screenshoots/smartdashboard/mentor 1.png"
CROPPED_SCREENSHOT_PATH = "/home/mohammad/Dev/image-for-plugins/improved/mentor_1_cropped.png"

def prepare_screenshot():
    print("Loading mentor 1.png...")
    img = Image.open(SCREENSHOT_PATH)
    # Crop out top white navbar (0-70) and left/right white page margins (x=0..185 and x=1730..end)
    # This leaves 100% pure, edge-to-edge dark Smartlearn Mentor Dashboard!
    cropped = img.crop((185, 70, 1730, img.height))
    cropped.save(CROPPED_SCREENSHOT_PATH, "PNG", quality=98)
    print(f"Saved cropped screenshot to {CROPPED_SCREENSHOT_PATH} ({cropped.width}x{cropped.height})")

def run_headless_chrome(html_path, output_png):
    cmd = [
        "google-chrome",
        "--headless",
        "--disable-gpu",
        f"--screenshot={output_png}",
        "--window-size=1920,1080",
        "--allow-file-access-from-files",
        html_path
    ]
    print(f"Generating {output_png}...")
    subprocess.run(cmd, check=True)
    if os.path.exists(output_png):
        size = os.path.getsize(output_png)
        print(f" -> Success! {os.path.basename(output_png)} ({size // 1024} KB)")

html_template = f"""<!DOCTYPE html>
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
    max-width: 980px;
    margin-bottom: 36px;
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
    font-size: 46px;
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
    font-size: 18px;
    color: #94a3b8;
    line-height: 1.55;
    font-weight: 400;
  }}
  .showcase-wrapper {{
    position: relative;
    width: 1540px;
    height: 680px;
    display: flex;
    justify-content: center;
  }}
  /* The real screenshot with sleek rounded bezel */
  .main-screenshot {{
    width: 1400px;
    height: 650px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.22);
    box-shadow: 0 40px 90px rgba(0,0,0,0.85), 0 0 60px rgba(99,102,241,0.18);
    object-fit: cover;
    object-position: top center;
  }}
  /* Annotated Feature Callout Cards */
  .callout {{
    position: absolute;
    background: rgba(15, 23, 42, 0.94);
    backdrop-filter: blur(14px);
    border: 1px solid rgba(255, 255, 255, 0.22);
    border-radius: 16px;
    padding: 16px 20px;
    width: 285px;
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
  .callout-1 {{ top: 25px; left: -15px; border-left: 4px solid #38bdf8; }}
  .callout-2 {{ top: 150px; right: -15px; border-left: 4px solid #818cf8; }}
  .callout-3 {{ bottom: 40px; right: 20px; border-left: 4px solid #c084fc; }}
</style>
</head>
<body>
  <div class="hero-top">
    <div class="tagline">✦ SMART DASHBOARD FOR MOODLE • v1.6.0</div>
    <div class="hero-title">Parent & Mentor <span>360° Portal</span></div>
    <div class="hero-sub">
      A centralized command center for parents, mentors, and advisors. Switch effortlessly between assigned mentees, track overall academic performance, monitor upcoming deadlines, and inspect real-time quiz & rubric results from a single unified view.
    </div>
  </div>
  <div class="showcase-wrapper">
    <img class="main-screenshot" src="file://{CROPPED_SCREENSHOT_PATH}">
    
    <div class="callout callout-1">
      <div class="callout-title">👥 Mentee Switcher & Filters</div>
      <div class="callout-desc">Instantly toggle between assigned students (Sara, Nesrin) and filter mentees by enrolled program.</div>
    </div>
    
    <div class="callout callout-2">
      <div class="callout-title">📈 Overall Performance KPIs</div>
      <div class="callout-desc">Live average grade percentages (61%, 17%) with direct drill-down into detailed student progress reports.</div>
    </div>
    
    <div class="callout callout-3">
      <div class="callout-title">🎯 Real-Time Results & Alerts</div>
      <div class="callout-desc">Instant visibility into recent quiz scores, rubric evaluations, and upcoming task deadlines.</div>
    </div>
  </div>
</body>
</html>
"""

def generate():
    prepare_screenshot()
    html_file = os.path.join(OUTPUT_DIR, "mentor_portal_showcase.html")
    png_file = os.path.join(OUTPUT_DIR, "mentor_portal_showcase.png")
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_template)
    run_headless_chrome(html_file, png_file)
    print("Done generating Option 3 style showcase for mentor 1.png!")

if __name__ == "__main__":
    generate()
