---
id: UNC@20.15.2@MMLCommand@RMV PERFNGPEIGRP
type: MMLCommand
name: RMV PERFNGPEIGRP（删除NG PEI组性能统计对象）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PERFNGPEIGRP
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- AMF性能对象管理
status: active
---

# RMV PERFNGPEIGRP（删除NG PEI组性能统计对象）

## 功能

**适用NF：AMF**

该命令用于删除指定的NG PEI组性能统计对象。

## 注意事项

- 该命令执行后立即生效。

- 在执行本命令之前请首先通过RMV NGPEIGRPMEM删除NG PEI群组下的所有成员。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NGPEIGPN | NG PEI群组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于标识NG PEI组的性能统计对象名称。NG PEI组内的PEI成员通过ADD NGPEIGRPMEM命令进行增加。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~128。不区分大小写，不支持空格及“\”且全局唯一。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PERFNGPEIGRP]] · NG PEI组性能统计对象（PERFNGPEIGRP）

## 使用实例

删除群组名称为“phone_xx”的PEI群组：

```
RMV PERFNGPEIGRP: NGPEIGPN="phone_xx";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-PERFNGPEIGRP.md`
