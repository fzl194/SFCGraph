# APN 业务域命令图谱 · 簇E：IPFD-015002 GRE（UDG + UNC 共用特性）

> **文件定位**：`three-layer-graph/draft/04-cluster-E-GRE-015002.md`
> **特性范围**：IPFD-015002 GRE（通用路由封装），UDG + UNC 共用，4 个配置子场景（基础 GRE 隧道 / Keepalive 检测 / 多租户共享 GRE / GRE over IPsec 编排入口）
> **Schema参考**：`三层图谱Schema-最终版-v0.1.md` §11 命令图谱（§11.3 MMLCommand / §11.4 CommandParameter / §11.5 ConfigObject / §11.6 CommandRule / §11.7 关系边）
> **结构对齐**：严格 follow 样板 `04-cluster-B-GWFD-010105.md`（表格列、`CMD-UDG-015002-xx` / `CMD-UNC-015002-xx` 编号、9 节组织、§5 参数表、§6 operates_on 边）
> **数据来源**：UDG 调测文档 1 篇 + UNC 概述/原理/激活/去激活文档 5 篇 + GRE 命令族 MML 手册原文（ADD/MOD/RMV/LST GRETUNNEL，UDG/UNC 手册同源同 id）
> **铁律**：命令/参数 100% 来自原始产品文档原文，零编造。手册未定位的命令标注「⚠️手册未定位」。
> **★复用声明**：`ADD GRETUNNEL`（18 参数全表）已在簇E IPSec draft `04-cluster-E-IPSec-015004.md` §5.18（`CMD-UDG-015004-19`）完整抽取并标注 17 参数行。本特性 ADD GRETUNNEL 命令族与 IPSec 场景**完全同源同一手册**（手册 id `_00841729` UDG/UNC 一致），故本文件**引用不重复抽全参数**，仅在 §1 登记 + §5.1 列参数清单 + §5.2 补 GRE 独有差异（Keepalive / GRE Key / 多租户 key 区分 / 嵌套约束），并把该命令的 `used_by_features` 扩展为 `IPFD-015004 IPSec + IPFD-015002 GRE`。

---

## 0. 命令清单总览（IPFD-015002 GRE 用到的全部命令）

### 0.1 按命令类型分布

| 类型 | 命令数 | 命令清单 |
|------|-------|---------|
| 配置类（ADD/MOD/RMV） | 3 | ADD GRETUNNEL（★复用 IPSec draft）、MOD GRETUNNEL（UNC 激活文档脚本中用于使能 Checksum/GRE Key/Keepalive）、RMV GRETUNNEL（UNC 去激活） |
| 查询类（LST/DSP） | 2 | LST GRETUNNEL（验证配置）、DSP TUNNELINFO（UDG 调测隧道状态，调测查询类，本期略参数） |
| 调测类（DSP GRE*） | 5 | DSP GREMSGSTATINFO / DSP GRETNLINFO / DSP GRETNLTAB / DSP GREPKTSTAT / DSP GRETNLSTAT（GRE 诊断/统计族，调测查询类，本期略参数） |
| Keepalive 计数类 | 2 | DSP GREKPLVSTAT（查询 Keepalive 报文计数）、RTR GREKPLVSTAT（重置计数）（调测查询类，本期略参数） |
| 前置依赖类（非本特性核心，但在激活脚本中出现） | 5 | ADD INTERFACE、ADD IFIPV4ADDRESS、MOD INTERFACE（MTU 调整）、ADD SRROUTE（隧道间静态路由）、ADD L3VPNINST（DSTVPNNAME 引用，VPN 组网场景）（归属簇A/簇E，本文件不重复抽参数，仅在 §6 operates_on 边中标注引用关系） |
| 调测连通性 | 1 | PING（UDG 调测步骤 2，调测类，本期略参数） |

> **★说明**：MOD GRETUNNEL 在 UNC 激活文档脚本（`激活支持GRE_06422610.md` 行 172-184）中用于「使能 Checksum / GRE Key / Keepalive」。手册 `_50121682`（修改GRE隧道）已定位，其参数集与 ADD GRETUNNEL 一致（同 18 参数，区别仅 verb=MOD，操作目标必须先存在）。本文件登记为 `CMD-UNC-015002-02`，参数表引用 §5.1（ADD/MOD 同表），不重复列。
> **★UDG vs UNC 差异**：UDG 产品文档**仅提供调测文档**（`调测GRE_06422611.md`），未提供独立的「激活/去激活」特性配置文档；UNC 提供完整的「激活支持GRE / 去激活支持GRE」特性配置文档。GRE 命令族手册 UDG 与 UNC **同源同 id**（`_00841729` 等），即命令能力两侧完全一致；UDG 通过调测文档（DSP TUNNELINFO + LST GRETUNNEL + PING）+ 命令手册使用 GRE，UNC 通过激活文档显式编排 ADD/MOD GRETUNNEL。

### 0.2 ConfigObject 分布（本特性涉及）

| 功能域 | 对象数 | 关键对象 |
|-------|-------|---------|
| GRE 隧道 | 1 | GRETUNNEL（★与 IPSec draft 共享同一对象 `OBJ-GRETUNNEL`，本特性扩展其 Keepalive/GRE Key/多租户/嵌套语义） |
| 前置依赖（引用，非本特性拥有） | 4 | INTERFACE（LoopBack 源/Tunnel 接口）、IFIPV4ADDRESS、L3VPNINST（DSTVPNNAME）、SRROUTE（隧道间静态路由） |

### 0.3 全局字段声明（status / used_by_features）

> **适用范围**：本文件 §1 所有 MMLCommand。
> **`status` 声明**：本文件 §1 所有 MMLCommand 的 `status` 字段值均为 `active`（Schema §11.3 MMLCommand.status 必备）。IPFD-015002 GRE 所有正式命令均处于启用状态，无 `deprecated` 或 `planned`。
> **`used_by_features` 声明**：ADD/MOD/RMV/LST GRETUNNEL 的 `used_by_features = ["IPFD-015002 GRE", "IPFD-015004 IPSec（GRE over IPsec 场景）"]`（命令同源，跨特性共用）。

---

## 1. MMLCommand 实例化（IPFD-015002 GRE，3 个核心配置命令 + 2 个查询/调测登记）

### 1.1 GRE 隧道核心命令（UDG + UNC 共用，3个配置 + 1个查询）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 关键参数 | `source_evidence_ids` |
|--------------|----------------|--------|------------------|-------------------|----------|----------------------|
| `CMD-UDG-015002-01` / `CMD-UNC-015002-01` | `ADD GRETUNNEL` | ADD | GRETUNNEL | ★创建 GRE 隧道（轻量封装不加密；18 参数全表见 IPSec draft §5.18；★GRE 独有：KEEPALVEN/KEEPALVPERIOD/KEEPALVRETRYCNT 链路检测、GREKEYEN/GREKEY 识别关键字、CHECKSUMEN 端到端校验、DSTVPNNAME 多租户 VPN、最多两层嵌套；最大 4096 记录） | TNLNAME, TNLTYPE(gre/gre6), SRCTYPE, SRCTYPE6, SRCIPADDR, SRCIPV6ADDR, SRCIFNAME, DSTIPADDR, DSTIPV6ADDR, DSTVPNNAME, KEEPALVEN, KEEPALVPERIOD, KEEPALVRETRYCNT, GREKEYEN, GREKEY, CHECKSUMEN, STATENABLE, REDUNDANCYEN | EV-GRE-01（ADD GRETUNNEL 手册）/ EV-GRE-02（UNC 激活文档）/ EV-GRE-03（GRE 特性概述） |
| `CMD-UNC-015002-02` | `MOD GRETUNNEL` | MOD | GRETUNNEL | 修改 GRE 隧道（UNC 激活文档脚本用于使能 Checksum/GRE Key/Keepalive；参数集与 ADD 同表 18 参数；操作目标必须先存在） | 同 ADD GRETUNNEL 18 参数 | EV-GRE-02（UNC 激活文档脚本行 172-184）/ EV-GRE-04（MOD GRETUNNEL 手册） |
| `CMD-UNC-015002-03` | `RMV GRETUNNEL` | RMV | GRETUNNEL | ★删除 GRE 隧道（UNC 去激活；高危：去激活时隧道上仍有报文将导致业务中断） | TNLNAME, TNLTYPE | EV-GRE-05（UNC 去激活文档）/ EV-GRE-06（RMV GRETUNNEL 手册） |
| `CMD-UDG-015002-04` / `CMD-UNC-015002-04` | `LST GRETUNNEL` | LST | GRETUNNEL | 查询 GRE 隧道配置（验证；UNC 激活文档验证方法步骤） | TNLNAME, TNLTYPE | EV-GRE-07（LST GRETUNNEL 手册）/ EV-GRE-01（UDG 调测文档步骤 3） |

### 1.2 GRE 调测/诊断/统计命令族（UDG + UNC 共用，本期略参数，登记用）

| `command_id` | `command_name` | `verb` | `object_keyword` | `command_summary` | 说明 |
|--------------|----------------|--------|------------------|-------------------|------|
| `CMD-UDG-015002-D1` | `DSP TUNNELINFO` | DSP | TUNNELINFO | UDG 调测步骤 1：显示隧道信息（预期隧道状态 UP） | 调测查询类，本期略参数（UDG 调测文档步骤 1） |
| `CMD-UDG-015002-D2` | `PING` | — | — | UDG 调测步骤 2：Ping 对端网元验证连通性 | 调测类，本期略参数（UDG 调测文档步骤 2） |
| `CMD-UDG/UNC-015002-D3` | `DSP GREMSGSTATINFO` | DSP | GREMSGSTATINFO | GRE 消息诊断信息 | 调测查询类，本期略参数 |
| `CMD-UDG/UNC-015002-D4` | `DSP GRETNLINFO` | DSP | GRETNLINFO | GRE 隧道诊断信息 | 调测查询类，本期略参数 |
| `CMD-UDG/UNC-015002-D5` | `DSP GRETNLTAB` | DSP | GRETNLTAB | GRE 隧道信息表 | 调测查询类，本期略参数 |
| `CMD-UDG/UNC-015002-D6` | `DSP GREPKTSTAT` | DSP | GREPKTSTAT | GRE 报文统计 | 调测查询类，本期略参数 |
| `CMD-UDG/UNC-015002-D7` | `DSP GRETNLSTAT` | DSP | GRETNLSTAT | GRE 隧道数目 | 调测查询类，本期略参数 |
| `CMD-UDG/UNC-015002-D8` | `DSP GREKPLVSTAT` | DSP | GREKPLVSTAT | GRE 隧道 Keepalive 报文计数查询 | 调测查询类，本期略参数（Keepalive 检测配套） |
| `CMD-UDG/UNC-015002-D9` | `RTR GREKPLVSTAT` | RTR | GREKPLVSTAT | GRE 隧道 Keepalive 报文计数重置 | 调测查询类，本期略参数（Keepalive 检测配套） |

---

## 2. ConfigObject 实例化（1 个核心 + 4 个引用）

### 2.1 GRE 隧道（1个，★与 IPSec draft 共享）

| `object_id` | `object_name` | `product_side` | `object_kind` | 标识参数 | 关键属性 | 包含/引用关系 |
|-------------|---------------|----------------|---------------|----------|----------|---------------|
| `OBJ-GRETUNNEL` | GRETUNNEL | UDG + UNC | entity | TNLNAME | TNLTYPE(gre/gre6), SRCTYPE/SRCTYPE6, SRCIPADDR/SRCIPV6ADDR/SRCIFNAME, DSTIPADDR/DSTIPV6ADDR, DSTVPNNAME, KEEPALVEN/KEEPALVPERIOD/KEEPALVRETRYCNT, GREKEYEN/GREKEY, CHECKSUMEN, STATENABLE, REDUNDANCYEN | refers_to INTERFACE（源 LoopBack）/ L3VPNINST（DSTVPNNAME）；★可嵌套（最多两层）；★多租户共享（同源同宿多隧道以 GRE key 区分） |

### 2.2 前置依赖（引用，非本特性拥有，4个）

| `object_id` | `object_name` | `product_side` | `object_kind` | 标识参数 | 归属特性 |
|-------------|---------------|----------------|---------------|----------|----------|
| `OBJ-INTERFACE`（引用） | INTERFACE | UDG + UNC | entity | IFNAME | 簇A/簇E（LoopBack 源接口 + Tunnel 接口） |
| `OBJ-IFIPV4ADDRESS`（引用） | IFIPV4ADDRESS | UDG + UNC | entity | IFNAME, IFIPADDR | 簇A/簇E（接口 IPv4 地址） |
| `OBJ-L3VPNINST`（引用） | L3VPNINST | UDG + UNC | entity | VRFNAME | 簇A（DSTVPNNAME 索引；VPN 组网场景） |
| `OBJ-SRROUTE`（引用） | SRROUTE | UDG + UNC | entity | AFTYPE, PREFIX, MASKLENGTH, IFNAME | 簇E（隧道间静态路由，业务流量引入 GRE 隧道） |

---

## 3. ConfigObject 间关系边（§11.7）

### 3.1 refers_to 边（3条）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| GRETUNNEL | `refers_to` | INTERFACE（LoopBack） | GRE 隧道引用源接口（SRCTYPE=if_name 时 SRCIFNAME 指向 LoopBack；手册原文：源接口 IPv4/IPv6 地址作为封装后报文源 IP） |
| GRETUNNEL | `refers_to` | L3VPNINST | GRE 隧道目的地址所属 VPN（DSTVPNNAME 索引；手册原文：该 VPN 必须先由 ADD L3VPNINST 定义） |
| GRETUNNEL | `refers_to` | GRETUNNEL（嵌套） | ★GRE 隧道可嵌套其他 GRE 隧道（特性概述应用限制原文：最多两层嵌套，超过两层第三层状态变 Down；Recursion 字段标记层数） |

### 3.2 depends_on 边（2条）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| GRETUNNEL | `depends_on` | INTERFACE + IFIPV4ADDRESS | GRE 隧道依赖源 LoopBack 接口及其 IP 地址已配置（UNC 激活文档步骤 1 前置：隧道源端口和目的端口已路由可达） |
| SRROUTE | `depends_on` | GRETUNNEL | 隧道间静态路由依赖 GRE 隧道存在（UNC 激活文档步骤 3：IFNAME="Tunnel1" 指向已创建的 GRE 隧道） |

### 3.3 conflicts_with 边（1条，★GRE vs IPSec 互斥）

| 起点 | 关系 | 终点 | 说明 |
|------|------|------|------|
| GRETUNNEL.SRCIPADDR/SRCIFNAME | `conflicts_with` | IPSECINTFCFG.SRCIFNAME（同源接口） | ★手册原文强约束：GRE 隧道的源地址不能和 IPSec 隧道的源地址相同（ADD GRETUNNEL 注意事项 + GRE 特性概述应用限制；CR-015002-02 详见 §4） |

---

## 4. CommandRule 实例化（本特性相关，4条）

> **★Schema 合规要点**：§11.6 `CommandRule governs MMLCommand`（反向）。`scope_type` = `command/parameter/object/relation`。

| `rule_id` | `rule_name` | `rule_type` | `rule_expression_mode` | `rule_source_kind` | `scope_type` | `scope_ref` | `rule_logic` | `violation_effect` | `severity` | `source_evidence_ids` |
|-----------|-------------|-------------|----------------------|-------------------|-------------|------------|--------------|-------------------|------------|----------------------|
| `CR-015002-01` | GRE 隧道嵌套最多两层 | `semantic_rule` | explicit | restriction | object | OBJ-GRETUNNEL（嵌套关系） | GRE 隧道可以嵌套其他 GRE 隧道，但最多支持两层嵌套（特性概述应用限制原文；GRE 报文头 Recursion 字段标记封装层数，封装层数大于 3 丢弃报文）。超过两层的第三层 GRE 隧道状态会变为 Down | 第三层嵌套隧道状态 Down，业务不通 | critical | EV-GRE-03（GRE 特性概述应用限制）/ EV-GRE-08（GRE 报文格式 Recursion 字段） |
| `CR-015002-02` | GRE 源地址与 IPSec 源地址互斥 | `semantic_rule` | explicit | restriction | relation | OBJ-GRETUNNEL ↔ OBJ-IPSECINTFCFGIPSEC | GRE 隧道的源地址不能和 IPSec 隧道的源地址相同（ADD GRETUNNEL 注意事项原文 + GRE 特性概述应用限制）。★GRE over IPsec 场景需双隧道编排：Tunnel1(GRE) 用 LoopBack1 作源，Tunnel2(IPsec) ACL 匹配 LoopBack 间流量，源接口不可共用（与 IPSec draft CR-015004-03 同源） | 隧道无法 UP 或递归封装 | critical | EV-GRE-01（ADD GRETUNNEL 注意事项）/ EV-GRE-03（GRE 特性概述） |
| `CR-015002-03` | GRE 识别关键字两端必须一致 | `parameter_dependency` | explicit | config | parameter | ADD/MOD GRETUNNEL.GREKEYEN + GREKEY | 使能识别关键字功能（GREKEYEN=TRUE）后，隧道两端必须指定完全相同的识别关键字（GREKEY）；或两端都不设置。手册原文：只有 Tunnel 两端设置的识别关键字完全一致时才能通过验证，否则将报文丢弃。明文输入仅支持数字 0~4294967295 | 报文被丢弃，隧道不通 | critical | EV-GRE-01（ADD GRETUNNEL.GREKEY 参数说明）/ EV-GRE-02（UNC 激活文档步骤 5 说明） |
| `CR-015002-04` | 多租户共享 GRE 以 GRE key 区分租户 | `semantic_rule` | explicit | config | object | OBJ-GRETUNNEL（多租户场景） | 多租户共享 GRE 隧道：建立同源同宿（源/目的地址相同）的多条 GRE 隧道，不同隧道以 GRE 报文头中的 GRE key 字段作为区分标签，不同租户以 IP 区分并通过静态路由将出接口配置到对应 GRE 隧道（多租户共享 GRE 隧道实现原理原文）。★GREKEY 必须逐隧道不同以区分租户 | 租户流量串道 | critical | EV-GRE-09（多租户共享 GRE 隧道实现原理） |

---

## 5. MMLCommand 关键参数集（ADD/MOD GRETUNNEL 复用 IPSec draft + GRE 独有差异）

> **Schema 参考**：§11.4 CommandParameter。`required_mode` 取值 `required / optional / conditional_required / conditional_optional`（Schema §11.4 必备字段）。

### 5.1 ADD GRETUNNEL / MOD GRETUNNEL 参数清单（18 参数，★复用 IPSec draft §5.18）

> **★复用声明**：ADD GRETUNNEL 全 18 参数表已在 IPSec draft `04-cluster-E-IPSec-015004.md` §5.18（`CMD-UDG-015004-19`）完整抽取，手册同源同 id（`_00841729` UDG/UNC 一致）。本节列参数清单 + 来源手册，详细取值范围/默认值/required_mode 见 IPSec draft §5.18，此处不重复。

| 命令 | 参数行数 | 来源手册路径（相对 `output/<产品>/`） |
|------|---------|--------------------------------------|
| ADD GRETUNNEL | 18 | UDG: `OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/GRE管理/GRE隧道/增加GRE隧道（ADD GRETUNNEL）_00841729.md`；UNC: `OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/GRE管理/GRE隧道/增加GRE隧道（ADD GRETUNNEL）_00841729.md`（同 id 同内容） |
| MOD GRETUNNEL | 18（同表） | UDG/UNC: `OM参考/命令/<产品> MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/GRE管理/GRE隧道/修改GRE隧道（MOD GRETUNNEL）_50121682.md`（参数集与 ADD 同表） |

**18 参数清单**（详见 IPSec draft §5.18）：

| 参数 | required_mode | 默认值 | GRE 场景用途 |
|------|---------------|--------|--------------|
| TNLNAME | required | 无 | 隧道名称（格式 Tunnel+X/Y/Z） |
| TNLTYPE | required | 无 | gre / gre6 |
| SRCTYPE | conditional_required(TNLTYPE=gre) | no_type | IPv4 源类型（no_type/ip_address/if_name） |
| SRCTYPE6 | conditional_required(TNLTYPE=gre6) | no_type | IPv6 源类型 |
| SRCIPADDR | conditional_required(SRCTYPE=ip_address) | 无 | 源 IPv4 地址 |
| SRCIPV6ADDR | conditional_required(SRCTYPE6=ip_address) | 无 | 源 IPv6 地址 |
| SRCIFNAME | conditional_required(SRCTYPE/SRCTYPE6=if_name) | 无 | 源接口名称（GRE 场景常用 LoopBack1） |
| DSTIPADDR | conditional_optional(TNLTYPE=gre) | 无 | 目的 IPv4 地址 |
| DSTIPV6ADDR | conditional_optional(TNLTYPE=gre6) | 无 | 目的 IPv6 地址 |
| DSTVPNNAME | optional | 无 | ★目的 VPN 名称（多租户/VPN 组网场景；必须先由 ADD L3VPNINST 定义） |
| KEEPALVEN | optional | FALSE | ★使能 Keepalive 链路检测（GRE 独有，见 §5.2） |
| KEEPALVPERIOD | conditional_optional(KEEPALVEN=TRUE) | 5 | Keepalive 报文发送周期（秒，1~32767） |
| KEEPALVRETRYCNT | conditional_optional(KEEPALVEN=TRUE) | 3 | 不可达计数器（1~255） |
| GREKEYEN | optional | FALSE | ★使能识别关键字（GRE 独有，多租户区分标签） |
| GREKEY | conditional_required(GREKEYEN=TRUE) | 无 | 识别关键字（密码类型 1~268；明文数字 0~4294967295） |
| CHECKSUMEN | optional | FALSE | ★使能端到端校验（GRE 独有，对应报文头 C 位） |
| STATENABLE | optional | FALSE | 使能报文统计 |
| REDUNDANCYEN | conditional_optional(TNLTYPE=gre/gre6) | FALSE | 使能备份隧道（静态地址用户流量备份） |

### 5.2 GRE 独有差异（IPSec draft 未展开的语义，本特性补齐）

> **★本节为 GRE 特性独有维度的展开**，IPSec draft §5.18 仅列参数骨架，未涉及 Keepalive 机制/多租户/嵌套语义。以下 100% 来自原始产品文档原文。

#### 5.2.1 Keepalive 链路检测机制（KEEPALVEN/KEEPALVPERIOD/KEEPALVRETRYCNT）

| 维度 | 原文依据 | 内容 |
|------|----------|------|
| 功能定位 | Keepalive 检测实现原理（`Keepalive检测_61317267.md`） | GRE 协议不具备检测链路状态的功能。若远端不可达，隧道不能及时关闭，源端会不断向对端转发数据而对端丢弃，形成数据黑洞。Keepalive 检测用于时刻检测隧道对端是否可达，对端不可达则及时关闭隧道连接 |
| 工作过程 | 同上 | ①源端使能后创建定时器，周期发送 Keepalive 探测报文，每发一个不可达计数+1；②对端每收到探测报文回送回应报文；③源端计数器未达预设值就收到回应→对端可达，清零；计数器达预设值（重试次数）仍未收到回应→对端不可达，关闭隧道连接 |
| 单向性 | 同上说明 + ADD GRETUNNEL.KEEPALVEN 配置原则 | Keepalive 是单向的。只要隧道一端配置 Keepalive，该端就具备功能，不要求对端也配置。隧道对端收到 Keepalive 探测报文，无论是否配置都会回送回应。要两端都具备需两端都使能 |
| 参数联动 | ADD GRETUNNEL 手册 + UNC 激活文档步骤 6 说明 | KEEPALVEN=TRUE 时 KEEPALVPERIOD（默认 5 秒）/KEEPALVRETRYCNT（默认 3 次）生效；不填则取默认值 |
| 业务价值 | ADD GRETUNNEL.KEEPALVEN 配置原则 | 业务模块选择承载隧道时，可防止选择对端不可达的 GRE 隧道，避免数据丢失（未使能时即使对端不可达本端 Tunnel 状态也可能为 Up） |

#### 5.2.2 GRE 识别关键字与多租户共享（GREKEYEN/GREKEY）

| 维度 | 原文依据 | 内容 |
|------|----------|------|
| 识别关键字验证 | ADD GRETUNNEL.GREKEYEN/GREKEY 参数说明 + UNC 激活文档步骤 5 说明 | 使能后收发双方进行通道识别关键字验证，只有两端关键字完全一致才通过，否则丢弃报文。明文输入仅支持数字 0~4294967295 |
| 多租户共享原理 | 多租户共享 GRE 隧道实现原理（`多租户共享GRE隧道_61317217.md`） | 建立同源同宿（源/目的地址相同）的多条 GRE 隧道，不同隧道以 GRE 报文头中的 GRE key 字段作为区分标签。不同租户以 IP 区分，通过静态路由将出接口配置到对应 GRE 隧道，GRE key 代表不同租户流量 |
| 转发面行为 | 同上 | 入隧道：不同租户流量由对应静态路由引入对应 GRE 隧道进行 GRE 封装；出隧道：不同 GRE 隧道流量通过 IP 源/目地址 + 剥离 IP 头后的 GRE key 找到对应 GRE 隧道下一跳转发 |
| 客户价值 | 同上客户价值表 | 运营商：节约公网 IP、提高接入设备利用率、增加投资效益；用户：节省开支 |

#### 5.2.3 端到端校验（CHECKSUMEN，对应报文头 C 位）

| 维度 | 原文依据 | 内容 |
|------|----------|------|
| 报文头 C 位 | GRE 报文格式（`GRE报文格式_61317188.md`） | C=校验和验证位。C=1 表示 GRE 头插入 Checksum 字段；C=0 表示不包含 |
| 非对称行为 | ADD GRETUNNEL.CHECKSUMEN 配置原则 | 本端配置校验和而对端没配置：本端不对接收报文校验，但对发送报文计算校验和；本端没配置而对端配置：本端对从对端发来的报文校验，但对发送报文不计算校验和 |

#### 5.2.4 嵌套约束与 Recursion 字段

| 维度 | 原文依据 | 内容 |
|------|----------|------|
| 最多两层嵌套 | GRE 特性概述应用限制（`IPFD-015002 GRE特性概述_61317365.md`） | GRE 隧道可以嵌套其他 GRE 隧道，但最多支持两层嵌套，超过两层嵌套的 GRE 隧道状态变为 Down。例如三层嵌套时第三层状态变 Down |
| Recursion 字段 | GRE 报文格式 Recursion 字段说明 | Recursion 表示 GRE 报文被封装的层数，完成一次 GRE 封装该字段+1，封装层数大于 3 丢弃报文（防无限封装）。RFC 1701 默认 0；RFC 2784 收发不一致不引起异常且接收端忽略；UNC 实现仅在加封装时标记嵌套层数，解封装不感知 |
| 规格上限 | GRE 特性概述特性规格 | 整个系统最大支持配置 GRE Tunnel 接口数量：4k（ADD GRETUNNEL 注意事项：最大记录数 4096） |

#### 5.2.5 GRE 轻量封装不加密（与 IPSec 对比）

| 维度 | 原文依据 | 内容 |
|------|----------|------|
| 封装不加密 | GRE 特性概述定义 + 原理概述 | GRE 是通用路由封装协议，对网络层协议报文进行封装使其能在另一网络层协议（如 IP）中传输，作为 VPN 第三层隧道协议提供透明传输通道。封装过程仅添加 GRE 头 + IP 头，无加密机制 |
| 与 IPSec 对比 | IPSec draft GRE over IPsec 场景 | GRE 提供隧道封装（组播/广播业务透传），IPSec 提供加密；GRE over IPsec 场景下 IPsec 加密 GRE 报文实现「封装+加密」叠加。★GRE 源地址不能与 IPSec 源地址相同（CR-015002-02） |

### 5.3 RMV GRETUNNEL 参数（UNC 去激活，2 参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| TNLNAME | string | 1~63（格式 Tunnel+X/Y/Z） | `required` | 无 | 隧道名称（引用 ADD GRETUNNEL 生成） |
| TNLTYPE | enum | gre / gre6 | `required` | 无 | 隧道类型 |

> **★高危说明**（UNC 去激活文档「对系统的影响」原文）：去激活 GRE 时，若 GRE 隧道上仍有报文通过，将导致业务中断。

### 5.4 LST GRETUNNEL 参数（验证查询，2 参数）

| 参数 | 类型 | 取值范围 | `required_mode` | 默认值 | 说明 |
|------|------|---------|-----------------|--------|------|
| TNLNAME | string | 1~63 | `required` | 无 | 隧道名称 |
| TNLTYPE | enum | gre / gre6 | `required` | 无 | 隧道类型 |

> **★LST GRETUNNEL 返回字段**（UNC 激活文档验证方法示例输出）：隧道名称/隧道类型/IPv4源类型/IPv6源类型/源IPv4地址/目的IPv4地址/源IPv6地址/目的IPv6地址/使能Keepalive功能/Keepalive报文发送周期/不可达计数器参数/源接口名称/目的VPN名称/使能识别关键字功能/识别关键字/使能端到端校验功能/使能报文统计功能/使能备份隧道功能（共 18 个返回字段，与 ADD 参数一一对应）。

---

## 6. MMLCommand `operates_on` ConfigObject 边表（§11.7）

> **Schema 参考**：§11.7 `MMLCommand operates_on ConfigObject`。

### 6.1 GRE 核心命令（4条）

| MMLCommand | operates_on -> ConfigObject | 说明 |
|------------|---------------------------|------|
| ADD GRETUNNEL (CMD-UDG/UNC-015002-01) | GRETUNNEL | ★创建 GRE 隧道（与 IPSec draft 共享对象；used_by_features 扩展含 IPFD-015002） |
| MOD GRETUNNEL (CMD-UNC-015002-02) | GRETUNNEL | 修改 GRE 隧道（使能 Checksum/GRE Key/Keepalive） |
| RMV GRETUNNEL (CMD-UNC-015002-03) | GRETUNNEL | 删除 GRE 隧道（去激活；高危） |
| LST GRETUNNEL (CMD-UDG/UNC-015002-04) | GRETUNNEL | 查询 GRE 隧道（验证） |

### 6.2 前置依赖命令（引用，非本特性拥有，5条）

| MMLCommand | operates_on -> ConfigObject | 说明 |
|------------|---------------------------|------|
| ADD INTERFACE（簇A/簇E） | INTERFACE | LoopBack 源接口 + Tunnel 接口（UNC 激活步骤 1） |
| ADD IFIPV4ADDRESS（簇A/簇E） | IFIPV4ADDRESS | 接口 IPv4 地址（LoopBack + Tunnel） |
| MOD INTERFACE（簇A/簇E） | INTERFACE | ★配置 GRE Tunnel MTU（≤ 出接口 MTU − GRE 头长度；UNC 激活步骤 2 说明） |
| ADD L3VPNINST（簇A） | L3VPNINST | VPN 实例（DSTVPNNAME 索引；VPN 组网场景前置） |
| ADD SRROUTE（簇E） | SRROUTE | 隧道间静态路由（UNC 激活步骤 3，IFNAME 指向 Tunnel1） |

---

## 7. ★CommandRule governs MMLCommand 边表（§11.6 反向）

> **★Schema 合规要点**：§11.6 `CommandRule governs MMLCommand / CommandParameter / ConfigObject`（反向：规则治理命令，非命令 has_rule）。

| CommandRule | governs -> MMLCommand / Parameter / ConfigObject | 治理逻辑摘要 |
|-------------|------------------------------------------------|--------------|
| CR-015002-01 | OBJ-GRETUNNEL（嵌套关系） | GRE 隧道嵌套最多两层，第三层状态 Down（Recursion 字段 >3 丢弃） |
| CR-015002-02 | OBJ-GRETUNNEL ↔ OBJ-IPSECINTFCFGIPSEC | GRE 源地址与 IPSec 源地址互斥（GRE over IPsec 双隧道编排不可共用源接口） |
| CR-015002-03 | ADD/MOD GRETUNNEL.GREKEYEN + GREKEY | 识别关键字两端必须完全一致，否则丢弃报文 |
| CR-015002-04 | OBJ-GRETUNNEL（多租户场景） | 多租户共享 GRE 以 GRE key 区分租户，逐隧道 key 不同 |

---

## 8. 使用实例脚本（保留手册原文，3 个配置子场景 + UDG 调测）

### 8.1 基础 GRE 隧道 + Keepalive + 校验 + 识别关键字（来源：UNC 激活支持GRE_06422610.md，本端配置）

```
//创建LoopBack接口，并配置IP地址10.3.3.11/32。
ADD INTERFACE:IFNAME="LoopBack1";
ADD IFIPV4ADDRESS:IFNAME="LoopBack1", IFIPADDR="10.3.3.11", SUBNETMASK="255.255.255.255", ADDRTYPE=main;

//创建Tunnel接口（GRE隧道），源接口LoopBack1，目的10.4.4.11。
ADD GRETUNNEL:TNLNAME="Tunnel1", TNLTYPE=gre, SRCTYPE=if_name, SRCIFNAME="LoopBack1", DSTIPADDR="10.4.4.11";
ADD IFIPV4ADDRESS:IFNAME="Tunnel1", IFIPADDR="10.10.1.201", SUBNETMASK="255.255.255.0", ADDRTYPE=main;

//增加隧道间静态路由。
ADD SRROUTE:AFTYPE=ipv4unicast,PREFIX="10.10.1.202",MASKLENGTH=24,IFNAME="Tunnel1";

//使能隧道端到端校验功能。
MOD GRETUNNEL:TNLNAME="Tunnel1", TNLTYPE=gre, CHECKSUMEN=TRUE;

//使能隧道识别关键字功能（两端必须相同）。
MOD GRETUNNEL:TNLNAME="Tunnel1", TNLTYPE=gre, GREKEYEN=TRUE, GREKEY="123";

//使能隧道Keepalive功能（周期5秒，重试3次）。
MOD GRETUNNEL:TNLNAME="Tunnel1", TNLTYPE=gre, KEEPALVEN=TRUE, KEEPALVPERIOD=5, KEEPALVRETRYCNT=3;
```

### 8.2 多租户共享 GRE 隧道（来源：多租户共享GRE隧道_61317217.md 实现原理，编排示例）

> **★说明**：多租户共享 GRE 隧道实现原理文档未提供完整脚本，仅描述原理（同源同宿多隧道 + 不同 GRE key + 静态路由分流）。以下脚本为依据原理文档 + ADD GRETUNNEL 手册使用实例的编排示例，标注「编排示例」。

```
//（编排示例）多租户共享 GRE：同源同宿两条隧道，以 GRE key 区分租户。
ADD GRETUNNEL:TNLNAME="Tunnel1", TNLTYPE=gre, SRCTYPE=if_name, SRCIFNAME="LoopBack1", DSTIPADDR="10.4.4.11", GREKEYEN=TRUE, GREKEY="100";
ADD GRETUNNEL:TNLNAME="Tunnel2", TNLTYPE=gre, SRCTYPE=if_name, SRCIFNAME="LoopBack1", DSTIPADDR="10.4.4.11", GREKEYEN=TRUE, GREKEY="200";

//不同租户 IP 通过静态路由出接口分别指向 Tunnel1/Tunnel2。
ADD SRROUTE:AFTYPE=ipv4unicast,PREFIX="<租户A网段>",MASKLENGTH=24,IFNAME="Tunnel1";
ADD SRROUTE:AFTYPE=ipv4unicast,PREFIX="<租户B网段>",MASKLENGTH=24,IFNAME="Tunnel2";
```

### 8.3 去激活 GRE 隧道（来源：UNC 去激活支持GRE_06422612.md）

```
//删除配置的GRE隧道Tunnel1（高危：隧道上仍有报文将导致业务中断）。
RMV GRETUNNEL: TNLNAME="Tunnel1",TNLTYPE=gre;
```

### 8.4 UDG 调测 GRE（来源：UDG 调测GRE_06422611.md）

```
//步骤1：查看GRE隧道状态（预期UP，异常DOWN参见GRE隧道故障处理定位思路）。
DSP TUNNELINFO;

//步骤2：Ping对端网元验证连通性（预期收到响应）。
PING: IPVERSION=IPv4, DESTIPV4ADDRESS="10.4.4.11";

//步骤3：检查GRE隧道配置是否正确。
LST INTERFACE:IFNAME="<接口名>";
LST GRETUNNEL:TNLNAME="<隧道名称>";
```

### 8.5 GRE over IPsec 编排入口（引用 IPSec draft）

> **★引用**：GRE over IPsec 双隧道编排完整脚本见 IPSec draft `04-cluster-E-IPSec-015004.md` §8.5（矩阵第 5 行），本文件不重复。关键点：Tunnel1(GRE) 用 LoopBack1 作源承载业务，Tunnel2(IPsec) ACL 匹配 LoopBack 间流量加密 GRE 报文，源接口不可共用（CR-015002-02）。

---

## 9. 抽取核对清单

### 9.1 配置类命令参数行数与来源手册路径

| 命令 | 参数行数 | 来源手册路径 |
|------|---------|-------------|
| ADD GRETUNNEL | 18（★复用 IPSec draft §5.18） | UDG: `output/UDG_Product_Documentation_CH_20.15.2/OM参考/命令/UDG MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/GRE管理/GRE隧道/增加GRE隧道（ADD GRETUNNEL）_00841729.md`；UNC: `output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/平台服务管理/VNRS功能管理/IP服务/VPN管理/GRE管理/GRE隧道/增加GRE隧道（ADD GRETUNNEL）_00841729.md`（同 id 同内容） |
| MOD GRETUNNEL | 18（同表） | `.../GRE隧道/修改GRE隧道（MOD GRETUNNEL）_50121682.md`（UDG/UNC 同 id） |
| RMV GRETUNNEL | 2 | `.../GRE隧道/删除GRE隧道（RMV GRETUNNEL）_00600977.md`（UDG/UNC 同 id） |
| LST GRETUNNEL | 2 | `.../GRE隧道/查询GRE隧道（LST GRETUNNEL）_49802638.md`（UDG/UNC 同 id） |
| **合计** | **40 参数行**（ADD/MOD 复用 18 + RMV 2 + LST 2，ADD/MOD 同表不双计） | 4 命令全部手册定位成功 |

### 9.2 ⚠️手册未定位列表

| 命令 | 状态 | 原因 |
|------|------|------|
| 无 | — | 本特性参考的全部命令（ADD/MOD/RMV/LST GRETUNNEL + DSP GRE* 族 + DSP/RTR GREKPLVSTAT）手册均已定位。 |

> **说明**：本特性未发现手册未定位命令。MOD GRETUNNEL（`_50121682`）、RMV GRETUNNEL（`_00600977`）、LST GRETUNNEL（`_49802638`）及 5 个 DSP GRE* 调测命令 + 2 个 Keepalive 计数命令手册均已定位（路径见 §0.1 + §9.1）。

### 9.3 与簇E IPSec draft 的关键差异（★复用核对项）

| 差异项 | IPSec draft（`04-cluster-E-IPSec-015004.md`） | 本文件（GRE 特性 draft） | 影响 |
|--------|----------------------------------------------|------------------------|------|
| **ADD GRETUNNEL 全参数表** | §5.18 完整抽取 18 参数（CMD-UDG-015004-19），`used_by_features` 仅 IPSec | §5.1 引用不重复，`used_by_features` 扩展为 IPSec + GRE | 命令复用，避免重复建模 |
| **Keepalive 机制语义** | 仅列参数骨架（KEEPALVEN/PERIOD/RETRYCNT），未展开机制 | §5.2.1 展开 Keepalive 检测原理（数据黑洞避免 + 单向性 + 计数器工作过程 + 业务价值） | GRE 独有链路检测可建模 |
| **GRE Key 多租户语义** | 仅列 GREKEYEN/GREKEY 参数，未涉及多租户 | §5.2.2 展开多租户共享原理（同源同宿多隧道 + GRE key 区分标签 + 静态路由分流 + 转发面行为） | 多租户 GRE 场景可建模 |
| **嵌套约束** | 未涉及（IPSec 不嵌套 GRE） | §5.2.4 + CR-015002-01 展开两层嵌套上限 + Recursion 字段语义 | GRE 嵌套限制可建模 |
| **Checksum 非对称行为** | 仅列 CHECKSUMEN 参数 | §5.2.3 展开端到端校验非对称行为（本端/对端配置不一致的收发校验差异）+ 报文头 C 位对应 | 校验机制可建模 |
| **GRE vs IPSec 对比** | GRE over IPsec 场景下 GRE 承载组播/广播 | §5.2.5 明确 GRE 轻量封装不加密，与 IPSec 加密能力对比 | 特性边界清晰 |
| **CommandRule** | CR-015004-03 GRE/IPSec 源地址互斥（同源） | §4 新增 4 条特性级 CR-015002-01~04（嵌套/源互斥/Key 一致/多租户），CR-015002-02 与 CR-015004-03 同源互补 | 特性级规则治理细化 |
| **UDG vs UNC 差异** | UDG 侧为主 | §0.1 明确：UDG 仅调测文档，UNC 有完整激活/去激活；命令族手册同源同 id，能力两侧一致 | 产品侧覆盖完整 |

### 9.4 抽取统计

| 维度 | 数量 |
|------|------|
| 配置类命令（手册定位成功） | 3（ADD/MOD/RMV GRETUNNEL） |
| 查询类命令 | 1（LST GRETUNNEL，抽参数） |
| 配置/查询类命令参数总行数 | 40（ADD/MOD 复用 18 同表不双计 + RMV 2 + LST 2） |
| 调测/诊断/统计命令（本期略参数） | 9（DSP TUNNELINFO / PING / DSP GRE* 5 个 / DSP GREKPLVSTAT / RTR GREKPLVSTAT） |
| ⚠️手册未定位命令 | 0 |
| ConfigObject | 1（OBJ-GRETUNNEL，与 IPSec draft 共享）+ 4 引用 |
| CommandRule | 4（CR-015002-01~04） |
| ConfigObject 关系边 | 6（refers_to 3 + depends_on 2 + conflicts_with 1） |
| operates_on 边 | 4（核心）+ 5（前置依赖引用） |
| 配置子场景脚本 | 5（基础 GRE + 多租户 + 去激活 + UDG 调测 + GRE over IPsec 引用） |

---

> 本文件为 IPFD-015002 GRE（UDG + UNC 共用特性）命令层抽取，严格对齐样板 `04-cluster-B-GWFD-010105.md`。
> **★关键贡献**：①ADD GRETUNNEL 复用 IPSec draft（CMD-UDG-015004-19）18 参数全表，避免重复建模，扩展 `used_by_features` 含 GRE；②补齐 GRE 独有语义：Keepalive 链路检测机制（数据黑洞避免 + 单向性）、GRE Key 多租户共享（同源同宿多隧道 + key 区分标签）、最多两层嵌套约束（Recursion 字段）、Checksum 端到端校验非对称行为；③明确 UDG（仅调测）vs UNC（完整激活/去激活）差异，命令族手册同源同 id 两侧能力一致；④建立 4 条特性级 CommandRule（嵌套上限/源地址互斥/Key 两端一致/多租户 key 区分）；⑤明确 GRE 轻量封装不加密，与 IPSec 加密能力对比，GRE over IPsec 编排引用 IPSec draft §8.5。
