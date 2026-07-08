---
id: UNC@20.15.2@MMLCommand@DSP OSPFV3BFD
type: MMLCommand
name: DSP OSPFV3BFD（查询OSPFv3 BFD状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: OSPFV3BFD
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- 查询OSPFv3 BFD状态
status: active
---

# DSP OSPFV3BFD（查询OSPFv3 BFD状态）

## 功能

该命令用于显示OSPFv3 BFD信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPFv3进程号 | 可选必选说明：可选参数<br>参数含义：OSPFv3进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| NBRROUTERID | 邻居路由器标识 | 可选必选说明：可选参数<br>参数含义：邻居路由器标识。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |
| AREAID | OSPFv3区域号 | 可选必选说明：可选参数<br>参数含义：OSPFv3区域号。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |
| IFNAME | 接口名 | 可选必选说明：可选参数<br>参数含义：接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/OSPFV3BFD]] · OSPFv3 BFD状态（OSPFV3BFD）

## 使用实例

在设备上建立OSPFv3进程1，建立邻居并配置BFD，然后查询：

```
DSP OSPFV3BFD: PROCID=1;
```

```

RETCODE = 0  操作成功。

结果如下
-------------------------
                                    OSPFv3进程号  =  1
                                    OSPFv3区域号  =  0.0.0.0
                                          接口名  =  Ethernet64/0/5
                                  邻居路由器标识  =  192.168.5.2
                                         BFD状态  =  Up
                                    本地IPv6地址  =  FE80::250:56FF:FE01:308
                                    远端IPv6地址  =  FE80::250:56FF:FE02:308
                                      路由器标识  =  192.168.5.1
                                          实例号  =  0
    BFD Module优先使用的BFD最小接收报文间隔（ms） =  200
    BFD Module优先使用的BFD最小发送报文间隔（ms） =  200
                    BFD Module优先使用的检测倍数  =  3
 OSPFv3 Module优先使用的BFD最小接收报文间隔（ms） =  200
 OSPFv3 Module优先使用的BFD最小发送报文间隔（ms） =  200
                 OSPFv3 Module优先使用的检测倍数  =  3
                  配置的BFD最小接收报文间隔（ms） =  200
                  配置的BFD最小发送报文间隔（ms） =  200
                                  配置的检测倍数  =  3
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-OSPFV3BFD.md`
