---
id: UDG@20.15.2@MMLCommand@LST CELLBINDGRP
type: MMLCommand
name: LST CELLBINDGRP（查询小区和小区组绑定关系）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: CELLBINDGRP
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- TCP优化服务管理
- 小区组绑定
status: active
---

# LST CELLBINDGRP（查询小区和小区组绑定关系）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询小区组和小区的绑定关系。

## 注意事项

- 如果不输入小区组名称，表示查询系统中所有小区组和小区的绑定关系。
- 如果输入小区组名称，表示查询指定的小区组和小区的绑定关系。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CELLGROUPNAME | 小区组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置小区组名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD CELLBINDGRP命令配置生成。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CELLBINDGRP]] · 小区和小区组绑定关系（CELLBINDGRP）

## 使用实例

- 假如运营商需要查询名称为TestCellGroupName的小区组下绑定的小区信息：
  ```
  LST CELLBINDGRP: CELLGROUPNAME="TestCellGroupName";
  ```
  ```

  RETCODE = 0  操作成功

  小区和小区组绑定关系
  ----------------
  小区组名称     小区名称
  TestCellGroupName  TestCellName
  TestCellGroupName  TestCellName2  
  (结果个数 = 2)

  ---    END
  ```
- 假如运营商需要查询所有的小区组下绑定的小区信息：
  ```
  LST CELLBINDGRP:;
  ```
  ```

  RETCODE = 0  操作成功

  小区和小区组绑定关系
  ----------------
  小区组名称     小区名称
  TestCellGroupName  TestCellName
  TestCellGroupName  TestCellName2 
  TestCellGroupName1 TestCellName3
  TestCellGroupName1 TestCellName4
  (结果个数 = 4)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-CELLBINDGRP.md`
