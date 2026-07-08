---
id: UDG@20.15.2@MMLCommand@ADD TIMERANGE
type: MMLCommand
name: ADD TIMERANGE（增加时间段）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: TIMERANGE
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 200
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 时间规则管理
- 时间段
status: active
---

# ADD TIMERANGE（增加时间段）

## 功能

**适用NF：PGW-U、UPF**

该命令用于配置一个时间段，描述一个特定的时间范围。当系统的业务需要在特定的时间段内生效时，使用此命令进行配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为200。
- 每个时间段下最多可以配32条周期时间段和12条绝对时间段。
- 如果时间段同时包含周期时间段、绝对时间段，则时间段生效范围是：绝对时间段的并集和周期时间段的并集的交集范围，若当前时间在这个范围之内则为生效，不在这范围内则失效。
- 如果时间段只包含周期时间段，则当前时间在周期时间段内则生效，在周期时间段外则为失效。
- 如果时间段只包含绝对时间段，则当前时间在绝对时间段内则生效，在绝对时间段外则为失效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TIMERANGENAME | 时间段名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置时间段的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写，以字母开头。<br>默认值：无<br>配置原则：无 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [时间段（TIMERANGE）](configobject/UDG/20.15.2/TIMERANGE.md)

## 使用实例

假设运营商需要设置一个时间段，名字为t1，则按如下命令配置：

```
ADD TIMERANGE:TIMERANGENAME="t1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加时间段（ADD-TIMERANGE）_82837419.md`
