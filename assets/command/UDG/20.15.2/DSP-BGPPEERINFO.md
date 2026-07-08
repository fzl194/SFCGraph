---
id: UDG@20.15.2@MMLCommand@DSP BGPPEERINFO
type: MMLCommand
name: DSP BGPPEERINFO（查询BGP对等体信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: BGPPEERINFO
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- 查询BGP对等体信息
status: active
---

# DSP BGPPEERINFO（查询BGP对等体信息）

## 功能

该命令用于显示BGP对等体信息。

## 注意事项

- 该命令执行后立即生效。
- 执行命令ADD BGPMULTIPEER或MOD BGPMULTIPEERAF创建或使能了BGP多源对等体后，对应的普通BGP对等体信息不再显示。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户所配置的VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：使用LST L3VPNINST命令查看可用VPN。 |
| AFTYPE | 地址族类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VRF的地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>- ipv4vpn：VPNv4地址族。<br>- ipv6uni：IPv6地址族。<br>- ipv6vpn：VPNv6地址族。<br>默认值：无 |
| SOURCEIFNAME | 多源接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用于给定多源对等体的接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：仅支持Ethernet及其子接口类型，不区分大小写。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/BGPPEERINFO]] · BGP对等体信息（BGPPEERINFO）

## 使用实例

显示BGP对等体信息：

```
DSP BGPPEERINFO:;
```

```

RETCODE = 0  操作成功。

结果如下
-------------------------
VPN实例名称    地址族类型            对等体地址       多源接口名称      对等体类型    BGP版本号    对等体路由器ID     对等体状态     本地端口号    对等体端口号    当前事件            对等体上一个阶段状态  BGP会话处于当前状态的时长  发送报文数  接收报文数   发送队列报文数  对端HoldTime时间（s） 最近KeepAlive报文时间  协商HoldTime时间（s）    协商Keepalive时间（s）   接收Update报文数   接收Open报文数    接收Keepalive报文数    接收Notification报文数   接收Route Refresh报文数   发送Update报文数  发送Open报文数   发送Keepalive报文数   发送Notification报文数   发送Route Refresh报文数   本端GR能力   对端RR能力   对端4字节AS能力   对端MP能力    对端GR能力    接收路由前缀数  接收活跃路由前缀数    发送路由前缀数
_public_       IPv4uni               10.2.2.2         NULL              IBGP          4            0.0.0.0            Idle状态       0             0               IHTimerExpired      Idle状态              NULL                       0           0            0               0                     NULL                   0                        0                        0                  0                 0                       0                       0                         0                 0                0                     0                        0                         FALSE        FALSE        FALSE             FALSE         FALSE         0               0                     0
vpna           IPv4uni               10.2.2.2         NULL              IBGP          4            0.0.0.0            Idle状态       0             0               IHTimerExpired      Idle状态              NULL                       0           0            0               0                     NULL                   0                        0                        0                  0                 0                       0                       0                         0                 0                0                     0                        0                         FALSE        FALSE        FALSE             FALSE         FALSE         0               0                     0
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询BGP对等体信息（DSP-BGPPEERINFO）_49802242.md`
