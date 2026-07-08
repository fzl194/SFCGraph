---
id: UNC@20.15.2@MMLCommand@LST OSPFINTERFACE
type: MMLCommand
name: LST OSPFINTERFACE（查询OSPF接口配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: OSPFINTERFACE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF接口配置
status: active
---

# LST OSPFINTERFACE（查询OSPF接口配置）

## 功能

该命令用于查询OSPF接口配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：可选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| AREAID | 区域标识 | 可选必选说明：可选参数<br>参数含义：OSPF区域号。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |
| IFNAME | 接口名 | 可选必选说明：可选参数<br>参数含义：指定特定的接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [OSPF接口配置（OSPFINTERFACE）](configobject/UNC/20.15.2/OSPFINTERFACE.md)

## 使用实例

查询OSPF接口配置：

```
LST OSPFINTERFACE:;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
                         进程号  =  1
                       区域标识  =  0.0.0.0
                         接口名  =  Ethernet64/0/7
               指定路由器优先级  =  1
                   接口网络类型  =  广播网
       在P2MP网络上忽略网络掩码  =  FALSE
             使能Smart-Discover  =  FALSE
             邻居失效的时间（s） =  40
    邻居发送Hello包时间间隔（s） =  10
 是否使能邻居失效定时器保守模式  =  FALSE
          重发LSA的时间间隔（s） =  5
发送Hello报文的Poll时间间隔（s） =  120
               等待超时时间（s） =  40
                     接口开销值  =  NULL
                        使能BFD  =  FALSE
   接收BFD包的最小时间间隔（ms） =  200
   发送BFD包的最小时间间隔（ms） =  200
                   本地检测倍数  =  3
        阻塞接口动态创建BFD特性  =  FALSE
    接口对LSA的传输延迟时间（s） =  1
               低链路质量Cost值  =  NULL
                     可达性抑制  =  不配置
                        使能MTU  =  FALSE
 禁止自动使能MPLS LDP功能标志位  =  缺省配置
          使能LDP和OSPF同步功能  =  FALSE
阻止接口上运行LDP和OSPF同步功能  =  TRUE
   禁止该接口接收和发送OSPF报文  =  FALSE
     OSPF共网段虚拟系统使能标志  =  FALSE
        OSPF虚Router-id配置标志  =  FALSE
          OSPF配置的虚Router-id  =  NULL
             保持最大开销值标志  =  TRUE
     保持最大开销值时间间隔（s） =  800
         永久保持最大开销值标志  =  FALSE
           抑制邻居时间间隔（s） =  800
  BFD会话与接口链路状态绑定标志  =  FALSE
      阻止指定OSPF接口的FRR能力  =  FALSE
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询OSPF接口配置（LST-OSPFINTERFACE）_00866061.md`
