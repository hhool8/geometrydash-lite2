"""
normalize_thumbs.py — Resize all rs/imgs thumbnails to 186x186 and
copy to data/image/game/{slug}/{slug}-m186x186.{ext}.
"""
import os, shutil
from PIL import Image

DOMAIN = 'geometrydash-lite2.poki2.online'

THUMB_MAP = {
    'geometry-dash-lite': ('rs/imgs/geometry-dash-lite.png', 'png'),
    'color-rush':          ('rs/imgs/color-rush.jpg',         'jpg'),
    'egg-dash':            ('rs/imgs/egg-dash.jpg',            'jpg'),
    'geometry-dash-arrow': ('rs/imgs/geometry-arrow.jpg',     'jpg'),
    'geometry-dash-deadlocked': ('rs/imgs/geometry-dash-deadlocked.jpg', 'jpg'),
    'geometry-dash-lite-2':     ('rs/imgs/geometrydash-lite-2.png',      'png'),
    'geometry-dash-meltdown':   ('rs/imgs/geometry-dash-meltdown.jpg',   'jpg'),
    'geometry-dash':       ('rs/imgs/geometrydash.jpg',       'jpg'),
    'geometry-rash':       ('rs/imgs/geometryrash.png',       'png'),
    'geometry-vibes-x-ball': ('rs/imgs/geometry-vibes-x-ball.jpg', 'jpg'),
    'golf-hit':            ('rs/imgs/golf-hit.jpg',           'jpg'),
}

TARGET_SIZE = 186

for slug, (src_path, ext) in THUMB_MAP.items():
    dest_dir = f'data/image/game/{slug}'
    os.makedirs(dest_dir, exist_ok=True)
    dest_path = f'{dest_dir}/{slug}-m186x186.{ext}'
    if not os.path.exists(src_path):
        print(f'  MISSING: {src_path}')
        continue
    img = Image.open(src_path).convert('RGB' if ext == 'jpg' else 'RGBA')
    img = img.resize((TARGET_SIZE, TARGET_SIZE), Image.LANCZOS)
    save_kwargs = {'optimize': True}
    if ext == 'jpg':
        save_kwargs['quality'] = 88
        img.save(dest_path, 'JPEG', **save_kwargs)
    else:
        img.save(dest_path, 'PNG', **save_kwargs)
    print(f'  {slug}: {src_path} -> {dest_path}')

print('Done.')
