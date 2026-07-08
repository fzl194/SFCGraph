---
id: UNC@20.15.2@MMLCommand@LST L2RULEBINDGRP
type: MMLCommand
name: LST L2RULEBINDGRP（查询层二规则与层二规则组的绑定关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: L2RULEBINDGRP
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务模板
- 层二规则绑定
status: active
---

# LST L2RULEBINDGRP（查询层二规则与层二规则组的绑定关系）

## 功能

**适用NF：SMF**

该命令用于查询层二规则与层二规则组的绑定关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| L2RULEGROUPNAME | 层二规则组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定层二规则组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD L2RULEGROUP命令配置生成。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@L2RULEBINDGRP]] · 层二规则与层二规则组的绑定关系（L2RULEBINDGRP）

## 使用实例

- 查询层二规则组名称为“rulegrp1”的绑定关系：
  ```
  LST L2RULEBINDGRP: L2RULEGROUPNAME="rulegrp1";
  RETCODE = 0  操作成功

  结果如下
  --------
  层二规则组名称  =  rulegrp1
  层二规则名称  =  rule1
  (结果个数 = 1)

  ---    END
  ```
- 查询系统中所有的层二规则与层二规则组的绑定关系：
  ```
  LST L2RULEBINDGRP:;
  RETCODE = 0  操作成功

  结果如下
  --------
  层二规则组名称  =  rulegrp1
  层二规则名称  =  rule1
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-L2RULEBINDGRP.md`
