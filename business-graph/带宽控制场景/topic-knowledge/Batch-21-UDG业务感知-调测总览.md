# Batch-21: UDG业务感知 - 调测总览

## 1. 概述

本文档涵盖UDG（User Data Gateway）业务感知（Service Awareness, SA）功能的调测总览。调测业务感知（文档编号87804007）是一个入口文档，它指向六类具体调测场景，形成了一个完整的SA调测矩阵：

- **七层（L7）调测**：基于URL等七层信息的业务识别与动作执行
  - 七层阻塞（L7 Block）
  - 七层重定向（L7 Redirect）
  - 七层Remark（L7 Remark）
- **三四层（L3/L4）调测**：基于IP、端口等三四层信息的业务识别与动作执行
  - 三四层阻塞（L3/L4 Block）
  - 三四层重定向（L3/L4 Redirect）
  - 三四层Remark（L3/L4 Remark）

该调测矩阵适用于SGW-U、PGW-U、UPF网元，覆盖GPRS/UMTS和5G网络架构。整个调测流程遵循由简到繁的递进顺序：先调通阻塞功能验证SA基本识别能力，再扩展到重定向和Remark功能。

---

## 2. 核心知识点

### 2.1 业务感知调测的总体方法论

UDG业务感知调测采用**渐进式验证**方法论，核心原则是：

1. **先验证基础网络可达**：测试终端接入网络、访问普通网页正常，确认UDG基础接入和Web浏览功能可用。
2. **先调通阻塞再扩展**：阻塞（Block）是SA最基础的动作，只需验证"报文是否被丢弃"，不涉及外部设备协同。阻塞调通后说明SA规则匹配链路完整。
3. **逐层扩展动作类型**：从阻塞扩展到重定向（需重定向设备协同），再到Remark（需关闭Alias Marking避免干扰），每一步只变更动作类型，不改变匹配规则。
4. **L7与L3/L4独立调测**：七层和三四层的过滤器配置不同（L7使用L7Filter+URL匹配，L3/L4使用Filter+IP/Port匹配），但动作机制（PCC策略组）相同。

### 2.2 调测前置条件

所有SA调测场景共享以下前置条件体系：

**通用前置条件：**
- SA相关功能配置已完成（阻塞/重定向/Remark的规则配置实例已激活）
- 镜像接口已安装第三方抓包工具（用于观察报文转发行为）
- 测试终端可用（含有效IMSI/APN）

**功能特定的前置条件（存在依赖链）：**

| 调测功能 | 前置依赖 | 说明 |
|----------|----------|------|
| 三四层阻塞 | 无（SA调测起点） | 仅需三四层业务阻塞配置已完成 |
| 三四层重定向 | 三四层阻塞调测完成 | 需与重定向设备互通配置 |
| 三四层Remark | 三四层重定向+阻塞调测完成 | 需关闭Alias Marking |
| 七层阻塞 | 无（L7 SA调测起点） | 需七层业务阻塞配置已完成 |
| 七层重定向 | 七层阻塞调测完成 | 需重定向设备互通+URL重定向配置 |
| 七层Remark | 七层重定向调测完成 | 需关闭Alias Marking |

**关键说明：** 调测存在明确的递进关系。三四层阻塞是三四层SA调测的入口，七层阻塞是七层SA调测的入口。文档中明确标注了每类调测的前置调测文档引用。

### 2.3 调测流程框架

所有六类调测场景遵循统一的**五步验证框架**，只是在具体验证点和查询命令上有所不同：

```
步骤1: 调整配置（如需变更动作类型）
  ↓
步骤2: 确认测试终端接入网络
  ↓
步骤3: 验证基础网络连通性（访问www.huawei.com等知名网站）
  ↓
步骤4: 触发SA规则（访问匹配URL或目标IP），抓包验证动作是否生效
  ↓
步骤5: 如验证失败 -> 逐层排查配置（User Profile -> Rule -> PCC策略组 -> 动作属性 -> FlowFilter -> L7Filter/Filter -> 特征库） -> 收集信息寻求技术支持
```

**调测验证判据总结：**

| 动作类型 | 验证方法 | 成功判据 |
|----------|----------|----------|
| 阻塞 | 访问触发地址 | 终端无法访问目标地址，Gi/N6侧无HTTP报文转发 |
| 重定向（L7） | 访问触发URL | 终端跳转到重定向目标页面，抓包见重定向报文 |
| 重定向（L3/L4） | 访问任意网页 | 重定向设备抓到报文，目的MAC为重定向设备MAC |
| Remark（L7/L3-L4） | 访问触发地址 | 出口报文ToS域DSCP值被修改为配置值（如CS1=0x08） |

### 2.4 调测工具与命令总览

**物理工具：**
- 测试终端（手机/终端设备，含有效SIM/USIM卡）
- 第三方抓包工具（部署在镜像接口上）
- OM Portal跟踪工具（替代方案）

**核心MML命令分类：**

| 类别 | 命令 | 用途 |
|------|------|------|
| 配置类 | ADD RULE | 新增规则（含动作类型配置） |
| 配置类 | MOD PCCACTIONPROP | 修改PCC动作属性（门控/重定向） |
| 配置类 | MOD USERPROFILE | 修改用户模板（关闭Alias Marking等） |
| 配置类 | MOD FILTER | 修改三四层过滤器 |
| 配置类 | ADD REDIRECT | 配置重定向目标 |
| 配置类 | ADD RULEBINDING | 绑定Rule到UserProfile |
| 配置类 | RMV RULE | 删除规则（切换动作类型前清理） |
| 配置类 | SET REFRESHSRV | 刷新业务使配置生效 |
| 查询类 | DSP SESSIONINFO | 查询用户会话信息（IP/APN） |
| 查询类 | LST RULE | 查询规则配置 |
| 查询类 | LST RULEBINDING | 查询UserProfile与Rule绑定关系 |
| 查询类 | LST PCCPOLICYGRP | 查询PCC策略组 |
| 查询类 | LST PCCACTIONPROP | 查询PCC动作属性 |
| 查询类 | LST FLOWFILTER | 查询流过滤器 |
| 查询类 | LST PROTBINDFLOWF | 查询流过滤器协议绑定 |
| 查询类 | LST L7FILTER | 查询七层过滤器 |
| 查询类 | LST FLTBINDFLOWF | 查询流过滤器绑定关系 |
| 查询类 | LST FILTER | 查询三四层过滤器 |
| 查询类 | LST USERPROFILE | 查询用户模板 |
| 查询类 | DSP SIGNATUREDB | 查询特征库加载状态 |
| 维护类 | EXP MML | 导出配置为MML脚本 |
| 维护类 | LOD SIGNATUREDB | 加载/升级特征库 |

### 2.5 常见问题分类与排查思路

**问题分类一：动作未生效（最常见）**

排查路径遵循配置链路的逆向追溯：

```
动作未生效
  → 检查 User Profile 是否绑定了正确的 Rule（LST RULEBINDING）
    → 检查 Rule 的策略类型和流过滤器是否正确（LST RULE）
      → 检查 PCC 策略组和动作属性是否正确（LST PCCPOLICYGRP + LST PCCACTIONPROP）
        → 检查 FlowFilter 及其绑定是否正确（LST FLOWFILTER + LST FLTBINDFLOWF）
          → 检查 L7Filter 或 Filter 的配置和生效标记（LST L7FILTER / LST FILTER）
            → 检查特征库是否正确加载（DSP SIGNATUREDB，仅七层场景）
```

**问题分类二：APN不匹配**

用户激活时使用的APN与规划值不一致，需返回步骤重新使用正确APN接入。通过DSP SESSIONINFO命令确认。

**问题分类三：入口报文已携带目标标记（Remark场景特有）**

如果上下行入口报文的DSCP值恰好与配置的Remark值相同，无法区分是Remark生效还是原始值。此时需重新配置一个与入口报文不同的Remark值。

**问题分类四：Alias Marking干扰（Remark场景特有）**

User Profile的Alias Marking功能使能时，报文ToS域的值不会被改写，导致无法观察Remark是否生效。调测Remark时必须通过MOD USERPROFILE命令将ALIASMARKFLAG设为DISABLE。

**问题分类五：特征库未加载（七层场景特有）**

七层SA依赖协议特征库进行业务识别。通过DSP SIGNATUREDB检查加载状态需为"Load Finish"且版本正确。如未加载需执行LOD SIGNATUREDB。

---

## 3. 配置调测要点

### 3.1 调测检查清单

**基础检查（所有场景）：**
- [ ] 测试终端使用正确APN接入网络
- [ ] 测试终端能正常访问www.huawei.com（基础网络连通性）
- [ ] 镜像接口抓包工具已就绪
- [ ] User Profile绑定的Rule名称和优先级与规划一致
- [ ] Rule的流过滤器名称和策略组名称与规划一致

**阻塞场景附加检查：**
- [ ] PCC动作属性中"上行发起下行门控"为Discard（阻塞核心配置）
- [ ] Filter的"生效标记"为"是"
- [ ] 三四层协议类型、服务器IP与规划一致（L3/L4场景）
- [ ] L7Filter的URL与规划一致（L7场景）

**重定向场景附加检查：**
- [ ] 重定向设备与UDG互通配置已完成
- [ ] PCC动作属性中重定向名称（UPINITREDIRNM/DNINITREDIRNM）已配置
- [ ] 重定向目标的URL/IP正确
- [ ] 重定向设备的MAC地址已知（L3/L4重定向验证用）

**Remark场景附加检查：**
- [ ] Alias Marking已关闭（ALIASMARKFLAG=DISABLE）
- [ ] Rule策略类型为REMARK_FPI
- [ ] Remark配置类型（CLASS）和分类类型（CS1等）正确
- [ ] 入口报文DSCP值与配置的Remark值不同

### 3.2 关键验证命令示例

**查询用户会话信息：**
```
DSP SESSIONINFO:QUERYTYPE=IMSI,IMSI="460000123456789";
```
用于获取测试终端的IP地址和APN，是所有调测场景的基础查询。

**查询规则配置（阻塞场景）：**
```
LST RULE:RULENAME="rule_test",POLICYTYPE=PCC;
```

**查询规则配置（Remark场景）：**
```
LST RULE:RULENAME="rule_test",POLICYTYPE=REMARK_FPI;
```

**查询规则配置（IP重定向场景）：**
```
LST RULE:RULENAME="rule_test",POLICYTYPE=IPREDIR;
```

**查询PCC动作属性：**
```
LST PCCACTIONPROP:PCCACTPROPNAME="pap_test";
```

**查询七层过滤器（L7场景）：**
```
LST L7FILTER:L7FILTERNAME="l7-test";
```

**查询三四层过滤器（L3/L4场景）：**
```
LST FILTER:FILTERNAME="filter_test";
```

**查询特征库加载状态（L7场景）：**
```
DSP SIGNATUREDB;
```

**导出配置（故障收集）：**
```
EXP MML;
```

### 3.3 典型问题处理

**问题：阻塞不生效，终端仍可访问目标地址**

处理步骤：
1. 检查APN是否正确（DSP SESSIONINFO）
2. 检查User Profile与Rule绑定（LST RULEBINDING）
3. 检查Rule的流过滤器和策略组（LST RULE）
4. 检查PCC动作属性的门控配置（LST PCCACTIONPROP，需"上行发起下行门控=Discard"）
5. 检查Filter/L7Filter配置和生效标记
6. 七层场景额外检查特征库加载状态
7. 如以上均正常，收集EXP MML导出和抓包信息，联系技术支持

**问题：重定向不生效，终端仍访问原始地址**

处理步骤：
1. 检查重定向目标配置（ADD REDIRECT）
2. 检查PCC动作属性的重定向名称配置
3. 检查重定向设备与UDG的互通
4. 对于L3/L4重定向，需先删除原有PCC阻塞Rule，再新增IPREDIR Rule
5. 配置变更后需执行SET REFRESHSRV刷新生效

**问题：Remark不生效，DSCP值未改变**

处理步骤：
1. 确认Alias Marking已关闭（MOD USERPROFILE:ALIASMARKFLAG=DISABLE）
2. 确认入口报文DSCP值与Remark目标值不同
3. 检查Rule的REMARK_FPI配置（REMARKCFGTYPE/REMARKCLASS）
4. 检查FlowFilter绑定关系

---

## 4. 与带宽控制的关系

SA调测是带宽控制场景验证的前提和基础，原因如下：

**4.1 SA识别是带宽管控的前提**

带宽控制的核心流程是：业务识别 -> 策略匹配 -> 动作执行。SA调测验证的正是"业务识别"和"动作执行"两个关键环节：
- **阻塞调测**：验证SA能正确识别业务并执行丢弃动作，这是带宽限速（门控=Discard）的基础
- **Remark调测**：验证SA能正确修改DSCP值，这是QoS标记和差异化带宽保障的基础
- **重定向调测**：验证SA能正确重定向流量，这是URL重定向管控（访问限制场景）的基础

**4.2 配置链路的复用关系**

带宽控制场景（PCC策略、BWM、FUP等）与SA调测共享同一套配置链路：
- User Profile -> Rule Binding -> Rule -> PCC Policy Group -> PCC Action Property -> FlowFilter -> Filter/L7Filter
- 带宽控制的URR（使用量报告规则）和门控（Gate）配置嵌入在PCC动作属性中
- SA调测验证的正是这条配置链路的完整性和正确性

**4.3 调测方法论的可迁移性**

SA调测采用的"渐进式验证"方法论可直接应用于带宽控制场景的调测：
- 先验证基础网络连通性
- 再验证SA识别准确性（通过阻塞动作）
- 最后验证带宽管控效果（限速、门控、Remark）
- 故障排查同样遵循配置链路逆向追溯

**4.4 特征库与协议识别**

带宽控制中的PCC规则、FUP门控等依赖SA准确识别业务类型（如区分视频流、文件下载、Web浏览）。SA调测中特征库加载状态的验证，直接决定了带宽控制策略能否精确匹配目标业务。

---

## 5. 关键术语

| 术语 | 说明 |
|------|------|
| SA (Service Awareness) | 业务感知，UDG识别用户数据报文所属业务类型的能力 |
| L7 (Layer 7) | 七层，指OSI第七层应用层，基于URL/HTTP等应用层信息进行业务识别 |
| L3/L4 (Layer 3/4) | 三四层，指OSI第三/四层网络层/传输层，基于IP/端口信息进行业务识别 |
| Rule | 规则，SA的核心配置对象，定义匹配条件和动作类型 |
| PCC (Policy and Charging Control) | 策略与计费控制，SA的动作执行框架 |
| PCC Action Property | PCC动作属性，定义具体执行动作（门控/重定向等） |
| PCC Policy Group | PCC策略组，动作属性的容器 |
| FlowFilter | 流过滤器，匹配报文流的过滤器组件 |
| L7Filter | 七层过滤器，基于URL等应用层信息匹配报文 |
| Filter | 三四层过滤器，基于IP/端口信息匹配报文 |
| User Profile | 用户模板，Rule的绑定容器，关联到具体用户 |
| Remark | 重标记，修改报文ToS域DSCP值的动作 |
| Redirect | 重定向，将报文转发到指定设备的动作 |
| Block | 阻塞，丢弃匹配报文的动作 |
| DSCP (Differentiated Services Code Point) | 差异化服务代码点，IP报文头中ToS域的字段，用于QoS标记 |
| ToS (Type of Service) | 服务类型，IP报文头中的字段，包含DSCP |
| Alias Marking | 别名标记，UDG的一种报文标记功能，调测Remark时需关闭 |
| Signature Database | 特征库/签名库，七层协议识别依赖的特征数据库 |
| S1-U/N3 | 接入侧接口（4G: S1-U / 5G: N3），面向无线侧 |
| Gi/N6 | DN侧接口（4G: Gi / 5G: N6），面向互联网侧 |
| GTP (GPRS Tunneling Protocol) | GPRS隧道协议，承载用户报文的封装协议 |
| IMSI (International Mobile Subscriber Identity) | 国际移动用户标识，唯一标识移动用户 |
| APN (Access Point Name) | 接入点名称，用户接入网络时使用的标识 |
| MML (Man-Machine Language) | 人机语言，UDG的命令行配置接口 |
| OM Portal | 操作维护门户，UDG的管理界面 |

---

## 6. 知识来源

| 序号 | 文件名 | 说明 |
|------|--------|------|
| 1 | 调测业务感知_87804007.md | 调测总览入口文档，指向六类具体调测场景 |
| 2 | 调测七层阻塞功能_87804012.md | L7阻塞调测：验证URL匹配后的报文丢弃 |
| 3 | 调测七层重定向功能_87804013.md | L7重定向调测：验证URL匹配后的HTTP重定向 |
| 4 | 调测七层Remark功能_87804014.md | L7 Remark调测：验证URL匹配后的DSCP修改 |
| 5 | 调测三四层阻塞功能_87804009.md | L3/L4阻塞调测：验证IP匹配后的报文丢弃 |
| 6 | 调测三四层重定向功能_87804010.md | L3/L4重定向调测：验证IP匹配后的报文重定向 |
| 7 | 调测三四层Remark功能_87804011.md | L3/L4 Remark调测：验证IP匹配后的DSCP修改 |

**源文档路径前缀：**
`output/UDG_Product_Documentation_CH_20.15.2/特性部署/业务专题/UDG业务感知专题/业务感知配置/`

**备注：** 文件1（调测业务感知_87804007.md）本身仅包含简短的入口指引（"具体操作请参见调测七层SA-HTTP业务内容计费"），核心知识提炼自其子目录"调测业务感知/"下的6个详细调测文档。这6个文档构成了完整的SA调测矩阵（2个识别层级 x 3种动作类型）。
