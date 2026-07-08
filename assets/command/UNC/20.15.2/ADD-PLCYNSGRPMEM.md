---
id: UNC@20.15.2@MMLCommand@ADD PLCYNSGRPMEM
type: MMLCommand
name: ADD PLCYNSGRPMEM（增加用于策略控制的网络切片群组成员）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: PLCYNSGRPMEM
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
- 用于策略控制的网络切片群组成员管理
status: active
---

# ADD PLCYNSGRPMEM（增加用于策略控制的网络切片群组成员）

## 功能

**适用NF：AMF**

该命令用于为应用于AM策略或者UE策略控制的网络切片群组添加成员。

## 注意事项

- 该命令执行后立即生效。

- 一个群组内可添加的最大网络切片数量是128。

- 最多可输入128条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NSGRPID | 网络切片群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定网络切片群组标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~16。本参数通过ADD PLCYNSGRP命令进行配置。<br>默认值：无<br>配置原则：无 |
| NSIDX | 网络切片索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定控制AM策略或UE策略的网络切片。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。本参数通过ADD PLMNNS命令进行配置。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PLCYNSGRPMEM]] · 用于策略控制的网络切片群组成员（PLCYNSGRPMEM）

## 使用实例

将eMBB这个网络切片（索引为18）添加到策略控制群组（组ID为6），执行如下命令：

```
ADD PLCYNSGRPMEM: NSGRPID=6, NSIDX=18;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-PLCYNSGRPMEM.md`
