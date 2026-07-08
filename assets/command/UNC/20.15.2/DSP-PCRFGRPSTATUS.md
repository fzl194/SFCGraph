---
id: UNC@20.15.2@MMLCommand@DSP PCRFGRPSTATUS
type: MMLCommand
name: DSP PCRFGRPSTATUS（显示PCRF组状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PCRFGRPSTATUS
command_category: 查询类
applicable_nf:
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- PCRF Diameter连接
- PCRF组状态
status: active
---

# DSP PCRFGRPSTATUS（显示PCRF组状态）

## 功能

**适用NF：PGW-C、GGSN**

此命令用来查询指定PCRF组状态信息，包括PCRF分组内每个PCRF的通信状态和master/slave状态。

## 注意事项

- 查询PCRF分组状态信息时，前提条件为PCRFGRPNAME在对象PCRFGROUP中已配置。
- 只有当PCRF绑定到PCRF Group并且PCRF有链路时，才可以查询到PCRF Group状态信息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PCRFGRPNAME | PCRF组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定PCRF分组的名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～128。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PCRFGRPSTATUS]] · PCRF组状态（PCRFGRPSTATUS）

## 使用实例

查询PCRF分组状态信息：PCRFGRPNAME为“testpcrfgrp1”：

```
DSP PCRFGRPSTATUS: PCRFGRPNAME="testpcrfgrp1";
```

```

PCRF组状态
----------
PCRF ID    POD名称               PCRF主机名    Gx 状态    Master/Slave    本端主机名
0          uncpod-0116-30-0-195  host1         Abnormal   Master          gxlocal     
1          uncpod-0116-30-0-195  host4         Abnormal   Slave           gxlocal     
(Number of results = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示PCRF组状态（DSP-PCRFGRPSTATUS）_09897121.md`
