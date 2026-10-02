"""Render the existing visitor badge count using personal octopus digit tiles."""

import argparse
from pathlib import Path
import re
import urllib.request
import xml.etree.ElementTree as ET

from PIL import Image


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
    digits = str(number).zfill(7)
    tile_dir = Path(__file__).parent / "assets" / "octopus-digits"
    canvas = Image.new("RGB", (120 * len(digits), 164), "white")
    for index, digit in enumerate(digits):
        with Image.open(tile_dir / f"{digit}.png") as tile:
            canvas.paste(tile.convert("RGB"), (120 * index, 0))
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
