"""License control item extraction from product markdown.

Each License control item in the source docs is represented as one markdown
subsection:

    #### [82209822 LKV3G5BCBC01 内容计费基本功能](...)
    | 归属NF | SGW-U、PGW-U、UPF |
    | --- | --- |
    | 功能描述 | ... |

The extractor keeps every source table row in *_raw fields, then derives
normalised fields from those raw values.
"""
from __future__ import annotations

import os
import re
from pathlib import Path


HEADING_RE = re.compile(r"^####\s+(?P<title>.+?)\s*$")
LINK_RE = re.compile(r"^\[(?P<label>[^\]]+)\]\([^)]*\)$")
ITEM_TITLE_RE = re.compile(
    r"^(?P<control_item_id>[A-Za-z0-9]+)\s+"
    r"(?P<license_code>[A-Za-z0-9]+)\s+"
    r"(?P<name>.+?)\s*$"
)
FEATURE_ID_RE = re.compile(r"\b(?:GWFD|WSFD|IPFD|NPFD|SFFD)-\d{6}\b")


RAW_FIELD_MAP = {
    "归属NF": "applicable_nf_raw",
    "适用NF": "applicable_nf_raw",
    "功能描述": "description_raw",
    "实现描述": "implementation_description_raw",
    "取值范围": "value_range_raw",
    "默认值": "default_value_raw",
    "对应特性": "feature_refs_raw",
    "相关控制项": "related_control_items_raw",
    "应用场景": "application_scenario_raw",
}


def extract_license_items(source: str | Path, project_root: str | Path, nf: str, version: str) -> list[dict]:
    source_path = Path(source)
    root_path = Path(project_root)
    items: list[dict] = []
    seen: set[str] = set()

    for md_path in sorted(source_path.rglob("*.md")):
        text = md_path.read_text(encoding="utf-8", errors="ignore")
        rel_source = _rel(md_path, source_path)
        license_domain = _license_domain(rel_source)
        control_item_type = _control_item_type(rel_source)

        for block in _iter_item_blocks(text):
            parsed = _parse_block(block)
            if not parsed:
                continue

            license_code = parsed["license_code"]
            item_id = f"{nf}@{version}@License@{license_code}"
            if item_id in seen:
                continue
            seen.add(item_id)

            rel_project = _rel(md_path, root_path)
            raw = parsed["raw_fields"]
            item = {
                "id": item_id,
                "nf": nf,
                "version": version,
                "source_path": rel_project,
                "source_heading_raw": parsed["source_heading_raw"],
                "applicable_nf_raw": raw.get("applicable_nf_raw", ""),
                "description_raw": raw.get("description_raw", ""),
                "implementation_description_raw": raw.get("implementation_description_raw", ""),
                "value_range_raw": raw.get("value_range_raw", ""),
                "default_value_raw": raw.get("default_value_raw", ""),
                "feature_refs_raw": raw.get("feature_refs_raw", ""),
                "related_control_items_raw": raw.get("related_control_items_raw", ""),
                "application_scenario_raw": raw.get("application_scenario_raw", ""),
                "control_item_id": parsed["control_item_id"],
                "license_code": license_code,
                "name": parsed["name"],
                "license_domain": license_domain,
                "control_item_type": control_item_type,
                "applicable_nf": normalize_nf(raw.get("applicable_nf_raw", "")),
                "feature_refs": extract_feature_refs(raw.get("feature_refs_raw", "")),
            }
            items.append(item)

    return items


def normalize_nf(value: str) -> list[str]:
    value = clean_text(value)
    if not value:
        return []
    if value.upper() == "ALL":
        return ["ALL"]
    parts = re.split(r"[、,，;/；]+", value)
    result = []
    for part in parts:
        token = clean_text(part)
        if token and token not in result:
            result.append(token)
    return result


def extract_feature_refs(value: str) -> list[str]:
    refs = []
    for match in FEATURE_ID_RE.findall(value or ""):
        if match not in refs:
            refs.append(match)
    return refs


def clean_text(value: str) -> str:
    value = value or ""
    value = value.replace("<br>", "\n")
    value = re.sub(r"\*\*", "", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def clean_key(value: str) -> str:
    value = value or ""
    value = re.sub(r"\*\*", "", value)
    return re.sub(r"\s+", " ", value).strip()


def raw_cell(value: str) -> str:
    return (value or "").strip()


def normalize_key(key: str) -> str:
    key = clean_key(key)
    if key.startswith("实现描述"):
        return "实现描述"
    return key


def _iter_item_blocks(text: str) -> Iterable[list[str]]:
    current: list[str] | None = None
    for line in text.splitlines():
        if HEADING_RE.match(line):
            if current:
                yield current
            current = [line]
            continue
        if current is not None:
            current.append(line)
    if current:
        yield current


def _parse_block(lines: list[str]) -> dict | None:
    heading = lines[0].strip()
    title = HEADING_RE.match(heading).group("title").strip()
    label = _heading_label(title)
    item_match = ITEM_TITLE_RE.match(label)
    if not item_match:
        return None

    raw_fields: dict[str, str] = {}
    for line in lines[1:]:
        row = _parse_table_row(line)
        if not row:
            continue
        key, value = row
        normalized = normalize_key(key)
        target = RAW_FIELD_MAP.get(normalized)
        if target:
            raw_fields[target] = raw_cell(value)

    return {
        "source_heading_raw": heading,
        "control_item_id": item_match.group("control_item_id"),
        "license_code": item_match.group("license_code"),
        "name": item_match.group("name").strip(),
        "raw_fields": raw_fields,
    }


def _heading_label(title: str) -> str:
    match = LINK_RE.match(title)
    return match.group("label").strip() if match else title.strip()


def _parse_table_row(line: str) -> tuple[str, str] | None:
    stripped = line.strip()
    if not stripped.startswith("|"):
        return None
    cells = [cell.strip() for cell in stripped.strip("|").split("|")]
    if len(cells) < 2:
        return None
    key, value = cells[0], "|".join(cells[1:]).strip()
    if re.fullmatch(r"-+", key) or re.fullmatch(r"-+", value):
        return None
    return key, value


def _license_domain(rel_path: str) -> str:
    parts = Path(rel_path).parts
    joined = "/".join(parts)
    if "Service Fabric License控制项" in joined:
        return "Service Fabric"
    if parts:
        first = parts[0]
        match = re.match(r"(.+?)\s+License控制项", first)
        if match:
            return match.group(1).strip()
    return ""


def _control_item_type(rel_path: str) -> str:
    name = Path(rel_path).name
    if "功能控制项" in name:
        return "function"
    if "资源控制项" in name:
        return "resource"
    # Service Fabric file has only resource-style numeric capacity control.
    if "Service Fabric License控制项" in rel_path:
        return "resource"
    return ""


def _rel(path: Path, root: Path) -> str:
    return os.path.relpath(str(path), str(root)).replace("\\", "/")
