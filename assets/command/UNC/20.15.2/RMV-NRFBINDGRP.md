---
id: UNC@20.15.2@MMLCommand@RMV NRFBINDGRP
type: MMLCommand
name: RMV NRFBINDGRP（删除对端NRF实例组成员）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NRFBINDGRP
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 分层NRF管理
- NRF拓扑配置
- NRF实例组成员管理
status: active
---

# RMV NRFBINDGRP（删除对端NRF实例组成员）

## 功能

**适用NF：NRF**

该命令用于删除对端NRF实例组的成员。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NRFINSTNAME | NRF实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示对端NRF实例组中NRF实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~38。<br>默认值：无<br>配置原则：无 |
| GROUPNAME | 实例组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示对端NRF实例组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFBINDGRP]] · 对端NRF实例组成员（NRFBINDGRP）

## 使用实例

当实例组名为nrfgroup001的对端NRF组中，实例名为nrfinstname001的NRF实例不再提供服务时，配置此命令。

```
RMV NRFBINDGRP: NRFINSTNAME="nrfinstname001", GROUPNAME="nrfgroup001";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NRFBINDGRP.md`
