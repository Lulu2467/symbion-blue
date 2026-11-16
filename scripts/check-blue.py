# -*- coding: utf-8 -*-
"""Check the blue prototype still matches the locked blue rules."""
import sys
from pathlib import Path

DEFAULTS = [
    Path(r"E:\file\研课symbion\homepage\H2-B-switching-twin-prototype.html"),
]

NEEDLES = {
    "--green: #008b68;": 1,
    "--green: #3c7a94;": 1,
    "--home-pair: 496px": 1,
    'data-plus="friend">Add a friend': 1,
    "padding: 1px 16px 0;": 2,
    "sheet:has(#friendResults) .sheet-actions { display: none; }": 1,
    "dir-enter:hover { background: #ebf5fa; border-color: #9eb8c6; }": 1,
    "set-nav button[data-set]:hover {\n    background: #f6f7f8; color: #1d1d1f;": 1,
    "background: #f6f7f8; color: #3c7a94; font-weight: 650;": 1,
    "padding: 16px 16px 14px; border-bottom: 1px solid #ededec;": 1,
    "padding: 12px 16px 8px 40px; font-size: 13px; line-height: 18px; color: #1d1d1f;": 1,
    "font: inherit; font-size: 13px; font-weight: 400; text-align: left; cursor: pointer; color: #1d1d1f;": 1,
    ".kd-label { padding: 0 16px; font-size: 13px; font-weight: 500; color: #8b9198; }": 1,
    "Type a name or an email to add someone.": 1,
    'data-rail-account="cosmos"><svg viewBox="0 0 1024 1024"': 1,
    "rail-me-menu button:hover svg { color: #3c7a94; }": 1,
}


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else next((p for p in DEFAULTS if p.exists()), None)
    if path is None or not path.exists():
        print("missing file")
        return 1
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    head, sep, tail = text.partition("</html>")
    failed = []
    if not sep or tail.strip():
        failed.append("html boundary")
    for needle, want in NEEDLES.items():
        got = body_count(head + sep, needle) if sep else text.count(needle)
        if got != want:
            failed.append(f"{got} != {want}: {needle}")
    if failed:
        print("\n".join(failed))
        return 1
    print(f"ok {path}")
    return 0


def body_count(body, needle):
    return body.count(needle)


if __name__ == "__main__":
    raise SystemExit(main())
