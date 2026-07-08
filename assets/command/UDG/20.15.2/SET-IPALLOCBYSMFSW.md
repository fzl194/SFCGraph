---
id: UDG@20.15.2@MMLCommand@SET IPALLOCBYSMFSW
type: MMLCommand
name: SET IPALLOCBYSMFSW（设置基于SMF分配地址的开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: IPALLOCBYSMFSW
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 64
category_path:
- 用户面服务管理
- 会话管理
- 会话地址管理
- 基于SMF分配地址开关
status: active
---

# SET IPALLOCBYSMFSW（设置基于SMF分配地址的开关）

## 功能

**适用NF：PGW-U、UPF**

该命令用于配置基于SMF分配地址开关。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为64。
- 开关为INHERIT时，按照基于SMF分配地址的全局开关的配置进行地址分配，不为INHERIT时，按照基于SMF分配地址的开关配置进行地址分配。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SMF | SMF名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SMF实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～255。只能由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：该SMF必须通过ADD CPNODEID命令配置过。 |
| SWITCH | IPv4 开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定基于SMF分配地址的IPv4开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>- INHERIT：继承。<br>默认值：无<br>配置原则：无 |
| IPV6SWITCH | IPv6 开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定基于SMF分配地址的IPv6开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>- INHERIT：继承。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IPALLOCBYSMFSW]] · 基于SMF分配地址开关（IPALLOCBYSMFSW）

## 使用实例

禁止名为smfnode1的SMF实例基于SMF分配地址：

```
SET IPALLOCBYSMFSW: SMF="smfnode1", SWITCH=DISABLE, IPV6SWITCH=DISABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-IPALLOCBYSMFSW.md`
