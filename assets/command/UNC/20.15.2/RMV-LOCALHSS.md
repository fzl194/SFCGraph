---
id: UNC@20.15.2@MMLCommand@RMV LOCALHSS
type: MMLCommand
name: RMV LOCALHSS（删除本地HSS）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV LOCALHSS（删除本地HSS）

## 功能

**适用网元：MME**

该命令用于删除一条本地HSS配置记录，HSS用主机名唯一标识。

## 注意事项

- 此命令执行后立即生效。
- 若[**SET IPAREAGPCTRL**](../../移动性管理/基于位置分配IP地址管理/基于位置分配IP地址策略管理/设置基于位置分配IP地址策略(SET IPAREAGPCTRL)_72345195.md)的参数“LOCALUSRSW(是否区分本网本地和本网异地用户)”设置为“YES(区分)”，删除HSS配置记录，可能会导致本网本地用户被识别为本网异地用户。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HSSHTNAM | 本地HSS主机名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本地HSS主机名。<br>数据来源：整网规划<br>取值范围：1~127位字符串<br>默认值：无<br>配置原则：<br>- 不能为非法字符，只允许输入字母，数字，“.”和“-”。例如:hss.epc.mnc123.mcc123.3gppnetwork.org<br>- 不允许配置字符串“NULL”。<br>- 若UNC和HSS直接连接时，该参数与[**ADD DMPE**](../../信令传输管理/Diameter管理/Diameter对端实体/增加Diameter对端实体(ADD DMPE)_72225963.md)中的“对端主机名”保持一致，若UNC通过DRA转接到HSS时，需获取对端HSS的主机名进行配置。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LOCALHSS]] · 本地HSS（LOCALHSS）

## 使用实例

运营商A网络调整，删除主机名为hss1502.huawei03.com的本地HSS记录。

RMV LOCALHSS: HSSHTNAM="hss1502.huawei03.com";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-LOCALHSS.md`
