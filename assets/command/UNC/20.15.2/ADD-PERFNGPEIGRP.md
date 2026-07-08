---
id: UNC@20.15.2@MMLCommand@ADD PERFNGPEIGRP
type: MMLCommand
name: ADD PERFNGPEIGRP（增加NG PEI组性能统计对象）
nf: UNC
version: 20.15.2
verb: ADD
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

# ADD PERFNGPEIGRP（增加NG PEI组性能统计对象）

## 功能

**适用NF：AMF**

该命令用于手工增加NG PEI组性能统计对象的配置。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入50条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NGPEIGPN | NG PEI群组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于标识NG PEI组的性能统计对象名称。NG PEI组内的PEI成员通过ADD NGPEIGRPMEM命令进行增加。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~128。不区分大小写，不支持空格及“\”且全局唯一。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [NG PEI组性能统计对象（PERFNGPEIGRP）](configobject/UNC/20.15.2/PERFNGPEIGRP.md)

## 使用实例

增加一个PEI群组，其群组名称为“phone_xx”：

```
ADD PERFNGPEIGRP: NGPEIGPN="phone_xx";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加NG-PEI组性能统计对象（ADD-PERFNGPEIGRP）_43239046.md`
