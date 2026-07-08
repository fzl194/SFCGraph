---
id: UNC@20.15.2@MMLCommand@RMV GTPPLOCINFO
type: MMLCommand
name: RMV GTPPLOCINFO（删除GTPP本端信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: GTPPLOCINFO
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- GTPP信令
- GTPP本地信息
status: active
---

# RMV GTPPLOCINFO（删除GTPP本端信息）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用来删除GTPP本端信息。

## 注意事项

- 该命令执行后立即生效。
- 当前版本不支持此命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOSTNAME | 本端主机名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本端主机名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GTPPLOCINFO]] · GTPP本端信息（GTPPLOCINFO）

## 使用实例

删除GTPP本端信息，本端主机名为“test”：

```
RMV GTPPLOCINFO: HOSTNAME="test";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-GTPPLOCINFO.md`
