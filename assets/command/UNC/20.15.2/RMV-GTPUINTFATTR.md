---
id: UNC@20.15.2@MMLCommand@RMV GTPUINTFATTR
type: MMLCommand
name: RMV GTPUINTFATTR（删除GTP-U IP地址接口属性）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV GTPUINTFATTR（删除GTP-U IP地址接口属性）

## 功能

**适用网元：SGSN、MME**

该命令用于删除指定GTPU IP地址在特定范围内的使用配置。

删除特定接口或者特定用户范围的GTPU IP地址后，该范围内用户的业务流程将使用 [**ADD GTPULE**](../Gtpu本端实体管理/增加GTP-U本地实体(ADD GTPULE)_72345581.md) 配置的0号组中的GTPU IP地址。

## 注意事项

- 该命令执行后立即生效。
- {“ALL_INTERFACE(所有接口)”+“ALL_USER(所有用户)”}为系统初始记录，不支持删除。
- {“ALL_USER(所有用户)”+“Iu接口”}为系统初始记录，不支持删除。
- 删除特定接口或者特定用户范围的GTPU IP地址后，如果在线用户中已经使用了对应GTPU IP地址，并且该GTPU IP地址也不在[**ADD GTPULE**](../Gtpu本端实体管理/增加GTP-U本地实体(ADD GTPULE)_72345581.md)配置的0号组中存在，在线用户需要重新激活才能进行业务。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DELTYPE | 删除条件 | 可选必选说明：可选参数<br>参数含义：本参数用于指定删除记录的Key类型。<br>数据来源：本端规划<br>取值范围：<br>- “BYINDEX(根据记录索引)”<br>- “BYINTFSUB(根据接口类型和用户范围)”<br>默认值：BYINDEX(根据记录索引) |
| INDEX | 记录索引 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定本配置记录的索引。<br>前提条件：该参数在<br>“删除条件”<br>参数配置为"BYINDEX(根据记录索引)"后生效。<br>数据来源：本端规划<br>取值范围：2~4294967295<br>默认值：无<br>配置原则：无。<br>说明：使用<br>[**LST GTPUINTFATTR**](查询GTP-U IP地址接口属性(LST GTPUINTFATTR)_72345585.md)<br>查询记录的索引。 |
| SUBRANGE | 用户范围 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定GTPU IP地址适用的用户范围。<br>前提条件：该参数在<br>“删除条件”<br>参数配置为<br>“BYINTFSUB(根据接口类型和用户范围)”<br>后生效。<br>数据来源：本端规划<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “SPECIAL_IMSIPRE(指定IMSI前缀)”<br>- “SPECIAL_NOID(指定运营商)”<br>默认值：无 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定用户归属的运营商标识。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“SPECIAL_NOID(指定运营商)”<br>后生效。<br>数据来源：全网规划<br>取值范围：0～64，128～254<br>默认值：无<br>配置原则：<br>- 若该参数需要配置为0或128～254之间的值时，请先在[**ADD MNO**](../../网络管理/归属网络运营商管理/MNO管理/MNO配置表/增加MNO配置信息(ADD MNO)_72345671.md)中配置取值相同的“MNOID”参数。<br>- 若该参数需要配置为1～64之间的值时，须先在[**ADD MVNO**](../../网络管理/归属网络运营商管理/MVNO管理/MVNO配置表/增加MVNO配置信息(ADD MVNO)_72225747.md)中配置取值相同的“MVNOID”参数。 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定用户的IMSI前缀。使用时按照IMSI最长匹配进行查询。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“SPECIAL_IMSIPRE(指定IMSI前缀)”<br>后生效。<br>数据来源：全网规划<br>取值范围：1~15位十进制数<br>默认值：无 |
| INTFTP1 | 接口类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定GTPU IP地址适用的接口类型。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“ALL_USER(所有用户)”<br>后生效。<br>数据来源：本端规划<br>取值范围：<br>- “ALL_INTERFACE(所有接口)”<br>- “GN-GGSN/GP(Gn-GGSN/Gp)”<br>- “GN-SGSN/S16(Gn-SGSN/S16)”<br>- “Iu(IU)”<br>- “S11(S11)”<br>- “S4(S4)”<br>默认值：无 |
| INTFTP2 | 接口类型2 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定GTPU IP地址适用的接口类型。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“SPECIAL_NOID(指定运营商)”<br>/<br>“SPECIAL_IMSIPRE(指定IMSI前缀)”<br>后生效。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_INTERFACE(所有接口)”<br>- “GN-GGSN/GP(Gn-GGSN/Gp)”<br>- “S11(S11)”<br>- “S4(S4)”<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GTPUINTFATTR]] · GTP-U IP地址接口属性（GTPUINTFATTR）

## 使用实例

将删除类型为BYINDEX、INDEX为2的记录删除：

RMV GTPUINTFATTR: DELTYPE=BYINDEX, INDEX=2;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除GTP-U-IP地址接口属性(RMV-GTPUINTFATTR)_72225663.md`
