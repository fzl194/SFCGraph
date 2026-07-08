---
id: UDG@20.15.2@MMLCommand@SET TRUNKATTR
type: MMLCommand
name: SET TRUNKATTR（设置宽带集群属性配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: TRUNKATTR
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- DN管理
- 宽带集群管理
- 宽带集群属性配置
status: active
---

# SET TRUNKATTR（设置宽带集群属性配置）

## 功能

**适用NF：SGW-U、PGW-U**

该命令用于控制是否对长时间处于空闲状态的集群用户进行去活处理，以及配置GTP-U消息头中是否携带Sequence Number字段。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | IDLEDEASW | GTPUSEQUENCESW |
| --- | --- | --- |
| 初始值 | DISABLE | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IDLEDEASW | 空闲去活开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制是否使能空闲去活功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| GTPUSEQUENCESW | Sequence Number开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置GTP-U消息头中是否携带Sequence Number字段。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@TRUNKATTR]] · 宽带集群属性配置（TRUNKATTR）

## 使用实例

将长时间处于空闲状态的集群用户进行去活处理的开关设置为开启：

```
SET TRUNKATTR: IDLEDEASW=ENABLE, GTPUSEQUENCESW=DISABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-TRUNKATTR.md`
