---
id: UNC@20.15.2@MMLCommand@ADD AREADECRYPT
type: MMLCommand
name: ADD AREADECRYPT（增加基于LAC/RAC关闭加密配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: AREADECRYPT
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
max_records: 256
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 用户安全管理
- 基于LAC_RAC关闭加密配置
status: active
---

# ADD AREADECRYPT（增加基于LAC/RAC关闭加密配置）

## 功能

**适用网元：SGSN**

该命令用于增加一条需要关闭加密功能的路由区/位置区的记录。

## 注意事项

- 该命令执行后立即生效。
- 本表最大记录数为256。
- 该命令用于对指定的路由区/位置区关闭加密功能。一般在SGSN独立覆盖的区域，可以配置指定的路由区或位置区关闭加密；对于MSC和SGSN共同覆盖的场景，可以配置位置区，来保证和MSC的关闭加密覆盖的区域相同。
- 对于PS、CS共同覆盖区域，要求加密算法必须相同，否则可能会存在由于加密算法不一致导致的流程失败的可能。
- SGSN的加密功能的实现，请参考[**ADD IUAUTHCIPH**](../Iu模式用户安全参数/增加Iu模式用户安全参数(ADD IUAUTHCIPH)_72225327.md)命令和[**ADD GBAUTHCIPH**](../Gb模式用户安全参数/增加Gb模式用户安全参数（ADD GBAUTHCIPH）_26145642.md)命令。
- 只有当[**SET MMFUNC**](../../../移动性管理/MM扩展功能管理/设置移动性管理扩展功能(SET MMFUNC)_26145512.md)命令中的参数“区域关闭加密功能”取值为“ENABLE(启用)”时，通过该命令配置的记录才生效。而且该命令配置的记录的优先级高于[**ADD IUAUTHCIPH**](../Iu模式用户安全参数/增加Iu模式用户安全参数(ADD IUAUTHCIPH)_72225327.md)命令和[**ADD GBAUTHCIPH**](../Gb模式用户安全参数/增加Gb模式用户安全参数（ADD GBAUTHCIPH）_26145642.md)命令配置的加密的优先级。即系统首先根据UE接入时携带的当前所在的LAI或RAI来判断是否需要关闭加密，若判断的结果为关闭加密，此时不管[**ADD IUAUTHCIPH**](../Iu模式用户安全参数/增加Iu模式用户安全参数(ADD IUAUTHCIPH)_72225327.md)命令或[**ADD GBAUTHCIPH**](../Gb模式用户安全参数/增加Gb模式用户安全参数（ADD GBAUTHCIPH）_26145642.md)命令是否配置为加密开启，加密协商的结果都是关闭加密。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IDTYPE | 标识类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定区域的标识类型。<br>数据来源：整网规划<br>取值范围：<br>“LA(位置区)”<br>，<br>“RA(路由区)”<br>。<br>配置原则：<br>- LA：表示该区域标识类型为位置区。<br>- RA：表示该区域标识类型为路由区。<br>默认值：无 |
| MCC | 移动国家代码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定移动国家代码。<br>数据来源：整网规划<br>取值范围：位数为3的十进制数字<br>默认值： 无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定移动网号。<br>数据来源：整网规划<br>取值范围：位数为2或3的十进制数字<br>默认值： 无 |
| LAC | 位置区域码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定位置区域码。<br>数据来源：整网规划<br>取值范围：0x0000～0xFFFF<br>默认值：无 |
| RAC | 路由区域码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定路由区域码。<br>前提条件：该参数在<br>“标识类型”<br>设置为<br>“RA(路由区)”<br>时生效。<br>数据来源：整网规划<br>取值范围：0x00～0xFF<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@AREADECRYPT]] · 基于LAC/RAC关闭加密配置（AREADECRYPT）

## 使用实例

增加一条基于路由区的关闭加密功能的记录，标识类型为“RA(路由区)”，移动国家代码为“123”，移动网号为“02”，位置区域码为“0x0628”，路由区域码为“0x52”。

ADD AREADECRYPT: IDTYPE=RA, MCC="123", MNC="02", LAC="0x0628", RAC="0x52";

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-AREADECRYPT.md`
