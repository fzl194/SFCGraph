---
id: UDG@20.15.2@MMLCommand@MOD BGPPEERGROUP
type: MMLCommand
name: MOD BGPPEERGROUP（修改BGP对等体组）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: BGPPEERGROUP
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- BGP对等体组
status: active
---

# MOD BGPPEERGROUP（修改BGP对等体组）

## 功能

该命令用于设置及更新IPv4或IPv6地址族下的对等体组的参数。

## 注意事项

- 该命令执行后立即生效。
- 修改常规路由器，本地接口地址，本地接口名称，存活时间，保持时间会导致所有属于该对等体组的对等体重连。
- 当前支持配置的认证算法及密码长度均符合IETF标准规定。
- 建议配置协议相关认证，增强协议安全性，否则可能存在协议安全风险。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户的BGP VPN实例。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：使用LST L3VPNINST命令查看可用VPN。 |
| GROUPNAME | 对等体组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定对等体组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～47；字符串由数字、字母、“.”、“-”或“_”组成。<br>默认值：无 |
| AFTYPE | 对等体组地址族类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定该对等体组支持的地址族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- public：公网地址族。<br>- ipv4uni：IPv4地址族。<br>- ipv6uni：IPv6地址族。<br>- noaf：不指定地址族。<br>默认值：无<br>配置原则：公网group配置public，私网则配置ipv4uni或ipv6uni或noaf。 |
| GROUPAS | 组自治域号 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“public”、“ipv4uni”、“ipv6uni” 或 “noaf”时为可选参数。<br>参数含义：该参数用于指定对等体组所在AS号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～11。取值范围是number<1-4294967295>或者number<1-65535>.number<0-65535>。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |
| ROUTEREFRESH | 路由刷新 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“public”、“ipv4uni”、“ipv6uni” 或 “noaf”时为可选参数。<br>参数含义：该参数用于指定该组是否支持路由刷新。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| FOURBYTEAS | 4字节AS号功能 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“public”、“ipv4uni”、“ipv6uni” 或 “noaf”时为可选参数。<br>参数含义：该参数用于指定该组是否具有4字节AS号能力。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| CONVENTIONAL | 常规路由器 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“public”、“ipv4uni” 或 “noaf”时为可选参数。<br>参数含义：该参数用于指定该组是否为常规路由器。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无<br>配置原则：使能常规路由器功能后，设备将不具备所有扩展功能（如路由刷新功能、GR能力及多地址族协商、接收或发布ADD-PATH路由）。 |
| LOCALIFADDR | 本地接口地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“public”、“ipv4uni”、“ipv6uni” 或 “noaf”时为可选参数。<br>参数含义：该参数用于指定该对等体组本地接口地址。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～39。取值为一个IP地址。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |
| LOCALIFNAME | 本地接口名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“public”、“ipv4uni”、“ipv6uni” 或 “noaf”时为可选参数。<br>参数含义：该参数用于指定该对等体组本地接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- 不区分大小写。 |
| EBGPMAXHOP | EBGP最大跳数 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“public”、“ipv4uni”、“ipv6uni” 或 “noaf”时为可选参数。<br>参数含义：该参数用于指定该对等体组非直连EBGP邻居间的最大跳数值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～255。<br>默认值：无<br>配置原则：VALIDTTLHOPS和EBGPMAXHOP参数均会影响到发送出去的BGP报文的TTL值，存在冲突，只能对同一对等体或对等体组使能两种功能中的一种。 |
| VALIDTTLHOPS | 指定需要检测的TTL跳数值 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“public”、“ipv4uni”、“ipv6uni” 或 “noaf”时为可选参数。<br>参数含义：该参数用于指定该对等体组GTSM功能的参数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～256。<br>默认值：无<br>配置原则：VALIDTTLHOPS和EBGPMAXHOP参数均会影响到发送出去的BGP报文的TTL值，存在冲突，只能对同一对等体或对等体组使能两种功能中的一种。当VALIDTTLHOPS参数配置成256时，不使能VALIDTTLHOPS功能。 |
| FAKEAS | 伪AS号 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“public”、“ipv4uni”、“ipv6uni” 或 “noaf”时为可选参数。<br>参数含义：该参数用于指定该对等体组的伪AS号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～11。取值范围是number<1-4294967295>或者number<1-65535>.number<0-65535>。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |
| ISIGNORE | 是否忽略 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“public”、“ipv4uni”、“ipv6uni” 或 “noaf”时为可选参数。<br>参数含义：该参数用于指定是否禁止与对等体组建立会话。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无<br>配置原则：配置ISIGNORE为TRUE，就意味着与对等体的会话终止，清除所有相关路由信息，需要慎重。 |
| CONNECTMODE | 连接模式 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“public”、“ipv4uni”、“ipv6uni” 或 “noaf”时为可选参数。<br>参数含义：该参数用于指定对等体组的建接方式，只侦听连接请求或只发起连接。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- null：既侦听连接请求，又主动发送连接请求。<br>- listenOnly：只侦听。<br>- connectOnly：只连接。<br>默认值：无<br>配置原则：如果不配置，对等体使用两种方式建连，既侦听连接请求，又主动发送连接请求，若两端邻居都配置该参数为listenOnly或connectOnly，则不能建立连接。邻居建立后再配置此参数，需要执行RBL BGPPEERGROUP命令使邻居重建才生效。 |
| ISLOGCHANGE | 是否记录日志 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“public”、“ipv4uni”、“ipv6uni” 或 “noaf”时为可选参数。<br>参数含义：该参数用于指定是否使能BGP记录指定对等体/对等体组会话状态和事件信息的功能。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| PSWDTYPE | 密码类型 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“public”、“ipv4uni”、“ipv6uni” 或 “noaf”时为可选参数。<br>参数含义：该参数用于指定认证密码的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- null：NULL。<br>- cipher：密文。<br>默认值：无<br>配置原则：和PSWDCIPHERTEXT一起配置，完成认证密码功能；配置PSWDTYPE，则不能配置Keychain安全机制，KEYCHAINNAME不能配置。cipher采用MD5认证，MD5认证为非安全认证，推荐使用Keychain安全机制。 |
| PSWDCIPHERTEXT | 密码 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PSWDTYPE”配置为“cipher”时为可选参数。<br>参数含义：该参数用于指定的认证密码。<br>数据来源：全网规划<br>取值范围：密码类型，输入长度范围为1～255。<br>默认值：无<br>配置原则：<br>- 和PSWDTYPE一起配置，完成认证密码功能。<br>- 字符不允许包括“？”和空格。<br>- 配置的密码建议至少包含大写、小写、数字、特殊字符中的2种，并且长度不能小于8。<br>- MD5属于不安全的加密算法，建议使用Keychain认证。 |
| KEYCHAINNAME | Keychain名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“public”、“ipv4uni”、“ipv6uni” 或 “noaf”时为可选参数。<br>参数含义：该参数用于指定该对等体组TCP连接时的Keychain认证名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～47。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- 和PSWDTYPE不能同时使用。<br>- 字符不允许包括“？”和空格。 |
| KEEPALIVETIME | 存活时间（s） | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“public”、“ipv4uni”、“ipv6uni” 或 “noaf”时为可选参数。<br>参数含义：该参数用于指定该对等体组的保活计时器时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～21845，单位是秒。<br>默认值：无<br>配置原则：KEEPALIVETIME和HOLDTIME配合使用，且HOLDTIME至少为KEEPALIVETIME的3倍。 |
| HOLDTIME | 保持时间（s） | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“public”、“ipv4uni”、“ipv6uni” 或 “noaf”时为可选参数。<br>参数含义：该参数用于指定该对等体组的保持计时器时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535，单位是秒。<br>默认值：无<br>配置原则：KEEPALIVETIME和HOLDTIME配合使用，且HOLDTIME至少为KEEPALIVETIME的3倍。 |
| PATHMTUDISCOVERY | 路径MTU发现功能 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“public”、“ipv4uni”、“ipv6uni” 或 “noaf”时为可选参数。<br>参数含义：该参数用于指定该对等体组是否能够进行路径MTU自动发现。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| DESCRIPTION | 描述 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“public”、“ipv4uni”、“ipv6uni” 或 “noaf”时为可选参数。<br>参数含义：为该对等体组添加描述信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～80。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |
| TRACKINGENABLE | 使能快速感知邻居不可达并断开连接功能 | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“public”、“ipv4uni”、“ipv6uni” 或 “noaf”时为可选参数。<br>参数含义：该参数用于指定是否对该对等体组使能Tracking功能，快速感知邻居断连。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无<br>配置原则：和TRACKINGDELAYTIME同时配置，完成使能Tracking功能。 |
| TRACKINGDELAYTIME | 邻居断连延迟时间（s） | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“public”、“ipv4uni”、“ipv6uni” 或 “noaf”时为可选参数。<br>参数含义：该参数用于指定该对等体组的Tracking延时参数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535，单位是秒。<br>默认值：无<br>配置原则：TRACKINGDELAYTIME不为0时，要求TRACKINGENABLE必须为TRUE。当TRACKINGENABLE为FALSE时，TRACKINGDELAYTIME会被设置为默认数值。 |
| CONNRETRYTIME | 重连时间（s） | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFTYPE”配置为“public”、“ipv4uni”、“ipv6uni” 或 “noaf”时为可选参数。<br>参数含义：该参数用于指定该对等体组在建立TCP连接时的连接重试时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535，单位是秒。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/BGPPEERGROUP]] · BGP对等体组（BGPPEERGROUP）

## 使用实例

- 修改在名称为“vrf1”的BGP VPN实例下对等体组asdf的IPv4地址族连接模式：
  ```
  MOD BGPPEERGROUP:VRFNAME="vrf1",GROUPNAME="asdf",AFTYPE=ipv4uni,CONNECTMODE=listenOnly;
  ```
- 修改在名称为“vrf1”的BGP VPN实例下对等体组asdf的IPv6地址族连接模式：
  ```
  MOD BGPPEERGROUP:VRFNAME="vrf1",GROUPNAME="asdf",AFTYPE=ipv6uni,CONNECTMODE=listenOnly;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改BGP对等体组（MOD-BGPPEERGROUP）_00600449.md`
