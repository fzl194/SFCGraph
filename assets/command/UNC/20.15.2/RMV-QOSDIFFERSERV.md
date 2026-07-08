---
id: UNC@20.15.2@MMLCommand@RMV QOSDIFFERSERV
type: MMLCommand
name: RMV QOSDIFFERSERV（删除DS域）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: QOSDIFFERSERV
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- DS域配置
status: active
---

# RMV QOSDIFFERSERV（删除DS域）

## 功能

该命令用来删除用户自创建的DS域。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DSNAME | DS域名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定DS域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：区分大小写，不支持空格。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/QOSDIFFERSERV]] · DS域（QOSDIFFERSERV）

## 使用实例

删除一个DS域d1：

```
RMV QOSDIFFERSERV:DSNAME="d1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除DS域（RMV-QOSDIFFERSERV）_00866565.md`
