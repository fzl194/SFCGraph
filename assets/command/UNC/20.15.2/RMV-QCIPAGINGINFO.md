---
id: UNC@20.15.2@MMLCommand@RMV QCIPAGINGINFO
type: MMLCommand
name: RMV QCIPAGINGINFO（删除QCI寻呼策略参数配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: QCIPAGINGINFO
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- QCI寻呼策略参数配置
status: active
---

# RMV QCIPAGINGINFO（删除QCI寻呼策略参数配置）

## 功能

**适用网元：MME**

该命令用于删除特定QCI（QoS Class Identifier）对应的寻呼策略配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令执行后，特定QCI消息出发的Paging策略使用系统默认的参数配置(通过[**SET EMM**](../MM协议参数管理/S1模式MM协议参数/设置S1模式MM协议参数(SET EMM)_72225207.md)设定)。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QCI | 标准QCI值 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要删除的寻呼策略对应的标准QCI值。<br>取值范围：1～254<br>默认值：无 |

## 操作的配置对象

- [QCI寻呼策略参数配置（QCIPAGINGINFO）](configobject/UNC/20.15.2/QCIPAGINGINFO.md)

## 使用实例

删除标准QCI为1的寻呼策略参数配置：

RMV QCIPAGINGINFO: QCI=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除QCI寻呼策略参数配置(RMV-QCIPAGINGINFO)_26305342.md`
