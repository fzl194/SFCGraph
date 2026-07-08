---
id: UNC@20.15.2@MMLCommand@RMV PLCYNSGRP
type: MMLCommand
name: RMV PLCYNSGRP（删除用于策略控制的网络切片群组）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV PLCYNSGRP（删除用于策略控制的网络切片群组）

## 功能

**适用NF：AMF**

该命令用于删除应用于AM策略或者UE策略控制的网络切片群组。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NSGRPID | 网络切片群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于标识应用于AM策略或者UE策略控制参数的网络切片群组。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~16。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PLCYNSGRP]] · 用于策略控制的网络切片群组（PLCYNSGRP）

## 使用实例

运营商不再需要针对群组1内的网络切片进行特殊的AM策略或者UE策略控制，故删除网络切片群组1，执行命令如下：

```
RMV PLCYNSGRP: NSGRPID=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-PLCYNSGRP.md`
