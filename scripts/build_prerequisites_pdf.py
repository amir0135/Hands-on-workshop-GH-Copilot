#!/usr/bin/env python3
"""Convert PREREQUISITES.md to PDF using markdown + cupsfilter (macOS built-in)."""
import subprocess
import sys
from pathlib import Path

import markdown

ROOT = Path(__file__).parent.parent
SRC = ROOT / "PREREQUISITES.md"
HTML = ROOT / "PREREQUISITES.html"
PDF = ROOT / "PREREQUISITES.pdf"

CSS = """
@page { size: A4; margin: 18mm 16mm; }
* { box-sizing: border-box; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  font-size: 11pt;
  line-height: 1.5;
  color: #1f2328;
  max-width: 100%;
  margin: 0;
  padding: 0;
}
h1 { font-size: 22pt; border-bottom: 2px solid #d0d7de; padding-bottom: 6px; margin-top: 0; }
h2 { font-size: 15pt; border-bottom: 1px solid #d0d7de; padding-bottom: 4px; margin-top: 22px; }
h3 { font-size: 12.5pt; margin-top: 16px; }
h4 { font-size: 11.5pt; }
p, li { font-size: 11pt; }
a { color: #0969da; text-decoration: none; }
hr { border: 0; border-top: 1px solid #d0d7de; margin: 18px 0; }
code {
  font-family: "SF Mono", Menlo, Consolas, monospace;
  background: #f6f8fa;
  padding: 1px 5px;
  border-radius: 4px;
  font-size: 10pt;
}
pre {
  background: #f6f8fa;
  padding: 10px 12px;
  border-radius: 6px;
  overflow-x: auto;
  page-break-inside: avoid;
}
pre code { background: transparent; padding: 0; font-size: 9.5pt; }
table { border-collapse: collapse; width: 100%; margin: 10px 0; page-break-inside: avoid; }
th, td { border: 1px solid #d0d7de; padding: 6px 10px; text-align: left; font-size: 10pt; vertical-align: top; }
th { background: #f6f8fa; }
blockquote {
  border-left: 4px solid #d0d7de;
  margin: 10px 0;
  padding: 4px 12px;
  color: #57606a;
  background: #f6f8fa;
}
ul, ol { padding-left: 22px; }
li { margin: 2px 0; }
"""


def main() -> int:
    md_text = SRC.read_text(encoding="utf-8")
    html_body = markdown.markdown(
        md_text,
        extensions=["extra", "tables", "fenced_code", "sane_lists", "toc"],
    )
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>GitHub Copilot Workshop — Prerequisites</title>
<style>{CSS}</style>
</head>
<body>
{html_body}
</body>
</html>"""
    HTML.write_text(html, encoding="utf-8")

    chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    result = subprocess.run(
        [
            chrome,
            "--headless=new",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={PDF}",
            HTML.as_uri(),
        ],
        capture_output=True,
    )
    if result.returncode != 0 or not PDF.exists():
        sys.stderr.write(result.stderr.decode(errors="replace"))
        return result.returncode or 1

    HTML.unlink(missing_ok=True)
    print(f"Wrote {PDF} ({PDF.stat().st_size:,} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
