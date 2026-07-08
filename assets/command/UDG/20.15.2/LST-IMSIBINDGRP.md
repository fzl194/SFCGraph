---
id: UDG@20.15.2@MMLCommand@LST IMSIBINDGRP
type: MMLCommand
name: LST IMSIBINDGRP（查询IMSI和IMSI组绑定关系）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: IMSIBINDGRP
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- TCP优化服务管理
- IMSI组配置
status: active
---

# LST IMSIBINDGRP（查询IMSI和IMSI组绑定关系）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询小区信息。

## 注意事项

- 如果不输入小区名称，表示查询系统中所有小区信息。
- 如果输入小区名称，表示查询指定的小区信息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSIGROUPNAME | IMSI 组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置IMSI组名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [IMSI和IMSI组绑定关系（IMSIBINDGRP）](configobject/UDG/20.15.2/IMSIBINDGRP.md)

## 使用实例

- 假如运营商需要查询名称为TestCellName的小区：
  ```
  LST CELL: CELLNAME="TestCellName";
  ```
  ```

  RETCODE = 0  操作成功

  小区信息
  ----------------
  小区名称  =  TestCellName
  小区ID  =  123456789
  (结果个数 = 1)

  ---    END
  ```
- 假如运营商需要查询所有的小区：
  ```
  LST CELL:;
  ```
  ```

  RETCODE = 0  操作成功

  小区信息
  ----------------
  小区名称       小区ID
  TestCellName   123456789
  TestCellName2  1234567890
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询IMSI和IMSI组绑定关系（LST-IMSIBINDGRP）_87096438.md`
