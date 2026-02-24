from pathlib import Path
from sys import exit

src = Path("README.md")
dst = Path("docs") / "index.md"
dst.parent.mkdir(parents=True, exist_ok=True)
data = src.read_bytes()
old = dst.read_bytes() if dst.exists() else None
if old != data:
    dst.write_bytes(data)
    exit(1)
else:
    exit(0)
