---
id: UNC@20.15.2@MMLCommand@RMV PLCYNSGRPMEM
type: MMLCommand
name: RMV PLCYNSGRPMEM（删除用于策略控制的网络切片群组成员）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV PLCYNSGRPMEM（删除用于策略控制的网络切片群组成员）

## 功能

**适用NF：AMF**

该命令用于从应用于AM策略或者UE策略控制的网络切片群组中删除成员。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NSGRPID | 网络切片群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定网络切片群组标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~16。本参数通过ADD PLCYNSGRP命令进行配置。<br>默认值：无<br>配置原则：无 |
| NSIDX | 网络切片索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定控制AM策略或UE策略的网络切片。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。本参数通过ADD PLMNNS命令进行配置。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PLCYNSGRPMEM]] · 用于策略控制的网络切片群组成员（PLCYNSGRPMEM）

## 使用实例

索引为9的网络切片不再需要进行特殊的AM策略控制，将其从群组1中删除，执行命令如下：

```
RMV PLCYNSGRPMEM: NSGRPID=1, NSIDX=9;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-PLCYNSGRPMEM.md`
