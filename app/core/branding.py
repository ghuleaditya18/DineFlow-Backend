import json
from pathlib import Path


_BASE_DIR = Path(__file__).resolve()
_BRANDING_PATH = next(
    (
        candidate
        for candidate in (
            _BASE_DIR.parents[2] / "shared" / "app_branding.json",
            _BASE_DIR.parents[3] / "shared" / "app_branding.json",
        )
        if candidate.is_file()
    ),
    _BASE_DIR.parents[2] / "shared" / "app_branding.json",
)
with _BRANDING_PATH.open(encoding="utf-8") as _branding_file:
    BRANDING = json.load(_branding_file)

APP_NAME = BRANDING["product_name"]
MODULE_NAMES = BRANDING["modules"]
