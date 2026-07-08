---
id: UDG@20.15.2@MMLCommand@DSP IFCOUNTERS
type: MMLCommand
name: DSP IFCOUNTERS（查询接口统计信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: IFCOUNTERS
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 接口管理
- 接口统计信息
status: active
---

# DSP IFCOUNTERS（查询接口统计信息）

## 功能

在监控接口的状态或检查接口的故障原因时，可执行该命令获取接口的统计信息。用户可以根据这些信息进行流量统计和接口的故障诊断等。

若不指定IFNAME参数时，则显示所有接口的统计信息；若指定IFNAME参数时，则可以显示指定接口的统计信息。

## 注意事项

- 该命令执行后立即生效。
- 若该功能未开启，可以使用**[MOD INTERFACE](../接口配置/修改接口（MOD INTERFACE）_50281674.md)**命令，将IFSTATIENABLE字段设置为TRUE，即可开启该功能。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：可选参数<br>参数含义：该参数用于设置获取统计计数的接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [接口统计信息（IFCOUNTERS）](configobject/UDG/20.15.2/IFCOUNTERS.md)

## 使用实例

显示接口的统计信息：

```
DSP IFCOUNTERS:IFNAME="Ethernet64/0/3";
```

```
RETCODE = 0  操作成功

结果如下
--------
                 接口名  =  Ethernet64/0/3
 接收字节速率（byte/s）  =  0
    接收报文速率（pps）  =  0
接收方向带宽利用率（%）  =  0.00%
   接收字节总数（byte）  =  0
           接收报文总数  =  0
       接收单播报文总数  =  0
       接收组播报文总数  =  0
       接收广播报文总数  =  0
 发送字节速率（byte/s）  =  0
    发送报文速率（pps）  =  0
发送方向带宽利用率（%）  =  0.00%
   发送字节总数（byte）  =  0
           发送报文总数  =  0
       发送单播报文总数  =  0
       发送组播报文总数  =  0
       发送广播报文总数  =  0
       发送丢弃报文总数  =  0
       发送错误报文总数  =  0
(结果个数 = 1)
---   END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询接口统计信息（DSP-IFCOUNTERS）_00841557.md`
