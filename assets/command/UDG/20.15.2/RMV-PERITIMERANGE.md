---
id: UDG@20.15.2@MMLCommand@RMV PERITIMERANGE
type: MMLCommand
name: RMV PERITIMERANGE（删除周期时间段）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: PERITIMERANGE
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 时间规则管理
- 周期时间段
status: active
---

# RMV PERITIMERANGE（删除周期时间段）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于删除配置的周期时间段信息。当系统的业务不再需要在特定的周期时间段内生效时，使用此命令进行删除周期时间段配置。

## 注意事项

- 该命令执行后立即生效。
- 如果只输入时间段名称，则删除该时间段下所有的周期时间段配置信息。
- 如果同时输入时间段名称和周期时间段的序号值，则删除该条周期时间段配置信息。
- 如果不输入参数，则删除所有时间段下所有的周期时间段配置信息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TIMERANGENAME | 时间段名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置时间段的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写，以字母开头。<br>默认值：无<br>配置原则：无 |
| PERITMRANGESEQ | 周期时间段序号 | 可选必选说明：可选参数<br>参数含义：该参数用于设置周期时间段的序号值。在一个时间段内，周期时间段序号不能重复，每一个序号代表一个周期时间段。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [周期时间段（PERITIMERANGE）](configobject/UDG/20.15.2/PERITIMERANGE.md)

## 使用实例

假设运营商需要删除一条周期时间段配置，则执行如下命令：

```
RMV PERITIMERANGE:TIMERANGENAME="t1",PERITMRANGESEQ=1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除周期时间段（RMV-PERITIMERANGE）_82837430.md`
