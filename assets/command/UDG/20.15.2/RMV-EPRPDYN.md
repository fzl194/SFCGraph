---
id: UDG@20.15.2@MMLCommand@RMV EPRPDYN
type: MMLCommand
name: RMV EPRPDYN（删除EPRPDYN对象）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: EPRPDYN
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务运维
- 业务性能统计管理
- EPRPDYN性能统计对象
status: active
---

# RMV EPRPDYN（删除EPRPDYN对象）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于删除EPRPDYN对象。

## 注意事项

- 该命令执行后立即生效。
- 删除EPRPDYN对象时，会同时删除EPRPDYN对象配置的所有本端IP地址和对端IP地址段。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| EPRPDYNNAME | 对象名称 | 可选必选说明：必选参数<br>参数含义：对象名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格以及特殊字符：“_”、“#”、“$”等。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@EPRPDYN]] · EPRPDYN对象（EPRPDYN）

## 使用实例

删除对象名为pgw1的EPRPDYN对象：

```
RMV EPRPDYN:EPRPDYNNAME="pgw1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-EPRPDYN.md`
