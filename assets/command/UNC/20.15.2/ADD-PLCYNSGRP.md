---
id: UNC@20.15.2@MMLCommand@ADD PLCYNSGRP
type: MMLCommand
name: ADD PLCYNSGRP（增加用于策略控制的网络切片群组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PLCYNSGRP
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- AM策略和UE策略管理
- 用于策略控制的网络切片群组管理
status: active
---

# ADD PLCYNSGRP（增加用于策略控制的网络切片群组）

## 功能

**适用NF：AMF**

该命令用于配置应用于AM策略或者UE策略控制的网络切片群组。AMF可基于该群组内的网络切片控制是否向PCF发起AM策略或者UE策略的偶联创建。

## 注意事项

- 该命令执行后立即生效。

- AM策略或者UE策略的控制参数通过ADD AMUEPLCYCTRL命令指定。
- 用于策略控制的网络切片群组成员通过ADD PLCYNSGRPMEM进行添加。

- 最多可输入16条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NSGRPID | 网络切片群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于标识应用于AM策略或者UE策略控制参数的网络切片群组。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~16。<br>默认值：无<br>配置原则：无 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数是对用于AM策略或者UE策略控制的网络切片群组的描述信息，在运维中起助记作用。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：<br>输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [用于策略控制的网络切片群组（PLCYNSGRP）](configobject/UNC/20.15.2/PLCYNSGRP.md)

## 使用实例

运营商期望仅使用eMBB切片的用户应用签约或AMF本地的AM策略（即不从PCF获取AM策略），首先需要为该切片创建并添加到群组，并通过ADD AMUEPLCYCTRL进行参数控制。为了添加切片群组，执行命令如下：

```
ADD PLCYNSGRP: NSGRPID=1, DESC="for eMBB";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加用于策略控制的网络切片群组（ADD-PLCYNSGRP）_25120876.md`
