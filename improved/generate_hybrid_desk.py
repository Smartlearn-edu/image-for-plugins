import os
import subprocess

OUTPUT_DIR = "/home/mohammad/Dev/image-for-plugins/improved"
DESK_COMPOSITE_PATH = "/home/mohammad/Dev/image-for-plugins/improved/desk_with_real_ui.png"

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

# ==============================================================================
# 5: Ultimate Hybrid Desk + Annotated Banner + White Frame
# ==============================================================================
html_hybrid_desk = f"""<!DOCTYPE html>
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
    background-image: radial-gradient(circle at 50% 0%, rgba(56, 189, 248, 0.25), transparent 50%),
                      radial-gradient(circle at 80% 30%, rgba(139, 92, 246, 0.22), transparent 40%);
    font-family: 'Inter', system-ui, -apple-system, sans-serif;
    color: white;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding-top: 45px;
    position: relative;
    overflow: hidden;
  }}
  .hero-top {{
    text-align: center;
    max-width: 950px;
    margin-bottom: 28px;
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
    margin-bottom: 12px;
    letter-spacing: 1px;
    text-transform: uppercase;
  }}
  .hero-title {{
    font-family: 'Outfit', sans-serif;
    font-size: 42px;
    font-weight: 800;
    line-height: 1.15;
    margin-bottom: 10px;
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
    font-size: 17px;
    color: #94a3b8;
    line-height: 1.5;
  }}
  .showcase-wrapper {{
    position: relative;
    width: 1540px;
    height: 700px;
    display: flex;
    align-items: center;
    justify-content: center;
  }}
  /* The desk photo framed with crisp white border as requested */
  .desk-screenshot {{
    width: 1260px;
    height: 680px;
    border-radius: 20px;
    border: 3px solid rgba(255, 255, 255, 0.88);
    box-shadow: 0 40px 100px rgba(0,0,0,0.85), 0 0 60px rgba(56,189,248,0.18);
    object-fit: cover;
    object-position: center;
  }}
  /* Annotated Callout Cards */
  .callout {{
    position: absolute;
    background: rgba(15, 23, 42, 0.92);
    backdrop-filter: blur(14px);
    border: 1px solid rgba(255, 255, 255, 0.22);
    border-radius: 16px;
    padding: 16px 20px;
    width: 270px;
    box-shadow: 0 20px 45px rgba(0,0,0,0.7), 0 0 30px rgba(139,92,246,0.25);
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
  .callout-1 {{ top: 40px; left: 15px; border-left: 4px solid #38bdf8; }}
  .callout-2 {{ top: 220px; right: 15px; border-left: 4px solid #818cf8; }}
  .callout-3 {{ bottom: 30px; left: 80px; border-left: 4px solid #c084fc; }}
</style>
</head>
<body>
  <div class="hero-top">
    <div class="tagline">✦ Ultimate Hybrid: Desk Monitor + White Frame + Annotations</div>
    <div class="hero-title">The <span>Smartlearn Dashboard</span> Experience</div>
    <div class="hero-sub">The aesthetic 3D desk environment displaying your 100% real Moodle dashboard, complete with feature callouts.</div>
  </div>
  <div class="showcase-wrapper">
    <img class="desk-screenshot" src="file://{DESK_COMPOSITE_PATH}">
    
    <div class="callout callout-1">
      <div class="callout-title">🔥 Gamified Streaks</div>
      <div class="callout-desc">Real-time streak counter and dynamic GPA metric badge on the live dashboard.</div>
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
# 6: Standalone Desk with White Frame (Compact / Small Screenshot showcase)
# ==============================================================================
html_white_frame_desk = f"""<!DOCTYPE html>
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
    background-image: radial-gradient(circle at 50% 50%, rgba(56, 189, 248, 0.18), transparent 65%);
    font-family: 'Inter', system-ui, -apple-system, sans-serif;
    color: white;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    position: relative;
    overflow: hidden;
  }}
  .header {{
    width: 1480px;
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
    width: 42px;
    height: 42px;
    background: linear-gradient(135deg, #38bdf8, #6366f1);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    font-weight: 800;
  }}
  .header-title {{
    font-family: 'Outfit', sans-serif;
    font-size: 24px;
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
  /* Crisp white border around the desk photo */
  .frame-container {{
    width: 1480px;
    height: 800px;
    border-radius: 22px;
    border: 4px solid #ffffff;
    box-shadow: 0 50px 110px rgba(0,0,0,0.9), 0 0 60px rgba(99,102,241,0.22);
    overflow: hidden;
    position: relative;
    background: #0f172a;
  }}
  .desk-img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
  }}
  .pills {{
    display: flex;
    gap: 20px;
    margin-top: 28px;
  }}
  .pill {{
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    padding: 10px 22px;
    border-radius: 12px;
    font-size: 15px;
    font-weight: 500;
    color: #e2e8f0;
  }}
</style>
</head>
<body>
  <div class="header">
    <div class="header-left">
      <div class="logo-box">S</div>
      <div class="header-title">Smartlearn Dashboard — Real UI on Desk Display</div>
    </div>
    <div class="header-tag">WHITE FRAME • 100% REAL DASHBOARD</div>
  </div>
  <div class="frame-container">
    <img class="desk-img" src="file://{DESK_COMPOSITE_PATH}">
  </div>
  <div class="pills">
    <div class="pill">⚡ <b>100% Real</b> Moodle UI</div>
    <div class="pill">🖥️ <b>3D Desk</b> Environment</div>
    <div class="pill">🖼️ <b>Crisp White</b> Frame</div>
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
    save_and_screenshot(html_hybrid_desk, "5_ultimate_hybrid_desk_annotated")
    save_and_screenshot(html_white_frame_desk, "6_desk_real_ui_white_frame")
    print("\nHybrid desk + white frame samples generated successfully!")
