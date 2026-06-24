# 06-Radius 鉴权链

> 数据源：`04-command-graph.md` §1.22/1.23 + §5.6 + `feature/WSFD-011305-Radius鉴权接入.md` §4.3 + `feature/WSFD-011306-Radius功能.md`
> 作用：Phase 3 鉴权参数（仅 TRANS_AUTH/NON_TRANS）/ Phase 5 Radius 链生成 / Phase 6 级联核查
> **级联强依赖**：Radius 功能(011306) → 鉴权接入(011305) → 二次鉴权(108007)，BR-APN-RADIUS-CASCADE

---

## 1. ACCESSMODE 4 取值（SET APNAUTHATTR，CMD-UNC-037）

| 参数 | 取值 | 中文 | 鉴权 | Radius | 账密来源 | PPP 用户 |
|------|------|------|------|--------|---------|---------|
| ACCESSMODE | **TRANS_NON_AUTH** | 透明不鉴权 | 否 | 否 | 不适用 | 是 |
| ACCESSMODE | **TRANS_AUTH** | 透明鉴权 | 是（UNC 代发） | **是** | UNC 公用配置（COMMONUSERNAME/PASS） | 是 |
| ACCESSMODE | **NON_TRANS** | 不透明 | 是（UE 透传） | **是** | UE PCO 携带 | 是 |
| ACCESSMODE | **LOC_AUTH** | 本地鉴权 | 是（本地匹配） | 否 | UE PCO + UNC 本地 | **否（限制）** |

**完整参数**：
| 参数 | required_mode | 说明 |
|------|--------------|------|
| APN | required | APN 名（需已 ADD APN） |
| ACCESSMODE | required | 4 取值之一 |
| COMMONUSERNAME | conditional_required | TRANS_AUTH/LOC_AUTH 用 |
| COMMONUSERPASS | conditional_required | 同上 |
| CFMCOMMUSERPASS | conditional_required | 必须与 COMMONUSERPASS 一致 |

> **TR-APN-02**：仅 ACCESSMODE=TRANS_AUTH/NON_TRANS 强依赖 Radius 功能；TRANS_NON_AUTH/LOC_AUTH 不调用 Radius。
> **BR-APN-LOC-AUTH-NO-PPP**：LOC_AUTH 不支持 PPP 用户。

---

## 2. Radius 三件套（WSFD-011306 功能 + WSFD-011305 接入共享对象）

### 2.1 ADD RDSSVRGRP（CMD-UNC-039，服务器组容器）

| 参数 | 说明 |
|------|------|
| RDSSVRGRPNAME | Radius 服务器组名（三件套共享） |

### 2.2 ADD RDSSVR（CMD-UNC-040，Radius 服务器）

| 参数 | 取值 | 说明 |
|------|------|------|
| RDSSVRGRPNAME | string | 所属服务器组 |
| SERVERTYPE | AUTHENTICATION / ACCOUNTING | 鉴权/计费 |
| PRIFLAG | PRIMARY / BACKUP / CARBON_COPY | 主/备/抄送 |
| PRIORITY | int | 优先级 |
| IPVERSION | ipv4 / ipv6 | — |
| SERVERIPV4 | IPv4 | 服务器 IP |
| CIPHERKEY | string | 密钥（如 ispchina） |

### 2.3 ADD APNRDSSVRGRP（CMD-UNC-041，APN↔服务器组绑定）

| 参数 | 说明 |
|------|------|
| APN | APN 名 |
| RDSSVRGRPNAME | 服务器组名 |
| PRIFLAG | PRIMARY/BACKUP |

### 2.4 ADD APNRDSCLIENTIP（CMD-UNC-042，APN Radius Client IP）

| 参数 | 取值 | 说明 |
|------|------|------|
| APN | string | — |
| INTFNAME | 如 giif1/0/0 | Giif 接口（鉴权 AAA / 计费 AAA 分接口） |
| CLIENTTYPE | AUTHENTICATION / ACCOUNTING | 鉴权/计费 |

### 2.5 其他 Radius 命令

| 命令 | command_id | 说明 |
|------|-----------|------|
| SET APNRDSACCTCTRL | CMD-UNC-043 | Radius 计费控制（SRVTRIGGER/SUPPORTACCTRSP） |
| SET APNRADIUSATTR | CMD-UNC-044 | Radius 域名增加/剥离 |
| SET RDSRSPADDRCHK | CMD-UNC-045 | Radius 响应端口检查 |
| SET FHBYPASS | CMD-UNC-046 | ★故障一键放通（优先级最高，绕过 Radius） |

---

## 3. Radius VPN 与 Gi 接口（前置）

```mml
ADD VPNINST:VPNINSTANCE="vpn_aaa";
ADD LOGICINF:IFNAME="giif1/0/0",LOGICIP="{auth_gi_ip}";   !-- 鉴权 AAA
ADD LOGICINF:IFNAME="giif1/0/1",LOGICIP="{acct_gi_ip}";   !-- 计费 AAA
```

> UNC Gi 逻辑接口：giif1/0/0 = 鉴权 AAA，giif1/0/1 = 计费 AAA。

---

## 4. 二次鉴权扩展（WSFD-108007，DN-AAA 场景，TR-APN-07 强时序）

> **强时序**：NETWORKINSTVPNMAP（前置）→ UPFRDSSVR（必须先于 CLIENTIP）→ UPFRDSCLIENTIP（必须最后，执行后 SMF 立即触发建链）

| 命令 | command_id | 关键参数 | 时序 |
|------|-----------|---------|------|
| ADD UPLIST4RDS | CMD-UNC-047 | UPLISTNAME, UPINSTANCEID | 1（PGW-U/UPF List） |
| ADD CPGTPUADDR | CMD-UNC-048 | IPVERSION, IPV4ADDR | 2（GTP-U 地址） |
| **ADD NETWORKINSTVPNMAP** | CMD-UNC-052 | VPNINSTANCE | **3（★必须前置，CR-APN-09）** |
| ADD RDSUPFCTRL | CMD-UNC-049 | UPLISTNAME, UPINSTANCEID, PREFERENCE, LOCKED | 4（控制） |
| **ADD UPFRDSSVR** | CMD-UNC-050 | SERVERTYPE, IPVERSION, SERVERIPV4, UPLISTNAME | **5（★必须先于 CLIENTIP，CR-APN-08）** |
| **ADD UPFRDSCLIENTIP** | CMD-UNC-051 | CLIENTYPE, UPLISTNAME, VPNINSTANCE, CLIENTIPV4 | **6（★必须最后，执行后 SMF 立即触发建链）** |

**约束**：
- BR-APN-DNAAA-IP-UNIQUE：直连 AAA 与经 UPF 中转 AAA 的 Radius Server IP 不可相同
- BR-APN-SECOND-AUTH-PROTO：仅支持 PAP/CHAP via Radius，不支持 EAP/Diameter

---

## 5. 配置实例（TRANS_AUTH 透明鉴权）

```mml
// APN 鉴权属性
SET APNAUTHATTR:APN="huawei.com",ACCESSMODE=TRANS_AUTH,COMMONUSERNAME="huawei123",COMMONUSERPASS="123",CFMCOMMUSERPASS="123";

// 配套依赖（WSFD-011306 Radius 功能）
// RDSSVRGRPNAME=isprg, SERVERIPV4=10.168.10.1, CIPHERKEY=ispchina
```

> 来源：`feature/WSFD-011305-Radius鉴权接入.md` §5.1

---

## 6. ACCESSMODE 变体（来源 WSFD-011305 §5.2）

```mml
// 变体A：透明接入（无鉴权，最简）
SET APNAUTHATTR:APN="huawei.com",ACCESSMODE=TRANS_NON_AUTH;
// 不需 Radius；COMMONUSERNAME/PASS 非强制

// 变体B：非透明接入（UE 携账密，UNC 透传 AAA）
SET APNAUTHATTR:APN="huawei.com",ACCESSMODE=NON_TRANS,COMMONUSERNAME="huawei123",COMMONUSERPASS="123",CFMCOMMUSERPASS="123";
// 必须开启 Radius 功能；UE PCO 携账密

// 变体C：本地鉴权（UNC 本地匹配，不调 Radius）
SET APNAUTHATTR:APN="huawei.com",ACCESSMODE=LOC_AUTH,COMMONUSERNAME="huawei123",COMMONUSERPASS="123",CFMCOMMUSERPASS="123";
// 不需 Radius；PPP 用户不支持
```
