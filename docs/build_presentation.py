#!/usr/bin/env python3
"""Renumber slide footers cleanly, enforce English-only presentation text, and export print-ready 16:9 PDF."""

from pathlib import Path
import os
import re
import shutil
import subprocess
import tempfile

DOCS_DIR = Path(__file__).resolve().parent
REPO_ROOT = DOCS_DIR.parent
HTML_PATH = DOCS_DIR / "slides.html"
PDF_REPO = DOCS_DIR / "fpa-valuechain-mc-presentation.pdf"
PDF_WORKSPACE = Path(r"c:\Users\User\iCloudDrive\Learning-icloud\FPA-Value-Chain-MC-Presentation.pdf")
PNG_CHECK_DIR = Path(
    r"C:\Users\User\.gemini\antigravity\brain\4efd6045-983c-4279-bc51-6a1ee8d1d8e1\scratch\slides_check_v3"
)

EDGE_CANDIDATES = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
]


def find_edge() -> str:
    for path in EDGE_CANDIDATES:
        if os.path.exists(path):
            return path
    raise FileNotFoundError("Microsoft Edge executable not found for headless PDF rendering.")


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

    if PDF_WORKSPACE.parent.exists():
        shutil.copyfile(PDF_REPO, PDF_WORKSPACE)

    import fitz

    PNG_CHECK_DIR.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(PDF_REPO)
    try:
        for i, page in enumerate(doc, 1):
            page.get_pixmap(dpi=130).save(PNG_CHECK_DIR / f"slide_{i:02d}.png")
        print(
            f"Slides: {n_slides} | Walkthroughs: {wf_total} | Thai: {len(thai_chars)} | "
            f"PDF pages: {doc.page_count} | Bytes: {PDF_REPO.stat().st_size}"
        )
    finally:
        doc.close()


if __name__ == "__main__":
    main()
