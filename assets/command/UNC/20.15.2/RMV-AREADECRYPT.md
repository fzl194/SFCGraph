---
id: UNC@20.15.2@MMLCommand@RMV AREADECRYPT
type: MMLCommand
name: RMV AREADECRYPT（删除基于LAC/RAC关闭加密配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: AREADECRYPT
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 用户安全管理
- 基于LAC_RAC关闭加密配置
status: active
---

# RMV AREADECRYPT（删除基于LAC/RAC关闭加密配置）

## 功能

**适用网元：SGSN**

该命令用于删除一条基于路由区/位置区的关闭加密功能的记录。

## 注意事项

该命令执行后立即生效。

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

- [[configobject/UNC/20.15.2/AREADECRYPT]] · 基于LAC/RAC关闭加密配置（AREADECRYPT）

## 使用实例

删除一条基于路由区的关闭加密功能的记录，标识类型为“RA(路由区)”，移动国家代码为“123”，移动网号为“02”，位置区域码为“0x0628”，路由区域码为“0x52”。

RMV AREADECRYPT: IDTYPE=RA, MCC="123", MNC="02", LAC="0x0628", RAC="0x52";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除基于LAC_RAC关闭加密配置(RMV-AREADECRYPT)_72225321.md`
