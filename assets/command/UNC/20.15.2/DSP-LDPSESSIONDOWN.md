---
id: UNC@20.15.2@MMLCommand@DSP LDPSESSIONDOWN
type: MMLCommand
name: DSP LDPSESSIONDOWN（显示LDP会话Down的相关信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: LDPSESSIONDOWN
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- LDP维护
status: active
---

# DSP LDPSESSIONDOWN（显示LDP会话Down的相关信息）

## 功能

该命令用于显示LDP会话Down的相关信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PEERLDPID | 邻居LDP ID | 可选必选说明：可选参数<br>参数含义：该参数用于表示对等体的LDP标识符，格式为<LSR ID>：<标签空间>。标签空间取值： “0”表示全局标签空间。 “1”表示接口标签空间。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LDPSESSIONDOWN]] · LDP会话Down的相关信息（LDPSESSIONDOWN）

## 使用实例

显示LDP会话Down的相关信息：

```
DSP LDPSESSIONDOWN:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
       LDP会话Down的信息  =
         -----------------------------------------------------------------------------------
          PeerID                  : 192.168.1.1:0
          Socket ID               : 2
          Peer Transport Address  : 192.168.1.1
          Local Transport Address : 192.168.1.2
          Flag                    : Local
          Reason                  : Reset MPLS LDP
          Sub Reason              : -
          Down Time               : 2017-09-07 03:27:11
          Duration Time           : 0D:0H:3M:3S
         -----------------------------------------------------------------------------------
         Discovery Source      MsgType     Time            MsgID        Result  OutInterface
         -----------------------------------------------------------------------------------
         Ethernet66/0/4
                                HelloRcv    03:26:46        64582        OK
                                            03:26:51        64584        OK
                                            03:26:56        64586        OK
                                            03:27:01        64588        OK
                                            03:27:06        64590        OK
                                            03:27:10        64592        OK
                                HelloSnd    03:26:42        74           OK
                                            03:26:47        76           OK
                                            03:26:52        78           OK
                                            03:26:57        80           OK
                                            03:27:01        82           OK
                                            03:27:06        84           OK
         -----------------------------------------------------------------------------------
          MsgType           Time            MsgID           Result           OutInterface
         -----------------------------------------------------------------------------------
          MessageRcv        03:25:51        2147483781      OK
                            03:26:06        2147483782      OK
                            03:26:21        2147483783      OK
                            03:26:36        2147483784      OK
                            03:26:51        2147483785      OK
                            03:27:06        2147483786      OK
          KeepaliveSnd      03:25:51        2147483665      OK               Ethernet66/0/4
                            03:26:06        2147483666      OK               Ethernet66/0/4
                            03:26:21        2147483667      OK               Ethernet66/0/4
                            03:26:36        2147483668      OK               Ethernet66/0/4
                            03:26:51        2147483669      OK               Ethernet66/0/4
                            03:27:06        2147483670      OK               Ethernet66/0/4
         -----------------------------------------------------------------------------------
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-LDPSESSIONDOWN.md`
