---
id: UDG@20.15.2@MMLCommand@RMV ABSTIMERANGE
type: MMLCommand
name: RMV ABSTIMERANGE（删除绝对时间段）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: ABSTIMERANGE
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
- 绝对时间段
status: active
---

# RMV ABSTIMERANGE（删除绝对时间段）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于删除配置的绝对时间段信息。当系统的业务不再需要在特定的绝对时间段内生效时，使用此命令进行删除绝对时间段配置。

## 注意事项

- 该命令执行后立即生效。
- 如果只输入时间段名称，则删除该时间段下所有的绝对时间段配置信息。
- 如果同时输入时间段名称和绝对时间段的序号值，则删除该条绝对时间段配置信息。
- 如果不输入参数，则删除所有时间段下所有的绝对时间段配置信息。
- 如果时间段已经被绑定到Rule、AclBindApn或者BwmRule，则不允许删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TIMERANGENAME | 时间段名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置时间段的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写，以字母开头。<br>默认值：无<br>配置原则：该参数使用ADD TIMERANGE命令配置生成。 |
| ABSTIMERANGESEQ | 绝对时间段序号 | 可选必选说明：可选参数<br>参数含义：该参数用于设置绝对时间段的序号值。在一个时间段内，绝对时间段序号不能重复，每一个序号代表一个绝对时间段。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～12。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@ABSTIMERANGE]] · 绝对时间段（ABSTIMERANGE）

## 使用实例

假设运营商需要删除一条绝对时间段配置，则执行如下命令：

```
RMV ABSTIMERANGE:TIMERANGENAME="t1",ABSTIMERANGESEQ=1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-ABSTIMERANGE.md`
