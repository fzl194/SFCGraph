---
id: UNC@20.15.2@MMLCommand@LST GMLCSELGRP
type: MMLCommand
name: LST GMLCSELGRP（查询GMLC选择策略组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GMLCSELGRP
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- LCS
- GMLC选择策略组
status: active
---

# LST GMLCSELGRP（查询GMLC选择策略组）

## 功能

**适用网元：MME**

该命令用于查询GMLC选择策略组。

## 注意事项

- 无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GMLCGRPID | GMLC选择策略组索引 | 可选必选说明：可选参数<br>参数含义：该参数在系统内唯一标识一个GMLC选择策略组。<br>数据来源：本端规划<br>取值范围：0~191<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GMLCSELGRP]] · GMLC选择策略组（GMLCSELGRP）

## 使用实例

1. 查询所有GMLC选择策略组。
  LST GMLCSELGRP:;
  ```
  %%LST GMLCSELGRP:;%%
  RETCODE = 0  操作成功。

  输出结果如下
  --------------
  GMLC选择策略组索引  =  0
                描述  =  noname
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询GMLC选择策略组(LST-GMLCSELGRP)_72345411.md`
