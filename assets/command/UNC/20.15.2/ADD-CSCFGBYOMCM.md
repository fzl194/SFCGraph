---
id: UNC@20.15.2@MMLCommand@ADD CSCFGBYOMCM
type: MMLCommand
name: ADD CSCFGBYOMCM（增加业务读取OM缓存数据的配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: CSCFGBYOMCM
command_category: 配置类
applicable_nf:
- PGW-C
- AMF
- SMF
- GGSN
- SGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 扩展调测
- OM调测
status: active
---

# ADD CSCFGBYOMCM（增加业务读取OM缓存数据的配置）

## 功能

**适用NF：PGW-C、AMF、SMF、GGSN、SGW-C**

该命令用于业务读取OM缓存数据，而不是从本地缓存读取。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入4096条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MMLNAME | 配置命令名称 | 可选必选说明：必选参数<br>参数含义：该参数表示配置命令的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~64。不能为非法字符，只允许输入字母和数字，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数表示配置命令的名称，比如PLMNNS，不要输入ADD/RMV/MOD/LST等操作字符，优先LST命令名称。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CSCFGBYOMCM]] · 业务读取OM缓存数据的配置（CSCFGBYOMCM）

## 使用实例

假设发现业务进程正在使用的PLMNNS配置缓存数据和OM的数据不一致，则可以使用该配置使得业务进程从OM读取配置数据：

```
ADD CSCFGBYOMCM:MMLNAME="PLMNNS";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加业务读取OM缓存数据的配置（ADD-CSCFGBYOMCM）_51335373.md`
