---
id: UNC@20.15.2@MMLCommand@RMV PCRFBINDGRP
type: MMLCommand
name: RMV PCRFBINDGRP（删除PCRF与PCRF Group的关联关系）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PCRFBINDGRP
command_category: 配置类
applicable_nf:
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- PCRF Diameter连接
- PCRF绑定
status: active
---

# RMV PCRFBINDGRP（删除PCRF与PCRF Group的关联关系）

## 功能

**适用NF：PGW-C、GGSN**

此命令用于从PCRF分组中删除指定的PCRF。

## 注意事项

- 该命令执行后立即生效。
- 当未指定PCRF主机名称时，禁止执行该命令。若需要执行，需将软参BYTE976的值设置为169。
- 当不指定PCRF时，是删除整个PCRF组。当指定PCRF时，是从指定组中移除该PCRF。
- 当PCRF从组中移除时：如果其是组内的当前Master PCRF，则会从组内剩下的PCRF中轮选下一个可用的PCRF作为新的Master PCRF。
- 从PCRF组内移除某个PCRF时，请采用新建并绑定新PCRF组，同时解绑定旧PCRF组的方式。当PCRF从指定组中移除后，如果该组内剩下的PCRF都不可用，将导致后续新建立并且关联到该PCRF组的会话授权失败，PCRF组整个被删除之后的结果与此类似。
- 轮选原则，按照配置顺序，选PCRF为主的PCRF，确保重启后或配置导出时顺序不变，建议规划备PCRF名称按备PCRF使用优先级的顺序进行排序。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PCRFGRPNAME | PCRF组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定PCRF分组的名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～128。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| PCRFHOSTNAME | PCRF主机名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定PCRF的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PCRFBINDGRP]] · PCRF与PCRF Group的关联关系（PCRFBINDGRP）

## 使用实例

删除Pcrf与PCRF Group的关联关系，删除PCRF组为“abc”的记录：

```
RMV PCRFBINDGRP:PCRFGRPNAME="abc";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-PCRFBINDGRP.md`
