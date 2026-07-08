---
id: UDG@20.15.2@MMLCommand@LST OSPFV3INTERFACE
type: MMLCommand
name: LST OSPFV3INTERFACE（查询OSPFv3接口配置）
nf: UDG
version: 20.15.2
verb: LST
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
- OSPFv3接口配置
status: active
---

# LST OSPFV3INTERFACE（查询OSPFv3接口配置）

## 功能

该命令用于查询OSPFv3接口配置。

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

- [OSPFv3接口配置（OSPFV3INTERFACE）](configobject/UDG/20.15.2/OSPFV3INTERFACE.md)

## 使用实例

查询OSPFv3接口配置：

```
LST OSPFV3INTERFACE:;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
                  OSPFv3进程号  =  1
                  OSPFv3区域号  =  0.0.0.0
                      接口名称  =  Ethernet64/0/3
                       使能MTU  =  TRUE
                  接口网络类型  =  广播网
            邻居失效的时间（s） =  40
     发送Hello包的时间间隔（s） =  10
是否使能邻居失效定时器保守模式  =  FALSE
         重发LSA的时间间隔（s） =  5
 发送Hello包的Poll时间间隔（s） =  120
                  超时时间（s） =  40
                    接口开销值  =  1
                       使能BFD  =  FALSE
  接收BFD包的最小时间间隔（ms） =  200
  发送BFD包的最小时间间隔（ms） =  200
                  本地检测倍数  =  3
       阻塞接口动态创建BFD特性  =  FALSE
   接口对LSA的传输延迟时间（s） =  1
              指定路由器优先级  =  1
禁止该接口接收和发送OSPFv3报文  =  FALSE
                        实例号  =  0
  OSPFv3共网段虚拟系统使能标志  =  FALSE
  OSPFv3虚拟路由器标识使能标识  =  FALSE
           OSPFv3虚拟路由器标识 =  NULL
 BFD会话与接口链路状态绑定标志  =  FALSE
   阻止指定OSPFv3接口的FRR能力  =  FALSE
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询OSPFv3接口配置（LST-OSPFV3INTERFACE）_50121594.md`
