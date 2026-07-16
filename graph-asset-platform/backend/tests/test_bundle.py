import io
import zipfile

from app.bundle import import_bundle, BundleResult
from app.store import Store
from app.registry import Registry


def _zip(files: dict) -> bytes:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        for name, content in files.items():
            z.writestr(name, content)
    return buf.getvalue()


CMD = (
    "---\n"
    "id: UDG@MMLCommand@ADD URR\n"
    "type: MMLCommand\n"
    "nf: UDG\n"
    "version: 20.15.2\n"
    "---\n"
    "# x\n"
)
CFG = (
    "---\n"
    "id: UDG@ConfigObject@URR\n"
    "type: ConfigObject\n"
    "nf: UDG\n"
    "version: 20.15.2\n"
    "---\n"
    "# y\n"
)


# ---------- 导入 ----------

def test_import_classifies_and_writes(tmp_data_dir):
    store = Store(tmp_data_dir)
    # 任意源排布：zip 内文件名/目录与最终归一化路径无关，平台只认 frontmatter
    data = _zip({"随便/flat.md": CMD, "ConfigObject/UDG/20.15.2/URR.md": CFG})
    res = import_bundle(data, store, Registry.load_default())
    assert res.added == 2 and res.updated == 0
    # 统一归一化路径
    assert store.exists("Command/UDG/20.15.2/UDG@MMLCommand@ADD URR.md")
    assert store.exists("ConfigObject/UDG/20.15.2/UDG@ConfigObject@URR.md")


def test_import_update_same_id_version(tmp_data_dir):
    store = Store(tmp_data_dir)
    import_bundle(_zip({"a.md": CMD}), store, Registry.load_default())
    # 同 id 同版本 = 更新（后传覆盖先传）
    res2 = import_bundle(_zip({"b.md": CMD}), store, Registry.load_default())
    assert res2.updated == 1 and res2.added == 0
    # 文件被覆盖（仍是 1 个文件）
    assert len(store.list_md()) == 1


def test_import_new_version_adds(tmp_data_dir):
    store = Store(tmp_data_dir)
    import_bundle(_zip({"a.md": CMD}), store, Registry.load_default())
    cmd_new_ver = CMD.replace("version: 20.15.2", "version: 20.16.0")
    res2 = import_bundle(_zip({"b.md": cmd_new_ver}), store, Registry.load_default())
    # 同 id 不同版本 → 新增一条版本记录
    assert res2.added == 1 and res2.updated == 0
    assert store.exists("Command/UDG/20.15.2/UDG@MMLCommand@ADD URR.md")
    assert store.exists("Command/UDG/20.16.0/UDG@MMLCommand@ADD URR.md")


def test_import_skips_invalid_and_warns(tmp_data_dir):
    store = Store(tmp_data_dir)
    bad = "---\ntype: MMLCommand\n---\nno id\n"   # 缺 id
    res = import_bundle(_zip({"bad.md": bad, "good.md": CMD}), store, Registry.load_default())
    assert res.added == 1
    assert any("bad.md" in w for w in res.warnings)


def test_import_skips_unknown_type(tmp_data_dir):
    store = Store(tmp_data_dir)
    unknown = (
        "---\n"
        "id: UDG@WTF@x\n"
        "type: WTF\n"
        "version: 20.15.2\n"
        "---\nx\n"
    )
    res = import_bundle(_zip({"unk.md": unknown, "good.md": CMD}), store, Registry.load_default())
    assert res.added == 1
    assert any("WTF" in w for w in res.warnings)


def test_import_merges_types_extension(tmp_data_dir):
    store = Store(tmp_data_dir)
    registry = Registry.load_default()
    assert not registry.known("Widget")
    # bundle 携带扩展类型
    ext_yaml = (
        "layer: Widget\n"
        "scope: nf\n"
        "id_segments: 3\n"
        "frontmatter_required: [id, type, nf, version]\n"
    )
    widget_md = (
        "---\n"
        "id: UDG@Widget@w1\n"
        "type: Widget\n"
        "nf: UDG\n"
        "version: 20.15.2\n"
        "---\n# widget\n"
    )
    res = import_bundle(_zip({"types/Widget.yaml": ext_yaml, "w.md": widget_md}),
                        store, registry)
    # 合并后该类型可用，对象被归一化写入
    assert registry.known("Widget")
    assert res.added == 1
    assert store.exists("Widget/UDG/20.15.2/UDG@Widget@w1.md")


def test_import_cross_nf_object(tmp_data_dir):
    store = Store(tmp_data_dir)
    ns_md = (
        "---\n"
        "id: NetworkScenario@demo\n"
        "type: NetworkScenario\n"
        "domain: demo\n"
        "scenario: demo\n"
        "---\n# ns\n"
    )
    res = import_bundle(_zip({"ns.md": ns_md}), store, Registry.load_default())
    assert res.added == 1
    assert store.exists("Business/demo/demo/NetworkScenario@demo.md")


def test_import_empty_bundle(tmp_data_dir):
    store = Store(tmp_data_dir)
    res = import_bundle(_zip({}), store, Registry.load_default())
    assert res.added == 0 and res.updated == 0
    assert len(store.list_md()) == 0


def test_import_non_md_files_ignored(tmp_data_dir):
    store = Store(tmp_data_dir)
    res = import_bundle(_zip({"readme.txt": "hi", "a.md": CMD}), store, Registry.load_default())
    assert res.added == 1
    assert len(store.list_md()) == 1
