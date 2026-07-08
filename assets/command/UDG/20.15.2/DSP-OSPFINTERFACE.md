---
id: UDG@20.15.2@MMLCommand@DSP OSPFINTERFACE
type: MMLCommand
name: DSP OSPFINTERFACE（显示OSPF接口信息）
nf: UDG
version: 20.15.2
verb: DSP
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
- 显示OSPF接口配置
status: active
---

# DSP OSPFINTERFACE（显示OSPF接口信息）

## 功能

该命令显示OSPF接口信息，用于显示接口下的OSPF相关配置信息包括接口的邻居状态、Hello包的发送配置、接口的OSPF网络类型等。

## 注意事项

这条命令显示的是动态数据。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPF进程号 | 可选必选说明：可选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| AREAID | 区域号 | 可选必选说明：可选参数<br>参数含义：OSPF区域号。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |
| IFNAME | 接口名 | 可选必选说明：可选参数<br>参数含义：指定特定的接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/OSPFINTERFACE]] · OSPF接口配置（OSPFINTERFACE）

## 使用实例

显示设备OSPF进程号为1的所有接口的信息：

```
DSP OSPFINTERFACE: PROCID=1;
```

```

RETCODE = 0  操作成功。

结果如下
-------------------------
                     OSPF进程号  =  1
                         区域号  =  0.0.0.0
                         接口名  =  Ethernet64/0/7
                       接口状态  =  DR
                      接口MTU值  =  1500
                     接口IP地址  =  192.168.7.1
                         GR状态  =  NA
                     接口开销值  =  1
                       认证类型  =  None
             使能Smart-discover  =  FALSE
   发送BFD包的最小时间间隔（ms） =  200
  发送Hello包的Poll时间间隔（s） =  120
               指定路由器优先级  =  1
                   本地检测倍数  =  3
                        使能BFD  =  FALSE
 P2MP网络上忽略对网络掩码的检查  =  FALSE
    接口对LSA的传输延迟时间（s） =  1
   接收BFD包的最小时间间隔（ms） =  200
              Hello报文间隔（s） =  10
        阻塞接口动态创建BFD特性  =  FALSE
          按链路创建BFD会话标志  =  FALSE
            使能BFD单臂Echo标志  =  FALSE
           抑制接口收发OSPF报文  =  FALSE
                       认证密码  =  NULL
      接口重传LSA的时间间隔（s） =  5
            发送DD报文时填MTU值  =  FALSE
                   等待时间（s） =  40
                   接口网络类型  =  广播网
                   验证字标识符  =  NULL
             邻居失效的时间（s） =  40
  MD5/HMAC-MD5/HMAC-SHA256 密码  =  NULL
                 接口不透明的ID  =  0
                   接口之前状态  =  Down
                     可达性抑制  =  FALSE
               去使能可达性抑制  =  FALSE
 禁止自动使能MPLS LDP功能标志位  =  缺省配置
                过滤所有类型LSA  =  FALSE
                     过滤7类LSA  =  FALSE
                 7类LSA过滤规则  =  空
                 7类LSA过滤名称  =  NULL
                     过滤3类LSA  =  FALSE
                 3类LSA过滤规则  =  空
                 3类LSA过滤名称  =  NULL
                     过滤5类LSA  =  FALSE
                 5类LSA过滤规则  =  空
                 5类LSA过滤名称  =  NULL
                     低链路开销  =  NULL
          使能LDP和OSPF同步功能  =  FALSE
阻止接口上运行LDP和OSPF同步功能  =  TRUE
             保持最大开销值标志  =  TRUE
     保持最大开销值时间间隔（s） =  800
             永久保持最大开销值  =  FALSE
           抑制邻居时间间隔（s） =  800
     OSPF共网段虚拟系统使能标志  =  TRUE
        OSPF虚Router-id配置标志  =  TRUE
          OSPF配置的虚Router-id  =  10.7.7.7
          OSPF生效的虚Router-id  =  10.7.7.7
  BFD会话与接口链路状态绑定标志  =  FALSE
      阻止指定OSPF接口的FRR能力  =  FALSE
                     开销值来源  =  OSPF协议
                   优雅迁移状态  =  关闭
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-OSPFINTERFACE.md`
