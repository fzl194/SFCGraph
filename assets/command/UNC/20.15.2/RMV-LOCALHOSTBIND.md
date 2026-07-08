---
id: UNC@20.15.2@MMLCommand@RMV LOCALHOSTBIND
type: MMLCommand
name: RMV LOCALHOSTBIND（删除Diameter本端主机与Diameter本端主机组的关联关系）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: LOCALHOSTBIND
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- Diameter管理
- Diameter连接
- Diamter本端主机组绑定
status: active
---

# RMV LOCALHOSTBIND（删除Diameter本端主机与Diameter本端主机组的关联关系）

## 功能

**适用NF：PGW-C、SMF**

此命令用于从Diameter本地主机分组中删除指定的Diameter本地主机。

## 注意事项

- 该命令执行后立即生效。
- 当不指定主机时，是删除整个Diameter本地主机组。当指定主机时，是从指定组中移除该主机。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOCGRPNAME | Diameter本端信息组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter本端主机组名。要求在系统内唯一，数据来源为运营商规划。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| LOCHOSTNAME | Diameter本端主机名 | 可选必选说明：可选参数<br>参数含义：本参数指定Diameter本端主机名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LOCALHOSTBIND]] · Diameter本端主机与Diameter本端主机组的关联关系（LOCALHOSTBIND）

## 使用实例

删除主机与Diameter本端主机分组的关联关系，删除Diameter本端主机分组为“abc”的记录：

```
RMV LOCALHOSTBIND: LOCGRPNAME="abc";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-LOCALHOSTBIND.md`
