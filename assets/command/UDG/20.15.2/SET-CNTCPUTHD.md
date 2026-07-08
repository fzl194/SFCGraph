---
id: UDG@20.15.2@MMLCommand@SET CNTCPUTHD
type: MMLCommand
name: SET CNTCPUTHD（设置容器CPU告警阈值）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: CNTCPUTHD
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统管理
- 资源管理
status: active
---

# SET CNTCPUTHD（设置容器CPU告警阈值）

## 功能

该命令用于设置容器CPU告警阈值。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | WARNTHD | RECVTHD |
> | --- | --- |
> | 80 | 70 |

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| WARNTHD | 告警上报门限 | 可选必选说明：必选参数<br>参数含义：该参数用于指定告警上报门限。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~100，单位是百分比。<br>默认值：无。<br>配置原则：<br>“告警恢复门限”必须小于“告警上报门限”。 |
| RECVTHD | 告警恢复门限 | 可选必选说明：必选参数<br>参数含义：该参数用于指定告警恢复门限。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~100，单位是百分比。<br>默认值：无。<br>配置原则：<br>“告警恢复门限”必须小于“告警上报门限”。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@CNTCPUTHD]] · 容器CPU阈值（CNTCPUTHD）

## 使用实例

设置容器CPU告警上报门限为90，恢复门限为80。

```
SET CNTCPUTHD: WARNTHD=90,RECVTHD=80;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-CNTCPUTHD.md`
