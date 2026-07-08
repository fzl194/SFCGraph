---
id: UDG@20.15.2@MMLCommand@SET NPFECSWITCH
type: MMLCommand
name: SET NPFECSWITCH（设置NP FEC配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: NPFECSWITCH
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 系统管理
- NP端口管理
- NP端口FEC功能启停
- NP板的FEC功能开关
status: active
---

# SET NPFECSWITCH（设置NP FEC配置）

## 功能

该命令用来设置NP卡端口FEC功能状态。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于NP卡加速模式场景。
- 当前NP卡FEC状态支持NP_FEC_NONE和FEC_MOD_RS两种状态，当NP卡外联口和交换机外联口的FEC状态不一致或NP卡级联口和对框级联口FEC状态不一致时，端口会物理DOWN。
- 当NP外联口插入40GE/10GE光模块时，仅支持设置为NP_FEC_NONE状态。当插入100GE/25GE光模块时，支持设置为NP_FEC_NONE或FEC_MOD_RS状态。当插入400GE/200GE光模块时，支持设置为NP_FEC_NONE或FEC_MOD_RS544_2CWORD状态。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NPINTERFACENAME | 接口名称 | 可选必选说明：必选参数。<br>参数含义：该参数用于指定NP卡上的端口。<br>数据来源：本端规划。<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，区分大小写。<br>配置原则：通过<br>**[LST INTERFACE](../../../../IP服务/接口管理/接口配置/查询接口（LST INTERFACE）_49801850.md)**<br>命令查询。<br>默认值：无。 |
| NPSWITCH | FEC状态 | 可选必选说明：必选参数。<br>参数含义：该参数用于指定FEC功能状态。<br>数据来源：本端规划。<br>取值范围：枚举类型。<br>- NP_FEC_NONE：FEC不使能。<br>- FEC_MOD_RS：RS-FEC(528,514)模式。<br>- FEC_MOD_RS544_2CWORD：RS-FEC(544,514)模式。<br>默认值：无。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/NPFECSWITCH]] · NP FEC状态（NPFECSWITCH）

## 使用实例

- 设置100GE66/0/8接口的FEC功能状态为FEC_MOD_RS：
  ```
  SET NPFECSWITCH:NPINTERFACENAME="100GE66/0/8",NPSWITCH=FEC_MOD_RS;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-NPFECSWITCH.md`
