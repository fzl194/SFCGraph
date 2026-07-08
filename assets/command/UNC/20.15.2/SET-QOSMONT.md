---
id: UNC@20.15.2@MMLCommand@SET QOSMONT
type: MMLCommand
name: SET QOSMONT（设置QoS监测配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: QOSMONT
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- QoS监测管理
- QoS监测控制
status: active
---

# SET QOSMONT（设置QoS监测配置）

## 功能

**适用NF：SMF**

该命令用于设置QoS监测配置。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| MONTSWITCH |
| --- |
| DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MONTSWITCH | QoS监测开关 | 可选必选说明：必选参数<br>参数含义：该参数用于配置QoS监测开关。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/QOSMONT]] · QoS监测配置（QOSMONT）

## 使用实例

QoS监测开关配置为ENABLE:

```
SET QOSMONT: MONTSWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置QoS监测配置（SET-QOSMONT）_81398995.md`
