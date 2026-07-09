"""wiki 索引数据模型（不可变）。"""
from dataclasses import dataclass


@dataclass(frozen=True)
class Node:
    path: str            # assets 根相对路径, 如 command/UDG/20.15.2/ADD-URR.md
    id: str              # front-matter id
    type: str            # ObjectType: MMLCommand/ConfigObject/Feature/License/Task/...
    name: str
    nf: str | None
    version: str | None
    status: str
    title: str           # 首个 H1 或 name
    group: tuple[tuple[str, str], ...]  # 分组字段, 如 (("category_path","用户面服务管理/..."),("verb","ADD"))


@dataclass(frozen=True)
class Edge:
    src: str             # 源 node path（必为真实文件）
    dst: str             # 目标 path（resolved）或 对象ID（未解析占位）
    relation_type: str
    resolved: bool       # dst 是否有对应文件


@dataclass(frozen=True)
class Index:
    nodes: dict[str, Node]                       # path -> Node
    id_to_path: dict[str, str]                   # 对象ID -> path
    out_edges: dict[str, tuple[Edge, ...]]       # src path -> 出向边
    reverse: dict[str, tuple[str, ...]]          # dst path -> 源 path 列表（反链）
