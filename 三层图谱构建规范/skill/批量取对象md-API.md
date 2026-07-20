# 批量取对象 Markdown API

> 供 Agent / SKILL 批量读取三层图谱对象的原始 markdown。
> 典型场景：Agent 逐层（业务层 → 特性层 → 任务层 → 命令层）批次拉取对象 md，逐步理解配置知识。

---

## 1. 用途

一次 POST 传入 1 个或多个对象 ID，返回每个 ID 对应的原始 markdown。

- **批量**：一次请求取任意多个 ID，避免逐个 GET 的往返开销。
- **部分失败容错**：某个 ID 不存在或版本不匹配，只该条计错，其余照常返回。
- **Agent 友好**：每个 ID 恰好一个条目，结构稳定，便于程序化遍历。

---

## 2. 端点

```
POST {BASE_URL}/api/v1/md
Content-Type: application/json
```

> `BASE_URL` 默认 `http://127.0.0.1:8000`（后端 `uvicorn` 启动地址）。

---

## 3. 请求体

| 字段 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `ids` | `string[]` | 是 | 对象 ID 列表，至少 1 个。ID 是版本无关逻辑 ID，可含 `@` 与空格（如 `UDG@MMLCommand@ADD URR`）。重复 ID 自动去重。 |
| `version` | `string\|null` | 否 | 全局版本号。**不传或 `null` → 每个 ID 各自取最新现存版本**。若某 ID 不在该版本，该条计错并回带可用版本。 |

**请求示例**：

```json
{
  "ids": [
    "UDG@MMLCommand@ADD URR",
    "UDG@ConfigObject@URR",
    "不存在的@ID"
  ],
  "version": "20.15.2"
}
```

---

## 4. 响应体

`200 OK`，JSON 对象 —— **key 是请求里的 ID，value 是结果条目**。每个条目二选一：

### 4.1 成功条目

```json
{
  "version": "20.15.2",
  "md": "# ADD URR\n## 参数\n..."
}
```

| 字段 | 类型 | 说明 |
|---|---|---|
| `version` | `string\|null` | 实际命中的版本。不传 `version` 时为该 ID 最新现存版本；跨 NF 类（业务层 BusinessDomain 等）恒为 `null`。 |
| `md` | `string` | 原始 markdown 全文，**含 frontmatter + `## 边` 声明 + 正文**（与 `GET /objects/{id}/md` 同源）。 |

### 4.2 失败条目

```json
{
  "error": "对象不存在",
  "available_versions": []
}
```

| 字段 | 类型 | 说明 |
|---|---|---|
| `error` | `string` | 失败原因。`"对象不存在"`（ID 完全不在库中）或 `"版本不存在: {id}@{version}"`（ID 在但指定版本缺失）。 |
| `available_versions` | `string[]` | 该 ID 的全部可用版本。ID 不存在时为 `[]`；版本不匹配时列出所有版本，供 Agent 改版本重试。 |

### 4.3 完整响应示例

```json
{
  "UDG@MMLCommand@ADD URR": {
    "version": "20.15.2",
    "md": "---\nid: UDG@MMLCommand@ADD URR\ntype: MMLCommand\n...\n---\n# ADD URR\n## 参数\n..."
  },
  "UDG@ConfigObject@URR": {
    "version": "20.15.2",
    "md": "---\nid: UDG@ConfigObject@URR\n...\n---\n# URR\n..."
  },
  "不存在的@ID": {
    "error": "对象不存在",
    "available_versions": []
  }
}
```

---

## 5. 版本解析规则

复用单对象版本解析（与 `GET /objects/{id}` 同语义）：

| 请求 | 行为 |
|---|---|
| 不传 `version` | 每个 ID 落到**各自最新现存版本**（语义化取最大）。若某 ID 仅存于旧版本，落到旧版本，不报错。 |
| 传 `version=X` | 每个 ID 取 `(id, X)` 实例。某 ID 不在 X → 该条计错，回带 `available_versions`，**不影响其余 ID**。 |

> 注意：批量场景下不同 ID 可能属于不同 NF、各自版本集合不同。传全局 `version` 时，对不在该版本的 ID 会被计错但不会拖垮整批——Agent 可据 `available_versions` 改版本重试，或干脆不传 `version` 让每个 ID 各取最新。

---

## 6. 调用示例

### 6.1 curl

```bash
curl -X POST http://127.0.0.1:8000/api/v1/md \
  -H "Content-Type: application/json" \
  -d '{
    "ids": ["UDG@MMLCommand@ADD URR", "UDG@ConfigObject@URR"],
    "version": "20.15.2"
  }'
```

### 6.2 Python（requests）

```python
import requests

BASE_URL = "http://127.0.0.1:8000"

def fetch_md(ids: list[str], version: str | None = None) -> dict:
    """批量取对象 md。返回 {id: {version, md} | {error, available_versions}}。"""
    resp = requests.post(
        f"{BASE_URL}/api/v1/md",
        json={"ids": ids, "version": version},
        timeout=60,
    )
    resp.raise_for_status()
    return resp.json()


# 用法:只取成功的 md,失败的收集起来重试
data = fetch_md(["UDG@MMLCommand@ADD URR", "UDG@ConfigObject@URR"])
md_map = {}
failed = []
for id_, item in data.items():
    if "md" in item:
        md_map[id_] = item["md"]
    else:
        failed.append((id_, item["error"], item["available_versions"]))
```

---

## 7. Agent 逐层批次调用模式（推荐）

核心组合：**先用 `GET /objects?layer=` 拿某层 ID 列表，再用 `POST /md` 批量取 md**。

### 7.1 两步法

```
步骤 1: GET /api/v1/objects?layer=任务层&nf=UDG&version=20.15.2
        → 拿到该层所有对象 ID 列表

步骤 2: POST /api/v1/md  body={"ids": [<上一步的 ID 列表>], "version": "20.15.2"}
        → 一次性拿到这层全部 md
```

### 7.2 逐层下钻伪代码

```python
# 1. 业务层 → 特性层 → 任务层 → 命令层,逐层批次取
for layer in ["业务层", "特性层", "任务层", "命令层"]:
    ids = requests.get(
        f"{BASE_URL}/api/v1/objects",
        params={"layer": layer, "nf": "UDG", "version": "20.15.2"},
    ).json()
    id_list = [row["id"] for row in ids]
    mds = fetch_md(id_list, version="20.15.2")
    # 处理本层 md ...
```

### 7.3 沿边跨层下钻

对象 md 的 `## 边` 段或正文里的 `[[wikilink]]` 指向关联对象。Agent 解析出这些 ID 后，可继续 `POST /md` 批量取下一批：

```python
# 拿到一批 md 后,解析其中的 [[ID]] 引用,作为下一批要取的 ID
import re
next_ids = set()
for md in md_map.values():
    next_ids.update(re.findall(r"\[\[([^\]]+)\]\]", md))
# 去掉已取过的,再批量取
new_ids = [i for i in next_ids if i not in md_map]
if new_ids:
    fetch_md(new_ids, version="20.15.2")
```

---

## 8. 错误处理建议

| 场景 | 建议 |
|---|---|
| HTTP 422 | `ids` 为空数组。请求体不合法,Agent 应修正后重试。 |
| 条目含 `error: "对象不存在"` | ID 写错了或库里没有。跳过或向用户反馈。 |
| 条目含 `error: "版本不存在"` + 非空 `available_versions` | 改用 `available_versions` 里的版本重试,或干脆不传 `version` 取最新。 |
| 网络超时 | 单次批量建议控制在几十到上百个 ID;超大批次可分批。 |

---

## 9. 配套端点速查

| 端点 | 用途 |
|---|---|
| `GET /api/v1/objects?layer=&nf=&version=&type=&q=&page=&size=` | 按 UI 层（命令层/特性层/任务层/业务层）列对象 ID,用于拼 `POST /md` 的 `ids`。 |
| `GET /api/v1/objects/{id}` | 单对象详情 + 出边（解析 md 里 `[[wikilink]]` 的辅助校验）。 |
| `GET /api/v1/objects/{id}/neighbors` | 单跳邻居（跨层）,用于沿边下钻。 |
| `GET /api/v1/objects/{id}/md` | 单对象原始 md（非批量场景）。 |
| `GET /api/v1/names` | `{id: name}` 字典,把 md 里的 `[[ID]]` 渲染成可读名。 |
| `GET /api/v1/stats` | 按 UI 层聚合的对象/边统计（了解库存量）。 |

---

## 10. UI 层 → 对象类型 对照

`POST /md` 不分层,任何对象 ID 都能取。但配合 `GET /objects?layer=` 时要知道每层包含哪些 type：

| UI 层 | registry 类型 |
|---|---|
| 命令层 | `MMLCommand`, `ConfigObject` |
| 特性层 | `Feature`, `License` |
| 任务层 | `Task`, `AtomTask`, `CompoundTask`, `FeatureTask` |
| 业务层 | `BusinessDomain`, `NetworkScenario`, `ConfigurationSolution` |

> ID 格式：`{nf}@{type}@{name}`（NF 类,3 段）或 `{domain}@{type}@{name}`（跨 NF 业务类,2 段）。`@` 与空格在 JSON body 里无需转义。
