# R4: GTP/PFCP 路径管理 — 规则挖掘

## 0. 探索范围

| 领域 | 核心命令 |
|------|---------|
| GTP 路径管理 | SET UPGTPPATH, ADD ECHOIPLIST |
| N4U 路径管理 | SET UPN4UPATH |
| 路径探测 | TST PATH, STR PATHSTST |
| 路径状态上报 | SET PATHSTATUSRPT |

---

## 1. 命令链路图

```
SET UPGTPPATH (全局 GTP 路径参数)
  ├→ ADD ECHOIPLIST (黑/白名单 IP 列表)
  ├→ TST PATH (单条路径探测)
  ├→ STR PATHSTST (批量路径探测)
  └→ SET PATHSTATUSRPT (路径状态上报开关)

SET UPN4UPATH (N4U 路径参数)
```

---

## 2. 显式规则

| # | 规则 | 来源 | 严重度 |
|---|------|------|--------|
| R4-E01 | ECHOLISTSWITCH=ENABLE 时需要 ECHOLISTTYPE 配置 | SET UPGTPPATH | 错误 |
| R4-E02 | DEACTIVEFLAG=ENABLE 时 ECHOTIME 必选 | SET UPGTPPATH | 错误 |
| R4-E03 | V1DATAECHOSW=ENABLE 时 LOGICINFTYPE 必选 | SET UPGTPPATH | 错误 |
| R4-E04 | ECHOINTERVAL 范围 60-3600 秒 | SET UPGTPPATH | 错误 |
| R4-E05 | N3REQUEST 范围 1-6（重试次数） | SET UPGTPPATH | 错误 |
| R4-E06 | T3RESPONSE 范围 1-20 秒 | SET UPGTPPATH | 错误 |
| R4-E07 | ECHOIPLIST 最大 200 条 | ADD ECHOIPLIST | 警告 |

---

## 3. 隐式规则

### 3.1 心跳超时链（heartbeat_timeout_chain）

**发现**：路径故障检测由 ECHOINTERVAL × N3REQUEST 决定超时时间，但这个计算关系不在任何一条命令中显式说明。

**证据**：
- ECHOINTERVAL: 心跳间隔（60-3600秒）
- N3REQUEST: 最大重试次数（1-6）
- T3RESPONSE: 重试间隔（1-20秒）
- 实际故障检测时间 ≈ T3RESPONSE × N3REQUEST + ECHOINTERVAL

**隐式规则**：

| # | 规则 | 涉及命令 | 类型 |
|---|------|---------|------|
| R4-I01 | 故障检测时间 = T3RESPONSE × N3REQUEST，该值过大导致路径故障发现慢，过小导致误判 | SET UPGTPPATH | 定量计算 |
| R4-I02 | UAC 路径（UACT3RESPONSE/UACN3REQUEST）应与普通路径参数协调 | SET UPGTPPATH | 一致性 |

### 3.2 路径故障级联（path_failure_cascade）

**发现**：DEACTIVEFLAG=ENABLE 时，GTP 路径故障会触发用户去激活，这是一个故障级联机制。

**证据**：
- SET UPGTPPATH: DEACTIVEFLAG + ECHOTIME 参数
- 路径断开 → ECHOTIME 内无恢复 → 去激活用户上下文

**隐式规则**：

| # | 规则 | 涉及命令 | 类型 |
|---|------|---------|------|
| R4-I03 | DEACTIVEFLAG=ENABLE 但 ECHOTIME 设置过小 → 短暂网络波动导致大规模用户去激活 | SET UPGTPPATH | 风险控制 |
| R4-I04 | DEACTIVEFLAG=DISABLE 时路径故障仅告警，用户保持连接但可能无法正常传输数据 | SET UPGTPPATH | 功能缺失 |

### 3.3 黑白名单过滤（blacklist_whitelist_filtering）

**发现**：ECHOIPLIST 配合 SET UPGTPPATH 的 ECHOLISTTYPE 实现路径管理的黑白名单控制。

**证据**：
- ADD ECHOIPLIST: 添加 IP 段
- SET UPGTPPATH.ECHOLISTTYPE: BLACK 或 WHITE
- BLACK: 名单内的 IP 不做路径探测
- WHITE: 只对名单内的 IP 做路径探测

**隐式规则**：

| # | 规则 | 涉及命令 | 类型 |
|---|------|---------|------|
| R4-I05 | ECHOLISTTYPE=WHITE 但 ECHOIPLIST 为空 → 不对任何 IP 做探测 → 所有路径不可达 | SET UPGTPPATH + ADD ECHOIPLIST | 空容器 |
| R4-I06 | ECHOLISTTYPE=BLACK 时，所有不在名单内的 IP 都会被探测 → 可能探测到不需要的路径 | SET UPGTPPATH | 功能风险 |

### 3.4 逻辑接口类型约束（logic_interface_binding）

**发现**：路径探测按逻辑接口类型(N3/S1_U/S11_U/N9c/Pa/Sc/S5S8_S)分别配置，不同接口类型有独立的探测参数。

**证据**：
- SET UPGTPPATH.LOGICINFTYPE: 必选参数（V1DATAECHOSW=ENABLE 时）

**隐式规则**：

| # | 规则 | 涉及命令 | 类型 |
|---|------|---------|------|
| R4-I07 | 每种 LOGICINFTYPE 应配置独立的路径探测参数，不同接口的可靠性要求不同 | SET UPGTPPATH | 属性兼容 |
