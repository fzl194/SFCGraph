---
id: UNC@20.15.2@MMLCommand@MOD LOCALHSS
type: MMLCommand
name: MOD LOCALHSS（修改本地HSS）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: LOCALHSS
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- LOCALHSS管理
status: active
---

# MOD LOCALHSS（修改本地HSS）

## 功能

**适用网元：MME**

该命令用于修改本地HSS信息。目前仅支持修改指定HSS的名称。

## 注意事项

- 此命令执行后立即生效。
- 此命令不区分主机名中的大小写字母，系统统一按照大写字母来处理。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HSSHTNAM | 本地HSS主机名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本地HSS主机名。<br>是否必选：必选<br>数据来源：整网规划<br>取值范围：1~127位字符串<br>默认值：无<br>配置原则：<br>- 不能为非法字符，只允许输入字母，数字，“.”和“-”。例如:hss.epc.mnc123.mcc123.3gppnetwork.org<br>- 不允许配置字符串“NULL”。<br>- 若UNC和HSS直接连接时，该参数与[**ADD DMPE**](../../信令传输管理/Diameter管理/Diameter对端实体/增加Diameter对端实体(ADD DMPE)_72225963.md)中的“对端主机名”保持一致，若UNC通过DRA转接到HSS时，需获取对端HSS的主机名进行配置。 |
| HSSNAM | 本地HSS名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本地HSS的名称，该名称仅起助记作用。<br>数据来源：整网规划<br>取值范围：0~32位字符串<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LOCALHSS]] · 本地HSS（LOCALHSS）

## 使用实例

将主机名为hss1502.huawei03.com的HSS名称修改为loaclhss2

MOD LOCALHSS: HSSHTNAM="hss1502.huawei03.com", HSSNAM="loaclhss2";

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-LOCALHSS.md`
