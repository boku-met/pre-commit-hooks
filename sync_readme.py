from pathlib import Path

src=Path("README.md")
dst=Path("docs") / "README.md"
dst.parent.mkdir(parents=True, exist_ok=True)
data=src.read_bytes()
old=dst.read_bytes() if dst.exists() else None
(old!=data) and dst.write_bytes(data)