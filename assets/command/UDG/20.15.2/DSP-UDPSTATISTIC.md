---
id: UDG@20.15.2@MMLCommand@DSP UDPSTATISTIC
type: MMLCommand
name: DSP UDPSTATISTIC（查询UDP报文统计）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: UDPSTATISTIC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IP协议统计
- UDP报文统计
status: active
---

# DSP UDPSTATISTIC（查询UDP报文统计）

## 功能

该命令用于查看UDP连接报文统计信息。

UDP连接报文统计信息主要分为发送和接收两大部分。BFD、LDP、TracerRoute等报文封装在UDP报文中进行发送。因此，例如当以上报文的发送出现异常时，可以通过查看本机收发UDP报文的数量，判断是否由于UDP报文收发不正常而导致网络异常。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPVERSION | IP版本 | 可选必选说明：可选参数<br>参数含义：该参数表示当前显示的统计信息的IP版本。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPv4：IPv4协议族。<br>- IPv6：IPv6协议族。<br>默认值：IPv4 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@UDPSTATISTIC]] · UDP报文统计（UDPSTATISTIC）

## 使用实例

显示当前系统IPv4协议的UDP报文相关统计信息：

```
DSP UDPSTATISTIC:;
```

```

        RETCODE = 0  操作成功

        结果如下
        -------------------------
                                          收到的UDP报文总数  =  0
                                   收到的校验和错误报文个数  =  0
           收到的UDP报文中长度小于UDP报文头部长度的报文个数  =  0
              收到的UDP报文中数据长度大于报文长度的报文个数  =  0
        收到的UDP报文中报文指定的端口无SOCKET侦听的报文个数  =  0
                              收到的UDP报文中广播报文的个数  =  0
          收到的UDP报文中因SOCKET被占用而无法处理的报文个数  =  0
                       收到的UDP报文中缺少PCB缓存的报文个数  =  0
                                          发送的UDP报文总数  =  0
                                                     IP版本  =  IPv4
        (结果个数 = 1)
        ---   END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-UDPSTATISTIC.md`
