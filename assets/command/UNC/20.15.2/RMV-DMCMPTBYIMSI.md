---
id: UNC@20.15.2@MMLCommand@RMV DMCMPTBYIMSI
type: MMLCommand
name: RMV DMCMPTBYIMSI（删除IMSI对应的Diameter兼容性）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: DMCMPTBYIMSI
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
- 信令传输管理
- Diameter管理
- Diameter协议接口兼容性IMSI号段配置
status: active
---

# RMV DMCMPTBYIMSI（删除IMSI对应的Diameter兼容性）

## 功能

**适用网元：SGSN、MME**

该命令用于删除Diameter兼容性参数策略。

## 注意事项

- 该命令执行后对已经附着的用户不立即生效，对新接入的用户立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter兼容性参数策略的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “FOREIGN_USER(外网用户)”<br>- “HOME_USER(本网用户)”<br>- “IMSI_PREFIX(指定IMSI前缀)”<br>默认值：无<br>配置原则：<br>- Diameter参数策略优先级从高到低为：“IMSI_PREFIX(指定IMSI前缀)”，“FOREIGN_USER(外网用户)”或“HOME_USER(本网用户)”。<br>- 系统优先查找高优先级的配置记录，如果查找不到，再查找低优先级的配置记录。 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“FOREIGN_USER(外网用户)”<br>或<br>“HOME_USER(本网用户)”<br>后生效。<br>数据来源：全网规划<br>取值范围：0～64，128～254<br>默认值：无<br>说明：- 对于外网用户，该参数是与其归属运营商签订可漫游协议，为其提供服务的MNO/MVNO运营商标识。<br>- 对于本网用户，该参数是为该用户归属的MNO/MVNO运营商标识。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件: 该参数在用户范围设定为<br>“IMSI_PREFIX(指定IMSI前缀)”<br>时，才需要配置。<br>数据来源：全网规划<br>取值范围：0～15位十进制数字字符串。<br>默认值：无<br>说明：IMSI前缀的匹配方式采取由前向后的最长匹配，即若对于用户可以匹配到多个用户群，则使用IMSI前缀最长的用户群配置。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DMCMPTBYIMSI]] · IMSI对应的Diameter兼容性（DMCMPTBYIMSI）

## 使用实例

场景参见 [**ADD DMCMPTBYIMSI**](增加IMSI对应的Diameter兼容性(ADD DMCMPTBYIMSI)_72225977.md) 的命令使用实例。

删除以12303为IMSI前缀的用户的配置策略：

RMV DMCMPTBYIMSI: SUBRANGE=IMSI_PREFIX, IMSIPRE="12303";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-DMCMPTBYIMSI.md`
