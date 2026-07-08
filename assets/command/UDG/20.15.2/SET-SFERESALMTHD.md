---
id: UDG@20.15.2@MMLCommand@SET SFERESALMTHD
type: MMLCommand
name: SET SFERESALMTHD（设置VNRS内部资源不足告警的阈值参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: SFERESALMTHD
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- VNRS内部资源不足告警的阈值参数
status: active
---

# SET SFERESALMTHD（设置VNRS内部资源不足告警的阈值参数）

## 功能

该命令用来设置ALM-231612426 VNRS内部资源不足告警的阈值参数。

## 注意事项

- 该命令执行后立即生效。
- 该命令存在系统初始记录，参数的初始设置值如下表：
  | RESTYPE | TRIGGERTHD | RESUMETHD |
  | --- | --- | --- |
  | IPv4RecmpNode | 80 | 70 |
  | IPv4ReasmNode | 80 | 70 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESTYPE | 资源类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ALM-231612426 VNRS内部资源不足告警的资源类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPv4RecmpNode：IPv4分片重排节点。<br>- IPv4ReasmNode：IPv4分片重组节点。<br>默认值：无<br>配置原则：无 |
| TRIGGERTHD | 触发阈值（%） | 可选必选说明：必选参数<br>参数含义：该参数用于指定ALM-231612426 VNRS内部资源不足告警的触发阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为2~100。<br>默认值：无<br>配置原则：<br>**触发阈值（%）**<br>必须大于<br>**恢复阈值（%）**<br>。 |
| RESUMETHD | 恢复阈值（%） | 可选必选说明：必选参数<br>参数含义：该参数用于指定ALM-231612426 VNRS内部资源不足告警的恢复阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～99。<br>默认值：无<br>配置原则：<br>**恢复阈值（%）**<br>必须小于<br>**触发阈值（%）**<br>。 |

## 操作的配置对象

- [VNRS内部资源不足告警的阈值参数（SFERESALMTHD）](configobject/UDG/20.15.2/SFERESALMTHD.md)

## 使用实例

```
设置IPv4分片重排节点资源不足导致的ALM-231612426 VNRS内部资源不足告警的阈值参数为触发阈值90%，恢复阈值80%：
SET SFERESALMTHD: RESTYPE=IPv4RecmpNode, TRIGGERTHD=90, RESUMETHD=80;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置VNRS内部资源不足告警的阈值参数（SET-SFERESALMTHD）_15771589.md`
