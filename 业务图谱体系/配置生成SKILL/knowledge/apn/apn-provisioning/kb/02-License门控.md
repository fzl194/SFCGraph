# 02-License 门控

> 数据源：`three-layer-graph/01-business-graph.md` §4 BusinessRule + `feature/*.md` §0 元数据 license_required + `04-command-graph.md` §1.1/1.16
> 作用：Phase 3 License 参数收集 / Phase 5 生成前置 / Phase 6 核查
> **License 编号禁止凭记忆填写，必须从 feature §0 元数据确认**

---

## 1. APN 业务域 License 清单

| License 编号 | 触发维度 | 适用产品侧 | 使能特性 | 关联 BR/CR |
|-------------|---------|-----------|---------|-----------|
| `LKV3G5V6PB01` | IPv6 承载（DP-APN-ADDR-TYPE=IPv6/双栈） | UDG | GWFD-020401 IPv6 承载上下文（承载链根） | BR-APN-IPV6-CASCADE |
| `LKV3G5VDSA01` | IPv4v6 双栈 | UDG | GWFD-020403 双栈（使能 GWFD-010105 的 IPv4v6 取值） | BR-APN-DUALSTACK-NEED-LICENSE |
| `LKV3G5P6PD01` | IPv6 Prefix Delegation（V6PREFIXLENGTH<64） | UDG | GWFD-020406 IPv6 PD | BR-APN-IPV6-CASCADE / CR-APN-05 |
| `LKV3G5LBAA01` | 基于位置地址分配（DP-APN-ADDR-MODE=UPF-LOCATION） | UDG | GWFD-020421 基于位置（母特性 GWFD-010105 无 License） | BR-APN-LOC-NEED-LICENSE |
| `LKV3G5L2TP01` | L2TP VPN（DP-APN-ACCESS-MODE=L2TP） | ★仅 UDG | GWFD-020412 L2TP U 面 LAC 执行 | BR-APN-L2TP-CU-ASYM / TR-APN-05 |

> 注：UNC 侧 WSFD-104410 L2TP C 面决策**无 License**（BR-APN-L2TP-CU-ASYM：C-U 不对称）。UNC IPv6/ARD/UPF选择/二次鉴权/别名APN/MPLS 等可能触发 UNC 侧 License，按 feature §0 元数据确认。

---

## 2. License 串联强依赖（BR-APN-IPV6-CASCADE）

```
LKV3G5V6PB01（IPv6 承载，根）
   ↓ 前级必须先激活
LKV3G5VDSA01（IPv4v6 双栈使能）
   ↓ 前缀长度 <64 时触发
LKV3G5P6PD01（IPv6 Prefix Delegation）
```

**违反效果**：IPv6 承载缺失会导致双栈/PD 无法生效；License 串联断裂。

---

## 3. SET LICENSESWITCH 命令

| 产品侧 | 命令 | 关键参数 | command_id |
|--------|------|---------|-----------|
| UDG | `SET LICENSESWITCH` | LICITEM, SWITCH(ENABLE/DISABLE) | CMD-UDG-001 |
| UNC | `SET LICENSESWITCH` | LICENSECODE, SWITCH | CMD-UNC-001 |

> ★两侧参数名不同：UDG 用 LICITEM，UNC 用 LICENSECODE（跨产品不对称）。

**配置实例**（UDG 双栈）：
```mml
SET LICENSESWITCH:LICITEM="LKV3G5V6PB01",SWITCH=ENABLE;
SET LICENSESWITCH:LICITEM="LKV3G5VDSA01",SWITCH=ENABLE;
```

---

## 4. License 缺失影响

| 场景 | 缺失 License | 现象 |
|------|-------------|------|
| 双栈配置 | LKV3G5VDSA01 | 配置命令成功但 IPv4v6 双栈功能不生效，难以排查（BR-APN-DUALSTACK-NEED-LICENSE） |
| 基于位置 | LKV3G5LBAA01 | 池组匹配不生效 |
| L2TP（UDG） | LKV3G5L2TP01 | L2TP 隧道无法建立 |
| IPv6 PD | LKV3G5P6PD01 | 前缀代理失败 |

> **关键**：License 缺失时命令往往仍可执行成功，但功能不生效。Phase 6 核查必须检查 License 是否已购+已开。
