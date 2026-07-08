---
id: UNC@20.15.2@MMLCommand@ADD LDPREMOTEPEER
type: MMLCommand
name: ADD LDPREMOTEPEER（添加LDP远端邻居）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: LDPREMOTEPEER
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 8192
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- MPLS管理
- LDP管理
- LDP远端邻居管理
status: active
---

# ADD LDPREMOTEPEER（添加LDP远端邻居）

## 功能

该命令用于添加LDP远端邻居。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为8192。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：目前仅支持_public_公网。 |
| REMOTEPEERNAME | 远端邻居名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定远端邻居名。配置LDP远端会话，需要指定远端邻居名和IP地址。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无 |
| REMOTEIP | 远端邻居IP地址 | 可选必选说明：必选参数<br>参数含义：该参数用于指定远端邻居IP地址。配置LDP远端会话，需要指定远端邻居名和IP地址。当下发0.0.0.0时表示remote IP被删除。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。<br>默认值：无 |
| NOMAPPING | 禁止发送mapping | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否禁止发送mapping。可以通过设置TRUE命令配置禁止向远端邻居分发标签，以节约系统资源。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE<br>配置原则：<br>- TRUE：禁止向远端邻居分发标签。<br>- FALSE：允许向远端邻居分发标签。 |
| HELLOSENDTIME | Hello报文发送时间（s） | 可选必选说明：可选参数<br>参数含义：该参数用于指定Hello报文发送时间。LSR使用Hello定时器周期性地发送Hello消息，向邻居LSR通告它在网络中的存在，并建立Hello邻接关系。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535，单位是秒。<br>默认值：无<br>配置原则：<br>- 缺省情况下，Hello发送定时器的值是Hello保持定时器值的1/3。<br>- 当配置的Hello发送定时器的值大于Hello保持定时器的值的1/3时，实际生效的值等于Hello保持定时器的值的1/3。 |
| HELLOHOLDTIME | Hello报文保持时间（s） | 可选必选说明：可选参数<br>参数含义：该参数用于指定Hello报文保持时间。建立了Hello邻接关系的LDP对等体之间，通过周期性发送Hello报文表明自己希望继续维持这种邻接关系。如果Hello保持定时器超时，没有收到新的Hello报文，则拆除Hello邻接关系。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为3～65535，单位是秒。<br>默认值：45<br>配置原则：如果LDP会话两端Hello保持定时器协商后的值小于9秒，则按照9秒处理。 |
| KASENDTIME | KA报文发送间隔时间（s） | 可选必选说明：可选参数<br>参数含义：该参数用于指定Keepalive报文发送间隔时间。LDP会话建立以后，LSR启动Keepalive发送定时器周期性地发送Keepalive消息，用于保持LDP会话。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535，单位是秒。<br>默认值：无<br>配置原则：<br>- 缺省情况下，Keepalive发送定时器的值是Keepalive保持定时器值的1/3。<br>- 当配置的Keepalive发送定时器的值大于Keepalive保持定时器的值的1/3时，实际生效的值等于Keepalive保持定时器的值的1/3。 |
| KAHOLDTIME | KA报文保持时间（s） | 可选必选说明：可选参数<br>参数含义：该参数用于指定Keepalive报文保持时间。LDP对等体之间通过LDP会话连接传送的LDP协议报文（PDU）维持LDP会话，如果会话保持定时器超时，没有收到任何LDP PDU，则关闭连接，结束LDP会话。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为30～65535，单位是秒。<br>默认值：45<br>配置原则：当两台设备之间有多条链路维持一个会话或本地会话和远端会话共存时，多条链路或本地和远端的Keepalive保持定时器配置的值需要保持一致，否则LDP会话可能不稳定。 |
| LSRIDIFNAME | 本地LSR ID绑定接口名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本地LSR ID绑定接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| IGPSYNCDELAY | IGP联动延迟时间（s） | 可选必选说明：可选参数<br>参数含义：该参数用于指定IGP联动延迟时间。故障链路的LDP会话重新建立以后，LDP会启动Delay定时器等待LSP的建立，当Delay定时器超时以后，LDP都会通知IGP同步流程结束。当取值为4294967295时，表示IGPSYNCDELAY取LDP实例下配置的IGP联动延迟时间，具体取值可通过LST LDPINSTANCE命令查看。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535，4294967295，单位是秒。<br>默认值：4294967295 |
| LABELADVMODE | 标签发布模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定标签发布模式。在MPLS体系中，由下游LSR决定将标签分配给特定FEC，再通知上游LSR。即标签由下游指定，标签的分配按从下游到上游的方向分发。 具有标签分发邻接关系的上游LSR和下游LSR必须对使用的标签发布方式达成一致。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DU：下游自主向上游分配标签。 对于一个特定的FEC，LSR无须从上游获得标签请求消息即进行标签分配与分发。<br>- DOD：上游按需向下游请求标签。 对于一个特定的FEC，LSR获得标签请求消息之后才进行标签分配与分发。<br>默认值：DU<br>配置原则：当两台设备之间有多条链路维持一个会话或本地会话和远端会话共存时，多条链路或本地和远端的标签发布模式需要保持一致。 |

## 操作的配置对象

- [LDP远端邻居（LDPREMOTEPEER）](configobject/UNC/20.15.2/LDPREMOTEPEER.md)

## 使用实例

添加LDP远端邻居：

```
ADD LDPREMOTEPEER:VRFNAME="_public_",REMOTEPEERNAME="r2",REMOTEIP="192.168.1.3",NOMAPPING=FALSE,HELLOSENDTIME=15,HELLOHOLDTIME=30,KASENDTIME=60,KAHOLDTIME=60,LSRIDIFNAME="Ethernet64/0/4",LABELADVMODE=DU,IGPSYNCDELAY=10;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/添加LDP远端邻居（ADD-LDPREMOTEPEER）_49802046.md`
