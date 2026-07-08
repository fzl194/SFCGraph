---
id: UNC@20.15.2@MMLCommand@SET GTPPUB
type: MMLCommand
name: SET GTPPUB（设置GTP-C协议参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: GTPPUB
command_category: 配置类
applicable_nf:
- SGSN
- MME
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- GTP-C协议管理
- GTP-C协议参数配置
status: active
---

# SET GTPPUB（设置GTP-C协议参数）

## 功能

**适用网元：SGSN、MME、AMF**

该命令用于配置GTP-C协议公共参数。

## 注意事项

- 系统初次运行时，会执行系统初始设置值。
- 该命令执行后立即生效。
- 当命令**[SET AMFN26PLCY](../../../../../接口管理/GTP-C接口配置管理/N26接口管理/N26策略管理/设置AMF N26接口策略（SET AMFN26PLCY）_62817114.md)**的参数“N26ITFMODE”取值为“COMBINE”时，该命令适用于SGSN、MME、AMF，否则，该命令仅适用于SGSN、MME。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PRVEXT | 发送私有信息 | 可选必选说明：可选参数<br>参数含义：该参数指示是否发送私有信息，私有信息包含了运行商或设备商定义的信息。<br>数据来源：整网规划<br>取值范围：<br>- “OFF(关闭)”<br>- “ON(打开)”<br>系统初始设置值：<br>“OFF(关闭)”<br>。<br>说明：此参数选择<br>“ON(打开)”<br>时，需要设置参数PE（私有信息）、PEID（企业号）。 |
| ECHOSIG | 发送ECHO Request的路径 | 可选必选说明：可选参数<br>参数含义：该参数用于定义发送Echo Request的GTP-C路径范围。发送Echo Request的作用是进行路径管理。参考3GPP协议中的29060部分。<br>数据来源：整网规划<br>取值范围：<br>- “NONE(无)”<br>- “ALL(全部)”<br>- “SPECIFIED(特定的)”<br>系统初始设置值：<br>“ALL(全部)”<br>。<br>配置原则：<br>- “NONE(无)”：在所有GTP-C路径都不发送Echo Request。<br>- “ALL(全部)”：在所有的GTP-C路径上发送Echo Request。<br>- “SPECIFIED(特定的)”：在特定的GTP-C路径上发送Echo Request。<br>说明：现网存在一类GGSN，这类GGSN的一个IP地址仅用于接收PDP上下文建立请求消息，其他IP地址建立PDP上下文。前者因为没有建立PDP上下文，可能不支持Echo探测。如果现网存在这类GGSN，需要配置为<br>“SPECIFIED(特定的)”<br>，同时需要执行命令<br>[**ADD GGSNCHARACT**](../../GnGp-GGSN_S5_S8接口管理/GGSN属性/增加GGSN属性配置信息(ADD GGSNCHARACT)_72225613.md)<br>或者<br>[**MOD GGSNCHARACT**](../../GnGp-GGSN_S5_S8接口管理/GGSN属性/修改GGSN属性配置信息(MOD GGSNCHARACT)_72345535.md)<br>配置到此GGSN的版本规则（对应参数<br>“GnGp接口的GTP-C路径版本规则”<br>）为<br>“V1”<br>。<br>配置为<br>“SPECIFIED(特定的)”<br>时，<br>UNC<br>对于没有建立PDP上下文的GGSN IP地址不发送Echo Request，而是有选择性的采用Create PDP Context Request消息来维护GTP-C路径状态。<br>如果现网存在以上类的GGSN，上述的配置不是推荐方案，最佳的解决方案是建议客户推动对端设备的运营商对此类GGSN做软件升级处理。 |
| EI | 发送Echo请求间隔（s） | 可选必选说明：可选参数<br>参数含义：该参数定义了v0，v1版本的GTP-C路径上发送Echo Request的间隔时间。参考3GPP协议中的29060部分。<br>数据来源：整网规划<br>取值范围：60~3600s<br>系统初始设置值：<br>“239”<br>。 |
| V2EI | 发送GTPv2 Echo请求间隔（s） | 可选必选说明：可选参数<br>参数含义：该参数定义了v2版本的GTP-C路径上发送Echo Request的间隔时间。参考3GPP协议中的29274部分。<br>数据来源：整网规划<br>取值范围：60~3600s<br>系统初始设置值：<br>“239”<br>。 |
| OTSIE | 乱序信元 | 可选必选说明：可选参数<br>参数含义：该参数定义了系统是否允许收到的GTP消息的信元顺序错误。<br>数据来源：整网规划<br>取值范围：<br>- “DENY(禁止)”<br>- “ALLOW(允许)”<br>系统初始设置值：<br>“DENY(禁止)”<br>。 |
| POTHD | 路径数过载门限（%） | 可选必选说明：可选参数<br>参数含义：该参数定义了GTP-C路径占用比（当前路径数/系统支持路径数）过载门限，如果当前路径占用比达到或超过此门限值，并且此前不存在ALM-80651 GTPC路径数过载告警，将触发该告警。<br>数据来源：整网规划<br>取值范围：0~100%<br>系统初始设置值：<br>“85”<br>。<br>配置原则：<br>“路径过载门限”<br>的值应该大于<br>“路径过载恢复门限”<br>的值。 |
| PNTHD | 路径数过载恢复（%） | 可选必选说明：可选参数<br>参数含义：该参数定义了GTP-C路径占用比（当前路径数/系统支持路径数）过载恢复门限，如果在50秒之内当前路径占用比都小于此门限值，并且此前已经存在ALM-80651 GTPC路径数过载告警，则恢复该告警。<br>数据来源：整网规划<br>取值范围：0~100%<br>系统初始设置值：<br>“80”<br>。 |
| PCTHD | 路径数拥塞门限（%） | 可选必选说明：可选参数<br>参数含义：该参数定义了GTP-C路径占用比（当前路径数/系统支持路径数）拥塞门限，如果当前路径占用比达到或超过此门限值，并且此前不存在ALM-80650 GTPC路径数拥塞告警，将触发该告警。<br>数据来源：整网规划<br>取值范围：0~100%<br>系统初始设置值：<br>“95”<br>。<br>配置原则：<br>“路径拥塞门限”<br>的值应该大于<br>“路径拥塞恢复门限”<br>的值。 |
| PRTHD | 路径数拥塞恢复（%） | 可选必选说明：可选参数<br>参数含义：该参数定义了GTP-C路径占用比（当前路径数/系统支持路径数）拥塞恢复门限，如果在50秒之内当前路径占用比都小于此门限值，并且此前已经存在ALM-80650 GTPC路径数拥塞告警，则恢复该告警。<br>数据来源：整网规划<br>取值范围：0~100%<br>系统初始设置值：<br>“90”<br>。 |
| PEID | 企业号 | 可选必选说明：可选参数<br>参数含义：运营商或设备商的企业编号，是私有信息的一部分。<br>前提条件：参数<br>“PRVEXT”<br>为<br>“ON(打开)”<br>时，此参数有效。<br>数据来源：整网规划<br>取值范围：0~65535<br>系统初始设置值：<br>“2011”<br>。 |
| PE | 私有信息 | 可选必选说明：可选参数<br>参数含义：私有信息包含了运营商或设备商定义的信息。<br>数据来源：整网规划<br>取值范围：长度不超过255位字符串<br>系统初始设置值：<br>“UNC”<br>。 |
| GTPEXT | 检查GTP扩展头类型个数上限 | 可选必选说明：可选参数<br>参数含义：该参数定义了检查控制面GTP-C扩展头类型个数上限，单位：个。系统检测的GTP-C扩展头类型个数的最大数值，若大于该值则判为异常GTP-C报文，异常GTP-C报文会被丢弃。<br>数据来源：整网规划<br>取值范围：1~255<br>系统初始设置值：<br>“10”<br>。 |
| GTPSUPEXTLIST | 检查GTP扩展头列表个数上限 | 可选必选说明：可选参数<br>该参数定义检查用户面GTP-C支持扩展头列表通知长度上限，单位：1字节。当网元接收到来自GSN的支持扩展头列表通知消息，且列表中扩展头列表长度大于该阈值，就认为该扩展头列表为巨型扩展头列表，判定为异常GTP报文，异常GTP-C报文会被丢弃。<br>数据来源：整网规划<br>取值范围： 1~255<br>系统初始设置值：<br>“100”<br>。 |
| GTPEXLEN | 检查GTP扩展头类型长度上限 | 可选必选说明：可选参数<br>参数含义：该参数定义了检查控制面GTP-C扩展头类型长度上限，单位：4字节。当网元接收到协议未定义的扩展头，且其长度大于该阈值，判定为异常GTP报文，异常GTP-C报文会被丢弃。<br>数据来源：整网规划<br>取值范围：1~255<br>系统初始设置值：<br>“100”<br>。 |
| GTPVER | 本端可处理的请求消息的最高GTP版本 | 可选必选说明：可选参数<br>参数含义：该参数定义了本端接收的请求消息中可处理的最高GTP版本。<br>数据来源：整网规划<br>取值范围：<br>- “GTPv0（GTPv0）”<br>- “GTPv1（GTPv1）”<br>- “GTPv2（GTPv2）”<br>系统初始设置值：<br>“GTPv2（GTPv2）”<br>。<br>配置原则：如果设置的版本过低，可能影响用户接入，请谨慎修改。建议使用系统初始值。 |
| POOLSRCPORTSW | 缺省SGSN透传源端口号开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制Pool组网中，缺省SGSN是否将源SGSN发送的v0，v1版本的Identification/SGSN Context Request的源端口号透传给目的SGSN。<br>数据来源：整网规划<br>取值范围：<br>- “OFF(关闭)”<br>- “ON(打开)”<br>系统初始设置值：<br>“ON(打开)”<br>。<br>配置原则：<br>- 当设置为“OFF(关闭)”时，可能会导致SGSN对接失败。<br>- 开关开启时，缺省SGSN透传源端口号；开关关闭时，缺省SGSN将源端口号改为由本SGSN分配。 |
| PEERRECOVERYSW | 对端Recovery处理开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制对端Recovery值变化时，是否去激活用户。<br>数据来源：整网规划<br>取值范围：<br>- “OFF(关闭)”<br>- “ON(打开)”<br>系统初始设置值：<br>“OFF(关闭)”<br>。<br>配置原则：当对端Recovery值变化时，<br>- 参数配置为“ON(打开)”，则针对2G/3G用户发起去激活，针对4G用户，当“WSFD-201203S-GW/P-GW故障下的业务恢复”特性开启时，执行S-GW重选，当“WSFD-201203S-GW/P-GW故障下的业务恢复”特性关闭时，执行分离。<br>- 参数配置为“OFF(关闭)”，则针对2G/3G用户不发起去激活，针对4G用户，当“WSFD-201203S-GW/P-GW故障下的业务恢复”特性开启时，执行S-GW重选，当“WSFD-201203S-GW/P-GW故障下的业务恢复”特性关闭时，不发起分离。 |
| PATHDOWNDEASW | GTPC路径断去激活开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制GTP-C路径断时，是否去激活用户。<br>数据来源：整网规划<br>取值范围：<br>- “OFF(关闭)”<br>- “ON(打开)”<br>系统初始设置值：<br>“OFF(关闭)”<br>。<br>配置原则：当GTPC路径断时，<br>- 参数配置为“ON(打开)”，则针对2G/3G用户发起去激活，针对4G用户，当“WSFD-201203S-GW/P-GW故障下的业务恢复”特性开启时，执行S-GW重选，当“WSFD-201203S-GW/P-GW故障下的业务恢复”特性关闭时，执行分离。<br>- 参数配置为“OFF(关闭)”，则针对2G/3G用户不发起去激活，针对4G用户，当“WSFD-201203S-GW/P-GW故障下的业务恢复”特性开启时，执行S-GW重选，当“WSFD-201203S-GW/P-GW故障下的业务恢复”特性关闭时，不发起分离。 |
| PATHVERDETECTSW | V0版本GTPC路径尝试使用V1版本探测开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制是否对V0版本GTP-C路径使用V1版本的Echo消息进行探测。如果V1版本Echo探测成功，该GTPC路径将升级为V1版本；如果V1版本探测不成功，该GTPC路径的版本不变。<br>数据来源：整网规划<br>取值范围：<br>- “OFF(关闭)”<br>- “ON(打开)”<br>系统初始设置值：<br>“ON(打开)”<br>。<br>配置原则：开关打开，V0版本的GTPC路径版本使用V1版本探测；开关关闭，V0版本的GTPC路径版本不使用V1版本探测。 |
| DNSGTPCPATHFILTERSW | 过滤故障状态的GTPC路径开关 | 可选必选说明：可选参数<br>参数含义：该参数用于针对DNS解析的IP地址列表，是否根据GTPC路径状态过滤故障状态的对端地址。当GTPC路径不存在时，认为GTPC路径状态为正常。<br>数据来源：整网规划<br>取值范围：<br>- “OFF(关闭)”<br>- “ON(打开)”<br>系统初始设置值：<br>“ON(打开)”<br>。<br>配置原则：<br>- 开关开启时，DNS解析结果只使用非故障状态的GTPC路径的IP地址列表；开关关闭时，不进行GTPC路径状态的判断。<br>- 如果将该开关关闭，可能会影响业务成功率，请谨慎修改。建议使用系统初始值。 |
| LOCRECOVERYSW | 本端recovery更新开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制本端Recovery值是否更新。本端Recovery值表示本端网元重启的次数。当开关关闭时，所有SPP进程重启后，本端Recovery值不变；反之，本端Recovery值自增1。当本端Recovery值等于255时，自增1后变为0。<br>数据来源：整网规划<br>取值范围：<br>- “OFF(关闭)”<br>- “ON(打开)”<br>系统初始设置值：<br>“ON(打开)”<br>。 |
| UDPCHKSW | GTPC报文校验功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置是否支持对GTP-C报文的UDP校验功能。开关打开时，支持UDP校验功能，此时发送GTP-C报文需要填写UDP校验和，接收GTP-C报文需要检查UDP校验和，并且校验失败的报文将被丢弃。开关关闭时，不支持UDP校验功能，此时发送GTP-C报文不需要填写UDP校验和，接收GTP-C报文需要检查UDP校验和，并且校验失败的报文将会继续接收，不会被丢弃。<br>数据来源：整网规划<br>取值范围：<br>- “OFF(关闭)”<br>- “ON(打开)”<br>系统初始设置值：<br>“ON(打开)”<br>。<br>说明：对于IPv6类型的GTP-C报文，在发送时不受该开关控制，必须填写UDP校验和，在接收时的处理仍然受该开关控制。 |
| UAMRECOVERY | UAMF融合模式recovery更新 | 可选必选说明：可选参数<br>参数含义：该参数用于控制如果AMF N26接口采用融合部署模式时（SET AMFN26PLCY命令“N26ITFMOD”配置为“COMBINE”），除所有SPP进程重启之外，是否需要AMF同时发生复位，本端Recovery值才自增1。<br>数据来源：整网规划<br>取值范围：<br>- “NO(否)”<br>- “YES(是)”<br>系统初始设置值：<br>“NO(否)”<br>。<br>配置原则：<br>- 设置为“YES(是)”后可能导致2/3/4G会话管理recovery维护功能受影响，建议保持“NO(否)”。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GTPPUB]] · GTP-C协议参数（GTPPUB）

## 使用实例

设置GTP-C公共配置表：打开发送私有信息开关，发送ECHO Request的路径为全部，发送Echo请求间隔为239秒，发送GTPv2 Echo请求间隔为239秒，乱序信元设置为“DENY”，路径数过载门限设置为85%，路径数过载恢复设置为80%，路径数拥塞门限设置为95%，企业号为2011，私有信息设置为“UNC”，检查GTP扩展头类型个数上限为10，检查GTP扩展头列表个数上限为100，检查GTP扩展头类型长度上限为100，本端可处理的请求消息的最高GTP版本设置为GTPv2，打开缺省SGSN透传源端口号开关，关闭对端Recovery处理开关，关闭GTPC路径断去激活开关，打开V0版本GTPC路径尝试使用V1版本探测开关，打开过滤故障状态的GTPC路径开关，打开本端recovery更新开关， 打开GTP-C报文UDP校验开关。

SET GTPPUB: PRVEXT=ON, ECHOSIG=ALL, EI=239, V2EI=239, OTSIE=DENY, POTHD=85, PNTHD=80, PCTHD=95, PRTHD=90, PEID=2011, PE="UNC", GTPEXT=10, GTPSUPEXTLIST=100, GTPEXLEN=100, GTPVER=GTPv2, POOLSRCPORTSW=ON, PEERRECOVERYSW=OFF, PATHDOWNDEASW=OFF, PATHVERDETECTSW=ON, DNSGTPCPATHFILTERSW=ON, LOCRECOVERYSW=ON, UDPCHKSW=ON;

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置GTP-C协议参数(SET-GTPPUB)_26145920.md`
