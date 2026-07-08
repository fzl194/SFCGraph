---
id: UDG@20.15.2@MMLCommand@MOD TWAMPCLIENT
type: MMLCommand
name: MOD TWAMPCLIENT（修改TWAMP客户端）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: TWAMPCLIENT
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPAPM功能管理
- TWAMP
- TWAMP客户端配置
status: active
---

# MOD TWAMPCLIENT（修改TWAMP客户端）

## 功能

该命令用于修改TWAMP客户端。

> **说明**
> - 该命令执行后立即生效。
>
> - 如果本条记录的客户端ID被发送端绑定，则仅允许修改DESCRIPTION参数。可以通过LST TWAMPSENDER命令来查看当前客户端ID是否被发送端绑定。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CLIENTID | 客户端ID | 可选必选说明：必选参数<br>参数含义：该参数用于配置客户端ID。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~12000。<br>默认值：无<br>配置原则：无 |
| TWAMPARCH | TWAMP架构 | 可选必选说明：可选参数<br>参数含义：该参数用于指定TWAMP架构。<br>数据来源：全网规划<br>取值范围：<br>- LIGHT（LIGHT）<br>默认值：无<br>配置原则：无 |
| AFTYPE | 地址族类型 | 可选必选说明：可选参数<br>参数含义：该参数用于用户指定地址族类型。<br>数据来源：全网规划<br>取值范围：<br>- IPV4（IPV4）<br>默认值：无<br>配置原则：无 |
| LOCALIPV4 | 本端IPV4地址 | 可选必选说明：该参数在"AFTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于指示本端IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。0.0.0.0～255.255.255.255。<br>默认值：无<br>配置原则：<br>采用点分十进制"X.X.X.X"格式。<br>IP地址必须是A、B或者C类地址，不能为环回地址（127.x.y.z）、组播地址（240.x.y.z）或（255.0.0.0）。<br>LOCALIPV4必须在<br>[**ADD TWAMPLOGICINF**](../本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md)<br>已经配置，可以用<br>[**LST TWAMPLOGICINF**](../本端逻辑接口配置/查询本地逻辑接口（LST TWAMPLOGICINF）_73142135.md)<br>查询。<br>LOCALIPV4不能已在<br>[**ADD TWAMPRESPONDER**](../TWAMP响应端配置/增加TWAMP响应端（ADD TWAMPRESPONDER）_73142131.md)<br>中配置，可以用<br>[**LST TWAMPRESPONDER**](../TWAMP响应端配置/查询TWAMP响应端（LST TWAMPRESPONDER）_73302049.md)<br>查询。 |
| PEERIPV4 | 对端IPV4地址 | 可选必选说明：该参数在"AFTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于指示对端IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。0.0.0.0～255.255.255.255。<br>默认值：无<br>配置原则：<br>采用点分十进制"X.X.X.X"格式。<br>IP地址必须是A、B或者C类地址，不能为环回地址（127.x.y.z）、组播地址（240.x.y.z）或（255.0.0.0）。 |
| LLOCALUDPPORT | 本端UDP端口 | 可选必选说明：该参数在"TWAMPARCH"配置为"LIGHT"时为条件必选参数。<br>参数含义：该参数用于配置本端UDP端口。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是65450~65530。<br>默认值：无<br>配置原则：无 |
| LPEERUDPPORT | 对端UDP端口 | 可选必选说明：该参数在"TWAMPARCH"配置为"LIGHT"时为条件必选参数。<br>参数含义：该参数用于配置对端UDP端口。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~65535。<br>默认值：无<br>配置原则：无 |
| DSCP | 差分服务码 | 可选必选说明：可选参数<br>参数含义：该参数用于配置差分服务码。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~63。<br>默认值：无<br>配置原则：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于配置VPN实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~31。<br>默认值：无<br>配置原则：<br>VRFNAME必须和关联的本地逻辑接口配置中的VRFNAME相同，本地逻辑接口配置中的VRFNAME可使用。 |
| DESCRIPTION | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于配置描述。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@TWAMPCLIENT]] · TWAMP客户端（TWAMPCLIENT）

## 使用实例

修改客户端ID为1的实例：

```
MOD TWAMPCLIENT: CLIENTID=1, DESCRIPTION="CLIENT1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-TWAMPCLIENT.md`
