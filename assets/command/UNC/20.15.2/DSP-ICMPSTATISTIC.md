---
id: UNC@20.15.2@MMLCommand@DSP ICMPSTATISTIC
type: MMLCommand
name: DSP ICMPSTATISTIC（查询ICMP报文统计）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: ICMPSTATISTIC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IP协议统计
- ICMP报文统计
status: active
---

# DSP ICMPSTATISTIC（查询ICMP报文统计）

## 功能

该命令用于查看ICMP报文统计信息。统计值可以通过RTR IPSTATISTIC命令清除。

ICMP（Internet Control Message Protocol）是一个差错报告机制，通常被IP层或更高层协议（TCP或UDP）使用。ICMP报文被封装在IP数据报内部，作为IP数据报的数据部分通过互联网传递。

当数据报产生差错时，ICMP只向数据报的源端报告这个差错，即不会去纠正这个差错也不会通知中间的网络设备。

通过查看DSP ICMPSTATISTIC命令的显示信息，可以查看到接收和发送的ICMP错误报文、echo报文和echo reply报文的统计信息。

例如在进行Ping和Trace-route操作时，可以通过在路由设备上查看DSP ICMPSTATISTIC命令的显示信息，判断本设备发送和接收的报文总数是否正确。

不指定参数时，查询所有接口的统计信息；当指定参数时，可以查询指定接口的统计信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：可选参数<br>参数含义：该参数表示对应接口的ICMP报文统计。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ICMPSTATISTIC]] · ICMP报文统计（ICMPSTATISTIC）

## 使用实例

显示当前系统的IP报文统计信息：

```
DSP ICMPSTATISTIC:;
```

```

        RETCODE = 0  操作成功

        结果如下
        -------------------------
          收到的ICMP报文中格式不正确的报文个数  =  0
          收到的ICMP报文中校验码错误的报文个数  =  0
                      收到的ICMP应答报文的个数  =  119
                收到的ICMP目的不可达报文的个数  =  9
                收到的ICMP源地址抑制报文的个数  =  0
                            发送的ICMP报文总数  =  0
                    收到的ICMP重定向报文的个数  =  0
                  收到的ICMP回显应答报文的个数  =  0
              收到的ICMP头部损坏差错报文的个数  =  0
                      收到的ICMP时间戳报文个数  =  0
                    收到的ICMP信息请求报文个数  =  0
                    收到的ICMP掩码请求报文个数  =  0
                    收到的ICMP掩码请求回应报文  =  0
                        收到的ICMP超时差错报文  =  0
                    发出的ICMP回显请求报文个数  =  0
            发送的ICMP目的不可达差错报文的个数  =  49
                  发送的ICMP源地址抑制报文个数  =  0
                    发送的ICMP重定向报文的个数  =  0
                        发送的ICMP回显应答报文  =  99
              发送的ICMP头部损坏差错报文的个数  =  0
                      发送的ICMP时间戳报文个数  =  0
                    发送的ICMP信息请求报文个数  =  0
                    发送的ICMP掩码请求报文个数  =  0
                    发送的ICMP掩码应答报文个数  =  0
                        发送的ICMP超时报文个数  =  0
                            接收的ICMP报文总数  =  108
        接收到的ICMP报文中首部不正确的报文个数  =  20
          发送的ICMP报文中格式不正确的报文个数  =  0
        (结果个数 = 1)
        ---   END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-ICMPSTATISTIC.md`
