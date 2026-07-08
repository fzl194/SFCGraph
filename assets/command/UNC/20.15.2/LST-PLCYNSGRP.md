---
id: UNC@20.15.2@MMLCommand@LST PLCYNSGRP
type: MMLCommand
name: LST PLCYNSGRP（查询用于策略控制的网络切片群组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PLCYNSGRP
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- AM策略和UE策略管理
- 用于策略控制的网络切片群组管理
status: active
---

# LST PLCYNSGRP（查询用于策略控制的网络切片群组）

## 功能

**适用NF：AMF**

该命令用于查询应用于AM策略或者UE策略控制的网络切片群组。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NSGRPID | 网络切片群组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于标识应用于AM策略或者UE策略控制参数的网络切片群组。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~16。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PLCYNSGRP]] · 用于策略控制的网络切片群组（PLCYNSGRP）

## 使用实例

- 查询“网络切片群组标识”为“1”的用于AM策略或者UE策略控制的网络切片群组，执行如下命令：
  ```
  %%LST PLCYNSGRP: NSGRPID=1;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  网络切片群组标识   =  1
           描述信息  =  group1
  (结果个数 = 1)

  ---    END
  ```
- 查询系统内当前配置的用于AM策略或者UE策略控制的网络切片群组，执行如下命令：
  ```
  %%LST PLCYNSGRP:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  网络切片群组标识   =  1
           描述信息  =  group1
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询用于策略控制的网络切片群组（LST-PLCYNSGRP）_25121192.md`
