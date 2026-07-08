---
id: UNC@20.15.2@MMLCommand@DSP RAWIPSTATISTIC
type: MMLCommand
name: DSP RAWIPSTATISTIC（查询RawIP报文统计）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: RAWIPSTATISTIC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IP协议统计
- RawIP报文统计
status: active
---

# DSP RAWIPSTATISTIC（查询RawIP报文统计）

## 功能

该命令用于查看RawIP报文统计信息。

RawIP报文统计信息主要分为发送和接收两大部分。

OSPF、ICMP报文封装在RawIP报文中进行发送。因此，例如当进行ping操作时，可以通过查看本机收发RawIP报文的数量，判断是否由于RawIP报文收发不正常而导致网络异常。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPVERSION | IP版本 | 可选必选说明：可选参数<br>参数含义：该参数用于指定RawIP报文统计的IP版本。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPv4：IPv4协议族。<br>- IPv6：IPv6协议族。<br>默认值：IPv4 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@RAWIPSTATISTIC]] · RawIP报文统计（RAWIPSTATISTIC）

## 使用实例

显示当前系统的RawIP报文统计：

```
DSP RAWIPSTATISTIC:;
```

```

        RETCODE = 0  操作成功

        结果如下
        ------------------------
                       接收报文计数  =  22
        接收报文PCB缓存查询失败计数  =  22
                       发送报文计数  =  0
        (结果个数 = 1)
        ---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-RAWIPSTATISTIC.md`
