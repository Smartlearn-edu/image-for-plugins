import os
from PIL import Image, ImageDraw

HERO_PATH = "/home/mohammad/Dev/image-for-plugins/readmefiles-generated images/smartdashboard/hero_dashboard.jpg"
SCREENSHOT_PATH = "/home/mohammad/Dev/image-for-plugins/screenshoots/smartdashboard/student1.png"
OUTPUT_PATH = "/home/mohammad/Dev/image-for-plugins/improved/desk_with_real_ui.png"

def create_composite():
    print("Loading base hero desk image...")
    hero = Image.open(HERO_PATH).convert("RGBA")
    
    print("Loading real screenshot...")
    screen = Image.open(SCREENSHOT_PATH).convert("RGBA")
    
    # Coordinates of monitor screen in hero_dashboard.jpg
    # (272, 80) to (1112, 583) -> w=840, h=503
    box_x = 272
    box_y = 80
    box_w = 840
    box_h = 503
    
    # Let's crop top 105px to completely remove the generic Moodle white navbar
    crop_box = (0, 105, screen.width, screen.height)
    cropped_screen = screen.crop(crop_box)
    
    # Resize to fit monitor screen (840, 503) using Lanczos for crispness
    resized_screen = cropped_screen.resize((box_w, box_h), Image.Resampling.LANCZOS)
    
    # Create rounded corner mask for the inner monitor screen (radius ~10px)
    mask = Image.new("L", (box_w, box_h), 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0, box_w, box_h), radius=10, fill=255)
    
    # Paste resized_screen onto hero using the rounded mask
    hero.paste(resized_screen, (box_x, box_y), mask)
    
    # Convert back to RGB and save
    hero_rgb = hero.convert("RGB")
    hero_rgb.save(OUTPUT_PATH, "PNG", quality=98)
    print(f"Successfully generated {OUTPUT_PATH} ({os.path.getsize(OUTPUT_PATH) // 1024} KB)")

if __name__ == "__main__":
    create_composite()
