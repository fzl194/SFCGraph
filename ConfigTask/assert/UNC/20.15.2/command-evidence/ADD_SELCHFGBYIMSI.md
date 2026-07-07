# 命令证据包：ADD SELCHFGBYIMSI
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/CHF选择/增加IMSI与CHF组的绑定关系（ADD SELCHFGBYIMSI）_88303804.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SMF、PGW-C、GGSN**

该命令用于增加IMSI与CHF组的绑定关系。一般用于拨测场景，将指定IMSI的用户的计费信息发送到指定CHF上，测试CHF的基本功能。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 该命令用于拨测CHF，拨测完成后建议立即删除该配置。
- SMF选择CHF的优先级从高到低依次是：基于IMSI选择CHF > 基于IMSI号段选择CHF > 基于PCF下发的信息选择CHF > 基于从UDM获取的签约CC选择CHF > 基于标准化服务发现选择CHF > 基于SMF本地配置的CC选择CHF。

- 最多可输入30条记录。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| IMSI | 用户的IMSI | local_planned | required | 无 | 字符串类型，输入长度范围是14~15。 |
| PRIMARYCHFGRP | 主CHF组 | global_planned | optional | 无 | 字符串类型，输入长度范围是0~63。 |
| SECONDARYCHFGRP | 备CHF组 | global_planned | optional | 无 | 字符串类型，输入长度范围是0~63。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011206

**md：`WSFD-011206/计费会话创建流程_01_10001.md`**
- 操作步骤上下文（±2 行原文）：
  L59:
    >   | ![](计费会话创建流程_01_10001.assets/zh-cn_image_0284971048_2.png) | 由UPF分配的用户IP地址。 |
    > 8. SMF**选择CHF**的方法按优先级从高到低排列如下所示。其中，CC是3GPP协议定义的一种用户签约付费属性，可以由UDM下发，也可以在SMF上本地配置。
    >     a. 拨测场景，SMF根据本地配置**ADD SELCHFGBYIMSI**命令选择CHF，即基于IMSI选择CHF。
    >     b. 配置基于IMSI号段选择CHF，针对现网存在多个CHF主备组，为了避免CHF之间业务不均衡，通过将不同IMSI号段范围和CHF主备组的绑定将用户分流到不同CHF。
    >     c. SMF从PCF下发的chargingInfo属性获取CHF的信息。

**md：`WSFD-011206/配置CHF选择方式_92091086.md`**
- 数据规划表（该命令的参数行）：
  | **ADD SELCHFGBYIMSI** | 用户的IMSI（IMSI） | 123456789012345 | 本端规划 | 配置IMSI与主备CHF组的绑定关系。一般用于拨测场景，将指定IMSI的用户的计费信息发送到指定CHF上，测试CHF的基本功能。 |
  | **ADD SELCHFGBYIMSI** | 主CHF组（PRIMARYCHFGRP） | ChfGroup1 | 全网规划 | 配置IMSI与主备CHF组的绑定关系。一般用于拨测场景，将指定IMSI的用户的计费信息发送到指定CHF上，测试CHF的基本功能。 |
  | **ADD SELCHFGBYIMSI** | 备CHF组（SECONDARYCHFGRP） | ChfGroup2 | 全网规划 | 配置IMSI与主备CHF组的绑定关系。一般用于拨测场景，将指定IMSI的用户的计费信息发送到指定CHF上，测试CHF的基本功能。 |
- 任务示例脚本（该命令行）：
  `ADD SELCHFGBYIMSI: IMSI="123456789012345", PRIMARYCHFGRP="ChfGroup1", SECONDARYCHFGRP="ChfGroup2";`
- 操作步骤上下文（±2 行原文）：
  L14:
    > UNC选择CHF的优先级从高到低依次是：基于IMSI选择CHF > 基于IMSI号段选择CHF > 基于PCF下发的信息选择CHF > 基于从UDM获取的签约CC选择CHF > 基于标准化服务发现选择CHF > 基于SMF本地配置的CC选择CHF > 基于SMF本地配置的全局默认CHF组选择CHF。如果无法通过高优先级的方式选择CHF，则依次向下使用低一级别的方式进行选择。
    > 
    > 其中，通过 **ADD SELCHFGBYIMSI** 命令配置基于IMSI选择CHF方式一般用于测试场景，将指定IMSI的用户的计费信息发送到指定CHF上，测试CHF的基本功能。
    > 
    > > **说明**
  L64:
    > 
    > - 配置基于IMSI选择CHF组。一般用于拨测场景，将指定IMSI的用户的计费信息发送到指定CHF上，测试CHF的基本功能。
    >   **ADD SELCHFGBYIMSI**
    > - 配置基于IMSI号段选择CHF。针对现网存在多个CHF主备组，为了避免CHF之间业务不均衡，通过将不同IMSI号段范围和CHF主备组的绑定将用户分流到不同CHF。
    >   ****ADD SELCHFGBIMSISEG****
  L134:
    > ADD TNFBINDGRP: TNFGRPINDEX=1, TNFINSINDEX=1;
    > ADD TNFBINDGRP: TNFGRPINDEX=2, TNFINSINDEX=2;
    > ADD SELCHFGBYIMSI: IMSI="123456789012345", PRIMARYCHFGRP="ChfGroup1", SECONDARYCHFGRP="ChfGroup2";
    > ```
    > 

## ④ 自动比对
- 命令真相参数（3）：['IMSI', 'PRIMARYCHFGRP', 'SECONDARYCHFGRP']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 1, '全网规划': 2}（多值→atom 应考虑 decision_driven）
