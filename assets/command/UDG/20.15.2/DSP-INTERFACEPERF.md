---
id: UDG@20.15.2@MMLCommand@DSP INTERFACEPERF
type: MMLCommand
name: DSP INTERFACEPERF（查询逻辑口报文统计信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: INTERFACEPERF
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- DN管理
- 逻辑接口管理
- 逻辑接口统计
- 接口统计
status: active
---

# DSP INTERFACEPERF（查询逻辑口报文统计信息）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来查看接口当前运行状态和接口统计信息。在监控接口的状态或检查接口的故障原因时，可执行该命令获取接口的状态信息和统计信息。用户可以根据这些信息进行流量统计和接口的故障诊断等。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INTERFACENAME | 逻辑接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定要查询的逻辑接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@INTERFACEPERF]] · 逻辑口报文统计信息（INTERFACEPERF）

## 使用实例

以paif接口为例，查看paif1/0/0接口的状态信息和统计信息：

```
DSP INTERFACEPERF: INTERFACENAME="paif1/0/0";
```

```

RETCODE = 0  操作成功。

结果如下
--------
                                逻辑接口名称  =  paif1/0/0
                                    当前状态  =  正常
                      接收的总报文个数（包）  =  102
                      发送的总报文个数（包）  =  102
                      接收的总字节数（字节）  =  7040
                      发送的总字节数（字节）  =  7040
        前5秒内通过接口接收的包速率（包/秒）  =  2
        前5秒内通过接口发送的包速率（包/秒）  =  2
    前5秒内通过接口接收的字节速率（比特/秒）  =  1120
    前5秒内通过接口发送的字节速率（比特/秒）  =  1120
                  接收的Ipv6总报文个数（包）  =  46
                  发送的Ipv6总报文个数（包）  =  46
                  接收的Ipv6总字节数（字节）  =  3680
                  发送的Ipv6总字节数（字节）  =  3680
    前5秒内通过接口接收的Ipv6包速率（包/秒）  =  1
    前5秒内通过接口发送的Ipv6包速率（包/秒）  =  1
前5秒内通过接口接收的Ipv6字节速率（比特/秒）  =  640
前5秒内通过接口发送的Ipv6字节速率（比特/秒）  =  640
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-INTERFACEPERF.md`
