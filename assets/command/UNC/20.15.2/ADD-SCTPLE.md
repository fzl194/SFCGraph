---
id: UNC@20.15.2@MMLCommand@ADD SCTPLE
type: MMLCommand
name: ADD SCTPLE（增加SCTP本地实体）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SCTPLE
command_category: 配置类
applicable_nf:
- MME
- AMF
effect_mode: 立即生效
is_dangerous: false
max_records: 1024
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- SCTP本地实体
status: active
---

# ADD SCTPLE（增加SCTP本地实体）

## 功能

**适用网元：MME、AMF**

此命令用于添加基于IP的宽带信令SCTP(Stream Control Transmission Protocol)偶联的本端信息，SCTP偶联是两个SCTP端点通过SCTP协议规定的4步握手机制建立起来的进行数据传递的逻辑联系或者通道。本命令中配置的是SCTP偶联的两个端点中的本端。

## 注意事项

- 此命令执行后立即生效。
- 此命令最大记录数为1024。
- 同一个SCTP本地实体组中的SCTP本地实体的IP地址不允许相同。
- 同一个SCTP本地实体组中的SCTP本地实体仅端口号为38412的实体支持建立多偶联。
- SCTP本地实体组被引用时可在该实体组下动态添加SCTP本地实体。
- SCTP本地实体组被引用时，如果该实体组下剩余的SCTP本地实体被引用且用途非UE或BOTH时不允许删除SCTP本地实体。
- IP地址和vpn名称必须在SERVICEIP表中已经配置，可以用[**LST SERVICEIP**](../../业务IP管理/业务IP/查询业务IP(LST SERVICEIP)_72226047.md)查询。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCTPLEIDX | SCTP本端实体索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SCTP本端实体索引用于唯一标识一个SCTP本端实体。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~1023。<br>默认值：无 |
| SCTPGROUPID | SCTP本端实体组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SCTP本端实体所属的组多个SCTP本端实体可以添加到一个实体组中，供NGAP(NG Application Protocol)和SFGAP（SFG Application Protocol）协议层使用该参数通过ADD SCTPLEGRP命令配置。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~255。<br>默认值：无 |
| IPVERSION | IP地址版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SCTP本端实体引用的逻辑IP地址版本。<br>数据来源：全网规划<br>取值范围：<br>- “IPV4(IPv4)”<br>- “IPV6(IPv6)”<br>默认值：无 |
| LOCALIPV41 | 本端IPv4地址1 | 可选必选说明：该参数在"IPVERSION"配置为"IPv4"时为条件必选参数。<br>参数含义：该参数用于指定SCTP本端实体引用的逻辑IPv4地址1。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| LOCALIPV42 | 本端IPv4地址2 | 可选必选说明：该参数在"IPVERSION"配置为"IPv4"时为条件可选参数。<br>参数含义：该参数用于指定SCTP本端实体引用的逻辑IPv4地址2。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| LOCALIPV61 | 本端IPv6地址1 | 可选必选说明：该参数在"IPVERSION"配置为"IPv6"时为条件必选参数。<br>参数含义：该参数用于指定SCTP本端实体引用的逻辑IPv6地址1。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无 |
| LOCALIPV62 | 本端IPv6地址2 | 可选必选说明：该参数在"IPVERSION"配置为"IPv6"时为条件可选参数。<br>参数含义：该参数用于指定SCTP本端实体引用的逻辑IPv6地址2。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无 |
| PORT | 端口号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SCTP本端实体的端口号。<br>数据来源：<br>取值范围：整数类型，取值范围为1024~65535。<br>默认值：38412 |
| CROSSIPFLG | 交叉路径是否可用 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SCTP本端实体的交叉路径是否可用选择为否时表示交叉路径不开启，选择为是时表示开启交叉路径。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- E_SCTP_CROSS_NO：交叉路径不可用<br>- E_SCTP_CROSS_YES：交叉路径可用<br>默认值：E_SCTP_CROSS_NO |
| SCTPPARAIDX | SCTP协议参数索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SCTP本端实体的参数配置索引，用于根据该索引获取到SCTP协议的参数配置信息该参数通过ADD SCTPPARA命令配置。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0~65534。<br>默认值：0 |
| USAGE | 用途 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SCTP本端实体的使用者信息，协议中定义了不同偶联可指定给不同类型的用户使用，如可指定使用者为UE、NON-UE或BOTH。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- E_SCTP_USAGE_UE<br>- E_SCTP_USAGE_NONUE<br>- E_SCTP_USAGE_BOTH<br>默认值：E_SCTP_USAGE_BOTH |
| WEIGHT | 权重 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SCTP本端实体的权重如果该值设置为0，则标识NGAP初始化消息不允许使用该SCTP本端实体，如果该值多个SCTP本端实体设置一样，则标识在多个SCTP本端实体间负载均衡。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0~255。<br>默认值：127<br>说明：该参数对SFGAP不生效。 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SCTP本端实体的描述信息。<br>数据来源：<br>取值范围：字符串类型，输入长度范围为0~32。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SCTPLE]] · SCTP本地实体（SCTPLE）

## 使用实例

1. 增加一条SCTP链路，本端有一个IPv4地址：该链路本地实体索引为0，地址类型为IPv4，本地IP1为192.168.15.10，本地端口号为38412，交叉路径设置为不可用，SCTP协议参数索引为0，用户类型为BOTH。
  ```
  ADD SCTPLE: SCTPLEIDX=1, SCTPGROUPID=0, IPVERSION=IPV4, LOCALIPV41="192.168.15.10", PORT=38412, CROSSIPFLG=E_SCTP_CROSS_NO, SCTPPARAIDX=0, USAGE=E_SCTP_USAGE_BOTH;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-SCTPLE.md`
