---
id: UNC@20.15.2@MMLCommand@ADD GTPUINTFATTR
type: MMLCommand
name: ADD GTPUINTFATTR（增加GTP-U IP地址接口属性）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: GTPUINTFATTR
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
- GTP-U接口管理
- GTP-U接口类型属性
status: active
---

# ADD GTPUINTFATTR（增加GTP-U IP地址接口属性）

## 功能

**适用网元：SGSN、MME**

该命令用于指定GTPU IP地址在指定的接口或者在指定的用户范围内使用，以满足不同的组网部署要求。

本命令需和 [**ADD GTPULE**](../Gtpu本端实体管理/增加GTP-U本地实体(ADD GTPULE)_72345581.md) 命令配合使用，通过 [**ADD GTPULE**](../Gtpu本端实体管理/增加GTP-U本地实体(ADD GTPULE)_72345581.md) 命令的 “组号” 与本命令的{ “接口类型” + “用户范围” }关联起来，满足各种组网规划的应用。

应用场景举例1：GnGp SGSN组网时，将GnGp接口与Iu接口隔离，通常划分独立的VPN，这就要求Iu接口上使用的GTPU IP地址能够独立指定，与GnGp接口的GTPU IP地址分开。比如数据规划时，将Iu接口的GTPU IP地址规划为32号组，其他接口的GTPU IP地址规划为0号组，通过本命令指定Iu接口与32号组关联，其他接口缺省与0号组关联。

## 注意事项

- 该命令执行后立即生效。
- 指定IMSI前缀的记录最大支持1024。
- 指定运营商标识的记录最大支持128。
- 用户范围参数选择为所有用户时的记录数最大支持6。
- {“接口类型”+“用户范围”}唯一标识一条记录。
- 不同的{“接口类型”+“用户范围”}允许指定相同的组号。
- {“ALL_INTERFACE(所有接口)”+“ALL_USER(所有用户)”}为系统初始记录，指定为[**ADD GTPULE**](../Gtpu本端实体管理/增加GTP-U本地实体(ADD GTPULE)_72345581.md)配置的0号组，不允许指定为其他组号。
- {“ALL_USER(所有用户)”+“Iu接口”}为系统初始记录，指定为[**ADD GTPULE**](../Gtpu本端实体管理/增加GTP-U本地实体(ADD GTPULE)_72345581.md)配置的32号组，不允许指定为其他组号。
- GTPU IP地址使用的优先级从高到低为：
    - 指定接口类型+“SPECIAL_IMSIPRE(指定IMSI前缀)”。
    - “ALL_INTERFACE(所有接口)”+“ SPECIAL_IMSIPRE(指定IMSI前缀)”。
    - 指定接口类型+“SPECIAL_NOID(指定运营商)”。
    - “ ALL_INTERFACE(所有接口)”+“ SPECIAL_NOID(指定运营商)”。
    - 指定接口类型+“ALL_USER(所有用户)”。
    - “ALL_INTERFACE(所有接口)”+“ALL_USER(所有用户)”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GTPU IP地址适用的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “SPECIAL_IMSIPRE(指定IMSI前缀)”<br>- “SPECIAL_NOID(指定运营商)”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定用户的IMSI前缀。使用时按照IMSI最长匹配进行查询。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“SPECIAL_IMSIPRE(指定IMSI前缀)”<br>后生效。<br>数据来源：全网规划<br>取值范围：1~15位十进制数<br>默认值：无 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定用户归属的运营商标识。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“SPECIAL_NOID(指定运营商)”<br>后生效。<br>数据来源：全网规划<br>取值范围：0～64，128～254<br>默认值：无<br>配置原则：<br>- 若该参数需要配置为0或128～254之间的值时，请先配置[**ADD MNO命令**](../../网络管理/归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md)的“MNOID”参数，取值与本参数取值相同。<br>- 若该参数需要配置为1～64之间的值时，须先配置[**ADD MVNO**](../../网络管理/归属网络运营商管理/MVNO管理/MVNO配置表/增加MVNO配置信息(ADD MVNO)_72225747.md)命令的“MVNOID”参数，取值与本参数取值相同。 |
| INTFTP1 | 接口类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定GTPU IP地址适用的接口类型。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“ALL_USER(所有用户)”<br>后生效。<br>数据来源：本端规划<br>取值范围：<br>- “ALL_INTERFACE(所有接口)”<br>- “GN-GGSN/GP(Gn-GGSN/Gp)”<br>- “GN-SGSN/S16(Gn-SGSN/S16)”<br>- “Iu(IU)”<br>- “S11(S11)”<br>- “S4(S4)”<br>默认值：无<br>说明：“GN-SGSN(Gn-SGSN)”<br>包含GnGp SGSN之间的接口以及GnGp SGSN与MME之间的接口。 |
| INTFTP2 | 接口类型2 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定GTPU IP地址适用的接口类型。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“SPECIAL_NOID(指定运营商)”<br>/<br>“SPECIAL_IMSIPRE(指定IMSI前缀)”<br>后生效。<br>数据来源：本端规划<br>取值范围：<br>- “ALL_INTERFACE(所有接口)”<br>- “GN-GGSN/GP(Gn-GGSN/Gp)”<br>- “S11(S11)”<br>- “S4(S4)”<br>默认值：无 |
| GRPID | 组号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GTPU IP所属的组。<br>数据来源：本端规划<br>取值范围：1~31<br>默认值：无<br>配置原则：请先配置<br>[**ADD GTPULE**](../Gtpu本端实体管理/增加GTP-U本地实体(ADD GTPULE)_72345581.md)<br>命令的<br>“组号”<br>参数取值与本参数取值相同。<br>说明：该参数在命令<br>[**ADD GTPULE**](../Gtpu本端实体管理/增加GTP-U本地实体(ADD GTPULE)_72345581.md)<br>中已配置。 逻辑接口获取本端GTPU IP组号的策略：<br>- 如果是NB-IoT业务，且GTPUINTFATTR表已配置，则从GTPUINTFATTR表中获取。<br>- 如果是NB-IoT业务，且GTPUINTFATTR表没有配置，则0号组作为选择本端GTPU IP的组号。 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数用于指定GTP-U IP地址接口属性的描述信息。<br>数据来源：本端规划<br>取值范围：0~31位字符串<br>默认值：无 |

## 操作的配置对象

- [GTP-U IP地址接口属性（GTPUINTFATTR）](configobject/UNC/20.15.2/GTPUINTFATTR.md)

## 使用实例

增加一条GTP-U IP地址接口属性配置，SUBRANGE为ALL_USER、INTFTP1为S11、GRPID为9、DESC为"huawei"：

ADD GTPUINTFATTR: SUBRANGE=ALL_USER, INTFTP1=S11, GRPID=9, DESC="huawei";

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加GTP-U-IP地址接口属性(ADD-GTPUINTFATTR)_26145984.md`
