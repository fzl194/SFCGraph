---
id: UNC@20.15.2@MMLCommand@SET NRFDRRTSTASW
type: MMLCommand
name: SET NRFDRRTSTASW（设置NRF双活备份状态忽略开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NRFDRRTSTASW
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF双活容灾参数
status: active
---

# SET NRFDRRTSTASW（设置NRF双活备份状态忽略开关）

## 功能

**适用NF：NRF**

该命令用于NRF双活容灾场景下，两个相互备份的NRF之间数据备份通道关闭时，当前NRF是否忽略数据备份状态，允许直接处理业务。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| FCSWITCH |
| --- |
| FUNC_OFF |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FCSWITCH | 双活备份状态忽略开关 | 可选必选说明：必选参数<br>参数含义：该参数表示NRF双活容灾场景下，NRF是否忽略数据备份状态，允许接入业务。开关打开时，表示忽略数据备份状态，NRF允许直接处理业务。开关关闭时，表示NRF需要等待数据备份状态进入实时备份状态时，才允许处理业务。<br>数据来源：本端规划<br>取值范围：<br>- FUNC_ON（打开）<br>- FUNC_OFF（关闭）<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFDRRTSTASW]] · NRF双活备份状态忽略开关（NRFDRRTSTASW）

## 使用实例

将NRF按照双活方式组网部署，在数据备份通道关闭时，设置当前NRF忽略数据备份状态，允许直接处理业务。

```
SET NRFDRRTSTASW: FCSWITCH=FUNC_ON;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置NRF双活备份状态忽略开关（SET-NRFDRRTSTASW）_52071375.md`
