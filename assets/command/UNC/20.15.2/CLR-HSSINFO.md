---
id: UNC@20.15.2@MMLCommand@CLR HSSINFO
type: MMLCommand
name: CLR HSSINFO（清除HSS信息）
nf: UNC
version: 20.15.2
verb: CLR
object_keyword: HSSINFO
command_category: 动作类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Diameter应用协议
- HSS管理
status: active
---

# CLR HSSINFO（清除HSS信息）

## 功能

**适用网元：SGSN、MME**

该命令用于模拟HSS RESET流程，将注册在该HSS的用户“SGSN Location Information Confirmed in HLR/HSS”或“MME Location Information Confirmed in HLR/HSS”标识和自学习主机名等与HSS相关的信息置为无效。

## 注意事项

HSS割接或者HSS修改本端主机名前使用此命令，以保证用户信息在SGSN/MME和HSS上一致。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HSSHTNAME | HSS主机名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定HSS主机名。<br>取值范围：1～127位字符串<br>默认值：无<br>配置原则：不能为非法字符，只允许输入字母，数字，“.”和“-”，大小写不敏感。例如：hss.epc.mnc123.mcc123.3gppnetwork.org |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@HSSINFO]] · HSS信息（HSSINFO）

## 使用实例

清除主机名为hss.epc.mnc123.mcc123.3gppnetwork.org的HSS在SGSN/MME的相关信息：

CLR HSSINFO: HSSHTNAME="hss.epc.mnc123.mcc123.3gppnetwork.org";

## 证据

- 原始手册：`evidence/UNC/20.15.2/CLR-HSSINFO.md`
