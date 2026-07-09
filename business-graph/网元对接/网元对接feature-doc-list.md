# 网元对接 引用特性清单（UPF网元对接子场景）

> Stage 1 产出 | 17个被初始配置文档引用的特性
> 反查源：`FeatureGraph/data/UDG/20.15.2/features.jsonl`（主表）+ `feature_relations.jsonl`（依赖）+ `feature_requires_license.jsonl`（License）
> 特性是**引用支撑**（非图谱主体），知识文档为精简版（见 `feature-knowledge/`）

---

## 特性总表（按 EV-FK 编号，feature_code 字母序）

| EV-FK | feature_code | 名称 | category | config_relevance | 目录特性 | 文档引用次数 | 主要对接面 | 反查状态 |
|-------|-------------|------|----------|------------------|---------|------------|-----------|---------|
| EV-FK-01 | GWFD-010105 | 用户面地址分配 | base | required | 否 | 4 | CS-2用户面 | ✓UDG |
| EV-FK-02 | GWFD-010234 | Single IP | base | none | 否 | 10 | CS-4路由 | ✓UDG |
| EV-FK-03 | GWFD-020161 | CU Full Mesh组网 | base | required | 否 | 3 | CS-4路由 | ✓UDG |
| EV-FK-04 | GWFD-020411 | MPLS VPN | base | required | 否 | 5 | CS-4路由 | ✓UDG |
| EV-FK-05 | GWFD-020421 | 基于位置的地址分配 | base | required | 否 | 4 | CS-2用户面 | ✓UDG |
| EV-FK-06 | IPFD-010000 | 接口与链路 | base | required | **是** | 2 | CS-1/CS-2接口 | ✓UDG(父目录) |
| EV-FK-07 | IPFD-010001 | 接口管理 | base | required | 否 | 6 | CS-1/CS-2接口 | ✓UDG |
| EV-FK-08 | IPFD-012000 | IP可靠性 | base | required | **是** | 20 | CS-4路由 | ✓UDG(父目录) |
| EV-FK-09 | IPFD-012003 | BFD | base | required | 否 | 57 | CS-4路由 | ✓UDG |
| EV-FK-10 | IPFD-014000 | 路由功能 | base | required | **是** | 32 | CS-4路由 | ✓UDG(父目录) |
| EV-FK-11 | IPFD-014001 | 支持OSPF | base | required | 否 | 18 | CS-4路由 | ✓UDG |
| EV-FK-12 | IPFD-014002 | 支持BGP | base | required | 否 | 46 | CS-4路由 | ✓UDG |
| EV-FK-13 | IPFD-014003 | 静态路由 | base | required | 否 | 18 | CS-4路由 | ✓UDG |
| EV-FK-14 | IPFD-015004 | IPSec功能 | base | required | 否 | 6 | CS-4路由 | ✓UDG |
| EV-FK-15 | IPFD-104403 | （未收录） | - | - | - | 3 | CS-4路由(待核实) | ⚠️UDG+UNC均未找到 |
| EV-FK-16 | NPFD-010000 | 操作维护功能 | operations | ops_only | **是** | 1 | CS-3网管/CS-5基础 | ✓UDG(父目录) |
| EV-FK-17 | NPFD-010014 | 支持NTP功能 | operations | ops_only | 否 | 1 | CS-5基础就绪 | ✓UDG |

---

## 特性分布分析

### 按对接面分布（印证"路由对接CS-4是主体"）
- **CS-4 路由对接（★主力）**：IPFD-012003/014002/014000/012000/014003/014001/015004 + GWFD-020411/020161/010234 + IPFD-104403 = **11个特性**，引用次数合计 ~218（占绝对多数）
- **CS-2 用户面对接**：GWFD-010105(用户面地址分配)、GWFD-020421(基于位置的地址分配) + 接口特性(IPFD-010000/010001)
- **CS-1 控制面对接(N4)**：IPFD-010000/010001(接口与链路/接口管理)
- **CS-3 网管对接**：NPFD-010000(操作维护功能)
- **CS-5 基础就绪**：NPFD-010014(NTP)、NPFD-010000(操作维护)

### 按前缀汇总
- IPFD（IP转发/路由）：10个，引用208次 → **路由对接域的绝对核心**
- GWFD（网关功能）：5个，引用26次
- NPFD（操作维护）：2个，引用2次

### config_relevance 分布
- required（需配置）：15个 → 图谱第2层主体
- none：GWFD-010234(Single IP) → 仅基础能力，无需显式配置
- ops_only：NPFD-010000/010014 → 操作维护类，CS-3/CS-5

---

## 待核实项

| 项 | 说明 | 处理 |
|----|------|------|
| IPFD-104403 | UDG+UNC features.jsonl 均未收录，仅在原始文档引用3次（集中在BGP over静态路由SDN文档） | 特性轨核实原文上下文；可能是子特性/笔误/未收录特性；不阻塞主体（特性是配角） |
| 目录特性(is_directory=true) | IPFD-010000/012000/014000、NPFD-010000 是父目录特性 | 特性轨文档标注其为父目录，角色说明其统辖的子能力 |

---

## 质量门禁
- [x] 17引用特性全部抽取并编号 EV-FK-01~17
- [x] 16/17 在 FeatureGraph 反查到（IPFD-104403 待核实）
- [x] 对接面映射完成（IPFD路由类集中CS-4，印证主体）
- [x] 引用次数统计完成
