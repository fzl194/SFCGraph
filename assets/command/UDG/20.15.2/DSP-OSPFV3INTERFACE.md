---
id: UDG@20.15.2@MMLCommand@DSP OSPFV3INTERFACE
type: MMLCommand
name: DSP OSPFV3INTERFACE（显示OSPFv3接口信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: OSPFV3INTERFACE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- 显示OSPFv3接口信息
status: active
---

# DSP OSPFV3INTERFACE（显示OSPFv3接口信息）

## 功能

该命令查询OSPFv3接口信息，用于查看接口下的OSPFv3相关配置信息包括接口的邻居状态、Hello包的发送配置、接口的OSPFv3网络类型等。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPFv3进程号 | 可选必选说明：可选参数<br>参数含义：OSPFv3进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| AREAID | OSPFv3区域号 | 可选必选说明：可选参数<br>参数含义：OSPFv3区域号。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |
| IFNAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@OSPFV3INTERFACE]] · OSPFv3接口配置（OSPFV3INTERFACE）

## 使用实例

显示设备OSPFv3进程号为1的所有接口的信息：

```
DSP OSPFV3INTERFACE: PROCID=1;
```

```

RETCODE = 0  操作成功。

结果如下
-------------------------
                 OSPFv3进程号  =  1
                 OSPFv3区域号  =  0.0.0.0
                     接口名称  =  Ethernet64/0/7
                        MTU值  =  1500
                       GR状态  =  正常模式
                   接口开销值  =  1
发送Hello包的Poll时间间隔（s） =  120
           指定路由器的优先级  =  1
  接口对LSA的传输延迟时间（s） =  1
    发送Hello包的时间间隔（s） =  10
       抑制接口收发OSPFv3报文  =  FALSE
             邻居重传间隔（s） =  5
                      使能MTU  =  TRUE
                 超时时间（s） =  40
                 接口网络类型  =  广播网
           邻居失效的时间（s） =  40
               备份指定路由器  =  10.2.2.2
                       实例号  =  1
                   指定路由器  =  10.1.1.1
                   高链路开销  =  0
                   低链路开销  =  1410065408
                  接口LSA数目  =  2
               邻接路由器数目  =  1
                接口LSA校验和  =  0x145f9
                 链路本地地址  =  FE80::250:56FF:FE8F:632E
                     前缀长度  =  0
                     连接协议  =  Up
                     邻居数目  =  1
                Hello包定时器  =  00:00:05
               DR本地链路地址  =  FE80::250:56FF:FE8F:632E
              BDR本地链路地址  =  FE80::250:56FF:FE8F:31FE
 当前发送报文的高32比特序列号  =  0
 当前发送报文的低32比特序列号  =  0
                     接口状态  =  DR
                  IGP隧道类型  =  空
                      使能BFD  =  FALSE
      阻塞接口动态创建BFD特性  =  FALSE
              BFD检测乘数间隔  =  3
    最小接收报文时间间隔（ms） =  200
    最小发送报文时间间隔（ms） =  200
                     认证标志  =  None
   OSPFv3自动扩容功能使能标志  =  TRUE
    OSPFv3虚Router-ID配置标志  =  TRUE
      OSPFv3配置的虚Router-ID  =  10.3.3.3
      OSPFv3生效的虚Router-ID  =  10.3.3.3
                 IPsec SA名称  =  NULL
BFD会话与接口链路状态绑定标志  =  FALSE
  阻止指定OSPFv3接口的FRR能力  =  FALSE
                 优雅迁移状态  =  关闭
（结果个数 = 1）
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-OSPFV3INTERFACE.md`
