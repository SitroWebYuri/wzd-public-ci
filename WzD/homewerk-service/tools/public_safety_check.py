from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

BLOCKED_NAME_PREFIXES = (
    "STAGE_",
    "H",
)

BLOCKED_SUFFIXES = {
    ".env",
    ".pdf",
    ".zip",
    ".7z",
    ".rar",
    ".jpg",
    ".jpeg",
    ".png",
    ".webp",
    ".heic",
    ".xlsx",
    ".docx",
    ".pem",
    ".key",
    ".p12",
    ".pfx",
}

BLOCKED_PARTS = {
    "secrets",
    "private",
    "scans",
    "photos",
    "invoices",
    "receipts",
    "artifacts",
    "exports",
    "node_modules",
    "__pycache__",
    ".pytest_cache",
    ".venv",
    "venv",
}

SUSPICIOUS_TEXT = (
    "BEGIN PRIVATE KEY",
    "BEGIN RSA PRIVATE KEY",
    "api_key=",
    "apikey=",
    "secret_key=",
    "password=",
    "token=",
    "access_token=",
    "refresh_token=",
)

ALLOWED_STAGE_FILES = set()


def is_blocked_path(path: Path) -> str | None:
    rel = path.relative_to(ROOT)
    parts = set(rel.parts)
    lower_name = path.name.lower()

    if parts & BLOCKED_PARTS:
        return f"blocked directory part: {sorted(parts & BLOCKED_PARTS)}"

    if lower_name in {".env", ".env.local", ".env.production"}:
        return "blocked env file"

    if any(lower_name.endswith(suffix) for suffix in BLOCKED_SUFFIXES):
        return f"blocked file suffix: {path.suffix}"

    if path.name.startswith("STAGE_") and str(rel) not in ALLOWED_STAGE_FILES:
        return "blocked private stage report"

    if path.name.startswith("H") and path.name.endswith(".md") and path.parent.name == "WzD":
        return "blocked private handoff"

    return None


def main() -> None:
    failures: list[str] = []

    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if ".git" in path.parts:
            continue

        reason = is_blocked_path(path)
        if reason:
            failures.append(f"{path.relative_to(ROOT)}: {reason}")
            continue

        if path.suffix.lower() in {".py", ".js", ".ts", ".tsx", ".json", ".yml", ".yaml", ".md", ".txt", ".sh"}:
            text = path.read_text(encoding="utf-8", errors="ignore")
            lower = text.lower()
            for marker in SUSPICIOUS_TEXT:
                if marker.lower() in lower:
                    failures.append(f"{path.relative_to(ROOT)}: suspicious text marker {marker!r}")

    if failures:
        print("Public safety check failed:")
        for failure in failures:
            print("-", failure)
        raise SystemExit(1)

    print("public-safety-ok")


if __name__ == "__main__":
    main()
