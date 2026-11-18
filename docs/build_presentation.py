#!/usr/bin/env python3
"""Build English 16:9 HTML presentation, standalone single-file HTML, PDF, and 16 slide PNG captures."""

from pathlib import Path
import base64
import os
import re
import shutil
import subprocess
import tempfile

DOCS_DIR = Path(__file__).resolve().parent
REPO_ROOT = DOCS_DIR.parent
HTML_PATH = DOCS_DIR / "slides.html"
PDF_REPO = DOCS_DIR / "fpa-valuechain-mc-presentation.pdf"
SLIDES_PNG_DIR = DOCS_DIR / "slides"
WORKSPACE_ROOT = Path(r"c:\Users\User\iCloudDrive\Learning-icloud")
PDF_WORKSPACE = WORKSPACE_ROOT / "FPA-Value-Chain-MC-Presentation.pdf"
HTML_STANDALONE = WORKSPACE_ROOT / "FPA-Value-Chain-MC-Presentation.html"

EDGE_CANDIDATES = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]


def find_edge() -> str:
    for path in EDGE_CANDIDATES:
        if os.path.exists(path):
            return path
    raise FileNotFoundError("Microsoft Edge executable not found for headless PDF rendering.")


def inline_images(html_text: str, base_dir: Path) -> str:
    """Embed relative PNG references as base64 data URIs so HTML works standalone anywhere."""
    pattern = re.compile(r'src="([^"]+\.png)"')

    def _repl(match: re.Match[str]) -> str:
        rel = match.group(1)
        img_path = (base_dir / rel).resolve()
        if not img_path.exists():
            return match.group(0)
        b64 = base64.b64encode(img_path.read_bytes()).decode("ascii")
        return f'src="data:image/png;base64,{b64}"'

    return pattern.sub(_repl, html_text)


def main() -> None:
    txt = HTML_PATH.read_text(encoding="utf-8")
    n_slides = txt.count('<section class="slide')
    if n_slides <= 0:
        raise ValueError("No slides found in slides.html")

    slide_idx = [0]

    def _sub_slide(_match: re.Match[str]) -> str:
        slide_idx[0] += 1
        return f"<span>Slide {slide_idx[0]} / {n_slides}</span>"

    txt = re.sub(r"<span>Slide \d+ / \d+</span>", _sub_slide, txt)

    wf_total = len(re.findall(r"Function Walkthrough \(\d+ / \d+\)", txt))
    wf_idx = [0]

    def _sub_wf(_match: re.Match[str]) -> str:
        wf_idx[0] += 1
        return f"Function Walkthrough ({wf_idx[0]} / {wf_total})"

    txt = re.sub(r"Function Walkthrough \(\d+ / \d+\)", _sub_wf, txt)
    HTML_PATH.write_text(txt, encoding="utf-8")

    thai_chars = re.findall(r"[\u0E00-\u0E7F]+", txt)
    if thai_chars:
        raise ValueError(f"Non-English Thai strings found in slides.html: {thai_chars[:5]}")

    if WORKSPACE_ROOT.exists():
        standalone_html = inline_images(txt, DOCS_DIR)
        HTML_STANDALONE.write_text(standalone_html, encoding="utf-8")

    edge = find_edge()
    udir = tempfile.mkdtemp(prefix="edge_pdf_")
    try:
        subprocess.run(
            [
                edge,
                "--headless=new",
                "--disable-gpu",
                f"--user-data-dir={udir}",
                "--no-sandbox",
                "--virtual-time-budget=3000",
                "--no-pdf-header-footer",
                f"--print-to-pdf={PDF_REPO}",
                "file:///" + str(HTML_PATH).replace("\\", "/"),
            ],
            check=True,
        )
    finally:
        shutil.rmtree(udir, ignore_errors=True)

    if WORKSPACE_ROOT.exists():
        shutil.copyfile(PDF_REPO, PDF_WORKSPACE)

    import fitz

    SLIDES_PNG_DIR.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(PDF_REPO)
    try:
        for i, page in enumerate(doc, 1):
            out_png = SLIDES_PNG_DIR / f"slide_{i:02d}.png"
            # 13.333in x 7.5in @ 120 DPI = 1600 x 900 crisp 16:9 PNGs
            page.get_pixmap(dpi=120).save(out_png)
        print(
            f"Slides: {n_slides} | Walkthroughs: {wf_total} | Thai: {len(thai_chars)} | "
            f"PDF pages: {doc.page_count} | PDF bytes: {PDF_REPO.stat().st_size} | "
            f"Standalone HTML bytes: {HTML_STANDALONE.stat().st_size if HTML_STANDALONE.exists() else 0}"
        )
    finally:
        doc.close()


if __name__ == "__main__":
    main()
