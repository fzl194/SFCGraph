---
id: UDG@20.15.2@MMLCommand@SET PODMEMTHD
type: MMLCommand
name: SET PODMEMTHD（设置POD内存告警阈值）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: PODMEMTHD
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统管理
- 资源管理
status: active
---

# SET PODMEMTHD（设置POD内存告警阈值）

## 功能

该命令用于设置POD内存告警阈值。

> **说明**
> - 该命令执行后立即生效。
>
> - 该命令仅在FusionStage裸机场景下生效。
> - 当某种POD类型通过[**ADD PODALMTH**](增加POD资源告警阈值（ADD PODALMTH）_87483778.md)命令或模板配置过内存类型阈值时，本命令配置的全局阈值对其不生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | WARNTHD | RECVTHD |
> | --- | --- |
> | 95 | 90 |

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| WARNTHD | 告警上报门限 | 可选必选说明：必选参数<br>参数含义：该参数用于指定告警上报门限。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~100，单位是百分比。<br>默认值：无。<br>配置原则：<br>“告警恢复门限”必须小于“告警上报门限”。 |
| RECVTHD | 告警恢复门限 | 可选必选说明：必选参数<br>参数含义：该参数用于指定告警恢复门限。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~100，单位是百分比。<br>默认值：无。<br>配置原则：<br>“告警恢复门限”必须小于“告警上报门限”。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PODMEMTHD]] · POD内存阈值（PODMEMTHD）

## 使用实例

设置容器内存告警上报门限为95，恢复门限为90。

```
SET PODMEMTHD: WARNTHD=95,RECVTHD=90;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置POD内存告警阈值（SET-PODMEMTHD）_37740493.md`
