import os
import subprocess
import time

OUTPUT_DIR = "/home/mohammad/Dev/image-for-plugins/improved"
SCREENSHOT_PATH = "/home/mohammad/Dev/image-for-plugins/screenshoots/smartdashboard/student1.png"

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
    else:
        print(f" -> Failed to create {output_png}")

# ==============================================================================
# OPTION 1: Device Framing & Hero Mockup Composition
# ==============================================================================
html_option1 = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@600;700;800&display=swap');
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1920px;
    height: 1080px;
    background: radial-gradient(ellipse 80% 60% at 50% -20%, rgba(139, 92, 246, 0.35), rgba(255, 255, 255, 0)),
                radial-gradient(circle at 10% 80%, rgba(56, 189, 248, 0.22), transparent 40%),
                radial-gradient(circle at 90% 80%, rgba(217, 70, 239, 0.22), transparent 40%),
                #080c14;
    font-family: 'Inter', system-ui, -apple-system, sans-serif;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    color: white;
    overflow: hidden;
    position: relative;
  }}
  .badge {{
    background: rgba(139, 92, 246, 0.15);
    border: 1px solid rgba(139, 92, 246, 0.4);
    padding: 8px 20px;
    border-radius: 999px;
    font-size: 14px;
    font-weight: 600;
    letter-spacing: 1px;
    text-transform: uppercase;
    color: #c4b5fd;
    margin-bottom: 24px;
    box-shadow: 0 0 30px rgba(139, 92, 246, 0.3);
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  .window-frame {{
    width: 1540px;
    background: #111827;
    border-radius: 18px;
    border: 1px solid rgba(255, 255, 255, 0.15);
    box-shadow: 0 50px 120px -20px rgba(0, 0, 0, 0.85),
                0 0 0 1px rgba(255, 255, 255, 0.08),
                0 0 60px rgba(139, 92, 246, 0.18);
    overflow: hidden;
    display: flex;
    flex-direction: column;
  }}
  .window-bar {{
    height: 48px;
    background: #182030;
    border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    display: flex;
    align-items: center;
    padding: 0 20px;
    justify-content: space-between;
  }}
  .dots {{
    display: flex;
    gap: 8px;
  }}
  .dot {{
    width: 12px;
    height: 12px;
    border-radius: 50%;
  }}
  .dot-red {{ background: #ff5f56; }}
  .dot-yellow {{ background: #ffbd2e; }}
  .dot-green {{ background: #27c93f; }}
  .url-bar {{
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.09);
    padding: 6px 160px;
    border-radius: 8px;
    font-size: 13px;
    color: #94a3b8;
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  .url-bar span {{ color: #e2e8f0; font-weight: 500; }}
  .window-actions {{
    display: flex;
    gap: 12px;
    color: #64748b;
    font-size: 14px;
  }}
  .screenshot-container {{
    width: 100%;
    height: 740px;
    background: #0f172a;
    overflow: hidden;
    position: relative;
  }}
  .screenshot-img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: top;
  }}
  .pills {{
    display: flex;
    gap: 20px;
    margin-top: 32px;
  }}
  .pill {{
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 10px 22px;
    border-radius: 12px;
    font-size: 15px;
    font-weight: 500;
    color: #e2e8f0;
    display: flex;
    align-items: center;
    gap: 10px;
    backdrop-filter: blur(10px);
  }}
</style>
</head>
<body>
  <div class="badge">
    <span>✦</span> Option 1: SaaS Device Frame Mockup
  </div>
  <div class="window-frame">
    <div class="window-bar">
      <div class="dots">
        <div class="dot dot-red"></div>
        <div class="dot dot-yellow"></div>
        <div class="dot dot-green"></div>
      </div>
      <div class="url-bar">
        <span>🔒</span> https://smartlearn.edu/<span>moodle/my/dashboard</span>
      </div>
      <div class="window-actions">
        <span>●</span><span>▲</span><span>■</span>
      </div>
    </div>
    <div class="screenshot-container">
      <img class="screenshot-img" src="file://{SCREENSHOT_PATH}">
    </div>
  </div>
  <div class="pills">
    <div class="pill">⚡ <b>100% Native</b> Moodle 4.x UI</div>
    <div class="pill">🎯 <b>Real-Time</b> GPA & Streak Calculation</div>
    <div class="pill">🌐 <b>Bilingual</b> RTL & LTR Ready</div>
  </div>
</body>
</html>
"""

# ==============================================================================
# OPTION 2: Screenshot Staging & "Studio Quality" Capture
# ==============================================================================
html_option2 = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@600;700;800&display=swap');
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1920px;
    height: 1080px;
    background: #090d16;
    background-image: radial-gradient(rgba(255, 255, 255, 0.07) 1px, transparent 1px),
                      radial-gradient(circle at 50% 20%, rgba(99, 102, 241, 0.18), transparent 60%);
    background-size: 32px 32px, 100% 100%;
    font-family: 'Inter', system-ui, -apple-system, sans-serif;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    color: white;
  }}
  .header {{
    width: 1500px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 24px;
  }}
  .header-left {{
    display: flex;
    align-items: center;
    gap: 14px;
  }}
  .logo-box {{
    width: 44px;
    height: 44px;
    background: linear-gradient(135deg, #3b82f6, #6366f1);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
    font-weight: 800;
  }}
  .header-title {{
    font-family: 'Outfit', sans-serif;
    font-size: 26px;
    font-weight: 700;
  }}
  .header-tag {{
    font-size: 13px;
    font-weight: 600;
    color: #94a3b8;
    background: rgba(255,255,255,0.05);
    padding: 8px 16px;
    border-radius: 8px;
    border: 1px solid rgba(255,255,255,0.08);
  }}
  .studio-card {{
    width: 1480px;
    height: 660px;
    background: #0f172a;
    border-radius: 24px;
    border: 1px solid rgba(255, 255, 255, 0.15);
    box-shadow: 0 40px 90px rgba(0, 0, 0, 0.75), 0 0 50px rgba(99, 102, 241, 0.15);
    overflow: hidden;
    position: relative;
    padding: 16px;
  }}
  .inner-viewport {{
    width: 100%;
    height: 100%;
    border-radius: 16px;
    overflow: hidden;
    position: relative;
    background: #0b1329;
  }}
  /* Crop out top Moodle header for distraction-free staged showcase */
  .inner-viewport img {{
    width: 100%;
    margin-top: -85px;
  }}
  .footer-caption {{
    margin-top: 24px;
    color: #94a3b8;
    font-size: 15px;
    display: flex;
    align-items: center;
    gap: 10px;
  }}
  .footer-caption span {{
    color: #6366f1;
    font-weight: 700;
  }}
</style>
</head>
<body>
  <div class="header">
    <div class="header-left">
      <div class="logo-box">S</div>
      <div class="header-title">Smartlearn Dashboard — Option 2: Studio Staged (Distraction-Free)</div>
    </div>
    <div class="header-tag">CLEAN CROP • NO NAVBAR NOISE</div>
  </div>
  <div class="studio-card">
    <div class="inner-viewport">
      <img src="file://{SCREENSHOT_PATH}">
    </div>
  </div>
  <div class="footer-caption">
    <span>★ WHY THIS WORKS:</span> We crop out the generic Moodle navbar to highlight the pure plugin UI in a clean museum-grade bezel.
  </div>
</body>
</html>
"""

# ==============================================================================
# OPTION 3: Hybrid README Approach (Branded Concept + Annotated Real UI)
# ==============================================================================
html_option3 = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@600;700;800&display=swap');
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1920px;
    height: 1080px;
    background: #07090e;
    background-image: radial-gradient(circle at 50% 0%, rgba(56, 189, 248, 0.22), transparent 50%),
                      radial-gradient(circle at 80% 30%, rgba(139, 92, 246, 0.18), transparent 40%);
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
    max-width: 900px;
    margin-bottom: 36px;
  }}
  .tagline {{
    display: inline-block;
    background: linear-gradient(135deg, rgba(56,189,248,0.2), rgba(139,92,246,0.2));
    border: 1px solid rgba(56,189,248,0.4);
    color: #38bdf8;
    padding: 6px 18px;
    border-radius: 99px;
    font-size: 13px;
    font-weight: 700;
    margin-bottom: 14px;
    letter-spacing: 1px;
    text-transform: uppercase;
  }}
  .hero-title {{
    font-family: 'Outfit', sans-serif;
    font-size: 44px;
    font-weight: 800;
    line-height: 1.15;
    margin-bottom: 12px;
    background: linear-gradient(to right, #ffffff, #94a3b8);
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
    line-height: 1.5;
  }}
  .showcase-wrapper {{
    position: relative;
    width: 1480px;
    height: 670px;
  }}
  .main-screenshot {{
    width: 1340px;
    height: 630px;
    margin: 0 auto;
    display: block;
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.18);
    box-shadow: 0 35px 80px rgba(0,0,0,0.8), 0 0 50px rgba(56,189,248,0.15);
    object-fit: cover;
    object-position: top;
  }}
  /* Annotated Callout Cards */
  .callout {{
    position: absolute;
    background: rgba(15, 23, 42, 0.9);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 16px;
    padding: 16px 20px;
    width: 270px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.6), 0 0 25px rgba(139,92,246,0.25);
    z-index: 10;
  }}
  .callout-title {{
    font-size: 15px;
    font-weight: 700;
    color: #38bdf8;
    margin-bottom: 4px;
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  .callout-desc {{
    font-size: 13px;
    color: #cbd5e1;
    line-height: 1.4;
  }}
  .callout-1 {{ top: 40px; left: 0px; border-left: 4px solid #38bdf8; }}
  .callout-2 {{ top: 220px; right: 0px; border-left: 4px solid #818cf8; }}
  .callout-3 {{ bottom: 30px; left: 60px; border-left: 4px solid #c084fc; }}
</style>
</head>
<body>
  <div class="hero-top">
    <div class="tagline">Option 3: Hybrid README Hero + Callouts</div>
    <div class="hero-title">The <span>Smartlearn Dashboard</span> Experience</div>
    <div class="hero-sub">Pair an impressive marketing headline with annotated, 100% real product screenshots.</div>
  </div>
  <div class="showcase-wrapper">
    <img class="main-screenshot" src="file://{SCREENSHOT_PATH}">
    
    <div class="callout callout-1">
      <div class="callout-title">🔥 Gamified Streaks</div>
      <div class="callout-desc">Real-time streak counter and dynamic GPA metric badge.</div>
    </div>
    
    <div class="callout callout-2">
      <div class="callout-title">📚 Bilingual Arabic/English</div>
      <div class="callout-desc">Full RTL support with live progress bars for active courses.</div>
    </div>
    
    <div class="callout callout-3">
      <div class="callout-title">⏰ Zero-Clutter Deadlines</div>
      <div class="callout-desc">Instant upcoming task alerts so students never miss an assignment.</div>
    </div>
  </div>
</body>
</html>
"""

# ==============================================================================
# OPTION 4: Ambient Studio Backdrop & 3D Perspective Depth
# ==============================================================================
html_option4 = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@600;700;800&display=swap');
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    width: 1920px;
    height: 1080px;
    background: #04060a;
    background-image: 
      radial-gradient(circle at 15% 50%, rgba(6, 182, 212, 0.28), transparent 45%),
      radial-gradient(circle at 85% 50%, rgba(217, 70, 239, 0.28), transparent 45%),
      linear-gradient(to bottom, #04060a 0%, #0a0f1d 100%);
    font-family: 'Inter', system-ui, -apple-system, sans-serif;
    color: white;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    position: relative;
    overflow: hidden;
  }}
  .ambient-title {{
    font-family: 'Outfit', sans-serif;
    font-size: 20px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #94a3b8;
    margin-bottom: 28px;
    display: flex;
    align-items: center;
    gap: 12px;
  }}
  .ambient-title span {{ color: #06b6d4; }}
  
  .stage-wrapper {{
    position: relative;
    width: 1540px;
    height: 760px;
    display: flex;
    align-items: center;
    justify-content: center;
  }}
  .ambient-screen {{
    width: 1360px;
    height: 740px;
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.22);
    box-shadow: -40px 25px 90px rgba(6, 182, 212, 0.35),
                40px 25px 90px rgba(217, 70, 239, 0.35),
                0 30px 60px rgba(0,0,0,0.9);
    object-fit: cover;
    object-position: top;
    background: #0f172a;
  }}
  /* Floating 3D Glass Cards on Sides */
  .float-card {{
    position: absolute;
    background: rgba(15, 23, 42, 0.75);
    backdrop-filter: blur(18px);
    border: 1px solid rgba(255, 255, 255, 0.25);
    border-radius: 20px;
    padding: 18px 24px;
    display: flex;
    align-items: center;
    gap: 16px;
    box-shadow: 0 25px 50px rgba(0,0,0,0.65);
    z-index: 20;
  }}
  .float-icon {{
    width: 52px;
    height: 52px;
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 26px;
  }}
  .icon-cyan {{ background: rgba(6, 182, 212, 0.2); border: 1px solid #06b6d4; }}
  .icon-magenta {{ background: rgba(217, 70, 239, 0.2); border: 1px solid #d946ef; }}
  .float-text h4 {{ font-size: 16px; font-weight: 700; color: white; margin-bottom: 3px; }}
  .float-text p {{ font-size: 13px; color: #94a3b8; }}
  
  .card-left {{ left: 10px; top: 120px; }}
  .card-right {{ right: 10px; bottom: 120px; }}
</style>
</head>
<body>
  <div class="ambient-title">
    <span>✦</span> Option 4: Cinematic Ambient Backdrop & 3D Depth
  </div>
  <div class="stage-wrapper">
    <img class="ambient-screen" src="file://{SCREENSHOT_PATH}">
    
    <div class="float-card card-left">
      <div class="float-icon icon-cyan">⚡</div>
      <div class="float-text">
        <h4>Live GPA: 58% ▲</h4>
        <p>Dynamic Academic Tracker</p>
      </div>
    </div>
    
    <div class="float-card card-right">
      <div class="float-icon icon-magenta">🔥</div>
      <div class="float-text">
        <h4>1 Days Active Streak</h4>
        <p>Gamified Engagement</p>
      </div>
    </div>
  </div>
</body>
</html>
"""

def save_and_screenshot(html_content, name):
    html_file = os.path.join(OUTPUT_DIR, f"{name}.html")
    png_file = os.path.join(OUTPUT_DIR, f"{name}.png")
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(html_content)
    run_headless_chrome(html_file, png_file)
    if os.path.exists(html_file):
        os.remove(html_file)

if __name__ == "__main__":
    save_and_screenshot(html_option1, "1_device_framing")
    save_and_screenshot(html_option2, "2_studio_staged_clean")
    save_and_screenshot(html_option3, "3_hybrid_readme_banner")
    save_and_screenshot(html_option4, "4_ambient_studio_backdrop")
    print("\nAll 4 samples generated successfully!")
