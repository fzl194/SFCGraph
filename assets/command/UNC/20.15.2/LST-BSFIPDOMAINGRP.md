---
id: UNC@20.15.2@MMLCommand@LST BSFIPDOMAINGRP
type: MMLCommand
name: LST BSFIPDOMAINGRP（查询IPDOMAIN组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: BSFIPDOMAINGRP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 本局信息管理
- SMF
- BSF信息管理
status: active
---

# LST BSFIPDOMAINGRP（查询IPDOMAIN组）

## 功能

该命令用于查询IPDOMAIN组。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRPNAME | IPDOMAIN组名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPDOMAIN组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@BSFIPDOMAINGRP]] · IPDOMAIN组（BSFIPDOMAINGRP）

## 使用实例

查询IPDOMAIN组"ipdomaingroup1"中的IPDOMAIN信息：

```
%%LST BSFIPDOMAINGRP: GRPNAME="ipdomaingroup1";%%
RETCODE = 0  操作成功

结果如下
--------
IPDOMAIN组名  =  ipdomaingroup1
IPDOMAIN名称  =  Domain_0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-BSFIPDOMAINGRP.md`
