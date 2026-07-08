---
id: UNC@20.15.2@MMLCommand@ADD LOCALHOSTBIND
type: MMLCommand
name: ADD LOCALHOSTBIND（增加Diameter本端主机与Diameter本端主机组的关联关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: LOCALHOSTBIND
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 1000
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- Diameter管理
- Diameter连接
- Diamter本端主机组绑定
status: active
---

# ADD LOCALHOSTBIND（增加Diameter本端主机与Diameter本端主机组的关联关系）

## 功能

**适用NF：PGW-C、SMF**

此命令用于添加指定的Diameter本端主机到本端主机分组中。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1000。
- 单个Diameter本端主机分组内最多可以有64个本端主机。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOCGRPNAME | Diameter本端信息组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter本端主机组名。要求在系统内唯一，数据来源为运营商规划。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数使用ADD LOCALHOSTGRP命令配置生成。 |
| LOCHOSTNAME | Diameter本端主机名 | 可选必选说明：必选参数<br>参数含义：本参数指定Diameter本端主机名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格。<br>默认值：无<br>配置原则：该参数使用ADD DIAMLOCINFO命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LOCALHOSTBIND]] · Diameter本端主机与Diameter本端主机组的关联关系（LOCALHOSTBIND）

## 使用实例

增加Diameter本端主机名与Diameter本端主机组的关联关系，组名为“abc”，主机名为“aaa”：

```
ADD LOCALHOSTBIND: LOCGRPNAME="abc", LOCHOSTNAME="aaa";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加Diameter本端主机与Diameter本端主机组的关联关系（ADD-LOCALHOSTBIND）_17057495.md`
