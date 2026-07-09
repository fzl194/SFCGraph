import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # platform-next/

import textwrap
import pytest


@pytest.fixture
def sample_assets(tmp_path: Path) -> Path:
    """微型 assets 样例树，覆盖命令/配置对象/特性/任务/证据 + 占位。"""
    root = tmp_path / "assets"
    (root / "command/UDG/20.15.2").mkdir(parents=True)
    (root / "configobject/UDG/20.15.2").mkdir(parents=True)
    (root / "feature/UDG/20.15.2").mkdir(parents=True)
    (root / "task/UDG/20.15.2").mkdir(parents=True)
    (root / "evidence/UDG/20.15.2").mkdir(parents=True)

    (root / "command/UDG/20.15.2/ADD-URR.md").write_text(textwrap.dedent("""\
        ---
        id: UDG@20.15.2@MMLCommand@ADD URR
        type: MMLCommand
        name: ADD URR
        nf: UDG
        version: 20.15.2
        verb: ADD
        object_keyword: URR
        category_path:
        - 用户面服务管理
        - 计费控制
        status: active
        ---
        # ADD URR（增加URR）

        ## 操作的配置对象

        - [URR](configobject/UDG/20.15.2/URR.md)

        ## 关联任务

        - [0-00001](task/UDG/20.15.2/0-00001.md)

        ## 证据

        - 原始手册：`evidence/UDG/20.15.2/增加URR（ADD-URR）_82837629.md`
    """), encoding="utf-8")

    (root / "configobject/UDG/20.15.2/URR.md").write_text(textwrap.dedent("""\
        ---
        id: UDG@20.15.2@ConfigObject@URR
        type: ConfigObject
        name: URR
        nf: UDG
        version: 20.15.2
        object_kind: entity
        status: active
        ---
        # URR

        ## 操作本对象的命令

        - [ADD URR](command/UDG/20.15.2/ADD-URR.md)
    """), encoding="utf-8")

    (root / "feature/UDG/20.15.2/GWFD-020350.md").write_text(textwrap.dedent("""\
        ---
        id: UDG@20.15.2@Feature@GWFD-020350
        type: Feature
        name: 计费基础特性
        nf: UDG
        version: 20.15.2
        feature_category: 计费
        status: active
        ---
        # 计费基础特性
    """), encoding="utf-8")

    (root / "feature/UDG/20.15.2/GWFD-020351.md").write_text(textwrap.dedent("""\
        ---
        id: UDG@20.15.2@Feature@GWFD-020351
        type: Feature
        name: 在线计费
        nf: UDG
        version: 20.15.2
        feature_category: 计费
        parent_feature_code: GWFD-020350
        status: active
        ---
        # 在线计费
    """), encoding="utf-8")

    (root / "task/UDG/20.15.2/0-00001.md").write_text(textwrap.dedent("""\
        ---
        id: UDG@20.15.2@Task@0-00001
        type: Task
        task_layer: atom
        name: 配置URR
        ref: UDG@20.15.2@MMLCommand@ADD URR
        status: inferred
        ---
        # 配置URR（ADD URR）

        ## 命令

        命令静态知识见 [ADD URR](command/UDG/20.15.2/ADD-URR.md)。关联对象 [[UDG@20.15.2@ConfigObject@URRGROUP]] 待建。
    """), encoding="utf-8")

    (root / "evidence/UDG/20.15.2/增加URR（ADD-URR）_82837629.md").write_text("# 手册原文\n", encoding="utf-8")
    return root
