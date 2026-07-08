---
id: UNC@20.15.2@MMLCommand@SET DFTGLBPCRFGRP
type: MMLCommand
name: SET DFTGLBPCRFGRP（设置全局缺省PCRF组）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: DFTGLBPCRFGRP
command_category: 配置类
applicable_nf:
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- PCRF Diameter连接
- 缺省全局PCRF组
status: active
---

# SET DFTGLBPCRFGRP（设置全局缺省PCRF组）

## 功能

**适用NF：PGW-C、GGSN**

此命令用来修改缺省全局PCRF分组。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PCRFGRPNAME | PCRF组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置绑定的PCRF组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～128。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DFTGLBPCRFGRP]] · 全局缺省PCRF组（DFTGLBPCRFGRP）

## 使用实例

修改DFTGLBPCRFGRP：PCRFGRPNAME为pcr：

```
SET DFTGLBPCRFGRP:PCRFGRPNAME="pcr";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-DFTGLBPCRFGRP.md`
