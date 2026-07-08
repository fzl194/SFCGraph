---
id: UDG@20.15.2@MMLCommand@ADD POOLGROUP
type: MMLCommand
name: ADD POOLGROUP（添加地址池组）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: POOLGROUP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: false
max_records: 40000
category_path:
- 用户面服务管理
- 会话管理
- 会话地址管理
- 地址池组
status: active
---

# ADD POOLGROUP（添加地址池组）

## 功能

**适用NF：PGW-U、UPF**

该命令用于添加一个新的地址池组。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为40000。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLGRPNAME | 地址池组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定地址池组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～79。不支持空格及特殊字符“#”、“$”和“&”等，由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：无 |
| IPV4ALLOCPRIALG | IPV4基于地址池优先级分配地址算法 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPv4地址池是否使用基于地址池优先级算法。若开启，则从该地址池组中选取IPv4类型地址时，按优先级算法进行选取。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：DISABLE<br>配置原则：<br>- ENABLE：开启基于地址池优先级算法选取IPV4地址的功能。<br>- DISABLE：关闭基于地址池优先级算法选取IPV4地址的功能。 |
| IPV6ALLOCPRIALG | IPV6基于地址池优先级分配地址算法 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IPv6地址池是否使用基于地址池优先级算法。若开启，则从该地址池组中选取IPv6类型地址时，按优先级算法进行选取。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：DISABLE<br>配置原则：<br>- ENABLE：开启基于地址池优先级算法选取IPV6地址的功能。<br>- DISABLE：关闭基于地址池优先级算法选取IPV6地址的功能。 |

## 操作的配置对象

- [地址池组（POOLGROUP）](configobject/UDG/20.15.2/POOLGROUP.md)

## 关联任务

- [0-00042](task/UDG/20.15.2/0-00042.md)

## 使用实例

创建一个地址池组，其中的IPv4地址池使用基于地址池优先级算法，IPv6地址池不使用基于地址池优先级算法：

```
ADD POOLGROUP: POOLGRPNAME="poolgroup1", IPV4ALLOCPRIALG=ENABLE, IPV6ALLOCPRIALG=DISABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/添加地址池组（ADD-POOLGROUP）_82837138.md`
