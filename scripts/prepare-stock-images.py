"""Create responsive web copies; leave supplied originals untouched."""
from pathlib import Path
from PIL import Image, ImageOps
import json
sources = [
('nutrition','young-woman-enjoying-healthy-lifestyle-in-home-2026-09-22-05-32-02-utc.jpg'),
('studio','women-resting-and-smiling-in-sunny-fitness-studio-2026-09-25-08-16-12-utc.jpg'),
('outdoors','two-women-chatting-after-an-outdoor-workout-2026-09-21-13-35-35-utc.jpg'),
('stretch','woman-stretching-on-a-blue-fitness-ball-in-a-brigh-2026-09-25-07-11-27-utc.JPG'),
('activewear','women-in-colorful-athletic-wear-holding-yoga-mats-2026-09-22-02-56-18-utc.jpg'),
('yoga','women-practicing-yoga-in-studio-on-blue-mats-2026-09-24-11-55-48-utc.jpg'),
('community','women-relaxing-and-chatting-at-the-gym-2026-10-27-20-11-16-utc.jpg'),
('tennis','smiling-women-enjoying-a-game-of-tennis-2026-09-22-06-01-48-utc.jpg'),
('rope','smiling-woman-holding-jump-rope-ready-to-exercise-2026-10-06-20-18-07-utc.jpg'),
('voices','smiling-active-people-standing-in-front-of-colored-2026-09-22-02-52-58-utc.jpg')]
out = Path(__file__).resolve().parents[1] / 'dist/images/stock'
out.mkdir(parents=True, exist_ok=True)
manifest = {}
for name, filename in sources:
    source = Path('/Users/mac/Downloads') / filename
    with Image.open(source) as original:
        im = ImageOps.exif_transpose(original).convert('RGB')
        manifest[name] = {'source':filename,'originalBytes':source.stat().st_size,'originalSize':im.size,'variants':[]}
        for width in (640,1280,2560):
            copy = im.resize((width,round(im.height*width/im.width)),Image.Resampling.LANCZOS)
            target = out / f'{name}-{width}.webp'
            copy.save(target,'WEBP',quality=90,method=6)
            manifest[name]['variants'].append({'file':target.name,'width':width,'height':copy.height,'bytes':target.stat().st_size})
    print(name, manifest[name]['variants'])
(out/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
