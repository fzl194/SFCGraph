---
id: UDG@20.15.2@MMLCommand@ADD SPECURRGRPLIST
type: MMLCommand
name: ADD SPECURRGRPLIST（增加特殊URR组列表）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: SPECURRGRPLIST
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 40000
category_path:
- 用户面服务管理
- 业务控制策略
- 计费控制
- 特殊使用率上报规则组列表
status: active
---

# ADD SPECURRGRPLIST（增加特殊URR组列表）

## 功能

**适用NF：PGW-U、UPF**

该命令用于配置特殊的使用量上报规则组列表，其他功能可以使用该列表内容决策当前业务流是否需要做特殊处理。如HTTP计费防欺诈功能，使用该列表内容决策当前业务流是否需要做防欺诈处理。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为40000。
- 当特殊使用量上报规则组列表用于防欺诈检测，在进行欺诈用户流量检测时，如果用户同时使能了离线计费和在线计费，欺诈流量统计只会使用URR Group中绑定的离线计费URR的流量（如果没有绑定则不统计），不统计在线计费URR的流量；使用N40融合计费时，如果使用了SID级计费，为了避免欺诈流量统计重复，不要将RG对应的URR Group设置为特殊使用量上报规则组。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| URRGROUPNAME | URR组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置特殊使用量上报规则组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD URRGROUP命令配置生成。 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SPECURRGRPLIST]] · 特殊URR组列表（SPECURRGRPLIST）

## 关联任务

- [[UDG@20.15.2@Task@0-00014]]

## 使用实例

配置URR组cp_token作为特殊的使用量上报规则组：

```
ADD SPECURRGRPLIST: URRGROUPNAME="cp_token";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加特殊URR组列表（ADD-SPECURRGRPLIST）_82837643.md`
