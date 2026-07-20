from .logical_id import split_id, segment_count
from .registry import Registry

def classify(id_: str, registry: Registry, frontmatter: dict) -> tuple:
    """返回 (相对目录, 文件名)。文件名恒为 {id}.md（= 版本无关逻辑ID）。"""
    nf, typ, _local = split_id(id_)
    entry = registry.get(typ)
    if entry is None:
        raise ValueError(f"未知类型 {typ!r}（id={id_!r}）")
    filename = f"{id_}.md"
    if entry["scope"] == "nf":
        version = frontmatter.get("version")
        if not version:
            raise ValueError(f"NF 类 {typ} 缺 frontmatter.version（id={id_!r}）")
        # nf 以 id 段0 为准（权威），frontmatter.nf 仅校验
        layer = entry["layer"]
        return f"{layer}/{nf}/{version}", filename
    # cross
    layer = entry["layer"]
    parts = [layer]
    for field in entry.get("path_fields", []):
        v = frontmatter.get(field)
        if not v:
            raise ValueError(f"跨NF类 {typ} 缺 frontmatter.{field}（id={id_!r}）")
        parts.append(v)
    return "/".join(parts), filename
