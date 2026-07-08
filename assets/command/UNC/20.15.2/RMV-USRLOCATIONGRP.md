---
id: UNC@20.15.2@MMLCommand@RMV USRLOCATIONGRP
type: MMLCommand
name: RMV USRLOCATIONGRP（删除用户位置组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: USRLOCATIONGRP
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务公共
- 用户位置组
status: active
---

# RMV USRLOCATIONGRP（删除用户位置组）

## 功能

**适用NF：PGW-C、SMF**

该命令用于删除位置组。当运营商希望删除位置组时，则配置该命令。

## 注意事项

- 该命令执行后立即生效。
- 如果不输入位置组名称，表示删除系统中所有位置组。
- 如果位置组已经绑定在USRPROFGROUP中，则不允许删除，需要执行命令RMV UPBINDUPG解除绑定关系后再删除。
- 删除位置组时，如果该位置组下已配置与用户位置的绑定关系，会同步删除绑定关系。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOCGROUPNAME | 位置组名称 | 可选必选说明：必选参数<br>参数含义：指定位置组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| LOCATIONNAME | 位置名称 | 可选必选说明：可选参数<br>参数含义：指定位置信息名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/USRLOCATIONGRP]] · 用户位置组（USRLOCATIONGRP）

## 使用实例

假如运营商需要删除名称为test01的位置组：

```
RMV USRLOCATIONGRP: LOCGROUPNAME="test01";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除用户位置组（RMV-USRLOCATIONGRP）_09897149.md`
