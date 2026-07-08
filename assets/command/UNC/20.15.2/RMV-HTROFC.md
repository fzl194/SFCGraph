---
id: UNC@20.15.2@MMLCommand@RMV HTROFC
type: MMLCommand
name: RMV HTROFC（删除HTR局向）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: HTROFC
command_category: 配置类
applicable_nf:
- SGSN
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
- HTR流控局向管理
- Gr HTR流控局向管理
- 配置局向
status: active
---

# RMV HTROFC（删除HTR局向）

## 功能

**适用网元：SGSN**

此命令用于删除HTR局向配置信息。在GT转发的组网配置下，只有STP对SGSN逻辑上可见，HLR目的实体对SGSN是不可见的，所以需要用户手动配置具体的HTR局向进行区分，以保证准确的流控对象，避免误控。详细功能说明可参见 [**SET HTR**](../流控功能管理/设置HTR功能(SET HTR)_72345749.md) 。

## 注意事项

- 此命令执行后立即生效。
- 执行此命令前必须保证本HTR局向中没有配置的IMSI号段存在。否则不允许删除本HTR局向，必须先删除IMSI号段的配置。可执行[**LST HTRIMSICFG**](../配置局向关联号段/查询HTR号段(LST HTRIMSICFG)_72225831.md)命令进行查看。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HTROFCINDEX | HTR局向索引 | 可选必选说明：必选参数<br>参数含义：待删除的HTR局向索引。<br>取值范围：0~9<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@HTROFC]] · HTR局向（HTROFC）

## 使用实例

删除记录，删除 “HTR局向索引” 为 “0” ：

RMV HTROFC: HTROFCINDEX=0;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-HTROFC.md`
