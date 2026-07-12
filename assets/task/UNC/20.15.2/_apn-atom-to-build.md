# UNC APN 域 · 待新建命令级 atom 清单

> **用途**：UNC APN 业务域（接入与会话管理）全新命令的 atom 新建计划。另一个 Agent 在重构 UNC 已有 212 条存量 atom（计费/PCC 域），**本清单只管 APN 域全新命令的新建**。
> **来源**：`业务图谱体系/APN业务域/apn-feature-doc-list.md`（24 个 UNC APN 特性）× 配置案例筛命令（调测不管，只看配置）。
> **方法**：汇总 md 反查——`assets/_intermediates/command-summary/UNC/20.15.2/` 686 个汇总 md 每个记录"被哪些特性引用"，Grep 24 个 APN 特性 ID 命中 97 个命令，去调测、去已有 → 68 条待新建。
> **SOP**：`assets/task/命令级atom构建SOP.md`（主线证据=汇总 md + 原始命令 md）。

---

## 0. 任务边界

| | 范围 | 谁做 |
|---|---|---|
| UNC 已有 212 atom 重构 | 计费/PCC 三场景存量规范化 | 另一个 Agent |
| **UNC APN 域全新 atom 新建** | **本清单 68 条**（0-00213 起接续） | **我** |
| UNC APN 域 compound/feature | 后续阶段（atom 建齐后再编排） | 待定 |

**硬约束**：只建配置命令（`ADD/MOD/SET/RMV/DEL/LOD`），**不建调测**（`DSP/LST/EXP/STP/STR/TST/PING`）。

---

## 1. 统计汇总

| 类别 | 数量 | 去向 |
|---|---|---|
| APN 域命中命令总数 | 97 | Grep 24 特性 ID 于 686 汇总 md |
| − 调测命令（排除） | 12 | 见 §2，不建 |
| − 已有 atom（排除） | 17 | 见 §3，_numbering.json 已覆盖 |
| **= 待新建 atom** | **68** | 见 §4，0-00213 起接续 |

---

## 2. 排除项 A：调测命令（12 条，不建）

> 用户明确："调测先不管，主要看配置"。调测命令见各特性原始"调测*.md"，不在 atom 体系展开。

| 命令 | 类型 |
|---|---|
| DSP PDUSESSION | 查询会话 |
| DSP IFSTATUS | 查询接口状态 |
| LST RULE / LST RULEBINDING | 查询规则 |
| LST APNUSRPROFG / LST APNADDRESSATTR | 查询 APN 属性 |
| LST ADDRPOOL | 查询地址池 |
| LST IFIPV4ADDRESS / LST IFIPV4ADDRESSIPSEC | 查询接口 IPv4 |
| LST IPSECINTFCFGIPSEC | 查询 IPSec 接口 |
| TST AAA | 拨测 AAA |
| PING | 连通性诊断 |

---

## 3. 排除项 B：已有 atom（17 条，_numbering.json 已覆盖）

> 这些命令虽被 APN 域特性引用，但 UNC 已有 atom（多为计费/PCC 域顺带所建），复用即可，不重建。

| 命令 | 现有 atom |
|---|---|
| ADD APN | 0-00004 |
| ADD APNUSRPROFG | 0-00008 |
| ADD L3VPNINST | 0-00040 |
| ADD LOGICINF | 0-00043 |
| ADD LOGICIP | 0-00044 |
| ADD NGMMSUBDATA | 0-00047 |
| ADD RULE | 0-00071 |
| ADD RULEBINDING | 0-00073 |
| ADD SRROUTE | 0-00081 |
| ADD UPBINDUPG | 0-00089 |
| ADD USERPROFILE | 0-00094 |
| ADD USRPROFGROUP | 0-00096 |
| ADD VPNINST | 0-00098 |
| ADD VPNINSTAF | 0-00099 |
| MOD VPNINSTAF | 0-00133 |
| SET APNREPORTATTR | 0-00152 |
| SET LICENSESWITCH | 0-00180 |

---

## 4. 待新建 atom（68 条，按功能类分组）

> 每条建 atom 时，从对应汇总 md（`assets/_intermediates/command-summary/UNC/20.15.2/{CMD}.md`）的「②各特性配置范式」段精确取"被哪些 APN 特性引用"，补到 atom 的"被引用于"反向链接。
> 编号：0-00213 起，按命令名字母序接续（与 UNC pre-build 惯例一致）。

### 4.1 接入方式 · IPSec（IPFD-016000，23 条）★最大簇

| # | 命令 | 一句话功能 |
|---|---|---|
| 1 | ADD IKEPEER | 增加 IKE 对端（IPSec 协商对端） |
| 2 | ADD IKEPEER6 | 增加 IKE 对端（IPv6） |
| 3 | ADD IKEPROPOSAL | 增加 IKE 提议（加密/认证/SHA 算法） |
| 4 | ADD ATTACHIKEPEER | 将 IKE 对端绑定到 IPSec 策略 |
| 5 | ADD IPSECPOLICY | 增加 IPSec 策略（IPv4） |
| 6 | ADD IPSECPOLICY6 | 增加 IPSec 策略（IPv6） |
| 7 | ADD IPSECPROPOSALIPSEC | 增加 IPSec 提议（ESP 算法） |
| 8 | ADD IPSECINTFCFG | 增加 IPSec 接口配置 |
| 9 | ADD IPSECINTFCFGIPSEC | 增加 IPSec 接口配置（IPSec 实例） |
| 10 | ADD PROPATTACHIPSECPROPOSAL | 绑定 IPSec 提议到接口 |
| 11 | ADD ACLGROUPIPSEC | 增加 ACL 组（IPSec） |
| 12 | ADD ACLGROUP6IPSEC | 增加 ACL 组 IPv6（IPSec） |
| 13 | ADD ACLRULEADV4IPSEC | 增加 ACL 高级规则 IPv4（IPSec） |
| 14 | ADD ACLRULEADV6IPSEC | 增加 ACL 高级规则 IPv6（IPSec） |
| 15 | ADD INTERFACEIPSEC | 增加接口（IPSec 实例） |
| 16 | ADD IFIPV4ADDRESSIPSEC | 配置接口 IPv4 地址（IPSec） |
| 17 | ADD IFIPV6ADDRESSIPSEC | 配置接口 IPv6 地址（IPSec） |
| 18 | ADD IPBINDVPNIPSEC | 将 IP 绑定 VPN（IPSec） |
| 19 | ADD L3VPNINSTIPSEC | 增加 L3VPN 实例（IPSec） |
| 20 | ADD VPNINSTAFIPSEC | 使能 VPN 实例地址族（IPSec） |
| 21 | ADD CERTSCENE | 增加证书场景（IPSec 证书认证） |
| 22 | SET IKEGLOBALCONFIG | 设置 IKE 全局参数 |
| 23 | SET IFIPV6ENABLEIPSEC | 使能接口 IPv6（IPSec） |

### 4.2 接入方式 · GRE（IPFD-015002，3 条）

| # | 命令 | 一句话功能 |
|---|---|---|
| 24 | ADD GRETUNNEL | 增加 GRE 隧道 |
| 25 | MOD GRETUNNEL | 修改 GRE 隧道 |
| 26 | RMV GRETUNNEL | 删除 GRE 隧道 |

### 4.3 地址分配 · 通用池/路由/接口（WSFD-010502/010504/104002/104001/104004，19 条）

| # | 命令 | 一句话功能 |
|---|---|---|
| 27 | ADD ADDRPOOL | 增加地址池（SMF 侧，IPv4/IPv6） |
| 28 | ADD ADDRPOOLGRP | 增加地址池组 |
| 29 | ADD ADDRUPGROUP | 增加地址池与 UPF 组绑定 |
| 30 | ADD SECTION | 增加地址段 |
| 31 | ADD POOLBINDAPN | 地址池绑定 APN |
| 32 | ADD POOLBINDGRP | 地址池绑定组 |
| 33 | ADD POOLGRPMAP | 地址池组映射 |
| 34 | SET APNADDRESSATTR | 设置 APN 地址分配属性（IPV4/V6ALLOCTYPE 等） |
| 35 | ADD SRROUTE6 | 增加静态路由（IPv6） |
| 36 | ADD OSPF | 启用 OSPF 进程 |
| 37 | ADD OSPFAREA | 增加 OSPF 区域 |
| 38 | ADD OSPFNETWORK | 增加 OSPF 网段 |
| 39 | ADD OSPFIMPORTROUTE | OSPF 引入外部路由 |
| 40 | ADD INTERFACE | 增加接口 |
| 41 | MOD INTERFACE | 修改接口 |
| 42 | ADD IFIPV4ADDRESS | 配置接口 IPv4 地址 |
| 43 | ADD IFIPV6ADDRESS | 配置接口 IPv6 地址 |
| 44 | ADD IPBINDVPN | 将 IP 绑定 VPN |
| 45 | SET IFIPV6ENABLE | 使能接口 IPv6 |

### 4.4 地址分配 · L2TP/LNS（WSFD-104410，1 条）

| # | 命令 | 一句话功能 |
|---|---|---|
| 46 | SET APNL2TPCTRL | 设置 APN L2TP 控制开关（L2TPSWITCH） |

> LNS 分配还复用 SET APNADDRESSATTR（IPV4ALLOCTYPE=LNS，见 4.3 #34）。

### 4.5 地址分配 · RADIUS（WSFD-010502 RADIUS 分配，11 条）

| # | 命令 | 一句话功能 |
|---|---|---|
| 47 | ADD RDSSVR | 增加 RADIUS 服务器 |
| 48 | ADD RDSSVRGRP | 增加 RADIUS 服务器组 |
| 49 | ADD RDSUPFCTRL | RDS UPF 控制 |
| 50 | ADD APNRDSCLIENTIP | APN RDS 客户端 IP |
| 51 | ADD APNRDSSVRGRP | APN 绑定 RDS 服务器组 |
| 52 | ADD UPFRDSCLIENTIP | UPF RDS 客户端 IP |
| 53 | ADD UPFRDSSVR | UPF RDS 服务器 |
| 54 | ADD UPLIST4RDS | UP 列表（RDS） |
| 55 | SET RDSACCTREQVSA | 设置 RDS 计费请求 VSA |
| 56 | SET APNRDSACCTCTRL | APN RDS 计费控制 |
| 57 | SET APNRADIUSATTR | APN RADIUS 属性 |

### 4.6 网元选择 · UPF（WSFD-107010/010202，3 条）

| # | 命令 | 一句话功能 |
|---|---|---|
| 58 | ADD UPNODE | 增加 UP 节点 |
| 59 | ADD UPFBINDGRP | UPF 绑定组 |
| 60 | ADD CPGTPUADDR | 控制面 GTP-U 地址 |

### 4.7 鉴权（WSFD-011305/011306/010301/108007/011307，5 条）

| # | 命令 | 一句话功能 |
|---|---|---|
| 61 | SET APNAUTHATTR | 设置 APN 鉴权属性（AUTHMODE） |
| 62 | ADD BLACKLIST | 增加黑名单 |
| 63 | MOD GBAUTHCIPH | 修改鉴权加密参数 |
| 64 | ADD NGUSRSECPARA | 增加下一代用户安全参数 |
| 65 | SET NGMMPROCTRL | 设置 NGMM 协议控制 |

### 4.8 接入控制（WSFD-106003，1 条）

| # | 命令 | 一句话功能 |
|---|---|---|
| 66 | SET FWSOFTPARA | 设置防火墙软参（接入控制相关） |

### 4.9 APN 基础 / 别名 APN（WSFD-106203/010501 等，2 条）

| # | 命令 | 一句话功能 |
|---|---|---|
| 67 | ADD APNALIAS | 增加 APN 别名（别名 APN 重定向） |
| 68 | MOD APN | 修改 APN 配置 |

---

## 5. 编号与建设策略

- **编号**：0-00213 起（接续现有 0-00212），按命令名字母序分配（UNC pre-build 惯例，与 `renumber_unc_tasks.py` 一致）。
- **主线证据**：每条 atom 用 `assets/_intermediates/command-summary/UNC/20.15.2/{CMD}.md`（已就绪）+ 原始命令 md（`output/UNC 20.15.2.../OM参考/命令/...`，权威源）。
- **模板**：命令级 atom SOP §5（frontmatter 7 字段）/ §6（正文 5 章节）/ §7（DP·rule 编号化）/ §8（关联 4 项）。
- **批次建议**：按功能类分批，IPSec 簇（23）→ 地址分配（19+1+11）→ 鉴权/接入控制/网元选择（9）→ GRE（3）→ APN 基础（2）。每批完成后更新 _numbering.json + index.md。
- **双向链接**：每条 atom 的"被引用于"段，grep compound/feature（1-/2-）反引——但 UNC APN 域 compound/feature 尚未建，初期反向链接可为空或指向待建占位。

---

## 6. 待确认（汇报后定）

1. 编号起点 0-00213 + 字母序分配——OK？
2. 批次顺序（IPSec 优先 vs 地址分配优先）？
3. "IPSEC 后缀"命令（ADD INTERFACEIPSEC 等）确认为独立 MML 命令（非变体），按独立 atom 建——OK？
4. UNC APN 域 compound/feature 反向链接初期留空（待编排阶段回填）——OK？
