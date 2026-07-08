---
id: UNC@20.15.2@MMLCommand@LST USRLOCATIONGRP
type: MMLCommand
name: LST USRLOCATIONGRP（查询用户位置组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: USRLOCATIONGRP
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务公共
- 用户位置组
status: active
---

# LST USRLOCATIONGRP（查询用户位置组）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询位置组。当运营商希望查询位置组时，则执行该命令。

## 注意事项

如果不输入位置组名称，表示查询系统中所有位置组。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOCGROUPNAME | 位置组名称 | 可选必选说明：可选参数<br>参数含义：指定位置组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/USRLOCATIONGRP]] · 用户位置组（USRLOCATIONGRP）

## 使用实例

- 假如运营商需要查询名称为test01的位置组信息：
  ```
  LST USRLOCATIONGRP: LOCGROUPNAME="test01";
  ```
  ```

  RETCODE = 0  操作成功

  位置组信息
  ----------
  位置组名称  =  test01
    位置名称  =  testloc01
  (结果个数 = 1)

  ---    END
  ```
- 假如运营商需要查询所有的位置组信息：
  ```
  LST USRLOCATIONGRP:;
  ```
  ```

  RETCODE = 0  操作成功

  位置组信息
  ----------
  位置组名称  =  test01
    位置名称  =  testloc01
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询用户位置组（LST-USRLOCATIONGRP）_09897150.md`
