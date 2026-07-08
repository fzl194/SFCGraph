---
id: UNC@20.15.2@MMLCommand@RMV CONNECTPLMN
type: MMLCommand
name: RMV CONNECTPLMN（删除互联PLMN）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: CONNECTPLMN
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 互联PLMN管理
status: active
---

# RMV CONNECTPLMN（删除互联PLMN）

## 功能

**适用网元：SGSN、MME**

此命令用于删除互联PLMN控制表中某个PLMN。

## 注意事项

- 此命令执行后立即生效。
- 删除后该PLMN的用户将不能在本USN网元接入，已接入用户不受影响。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待删除的互联PLMN的移动国家号码。<br>取值范围：3位十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待删除的互联PLMN的移动网号码。<br>取值范围：位数为2或3的十进制数字<br>默认值：无 |
| MATCHIMSI | 匹配IMSI | 可选必选说明：可选参数<br>参数含义：该参数用于指定除了MCC和MNC外的IMSI的字段。<br>取值范围：长度不超过10的十进制数字<br>默认值：无<br>说明：如果待删除的配置中配置了该参数，删除时需要填写该参数，否则不需要。 |
| NOID | 运营商标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待删除的运营商标识。<br>取值范围：0~64，128~254<br>默认值：无<br>配置原则：<br>- 若该参数需要配置为0或128～254之间的值时，请先在[**ADD MNO**](../归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md)中配置取值相同的“MNOID”参数。<br>- 若该参数需要配置为1～64之间的值时，须先在[**ADD MVNO**](../归属网络运营商管理/MVNO管理/MVNO配置表/增加MVNO配置信息(ADD MVNO)_72225747.md)中配置取值相同的“MVNOID”参数。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CONNECTPLMN]] · 互联PLMN（CONNECTPLMN）

## 使用实例

删除互联PLMN，其中，移动国家码为123，移动网号为00：

RMV CONNECTPLMN: MCC="123", MNC="00";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-CONNECTPLMN.md`
