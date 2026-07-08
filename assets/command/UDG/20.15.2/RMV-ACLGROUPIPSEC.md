---
id: UDG@20.15.2@MMLCommand@RMV ACLGROUPIPSEC
type: MMLCommand
name: RMV ACLGROUPIPSEC（删除ACL规则组）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: ACLGROUPIPSEC
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- ACL管理
- ACL规则组
status: active
---

# RMV ACLGROUPIPSEC（删除ACL规则组）

## 功能

![](删除ACL规则组（RMV ACLGROUPIPSEC）_80432534.assets/notice_3.0-zh-cn.png)

删除ACL规则组，影响业务流量使用IPSEC进行加解密功能，有业务影响。

该命令用于删除ACL规则组。

> **说明**
> - 该命令执行后立即生效。
>
> - 如果规则组下配置了规则，则所有规则会一并删除。
> - 如果有业务已经在IPSEC策略中配置了该规则组，不可以删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ACLNAME | ACL规则组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定规则组名称或是编号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不支持空格，区分大小写。以英文字母a～z或A～Z开始，可以是英文字母、数字、连字符“-”、下划线“_”或中文字符的组合。整数形式，取值范围是3000～3999（高级ACL），但兼容CE版本，允许配置其他数值但不会生效。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@ACLGROUPIPSEC]] · ACL规则组（ACLGROUPIPSEC）

## 使用实例

用户不再使用ACL进行报文过滤，可以将规则组3005删除：

```
RMV ACLGROUPIPSEC: ACLNAME="3005";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-ACLGROUPIPSEC.md`
