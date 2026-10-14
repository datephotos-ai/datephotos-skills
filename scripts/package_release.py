#!/usr/bin/env python3
"""Build a release from an explicit public-file allowlist."""
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
VERSION = "0.1.0"
FILES = [
    "README.md", "LICENSE",
    "skills/dating-profile-coach/SKILL.md",
    "skills/dating-profile-coach/LICENSE",
    "skills/dating-profile-coach/agents/openai.yaml",
    "skills/dating-profile-coach/references/photo-checklist.md",
    "skills/dating-profile-coach/references/bio-and-openers.md",
    "skills/dating-profile-coach/references/report-template.md",
    "examples/hinge-review.md",
]


def build(destination):
    destination = Path(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    # Validate every input before replacing any prior package.
    payloads = []
    for relative in FILES:
        path = ROOT / relative
        if not path.is_file() or path.is_symlink() or ROOT not in path.resolve().parents:
            raise ValueError(f"Not a regular public release file: {relative}")
        payloads.append((relative, path.read_bytes()))
    temporary = destination.with_suffix(".tmp")
    with zipfile.ZipFile(temporary, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for relative, content in sorted(payloads):
            item = zipfile.ZipInfo("datephotos-skills/" + relative, date_time=(2026, 10, 14, 0, 0, 0))
            item.compress_type = zipfile.ZIP_DEFLATED
            item.external_attr = 0o100644 << 16
            archive.writestr(item, content)
    temporary.replace(destination)
    return destination


if __name__ == "__main__":
    print(build(ROOT / f"dist/datephotos-skills-{VERSION}.zip"))
