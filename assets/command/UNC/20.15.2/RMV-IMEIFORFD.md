---
id: UNC@20.15.2@MMLCommand@RMV IMEIFORFD
type: MMLCommand
name: RMV IMEIFORFD（删除强制分离策略）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: IMEIFORFD
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 强制分离业务IMEI配置
status: active
---

# RMV IMEIFORFD（删除强制分离策略）

## 功能

**适用网元：SGSN**

此命令用于删除当前分离非活动用户的IMEISV（International Mobile station Equipment Identity and Software Version）匹配规则。分离非活动用户功能由分离非活动用户定时器（ [**SET GBDETACH**](../分离非活动用户/Gb模式分离非活动用户参数/设置Gb分离非活动用户参数(SET GBDETACH)_72345095.md) 或 [**SET IUDETACH**](../分离非活动用户/Iu模式分离非活动用户参数/设置Iu分离非活动用户参数(SET IUDETACH)_26305310.md) ）控制，定时器（NACTTMR）默认时长为360分钟。定时器超时后， UNC 将使用手机所带的IMEISV与规则的掩码按位进行"与"运算，并和匹配规则比较。如果相同， UNC 将保留该用户；否则 UNC 将强制分离该非活动用户。如果手机不携带IMEISV，则默认不匹配规则， UNC 强制分离该用户。

## 注意事项

在分离非活动用户定时器超时后， UNC 强制分离在 [**ADD IMEIFORFD**](增加强制分离策略(ADD IMEIFORFD)_26305298.md) 中没有配置的（包括未配置和先配置后通过此命令删除的）用户。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMEISV | IMEISV | 可选必选说明：必选参数<br>参数含义：该参数用于表示待删除的IMEISV字段。<br>取值范围：16位十进制数字<br>默认值：无<br>说明：“IMEISV”<br>只能由16位0～9的数字组成。 |
| MASK | 掩码 | 可选必选说明：可选参数<br>参数含义：该参数用于表示待删除IMEISV字段相应的掩码。<br>取值范围：16位二进制数字<br>默认值：无 |

## 操作的配置对象

- [强制分离策略（IMEIFORFD）](configobject/UNC/20.15.2/IMEIFORFD.md)

## 使用实例

删除一条IMEISV为1234567890123456，掩码为1111111111111111的匹配规则:

RMV IMEIFORFD: IMEISV="1234567890123456", MASK="1111111111111111";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除强制分离策略(RMV-IMEIFORFD)_72345085.md`
