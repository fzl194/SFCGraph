---
id: UNC@20.15.2@MMLCommand@ADD SBILINKSETPROP
type: MMLCommand
name: ADD SBILINKSETPROP（增加SBI链路集策略）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SBILINKSETPROP
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- SBI管理
- 服务化接口链路集策略管理
status: active
---

# ADD SBILINKSETPROP（增加SBI链路集策略）

## 功能

该命令用于增加服务化接口链路集策略。

## 注意事项

- 该命令执行后立即生效。

- 如果使用[**ADD SBILINKSETPROP**](增加SBI链路集策略（ADD SBILINKSETPROP）_29053325.md)增加SBI链路集策略，则需要使用[**ADD SBILINKCFG**](../服务化接口链路属性管理/增加SBI接口链路属性配置（ADD SBILINKCFG）_83813628.md)增加SBI接口链路配置，否则SBI链路集策略不生效。
- 如果使用[**ADD SBILINKCFG**](../服务化接口链路属性管理/增加SBI接口链路属性配置（ADD SBILINKCFG）_83813628.md)配置的对端NF类型是SCP或SEPP，无法按照整系统控制链路数。
- SYSCTRLFLG设置为是，指定链路集中的链路建立是按整系统控制；设置为否，指定链路集中的链路建立是按单进程控制。

- 最多可输入255条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SBI链路集策略的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~255。<br>默认值：无<br>配置原则：无 |
| SYSCTRLFLG | 系统控制标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定链路集中的链路建立是按整系统控制还是按单进程控制。整系统控制即指定链路集中建立的链路数量为该指定的链路数量，单进程控制即每进程建立链路，整系统的链路数量为进程数乘以每进程链路数。<br>数据来源：全网规划<br>取值范围：<br>- “YES（是）”：是<br>- “NO（否）”：否<br>默认值：NO<br>配置原则：无 |
| LINKNUMPERPROC | 单进程链路数量 | 可选必选说明：该参数在"SYSCTRLFLG"配置为"NO"时为条件可选参数。<br>参数含义：该参数用于指定链路集在单个HTTP进程中可建立的链路数量。如该参数配置为2，则单个HTTP进程中可建立2条链路，如果整系统中存在4个HTTP进程，则该链路集下建立的链路数为8条。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~16，单位是条。<br>默认值：1<br>配置原则：无 |
| LINKNUMSYS | 整系统链路数量 | 可选必选说明：该参数在"SYSCTRLFLG"配置为"YES"时为条件可选参数。<br>参数含义：该参数用于指定链路集中链路按整系统控制时，该链路集下建立的链路数量。该参数值不可大于HTTP进程数量，若大于则默认设置为当前HTTP进程数量。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~16。<br>默认值：4<br>配置原则：无 |
| LINKNUM | 链路数量 | 可选必选说明：可选参数<br>参数含义：该参数用于指定链路集下可配置的链路数量。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是2~64。<br>默认值：2<br>配置原则：<br>当<br>[**SET HTTPCONF**](../../HTTP管理/HTTP属性管理/设置HTTP属性（SET HTTPCONF）_83972196.md)<br>命令中参数“SignalRouting”设置为"TRUE"时，即信令路由功能打开时，该参数才会生效。 |
| STRATEGY | 策略 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SBI链路集下存在多条链路时的链路选择策略。<br>数据来源：本端规划<br>取值范围：<br>- “Turns（Turns）”：负荷分担<br>- “Weight（Weight）”：权重<br>- “Priority（Priority）”：优先级<br>默认值：Turns<br>配置原则：<br>当<br>[**SET HTTPCONF**](../../HTTP管理/HTTP属性管理/设置HTTP属性（SET HTTPCONF）_83972196.md)<br>命令中参数“SignalRouting”设置为"TRUE"时，即信令路由功能打开时，该参数才会生效。 |
| STREAMNUMARRAY | StreamId数量数组 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SBI链路集下指定链路数量的StreamId数组。该参数只在信令路由功能开启时生效，信令路由开关可通过<br>[**SET HTTPCONF**](../../HTTP管理/HTTP属性管理/设置HTTP属性（SET HTTPCONF）_83972196.md)<br>命令打开。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：[10000 10000]<br>配置原则：<br>当<br>[**SET HTTPCONF**](../../HTTP管理/HTTP属性管理/设置HTTP属性（SET HTTPCONF）_83972196.md)<br>命令中参数“SignalRouting”设置为"TRUE"时，即信令路由功能打开时，该参数才会生效。 |
| WEIGHTARRAY | 权重数组 | 可选必选说明：该参数在"STRATEGY"配置为"Weight"时为条件必选参数。<br>参数含义：该参数用于指定SBI链路集下指定链路数量的权重数组。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：[1 1]<br>配置原则：<br>当<br>[**SET HTTPCONF**](../../HTTP管理/HTTP属性管理/设置HTTP属性（SET HTTPCONF）_83972196.md)<br>命令中参数“SignalRouting”设置为"TRUE"时，即信令路由功能打开时，该参数才会生效。 |
| PRIORITYARRAY | 优先级数组 | 可选必选说明：该参数在"STRATEGY"配置为"Priority"时为条件必选参数。<br>参数含义：该参数用于指定SBI链路集下指定链路数量的优先级数组。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：[1 1]<br>配置原则：<br>当<br>[**SET HTTPCONF**](../../HTTP管理/HTTP属性管理/设置HTTP属性（SET HTTPCONF）_83972196.md)<br>命令中参数“SignalRouting”设置为"TRUE"时，即信令路由功能打开时，该参数才会生效。 |
| DESCRIPTION | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SBI链路集策略描述信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| NFIPWITHSRVPORT | NF IP是否与NFService端口号组合 | 可选必选说明：可选参数<br>参数含义：该参数用于控制当对端NFService没有IP地址，使用对端NF的IP地址时，端口号是否从对端NFService中获取。<br>数据来源：全网规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无<br>配置原则：无 |
| FAULTLINKPCT | 进程内链路集故障阈值 | 可选必选说明：可选参数<br>参数含义：该参数用于判定链路集在单个HTTP进程中是否为故障，当故障链路数占比大于等于此参数，则认为进程内到对端的链路集故障。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~100，单位是百分比。<br>默认值：0<br>配置原则：<br>如果针对某个对端NF的链路集生效，则配置该参数。针对所有链路集均生效，则不配置本参数，使用<br>[**SET SBILINKSETCFG**](../服务化接口链路集管理/设置服务化接口链路集属性（SET SBILINKSETCFG）_83653668.md)<br>命令配置。如果都配置，则优先使用<br>[**ADD SBILINKSETPROP**](增加SBI链路集策略（ADD SBILINKSETPROP）_29053325.md)<br>的命令配置生效。 |
| FAULTPROCESSPCT | 系统内链路集故障阈值 | 可选必选说明：可选参数<br>参数含义：该参数用于判定链路集在系统内是否为故障，当存在链路集故障的进程数占比大于等于此参数，则认为系统内链路集故障，该链路集对应的NF服务不可达。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~100，单位是百分比。<br>默认值：0<br>配置原则：<br>如果针对某个对端NF的链路集生效，则配置该参数。针对所有链路集均生效，则不配置本参数，使用<br>[**SET SBILINKSETCFG**](../服务化接口链路集管理/设置服务化接口链路集属性（SET SBILINKSETCFG）_83653668.md)<br>命令配置。如果都配置，则优先使用<br>[**ADD SBILINKSETPROP**](增加SBI链路集策略（ADD SBILINKSETPROP）_29053325.md)<br>的命令配置生效。 |

## 操作的配置对象

- [SBI链路集策略（SBILINKSETPROP）](configobject/UNC/20.15.2/SBILINKSETPROP.md)

## 使用实例

- 若运营商想增加本端到对端NFTYPE为SMF的链路集策略，指定单个HTTP进程中配置的链路数为2，则执行如下命令：
  ```
  ADD SBILINKSETPROP: INDEX=1, LINKNUMPERPROC=2;
  ADD SBILINKCFG: INDEX=1, LINKTYPE=Dynamic, SBIAPLEIDX=1, NFTYPE=NFTypeSMF, PROPIDX=1, DESC="sbilink";
  ```
- 若运营商想增加一个服务化接口链路集的策略信息，指定索引为1，链路数为2，策略为Turns（轮询），链路的STREAMNUM都是10000，可以执行如下命令：
  ```
  ADD SBILINKSETPROP:INDEX=1,SYSCTRLFLG=NO,LINKNUMPERPROC=1,LINKNUM=2,STRATEGY=Turns,STREAMNUMARRAY="[10000 10000]";
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加SBI链路集策略（ADD-SBILINKSETPROP）_29053325.md`
