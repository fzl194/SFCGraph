---
id: UNC@20.15.2@MMLCommand@BLK RU
type: MMLCommand
name: BLK RU（闭塞CSDB RU）
nf: UNC
version: 20.15.2
verb: BLK
object_keyword: RU
command_category: 调测类
effect_mode: ''
is_dangerous: true
category_path:
- 平台服务管理
- CSDB功能管理
- CSDB管理
- 闭塞管理
status: active
---

# BLK RU（闭塞CSDB RU）

## 功能

![](闭塞CSDB RU（BLK RU）_36508136.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，操作不当，将导致CSDB RU整体负载不均和CSDB整体系统规格下降，请谨慎使用并联系华为技术支持协助操作。

该命令用于闭塞CSDB RU，使RU上的数据迁移到其他RU上。在分批升级之前，执行本命令，将数据迁移到其他RU上。

## 注意事项

- 该命令执行后，需要通过**[LST BLKHISTORY](查询CSDB RU闭塞信息（LST BLKHISTORY）_36508138.md)**命令查询闭塞结果。
- 同一子集群中，必须所有的RU都处于解闭状态后才可以执行**[BLK RU](闭塞CSDB RU（BLK RU）_36508136.md)**操作。
- 在执行**[BLK RU](闭塞CSDB RU（BLK RU）_36508136.md)**后，RU处于**处理中**和**处理成功**状态时，禁止进行扩缩容和动态上下线操作。
- 该命令在容器场景下不支持。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCALEGROUP | 物理资源组名称 | 可选必选说明：必选参数。<br>参数含义：该参数用于指定唯一一个物理资源组。<br>数据来源：该物理资源组名称可以通过<br>**[LST SERVICERUSTATE](../../../单体服务编排功能管理/系统管理/资源管理/RU信息/查询RU的信息(LST SERVICERUSTATE)_29626965.md)**<br>命令查询获取，对应<br>**ScaleGroup的名字**<br>。<br>取值范围：字符串类型，长度为1～63。<br>默认值：无。 |
| RULIST | RU列表 | 可选必选说明：必选参数。<br>参数含义：闭塞RU列表，列表由一个或多个RU的RU ID组成，中间采用英文逗号进行分隔。<br>数据来源：该RU列表中RU ID可以通过<br>**[LST SERVICERUSTATE](../../../单体服务编排功能管理/系统管理/资源管理/RU信息/查询RU的信息(LST SERVICERUSTATE)_29626965.md)**<br>命令查询获取，对应<br>**RU的ID**<br>。<br>取值范围：字符串类型，长度为1～255。<br>默认值：无。<br>配置原则：<br>- 每次只能闭塞一个子集群的一个或者多个RU。<br>- 每次闭塞RU个数必须小于该子集群所有正常RU个数的1/3。 |

## 操作的配置对象

- [解闭CSDB RU（RU）](configobject/UNC/20.15.2/RU.md)

## 使用实例

闭塞“物理资源组名称”为“SG1_CSDB_ForCommon”、“RULIST”为“64,65”的RU：

BLK RU: SCALEGROUP="SG1_CSDB_ForCommon", RULIST="64,65";

## 证据

- 原始手册：`evidence/UNC/20.15.2/闭塞CSDB-RU（BLK-RU）_36508136.md`
