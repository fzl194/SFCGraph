---
id: UDG@20.15.2@MMLCommand@RMV POOLGROUP
type: MMLCommand
name: RMV POOLGROUP（删除地址池组）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: POOLGROUP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: true
category_path:
- 用户面服务管理
- 会话管理
- 会话地址管理
- 地址池组
status: active
---

# RMV POOLGROUP（删除地址池组）

## 功能

**适用NF：PGW-U、UPF**

![](删除地址池组（RMV POOLGROUP）_82837140.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，删除时将导致地址资源变少，可能导致激活失败。

该命令用于删除指定的地址池组。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 删除地址池组时，会删除关联的PoolBindGroup实例。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLGRPNAME | 地址池组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定地址池组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～79。不支持空格及特殊字符“#”、“$”和“&”等，由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD POOLGROUP命令配置生成。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/POOLGROUP]] · 地址池组（POOLGROUP）

## 使用实例

删除地址池组名为poolgroup1的地址池组：

```
RMV POOLGROUP: POOLGRPNAME="poolgroup1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-POOLGROUP.md`
