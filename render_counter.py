"""Render the existing visitor badge count using personal octopus digit tiles."""

import argparse
from pathlib import Path
import re
import urllib.request
import xml.etree.ElementTree as ET

from PIL import Image, ImageDraw, ImageFont


def read_count():
    request = urllib.request.Request(
        "https://visitor-badge.laobi.icu/badge?page_id=XINGYI-PU.XINGYI-PU",
        headers={"User-Agent": "XINGYI-PU-profile-counter"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        root = ET.fromstring(response.read())
    values = [
        node.text.strip()
        for node in root.iter()
        if node.tag.endswith("}text")
        and node.text
        and re.fullmatch(r"\d+", node.text.strip())
    ]
    if not values or len(set(values)) != 1:
        raise ValueError("Visitor badge did not return an unambiguous numeric count")
    return int(values[0])


def render(number, destination):
    if not 0 <= number <= 999999:
        raise ValueError("The six-place counter supports counts from 0 to 999999")
    digits = str(number).zfill(6)
    tile_dir = Path(__file__).parent / "assets" / "octopus-digits"
    canvas = Image.new("RGB", (720, 164), "white")
    font = ImageFont.load_default(size=28)
    for index, digit in enumerate(digits):
        # Left to right: hundred-thousands (dance) ... units (sleep).
        character = 9 - index
        with Image.open(tile_dir / f"{character}.png") as tile:
            canvas.paste(tile.convert("RGB").crop((0, 0, 120, 120)), (120 * index, 0))
        draw = ImageDraw.Draw(canvas)
        left = 120 * index
        draw.rounded_rectangle((left + 39, 123, left + 81, 158), radius=12, fill="#fff0ef")
        draw.text((left + 60, 140), digit, font=font, fill="#a51623", anchor="mm")
    destination.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(destination, optimize=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--number", help="Preview digits; omitted in the live workflow")
    parser.add_argument("--output", default="assets/octopus-counter.png")
    args = parser.parse_args()
    number = read_count() if args.number is None else int(args.number)
    if number < 0:
        raise ValueError("Count must be nonnegative")
    render(number, Path(args.output))
    print(f"Rendered visitor count: {number}")
