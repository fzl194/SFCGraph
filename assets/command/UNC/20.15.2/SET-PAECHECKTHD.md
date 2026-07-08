---
id: UNC@20.15.2@MMLCommand@SET PAECHECKTHD
type: MMLCommand
name: SET PAECHECKTHD（设置PAE寻呼反压流控检测阈值）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: PAECHECKTHD
command_category: 配置类
applicable_nf:
- MME
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 设备管理
- 流控管理
- 业务流控管理
- PAE寻呼反压流控管理
status: active
---

# SET PAECHECKTHD（设置PAE寻呼反压流控检测阈值）

## 功能

**适用NF：MME、AMF**

该命令用于设置LINK节点相关资源过载检测阈值参数，包括link-pod内pBuf资源使用率过载、恢复门限，PAE与虚拟交换机间消息发送队列使用率过载、恢复门限等信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESTYPE | 资源类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示检测的资源类型。<br>数据来源：本端规划<br>取值范围：<br>- PBUF（link-pod内使用的pBuf资源）<br>- SHAREQUEUE（PAE与软SDN间消息发送队列）<br>默认值：无<br>配置原则： 无 |
| TRIGTHD | 触发过载阈值（%） | 可选必选说明：可选参数<br>参数含义：该参数用于表示触发资源过载的阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为2～99。<br>默认值：80<br>配置原则： 无 |
| RESUMTHD | 触发过载恢复阈值（%） | 可选必选说明：可选参数<br>参数含义：该参数用于表示触发资源过载恢复的阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为2～99。<br>默认值：50<br>配置原则： 无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PAECHECKTHD]] · PAE寻呼反压流控检测阈值（PAECHECKTHD）

## 使用实例

设置PAE寻呼反压流控检测阈值的资源类型为link-pod内使用的pBuf资源，触发过载阈值（%）为60，触发过载恢复阈值（%）为30：

```
SET PAECHECKTHD: RESTYPE=PBUF, TRIGTHD=60, RESUMTHD=30;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-PAECHECKTHD.md`
