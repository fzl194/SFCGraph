---
id: UNC@20.15.2@MMLCommand@SET OFCTHRESHOLD
type: MMLCommand
name: SET OFCTHRESHOLD（设置离线计费阈值）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: OFCTHRESHOLD
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 对新用户生效
is_dangerous: false
max_records: 100
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- 离线计费基础参数
- 离线计费模板
status: active
---

# SET OFCTHRESHOLD（设置离线计费阈值）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用来配置控制话单生成条件中的计费阈值，包括时间阈值、流量阈值、计费条件改变次数、话单最多携带的容器数、MME/SGSN/SGW/ePDG地址改变次数等。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为100。
- 如果GPRS/UMTS接入的离线计费模板和PGW离线计费模板中的时间、流量、最小流量阈值不同，当发生2/3G与4G的切换时，切换后新建话单受切换后RAT对应的模板阈值控制。
- 如果阈值配置过小（时间阈值小于10分钟、流量阈值小于10MB）会导致话单产生过多而引起性能下降。
- 如果配置的流量阈值超过0xC0000000（3G）时，请务必优先配置软参BYTE86。
- 该命令的TIMETHRESHOLD和VOLUMETHRESHOLD参数修改后对新用户或用户发生在线自动恢复时生效。
- 该命令的TIMETHRESHCCFH和VOLTHRESHCCFH参数修改后对新用户或用户发生在线转离线时生效。
- 对于漫游用户，如果DWORD17非0，流量阈值以DWORD17为准。
- 该命令的MINVOLTHRESHOLD和MAXSVCCONTAINER参数修改后仅对新入网的用户生效，对已在线的用户不生效。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | THRESHINHERIT | TIMETHRESHOLD | VOLUMETHRESHOLD | MINVOLTHRESHOLD | CONDITIONCHANGE | SERVINGNODECHNG | MAXSVCCONTAINER | TIMETHRESHCCFH | VOLTHRESHCCFH | SECRUTHRESHOLD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 初始值 | INHERIT | 60 | 10240 | 0 | 3 | 3 | 20 | 4294967295 | 9000000001 | 3 |

- 该命令设定后的数据，需要通过LST OFCTEMPLATE命令进行查看。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OFCTEMPLATENAME | 离线计费模板名 | 可选必选说明：必选参数<br>参数含义：配置离线模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD OFCTEMPLATE命令配置生成。<br>- 该功能根据此参数设置对应离线计费模板的离线计费阈值。 |
| THRESHINHERIT | 继承上一级配置 | 可选必选说明：可选参数<br>参数含义：用来表示计费阈值不取此模板配置，而是继承上一级别的离线计费模板的计费阈值配置。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- NON_INHERIT：不继承上一级配置。<br>- INHERIT：继承上一级配置。<br>默认值：无<br>配置原则：<br>- ADD OFCTEMPLATE增加一个离线计费模板时，此参数默认值为INHERIT。<br>- UNC可基于UserProfile、APN、Charge Characteristic、全局多个层次绑定离线计费模板，优先级依次降低。继承上一级别的配置指的是继承比当前层次优先级低一级的配置。具体各层次绑定离线计费模板的命令请参见SET USRPROFCHARGE、SET APNCHARGECTRL及ADD GLBOFCTEMPLATE。 |
| TIMETHRESHOLD | 时长阈值（分） | 可选必选说明：条件可选参数<br>前提条件：该参数在“THRESHINHERIT”配置为“NON_INHERIT”时为可选参数。<br>参数含义：指定产生CDR话单的时间阈值。当用户在线达到配置的时间阈值，系统为用户产生一张中间话单，然后重新计时；0表示无效值，设置为0时，时间阈值不生效。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～1440，单位是分钟。<br>默认值：无<br>配置原则：ADD OFCTEMPLATE增加一个离线计费模板时，此参数默认值为60分钟。 |
| VOLUMETHRESHOLD | 流量阈值（千字节） | 可选必选说明：条件可选参数<br>前提条件：该参数在“THRESHINHERIT”配置为“NON_INHERIT”时为可选参数。<br>参数含义：指定产生CDR话单的流量阈值。表示用户流量达到此流量阈值时系统生成中间话单；设置为0时，流量阈值由BYTE86软参控制。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0，20～9000000000，单位是千字节。<br>默认值：无<br>配置原则：<br>- ADD OFCTEMPLATE增加一个离线计费模板时，此参数默认值为10240千字节。<br>- 流量阈值超过0xC0000000（3G）时，请务必优先配置软参BYTE86。 |
| MINVOLTHRESHOLD | 最小流量阈值（千字节） | 可选必选说明：条件可选参数<br>前提条件：该参数在“THRESHINHERIT”配置为“NON_INHERIT”时为可选参数。<br>参数含义：指定产生CDR话单的最小流量阈值。默认值是0kB，表示无效值，此时最小流量阈值不生效；如果不为0时，当时间阈值到时，只有同时满足最小流量阈值时才会生成时间阈值话单。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535，单位是千字节。<br>默认值：无<br>配置原则：<br>- ADD OFCTEMPLATE增加一个离线计费模板时，此参数默认值为0。<br>- 建议设置最小流量阈值小于流量阈值。 |
| CONDITIONCHANGE | 计费条件改变阈值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“THRESHINHERIT”配置为“NON_INHERIT”时为可选参数。<br>参数含义：用于指定计费条件改变几次后会产生话单。当计费条件（如QoS、费率时段、在线转离线、ECGI、 CGI、SAI、RAI、TAI ）改变达到配置的最大变更次数时系统生成中间话单。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～10。<br>默认值：无<br>配置原则：ADD OFCTEMPLATE增加一个离线计费模板时，此参数默认值为3。 |
| SERVINGNODECHNG | Serving Node改变次数阈值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“THRESHINHERIT”配置为“NON_INHERIT”时为可选参数。<br>参数含义：当网元形态为GGSN时，用于指定本PDP涉及的SGSN的IP地址最多改变次数；当网元形态为PGW时，用于指定本PDP涉及的SGW/ePDG的IP地址最多改变次数；当网元形态为SGW时用于指定本PDP涉及的MME的IP地址最多改变次数。当用户上下文在MME/SGSN/SGW间切换，MME/SGSN/SGW IP地址发生改变达到配置的最大改变次数时系统生成中间话单；0表示无效值，设置为0时，MME/SGSN/SGW/ePDG改变阈值不生效。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～5。<br>默认值：无<br>配置原则：ADD OFCTEMPLATE增加一个离线计费模板时，此参数默认值为3。 |
| MAXSVCCONTAINER | 最大携带的业务容器数量 | 可选必选说明：条件可选参数<br>前提条件：该参数在“THRESHINHERIT”配置为“NON_INHERIT”时为可选参数。<br>参数含义：用于指定话单中最多可以携带的业务容器数量。当话单中业务容器达到最大携带的业务容器数量配置的值时，生成话单。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～40。<br>默认值：无<br>配置原则：ADD OFCTEMPLATE增加一个离线计费模板时，此参数默认值为20。 |
| TIMETHRESHCCFH | 在线计费转离线计费后的时长阈值（分钟） | 可选必选说明：条件可选参数<br>前提条件：该参数在“THRESHINHERIT”配置为“NON_INHERIT”时为可选参数。<br>参数含义：该参数用于指定在线计费用户转离线后产生CDR话单的时间阈值。当用户在线达到配置的时间阈值，系统为用户产生一张中间话单，然后重新计时；0表示无效值，设置为0时，表示在线转离线后时间阈值不生效；配置为4294967295时，表示在线转离线后继承转离线前的时间阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～1440，4294967295，单位是分钟。<br>默认值：无<br>配置原则：无 |
| VOLTHRESHCCFH | 在线计费转离线计费后的流量阈值（千字节） | 可选必选说明：条件可选参数<br>前提条件：该参数在“THRESHINHERIT”配置为“NON_INHERIT”时为可选参数。<br>参数含义：该参数用于指定在线计费用户转离线后产生CDR话单的流量阈值。用户流量达到此流量阈值时系统生成中间话单；0表示无效值，设置为0时，表示在线转离线后流量阈值不生效；配置为9000000001时，表示在线转离线后继承转离线前的流量阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0，20～9000000000，9000000001，单位是千字节。<br>默认值：无<br>配置原则：无 |
| SECRUTHRESHOLD | RAN-SecondaryRAT-Usage-Report生成话单的阈值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“THRESHINHERIT”配置为“NON_INHERIT”时为可选参数。<br>参数含义：用于指定RAN-SecondaryRAT-Usage-Report触发生成话单的阈值。取值范围为1-10。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～10。<br>默认值：无<br>配置原则：ADD OFCTEMPLATE增加一个离线计费模板时，此参数默认值为3。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@OFCTHRESHOLD]] · 离线计费阈值（OFCTHRESHOLD）

## 使用实例

设置名为“OFCThreshold”的离线计费模板的计费阈值，设置时长阈值为5分钟，流量阈值为2000千字节，最小流量阈值为100千字节：

```
SET OFCTHRESHOLD:OFCTEMPLATENAME="OFCThreshold",THRESHINHERIT=NON_INHERIT,TIMETHRESHOLD=5,VOLUMETHRESHOLD=2000,MINVOLTHRESHOLD=100;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-OFCTHRESHOLD.md`
