---
id: UNC@20.15.2@MMLCommand@RMV EMMPROCTRLIMSI
type: MMLCommand
name: RMV EMMPROCTRLIMSI（删除指定用户S1模式移动性管理流程控制参数）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: EMMPROCTRLIMSI
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- MM流程管理
- S1模式MM流程控制参数
status: active
---

# RMV EMMPROCTRLIMSI（删除指定用户S1模式移动性管理流程控制参数）

## 功能

**适用网元：MME**

此命令用于删除指定用户S1模式移动性管理流程控制参数。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “FOREIGN_USER(外网用户)”<br>- “HOME_USER(本网用户)”<br>- “IMSI_PREFIX(指定IMSI前缀)”<br>- “SPECIFIC_IMSI(特定IMSI)”<br>默认值：无<br>配置原则：<br>- 优先级从高到低为：<br>“SPECIFIC_IMSI（指定IMSI）”<br>，<br>“IMSI_PREFIX（指定IMSI前缀）”<br>，<br>“FOREIGN_USER(外网用户)”<br>或<br>“HOME_USER(本网用户)”<br>。<br>- 系统优先查找高优先级的配置记录，如果查找不到，再查找低优先级的配置记录。 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“HOME_USER(本网用户)”<br>或<br>“FOREIGN_USER(外网用户)”<br>后生效。<br>数据来源：全网规划<br>取值范围：0～64，128～254<br>默认值：无<br>配置原则：<br>- 当用户为MNO用户时，该参数需要配置为“0”或128～254之间的值，该取值必须和<br>[**ADD MNO**](../../../网络管理/归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md)<br>配置的<br>“MNOID”<br>参数取值相同。<br>- 当用户为MVNO用户时，该参数需要配置为1～64之间的值，该取值必须和<br>[**ADD MVNO**](../../../网络管理/归属网络运营商管理/MVNO管理/MVNO配置表/增加MVNO配置信息(ADD MVNO)_72225747.md)<br>中配置的<br>“MVNOID”<br>参数取值相同。<br>说明：- 对于外网用户，该参数是与其归属运营商签订可漫游协议，为其提供服务的MNO/MVNO运营商标识。<br>- 对于本网用户，该参数是为该用户归属的MNO/MVNO运营商标识。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定IMSI前缀。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“IMSI_PREFIX（指定IMSI前缀）”<br>后生效。<br>数据来源：全网规划<br>取值范围：5～14位十进制数字字符串。<br>默认值：无<br>说明：IMSI前缀的匹配方式采取由前向后的最长匹配，即若对于用户可以匹配到多个用户群，则使用IMSI前缀最长的用户群配置。 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>参数说明：该参数用于指定国际移动用户标识。<br>前提条件：此参数在<br>“用户范围”<br>配置为<br>“SPECIFIC_IMSI（指定IMSI）”<br>后生效。<br>取值范围：14～15位十进制数字字符串<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@EMMPROCTRLIMSI]] · 指定用户S1模式移动性管理流程控制参数（EMMPROCTRLIMSI）

## 使用实例

删除指定用户S1模式移动性管理流程控制参数配置， “用户范围” 为 “IMSI_PREFIX（指定IMSI前缀）” :

RMV EMMPROCTRLIMSI: SUBRANGE=IMSI_PREFIX, IMSIPRE="12345" ;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-EMMPROCTRLIMSI.md`
