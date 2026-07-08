---
id: UDG@20.15.2@MMLCommand@RMV HBUSRATTRCONF
type: MMLCommand
name: RMV HBUSRATTRCONF（删除高带宽用户属性）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: HBUSRATTRCONF
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 体验分级
- 体验分级用户匹配
- 高带宽用户属性
status: active
---

# RMV HBUSRATTRCONF（删除高带宽用户属性）

## 功能

**适用NF：PGW-U、UPF**

该命令用于删除高带宽用户属性配置。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CONFNAME | 高带宽用户属性名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置高带宽用户属性名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@HBUSRATTRCONF]] · 高带宽用户属性（HBUSRATTRCONF）

## 使用实例

删除ConfName为conf1的高带宽用户属性配置：

```
RMV HBUSRATTRCONF: CONFNAME="conf1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-HBUSRATTRCONF.md`
