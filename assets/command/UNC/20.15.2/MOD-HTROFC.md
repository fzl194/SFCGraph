---
id: UNC@20.15.2@MMLCommand@MOD HTROFC
type: MMLCommand
name: MOD HTROFC（修改HTR局向）
nf: UNC
version: 20.15.2
verb: MOD
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

# MOD HTROFC（修改HTR局向）

## 功能

**适用网元：SGSN**

该命令用于修改HTR局向配置信息。在GT转发的组网配置下，只有STP对SGSN逻辑上可见，HLR目的实体对SGSN是不可见的，所以需要用户手动配置具体的HTR局向进行区分，以保证准确的流控对象，避免误控。详细功能说明可参见 [**SET HTR**](../流控功能管理/设置HTR功能(SET HTR)_72345749.md) 。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HTROFCINDEX | HTR局向索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定HTR局向的索引。<br>数据来源：本端规划<br>取值范围：0~9<br>默认值：无 |
| HTROFCNAME | HTR局向名称 | 可选必选说明：可选参数<br>参数含义：该参数用于修改该指定HTR局向名称。<br>数据来源：本端规划<br>取值范围：0~32<br>默认值：无 |
| HTROFCSWITCH | 局向流控开关 | 可选必选说明：可选参数<br>参数含义：该参数用于修改指定局向流控开关。<br>数据来源：整网规划<br>取值范围：<br>- “YES（是）”<br>- “NO（否）”<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/HTROFC]] · HTR局向（HTROFC）

## 使用实例

修改记录，将HTR局向索引为0的局向名称改为ShangHaiHLR，局向流控开关改为YES：

MOD HTROFC: HTROFCINDEX=0, HTROFCNAME="ShangHaiHLR", HTROFCSWITCH=YES;

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-HTROFC.md`
