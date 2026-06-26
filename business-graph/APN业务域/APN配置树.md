# APN配置树

> 本文档用提供APN配置树，介绍APN场景下各个业务特性之间的配置逻辑。
>
> **路径说明**：本文档中所有路径均相对于SKILL.md所在目录。
>
> **原理说明**：各配置选项的详细技术原理见 `references/00-配置原理知识.md`。

## 配置树结构

SMF网元配置来源于UNC配置指南，UPF网元配置来源于UDG配置指南。

### 配置路径完整表格

| 配置路径 | 当前节点 | 节点类型 | 节点边 | 特性编号 |
|---------|----------|---------|-------|----------|
| APN开通 | APN开通 | root | AND | - |
| APN开通:APN基础信息 | APN基础信息 | leaf | | - |
| APN开通:地址分配信息 | 地址分配信息 | branch | OR | - |
| APN开通:鉴权计费信息 | 鉴权计费信息 | branch | AND | - |
| APN开通:接入方式信息 | 接入方式信息 | branch | OR | - |
| APN开通:地址分配信息:UPF分配 | UPF分配 | branch | OR | - |
| APN开通:地址分配信息:SMF分配 | SMF分配 | branch | OR | - |
| APN开通:地址分配信息:UDM分配 | UDM分配 | leaf | | WSFD-010502 |
| APN开通:地址分配信息:Radius分配 | Radius分配 | leaf | | WSFD-010502 |
| APN开通:地址分配信息:DHCP分配 | DHCP分配 | leaf | | WSFD-010502 |
| APN开通:地址分配信息:LNS分配 | LNS分配 | leaf | | WSFD-104410 |
| APN开通:地址分配信息:UPF分配:基于APN/DNN | 基于APN/DNN | leaf | | GWFD-010105 |
| APN开通:地址分配信息:UPF分配:基于SMF | 基于SMF | leaf | | GWFD-010105 |
| APN开通:地址分配信息:UPF分配:基于位置区 | 基于位置区 | leaf | | GWFD-020421 |
| APN开通:地址分配信息:SMF分配:基于APN/DNN | 基于APN/DNN | leaf | | WSFD-010502 |
| APN开通:地址分配信息:SMF分配:基于UPF | 基于UPF | leaf | | WSFD-010502 |
| APN开通:地址分配信息:SMF分配:基于位置区 | 基于位置区 | leaf | | WSFD-010502 |
| APN开通:鉴权计费信息:Radius鉴权接入 | Radius鉴权接入 | leaf | | WSFD-011305 |
| APN开通:鉴权计费信息:Radius功能 | Radius功能 | leaf | | WSFD-011306 |
| APN开通:接入方式信息:VPN | VPN | leaf | | - |
| APN开通:接入方式信息:GRE | GRE | leaf | | IPFD-015002 (SMF+UPF) |
| APN开通:接入方式信息:IPSec | IPSec | leaf | | IPFD-016000 (SMF)<br>IPFD-015004 (UPF) |

---

## 节点类型说明

| 节点类型 | 说明 | 规则 |
|---------|------|------|
| root | 根节点 | APN开通 |
| AND | 与节点 | 所有子节点都必须实例化 |
| OR | 或节点 | 根据配置方案选择其中一个子节点 |
| branch | 分支节点 | 内部节点，需要展开 |
| leaf | 叶子节点 | 特性终点，获取特性编号 |

---

## 配置树实例化规则

### 1. 地址分配信息实例化（OR节点）

根据配置方案中的"地址分配方式"选择具体路径：

| 地址分配方式 | 配置树选择路径 | 对应特性 |
|-------------|--------------|---------|
| UPF分配（基于APN/DNN） | 地址分配信息:UPF分配:基于APN/DNN | GWFD-010105 |
| UPF分配（基于SMF） | 地址分配信息:UPF分配:基于SMF | GWFD-010105 |
| UPF按位置区分配 | 地址分配信息:UPF分配:基于位置区 | GWFD-020421 |
| SMF分配 | 地址分配信息:SMF分配:* | WSFD-010502 |
| UDM静态分配 | 地址分配信息:UDM分配 | WSFD-010502 |
| RADIUS分配 | 地址分配信息:Radius分配 | WSFD-010502 |
| DHCPv4分配 | 地址分配信息:DHCP分配:DHCPv4 | WSFD-010502 |
| DHCPv6分配 | 地址分配信息:DHCP分配:DHCPv6 | WSFD-010502 |
| LNS分配 | 地址分配信息:LNS分配 | WSFD-104410 |

### 2. 接入方式信息实例化（OR节点）

根据配置方案中的"接入方式"选择具体路径：

| 接入方式 | 配置树选择路径 | 对应特性 | 技术依据 |
|---------|--------------|---------|---------|
| **标准Internet访问** | 接入方式信息:VPN | - | 直接访问Internet，无需隧道 |
| **GRE隧道** | 接入方式信息:GRE | IPFD-015002 | GRE仅封装不加密，性能开销低 |
| **IPSec隧道** | 接入方式信息:IPSec | IPFD-016000(SMF)<br>IPFD-015004(UPF) | IPSec提供数据加密和认证 |

> **说明**："VPN"在此配置树中表示无隧道直通模式（Native/IPv4），对应直接Internet访问场景。
> GRE和IPSec是隧道接入方式，需要配置相应的隧道特性。

### 3. 鉴权计费信息实例化（AND节点）

鉴权计费信息是AND节点，包含两个叶子节点：
- `鉴权计费信息:Radius鉴权接入` (WSFD-011305)
- `鉴权计费信息:Radius功能` (WSFD-011306)

**配置树节点说明**：
| 配置树节点 | 节点类型 | 特性编号 | 说明 |
|-----------|---------|---------|------|
| 鉴权计费信息:Radius鉴权接入 | leaf | WSFD-011305 | Radius鉴权接入（AUTHMODE参数控制鉴权方式） |
| 鉴权计费信息:Radius功能 | leaf | WSFD-011306 | Radius功能（Radius服务器相关配置） |

**根据用户选择的鉴权方式，确定配置树节点的选中状态**：

| 用户选择的鉴权方式 | AUTHMODE值 | Radius鉴权接入 | Radius功能 | 技术依据 |
|------------------|-----------|---------------|-----------|---------|
| 透明接入 | TRANS_NON_AUTH | ✅ 选中 | ❌ 不选 | HSS/UDM已完成鉴权，无需AAA二次鉴权 |
| 透明鉴权 | TRANS_AUTH | ✅ 选中 | ✅ 选中 | 使用网络侧配置的用户名和密码 |
| 不透明接入 | NON_TRANS | ✅ 选中 | ✅ 选中 | 用户通过PCO携带用户名密码，企业AAA二次鉴权 |
| 本地鉴权 | LOC_AUTH | ✅ 选中 | ❌ 不选 | UNC本地配置用户名密码，无AAA服务器 |

> **配置树实例化规则**：鉴权计费信息下的所有子节点（Radius鉴权接入、Radius功能）都需要在实例化结果中列出，根据上表确定是否选中。
> **依据**：`00-配置原理知识.md` 第2章鉴权接入原理

## 配置树实例化模板

请参考`templates/instance-template.md`。

---

## 特殊场景处理

### 1. 透明接入(TRANS_NON_AUTH)

- HSS/UDM已完成用户鉴权，不需要AAA二次鉴权
- WSFD-011305 Radius鉴权接入：需要配置，将AUTHMODE设为TRANS_NON_AUTH
- WSFD-011306 Radius功能：不需要配置

### 2. 透明鉴权(TRANS_AUTH)

- 需要配置Radius鉴权接入（设置AUTHMODE=TRANS_AUTH）
- 需要配置Radius功能（Radius服务器存在）

### 3. 不透明接入(NON_TRANS)

- 需要配置Radius鉴权接入（设置AUTHMODE=NON_TRANS）
- 需要配置Radius功能（Radius服务器存在）

### 4. VPN接入方式

- **"VPN"在配置树中含义**：无隧道直通模式（Native/IPv4），对应直接Internet访问场景
- **GRE和IPSec是隧道接入方式**（需要配置隧道特性）
- 区分"VPN类型"（配置树节点）与"VPN隧道"（隧道技术）的概念

### 5. GRE隧道嵌套限制

GRE隧道最多支持两层嵌套，超过两层隧道状态会变为Down。

### 6. DHCPv4与DHCPv6分配

DHCPv4和DHCPv6分配使用**同一个特性**（WSFD-010502），通过IPV4ALLOCTYPE和IPV6ALLOCTYPE参数分别配置。

### 7. UPF分配可靠性功能（GWFD-010108）

UPF分配IP地址时，支持用户面地址自动检测功能，用于检测UPF分配的IP地址与PDN/DN侧服务器的路由可达性。

| 探测方式 | 原理 | 适用场景 |
|---------|------|---------|
| PING探测 | 构造ICMP请求报文，期待应答 | 常规连通性测试 |
| DNS探测 | 构造域名查询报文发送给DNS Server | 防火墙禁止PING的环境 |
| Tracert探测 | 发送TTL递增的ICMP报文，查看故障位置 | 故障定位 |

**关键命令**：STR PDNROUTETST / STP PDNROUTETST / DSP PDNTSTRESULT

### 8. LNS分配场景（WSFD-104410 / GWFD-020412）

LNS分配是指通过L2TP隧道与LNS服务器交互，地址由LNS服务器通过PPP协商分配。

| 阶段 | 内容 |
|-----|------|
| LCP协商 | 链路创建，协商MRU、鉴权类型 |
| 鉴权协商 | PAP/CHAP鉴权 |
| 网络协商 | IPv4: IPCP协商获取UE IP地址<br>IPv6: IPv6CP协商获取接口ID + Router Solicitation获取前缀 |

**关键配置参数**：
- SMF: `ADD APNL2TPATTR: APN="xxx", LNSIP="x.x.x.x", LNSNAME="xxx", LNSPWD="xxx";`
- SMF: `SET APNADDRESSATTR: APN="xxx", IPV4ALLOCTYPE=LNS;`