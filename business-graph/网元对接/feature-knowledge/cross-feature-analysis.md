# 跨特性分析 cross-feature-analysis
> EV ID: EV-CA-01 | 17引用特性横向归纳
> 业务域=网元对接，子场景=UPF网元对接
> 特性定位=引用支撑（非图谱主体，主体=对接面CS）；为第2层特性图谱(02-feature-graph.md)与第4层命令图谱提供数据源

---

## 1. 特性分类总览（→第2层 Feature.feature_group / 对接面映射）

### 1.1 按特性前缀分类（feature_group）

| 前缀组 | 数量 | 含义 | 成员 |
|--------|------|------|------|
| **IPFD**（IP Forwarding，路由转发类） | **10** | IP基本特性：接口/可靠性/路由/IPSec | IPFD-010000 / 010001 / 012000 / 012003 / 014000 / 014001 / 014002 / 014003 / 015004 / 104403 |
| **GWFD**（Gateway Function，网关功能类） | **5** | 2/3/4G/5G业务基本特性+组网演进：地址分配/SingleIP/CU组网/MPLS VPN/位置地址 | GWFD-010105 / 010234 / 020161 / 020411 / 020421 |
| **NPFD**（Network Platform O&M，操作维护类） | **2** | 网管特性：运维根+NTP | NPFD-010000 / 010014 |

### 1.2 按 feature_category 分类

| category | 数量 | 成员 |
|----------|------|------|
| `base`（基础/业务特性） | 15 | 全部IPFD(10) + 全部GWFD(5) |
| `operations`（运维特性） | 2 | NPFD-010000 / NPFD-010014 |

### 1.3 按 is_directory（目录父节点）分类

| 是否目录 | 数量 | 成员 |
|----------|------|------|
| **目录父节点（is_directory=true）** | **4** | IPFD-010000（接口与链路）/ IPFD-012000（IP可靠性）/ IPFD-014000（路由功能）/ NPFD-010000（操作维护功能） |
| 叶子特性 | 13 | 其余特性 |

### 1.4 特性 → 对接面映射表（→对接面CS主体）

> 对接面定义参见 `topic-batch-plan.md`：CS-1控制面(N4) / CS-2用户面(业务接口+会话接入) / CS-3网管对接 / CS-4路由对接 / CS-5基础就绪

| feature_code | 名称 | 主要对接面 | 引用篇数 | 核心度 |
|--------------|------|-----------|---------|--------|
| IPFD-014000 | 路由功能(目录) | **CS-4** 路由对接 | 29 | ★★★★★ |
| IPFD-012003 | BFD | **CS-4** 路由对接 | 20 | ★★★★★ |
| IPFD-012000 | IP可靠性(目录) | **CS-4** 路由对接 | 20 | ★★★★★ |
| IPFD-014002 | 支持BGP | **CS-4** 路由对接 | 17 | ★★★★★ |
| IPFD-014003 | 静态路由 | **CS-4** 路由对接 | 9 | ★★★★ |
| IPFD-014001 | 支持OSPF | **CS-4** 路由对接 | 6 | ★★★★ |
| GWFD-010234 | Single IP | **CS-2** 用户面(业务接口) | 5 | ★★★★ |
| GWFD-020411 | MPLS VPN | **CS-4** 路由对接 | 5 | ★★★★ |
| IPFD-015004 | IPSec功能 | **CS-4** 路由对接 | 3 | ★★★ |
| IPFD-104403 | BFD(初始配置引用代号) | **CS-4** 路由对接(SDN) | 3 | ★★（别名） |
| IPFD-010000 | 接口与链路(目录) | **CS-2** 用户面(接口) | 2 | ★★★ |
| IPFD-010001 | 接口管理 | **CS-2** 用户面(接口) | 2 | ★★★ |
| GWFD-010105 | 用户面地址分配 | **CS-2** 用户面(会话接入) | 1 | ★★★★ |
| GWFD-020161 | CU Full Mesh组网 | **CS-1** 控制面(N4组网) | 1 | ★★★ |
| GWFD-020421 | 基于位置的地址分配 | **CS-2** 用户面(会话接入) | 1 | ★★★ |
| NPFD-010000 | 操作维护功能(目录) | **CS-3/CS-5** 网管/基础 | 1 | ★★ |
| NPFD-010014 | 支持NTP功能 | **CS-3/CS-5** 网管/基础 | 1 | ★★★ |

**对接面集中度印证图谱主体**：
- **CS-4 路由对接**：IPFD路由转发类(10) 全部落此，是图谱绝对主体（引用篇数 29+20+20+17+9+6+5+3+3=112，占17特性总引用的 ~80%）
- **CS-2 用户面**：GWFD-010105/020421（会话接入地址分配）+ GWFD-010234（业务接口SingleIP）+ IPFD-010000/010001（接口基础）
- **CS-1 控制面**：仅 GWFD-020161（CU Full Mesh N4组网）
- **CS-3/CS-5 网管/基础**：NPFD-010000/010014

---

## 2. 共性分析（→FeatureRule）

### 2.1 IPFD 路由转发类共性（10特性）

- **config_relevance = `required`**（10/10 全部）：路由/接口/可靠性能力均为对接必备
- **目录体系三层根**：IPFD-010000(接口) / IPFD-012000(可靠性) / IPFD-014000(路由)，子能力分散承载
- **共享路由命令模式**：`VPN实例(VPNINST/L3VPNINST) → 路由协议(OSPF/BGP/静态) → BFD检测` 的三段式，几乎贯穿CS-4全部方案
- **BFD与路由协议耦合**：IPFD-012003 BFD 被 OSPF/BGP/静态路由方案全部引用（"OSPF+BFD"/"BGP over OSPF+静态路由+BFD"/"静态路由+BFD"），形成"路由+BFD"标准搭档
- **NF支持统一**：除3个目录父节点标"目录"外，叶子特性 nf_support_map 均为 `GGSN(2G&3G)=M; S/PGW-U(4G)=M; S/PGW-U(5G NSA)=M; UPF(5G)=M; NB-IoT=M`（5G UPF全支持）

### 2.2 GWFD 网关功能类共性（5特性）

- **UDG网元角色相关能力**：均围绕UPF/PGW-U/SGW-U作为业务网关的"地址分配+接口复用+组网"能力
- **config_relevance 多为 `required`**（4/5）：仅 GWFD-010234 Single IP 标 `none`（其为地址复用机制，非独立配置项）
- **地址分配双子特性**：GWFD-010105（基础地址池）+ GWFD-020421（位置维度叠加）形成"父-子增强"关系
- **MPLS VPN 独立成轨**：GWFD-020411 是唯一跨"NP卡直连PE/非SDN/网络加速卡/SDN"四类部署的路由方案特性（引用5篇分散在4类部署）

### 2.3 NPFD 操作维护类共性（2特性）

- **config_relevance = `ops_only`**（2/2）：仅运维配置，不直接产生对接信令
- **父目录承载**：NPFD-010000 为运维根，NPFD-010014 NTP 是其在对接场景唯一落地的子能力
- **非主体**：在UPF对接图谱中为辅助特性（保障时间一致性，便于证书/Timestamp/日志对齐）

### 2.4 通用共性（17特性）

- **feature_category**：15 base + 2 operations，无独立付费/增值特性类别
- **License控制稀疏**：仅3特性受控（见 §4），其余14特性无License
- **显式 depends_on 稀疏**：仅4特性有显式依赖（见 §3），其余13为"基础/目录特性"无显式依赖记录

---

## 3. 依赖关系分析（→depends_on 边）

### 3.1 显式 depends_on（4条边）

| 源特性 | 依赖目标 | 语义 | 备注 |
|--------|---------|------|------|
| **GWFD-010105** 用户面地址分配 | `GWFD-010224` N4接口 | 地址分配需N4接口偶联前提 | 外部特性（不在17引用集内） |
| **GWFD-010105** 用户面地址分配 | `GWFD-010233` Sxb接口 | 地址分配需Sxb接口前提 | 外部特性（不在17引用集内） |
| **GWFD-020161** CU Full Mesh组网 | `GWFD-010224` N4/Sx接口 PFCP协议 | CU Full Mesh建立在N4/Sx PFCP之上 | 外部特性（不在17引用集内） |
| **GWFD-020421** 基于位置的地址分配 | `GWFD-010105` 用户面地址分配 | 位置维度叠加在基础地址池之上 | **17引用集内闭环依赖** |

### 3.2 父子目录关系（is_directory隐含父子边，非depends_on）

- IPFD-010000(接口与链路) → IPFD-010001(接口管理)
- IPFD-012000(IP可靠性) → IPFD-012003(BFD) / IPFD-104403(BFD别名)
- IPFD-014000(路由功能) → IPFD-014001(OSPF) / IPFD-014002(BGP) / IPFD-014003(静态路由)
- NPFD-010000(操作维护) → NPFD-010014(NTP)

> 注：父子边在第2层特性图谱中按 `parent_feature_code` 字段建模，不计入 depends_on。

### 3.3 依赖图小结

```
GWFD-010224(N4接口,外部) ←──┐
GWFD-010233(Sxb接口,外部)←──┤
                              ├── GWFD-010105(用户面地址分配) ←── GWFD-020421(基于位置的地址分配)
GWFD-010224(N4/Sx PFCP,外部)─┘
                              └── GWFD-020161(CU Full Mesh)

其余13特性：基础/目录特性，无显式depends_on（在图谱中作为独立特性节点）
```

---

## 4. License 链（→requires_license 边）

### 4.1 受License控制特性（3个）

| feature_code | 名称 | license_code | license项 |
|--------------|------|-------------|----------|
| **GWFD-020161** | CU Full Mesh组网 | `LKV3G5CUFM01` | CU Full Mesh组网 |
| **GWFD-020411** | MPLS VPN | `LKV3G5MPLS01` | MPLS VPN |
| **GWFD-020421** | 基于位置的地址分配 | `LKV3G5LBAA01` | 基于位置的地址分配 |

### 4.2 无License控制特性（14个）

全部10个IPFD特性 + GWFD-010105 / GWFD-010234 + 全部2个NPFD特性

### 4.3 License分布特征

- **License全部集中在GWFD网关类**（3/5 GWFD受控），IPFD路由转发类与NPFD运维类完全免费
- **受控特性均为"组网演进/分布式解决方案"增值能力**：CU Full Mesh(分布式C/U解耦) / MPLS VPN(L3VPN承载) / 基于位置地址分配(差异化地址策略)
- **CS-4路由对接主体特性(IPFD路由类)零License** → 路由对接基线能力免费，仅MPLS VPN这一进阶方案收费
- **第1层业务图谱 License节点**：建议生成3个License节点（LKV3G5CUFM01 / LKV3G5MPLS01 / LKV3G5LBAA01），各连1条 `requires_license` 边

---

## 5. 关键发现

### 5.1 IPFD-104403 = IPFD-012003 BFD 别名（重要规范化处理）

- **现象**：IPFD-104403 仅出现在SDN侧"BGP over静态路由+BFD"3篇(IPv4/IPv4v6/IPv6)，文档链接实际指向 `IPFD-012000 IP可靠性/IPFD-012003 BFD`
- **本质**：初始配置文档对BFD特性的历史引用代号，IPFD-104403 未在 features.jsonl 登记
- **图谱规范处理**：
  - **规范节点用 `IPFD-012003 BFD`**（合并引用篇数：20+3=23）
  - **IPFD-104403 作为别名/历史引用证据保留**，在第2层特性图谱中标注 `alias_of: IPFD-012003`，不单独建节点（避免重复）
  - 附录A中保留IPFD-104403条目但标注"别名"

### 5.2 引用集中度印证 CS-4 主体地位

| 排名 | feature_code | 引用篇数 | 占比 |
|------|-------------|---------|------|
| 1 | IPFD-014000 路由功能(目录) | 29 | 20.7% |
| 2 | IPFD-012003 BFD / IPFD-012000 IP可靠性(目录) | 20 / 20 | 14.3% each |
| 4 | IPFD-014002 支持BGP | 17 | 12.1% |
| 5 | IPFD-014003 静态路由 | 9 | 6.4% |
| 6 | IPFD-014001 支持OSPF | 6 | 4.3% |

> **Top 6 全部为 IPFD 路由转发类，累计 101 篇 / 140 总引用 ≈ 72%** → 强烈印证"UPF网元对接图谱主体 = CS-4 路由对接面"，第2层特性图谱与第4层命令图谱资源应向 IPFD 路由类倾斜。

### 5.3 目录特性是父节点，子能力分散在路由方案中

- **3个IPFD目录父节点**（IPFD-010000/012000/014000）+ 1个NPFD目录父节点（NPFD-010000）共承载 **53篇引用**（29+20+2+1+1=53，去重后代际覆盖全部70篇md的主体）
- 目录父节点本身不承载具体MML命令（标注"具体命令由子特性承载"），在图谱中作为"能力分类根"存在
- 子能力（IPFD-010001/012003/014001/014002/014003）才是命令与配置对象的实际承载者

### 5.4 四类部署形态贯穿CS-4（路由对接的横切维度）

IPFD路由类 + GWFD-020411 MPLS VPN 在以下四类部署形态中均有引用，构成CS-4的横切分类轴：
1. **NP卡直连PE**
2. **非SDN无NP卡**（自动部署+手动部署）
3. **网络加速卡直连DC-GW**
4. **SDN**

此横切维度建议在第1层业务图谱的对接面CS-4下作为子结构（如 CS-4.1~CS-4.4）建模。

### 5.5 Single IP（GWFD-010234）特殊定位

- 引用5篇但 `config_relevance=none`（17特性中唯一一个 none）
- 原因：Single IP 是"地址复用机制"而非独立配置项，其能力通过 ADD LOGICINF 等接口命令隐式生效
- 图谱处理：保留为特性节点但标注 `config_relevance=none`，不强制关联Task

---

## 附录A 特性索引表（EV-FK-01~17）

| EV ID | feature_code | 名称 | 前缀组 | category | is_directory | config_relevance | 对接面 | 引用篇数 | 父特性 | 核心度 |
|-------|-------------|------|--------|----------|-------------|------------------|--------|---------|--------|--------|
| EV-FK-01 | GWFD-010105 | 用户面地址分配 | GWFD | base | false | required | CS-2 | 1 | GWFD-010100 | ★★★★ |
| EV-FK-02 | GWFD-010234 | Single IP | GWFD | base | false | **none** | CS-2 | 5 | GWFD-010220 | ★★★★ |
| EV-FK-03 | GWFD-020161 | CU Full Mesh组网 | GWFD | base | false | required | CS-1 | 1 | GWFD-020160 | ★★★ |
| EV-FK-04 | GWFD-020411 | MPLS VPN | GWFD | base | false | required | CS-4 | 5 | GWFD-020410 | ★★★★ |
| EV-FK-05 | GWFD-020421 | 基于位置的地址分配 | GWFD | base | false | required | CS-2 | 1 | GWFD-020420 | ★★★ |
| EV-FK-06 | IPFD-010000 | 接口与链路 | IPFD | base | **true** | required | CS-2 | 2 | (根) | ★★★ |
| EV-FK-07 | IPFD-010001 | 接口管理 | IPFD | base | false | required | CS-2 | 2 | IPFD-010000 | ★★★ |
| EV-FK-08 | IPFD-012000 | IP可靠性 | IPFD | base | **true** | required | CS-4 | 20 | (根) | ★★★★★ |
| EV-FK-09 | IPFD-012003 | BFD | IPFD | base | false | required | CS-4 | 20 | IPFD-012000 | ★★★★★ |
| EV-FK-10 | IPFD-014000 | 路由功能 | IPFD | base | **true** | required | CS-4 | 29 | (根) | ★★★★★ |
| EV-FK-11 | IPFD-014001 | 支持OSPF | IPFD | base | false | required | CS-4 | 6 | IPFD-014000 | ★★★★ |
| EV-FK-12 | IPFD-014002 | 支持BGP | IPFD | base | false | required | CS-4 | 17 | IPFD-014000 | ★★★★★ |
| EV-FK-13 | IPFD-014003 | 静态路由 | IPFD | base | false | required | CS-4 | 9 | IPFD-014000 | ★★★★ |
| EV-FK-14 | IPFD-015004 | IPSec功能 | IPFD | base | false | required | CS-4 | 3 | IPFD-015000 | ★★★ |
| EV-FK-15 | IPFD-104403 | BFD(初始配置引用代号，**别名→IPFD-012003**) | IPFD | base | false | required | CS-4(SDN) | 3 | IPFD-012000 | ★★（别名） |
| EV-FK-16 | NPFD-010000 | 操作维护功能 | NPFD | **operations** | **true** | **ops_only** | CS-3/CS-5 | 1 | (根) | ★★ |
| EV-FK-17 | NPFD-010014 | 支持NTP功能 | NPFD | **operations** | false | **ops_only** | CS-3/CS-5 | 1 | NPFD-010000 | ★★★ |

---

## 附录B MML命令交叉参考（特性→关联MML命令，供第4层命令图谱）

| feature_code | 名称 | 关联MML命令 |
|--------------|------|------------|
| GWFD-010105 | 用户面地址分配 | ADD POOL / ADD POOLGROUP / ADD POOLBINDGROUP / ADD POOLGRPMAP / SET IPALLOCRULE / ADD APN / SET APNSGLPASS |
| GWFD-010234 | Single IP | ADD LOGICINF / LST LOGICINF / SET UPINFO / ADD VPNINST |
| GWFD-020161 | CU Full Mesh组网 | ADD LOGICINF(N4if) / SET UPINFO / ADD VPNINST |
| GWFD-020411 | MPLS VPN | ADD BGPPEER / ADD BGPVRF / ADD BGPVRFAF / ADD MPLSIF / ADD VPNTARGET / ADD L3VPNINST / ADD VPNINSTAF / SET MPLSSITE |
| GWFD-020421 | 基于位置的地址分配 | ADD SECTION / ADD POOL / SET IPALLOCRULE(按位置) |
| IPFD-010000 | 接口与链路(目录) | *(父目录，命令由IPFD-010001承载)* |
| IPFD-010001 | 接口管理 | MOD INTERFACE / SET FABRICMTU / LST INTERFACE / LST FABRICMTU / DSP IFSTATUS / SET IFIPV6ENABLE |
| IPFD-012000 | IP可靠性(目录) | *(父目录，命令由IPFD-012003承载)* |
| IPFD-012003 | BFD | SET BFD / ADD BFDSESSION / DSP BFDSESSION / ADD AUTOSCALINGBFD(SDN) |
| IPFD-014000 | 路由功能(目录) | *(父目录，命令由OSPF/BGP/静态路由子特性承载)* |
| IPFD-014001 | 支持OSPF | ADD OSPF / ADD OSPFAREA / ADD OSPFNETWORK / ADD OSPFINTERFACE / ADD OSPFIMPORTROUTE / DSP OSPFPEER |
| IPFD-014002 | 支持BGP | SET BGP / ADD BGPPEER / ADD BGPVRF / ADD BGPVRFAF / ADD BGPPEERAF / ADD IMPORTROUTE |
| IPFD-014003 | 静态路由 | ADD SRROUTE / ADD IMPORTROUTE / DSP SRROUTE / DSP ROUTE / RMV SRROUTE |
| IPFD-015004 | IPSec功能 | *(IPsec隧道配置命令，详见"配置IPsec"实例)* |
| IPFD-104403 | BFD(SDN别名) | ADD AUTOSCALINGBFD / ADD AUTOSCALINGSRBFD / DSP BFDSESSION *(SDN语境，规范节点IPFD-012003)* |
| NPFD-010000 | 操作维护(目录) | *(父目录，命令由子特性如NPFD-010014承载)* |
| NPFD-010014 | 支持NTP功能 | *(NTP激活与同步配置，详见"激活支持NTP功能"特性指南)* |

**命令去重提示（供第4层 builder）**：
- `ADD LOGICINF` 同时出现在 GWFD-010234 / GWFD-020161（接口配置共享命令）
- `ADD VPNINST` 同时出现在 GWFD-010234 / GWFD-020161（VPN实例共享命令）
- `ADD BGPPEER / ADD BGPVRF / ADD BGPVRFAF` 同时出现在 GWFD-020411 / IPFD-014002（MPLS VPN依赖BGP VRF）
- `ADD IMPORTROUTE` 同时出现在 IPFD-014002 / IPFD-014003（路由引入共享命令）
- `DSP BFDSESSION` 同时出现在 IPFD-012003 / IPFD-104403（同一能力别名的共享命令，去重时归并到IPFD-012003）

---

## 附录C 配置对象复用矩阵（特性→配置对象，供第4层）

| 配置对象 | 承载特性（feature_code） | 复用度 |
|---------|-------------------------|--------|
| **POOL / POOLGROUP**（地址池） | GWFD-010105, GWFD-020421 | 2特性共享 |
| **IPALLOCRULE**（IP分配规则） | GWFD-010105, GWFD-020421 | 2特性共享 |
| **APN**（接入点名） | GWFD-010105 | 1特性 |
| **SECTION**（地址分段） | GWFD-020421 | 1特性 |
| **LOGICINF**（逻辑接口：N4if/Saif/Paif/Scif） | GWFD-010234, GWFD-020161 | 2特性共享 |
| **UPINFO**（用户面信息） | GWFD-010234, GWFD-020161 | 2特性共享 |
| **VPNINST**（VPN实例） | GWFD-010234, GWFD-020161 | 2特性共享 |
| **N4偶联 / C/U面对接关系 / Full Mesh拓扑** | GWFD-020161 | 1特性（对接面专属） |
| **L3VPNINST / VPNINSTAF**（L3VPN实例） | GWFD-020411 | 1特性 |
| **VPNTARGET**（RT路由目标） | GWFD-020411 | 1特性 |
| **MPLSIF**（MPLS接口） | GWFD-020411 | 1特性 |
| **BGP VRF**（BGP VRF地址族） | GWFD-020411, IPFD-014002 | 2特性共享 |
| **INTERFACE**（接口） | IPFD-010001 | 1特性 |
| **FABRICMTU**（MTU） | IPFD-010001 | 1特性 |
| **接口IPv6使能** | IPFD-010001 | 1特性 |
| **BFDSESSION**（BFD会话） | IPFD-012003, IPFD-104403 | 2特性（别名归并后=1） |
| **BFD**（BFD全局） | IPFD-012003 | 1特性 |
| **AUTOSCALINGBFD**（SDN BFD） | IPFD-012003, IPFD-104403 | 别名归并 |
| **AUTOSCALINGSRBFD**（SDN SR-BFD） | IPFD-104403 | 1特性（SDN专属） |
| **OSPF进程 / OSPFAREA / OSPFNETWORK / OSPFINTERFACE** | IPFD-014001 | 1特性 |
| **BGP进程 / BGPPEER / BGPVRFAF / BGPPEERAF** | IPFD-014002 | 1特性 |
| **SRROUTE**（静态路由） | IPFD-014003 | 1特性 |
| **IMPORTROUTE**（路由引入） | IPFD-014002, IPFD-014003 | 2特性共享 |
| **IPsec隧道 / SA / 安全策略** | IPFD-015004 | 1特性 |
| **NTP同步参数 / 时间源** | NPFD-010014 | 1特性 |

**复用矩阵要点**：
- **最高复用对象**：LOGICINF / UPINFO / VPNINST（接口+VPN三件套，被GWFD-010234+GWFD-020161共享）→ 印证"业务接口数据配置"的统一底座
- **地址池族**：POOL/POOLGROUP/IPALLOCRULE 在 GWFD-010105+GWFD-020421 形成父子复用
- **路由协议族对象互不复用**：OSPF/BGP/静态路由各自独立对象，仅 IMPORTROUTE（路由引入）在BGP+静态路由间共享
- **MPLS VPN 独占对象最多**：L3VPNINST/VPNTARGET/MPLSIF 为 GWFD-020411 独占，印证其为进阶增值方案

---

## 汇总统计（供下游图谱builder快速校验）

| 维度 | 数值 |
|------|------|
| 引用特性总数 | 17（EV-FK-01~17） |
| 规范特性节点数（去别名后） | **16**（IPFD-104403 别名归并到 IPFD-012003） |
| 前缀组分布 | IPFD:10 / GWFD:5 / NPFD:2 |
| 目录父节点数 | 4（IPFD-010000/012000/014000 + NPFD-010000） |
| depends_on 显式边数 | 4（其中3条指向外部特性 GWFD-010224/010233） |
| requires_license 边数 | 3（LKV3G5CUFM01/MPLS01/LBAA01） |
| 关联MML命令（去重前） | ~50条 |
| 配置对象（去重前） | ~30个 |
| 总引用篇数 | 140（IPFD:112 + GWFD:13 + NPFD:2 + 别名IPFD-104403:3；含目录父节点重复计数） |
| CS-4 路由对接占比 | ~80%（112/140） |

---

> 本分析为第2层特性图谱(02-feature-graph.md)与第4层命令图谱(04-command-graph.md)的数据源。下游builder应注意：
> 1. **IPFD-104403 别名归并**到 IPFD-012003，不单独建节点
> 2. **目录父节点**（4个）建为特性节点但 `is_directory=true`，不直接挂MML命令
> 3. **CS-4 横切四类部署**（NP卡直连PE/非SDN无NP卡/网络加速卡直连DC-GW/SDN）建议作为对接面子结构
> 4. **License节点**仅3个，全部连GWFD网关类
