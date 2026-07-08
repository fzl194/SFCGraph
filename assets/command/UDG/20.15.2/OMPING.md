---
id: UDG@20.15.2@MMLCommand@OMPING
type: MMLCommand
name: OMPING（OM Ping）
nf: UDG
version: 20.15.2
verb: OMPING
object_keyword: ''
command_category: 调测类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统管理
- 路由管理
- 网络管理
status: active
---

# OMPING（OM Ping）

## 功能

该命令用来检查OM网络平面与目标主机的网络连接状况。Ping是最常见的网络命令，通过向目标主机发送ICMP请求回显数据包，来探测目标主机是否可达、网络通信延迟以及网络丢包状况。

> **说明**
> - 最多支持10个OMPING命令同时执行。
> - 该命令在OMLB服务主节点执行，复位OMLB主节点或者OMLB发生主备倒换会终止正在执行的OMPING任务。
> - 该命令支持通过配置参数来实现长时间执行。在该场景下命令输出结果较多，建议执行命令前在MML页面启动重定向，待命令执行结束后下载重定向文件。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| IPTYPE | IP版本 | 可选必选说明：必选参数。<br>参数含义：源IP地址和目的IP地址的类型。<br>取值范围：<br>- IPV4(IPv4类型)<br>- IPV6(IPv6类型)<br>默认值：IPV4(IPv4类型)。<br>配置原则：无。 |
| SRCIPV4 | 源IPv4地址 | 可选必选说明：条件可选参数，当IP版本为IPV4时为可选参数。<br>参数含义：发送ICMP数据包时使用的源IP地址，参数为空时，将使用OM Portal浮动IP。<br>取值范围：合法的IPv4地址，且必须是OM Portal浮动IP或OMLB主节点物理IP。<br>默认值：无。<br>配置原则：可以通过执行<br>[**LST OMIP**](../代理管理/查询OM IP (LST OMIP)_76163349.md)<br>查询获得。 |
| DSTIPV4 | 目的IPv4地址 | 可选必选说明：条件必选参数，当IP版本为IPV4时为必选参数。<br>参数含义：发送ICMP数据包时使用的目的IP地址。<br>取值范围：合法的IPv4地址。<br>默认值：无。<br>配置原则：无。 |
| SRCIPV6 | 源IPv6地址 | 可选必选说明：条件可选参数，当IP版本为IPV6时为可选参数。<br>参数含义：发送ICMP数据包时使用的源IP地址，参数为空时，将使用OM Portal浮动IP。<br>取值范围：合法的IPv6地址，且必须是OM Portal浮动IP或OMLB主节点物理IP。<br>默认值：无。<br>配置原则：可以通过执行<br>[**LST OMIP**](../代理管理/查询OM IP (LST OMIP)_76163349.md)<br>查询获得。 |
| DSTIPV6 | 目的IPv6地址 | 可选必选说明：条件必选参数，当IP版本为IPV6时为必选参数。<br>参数含义：发送ICMP数据包时使用的目的IP地址。<br>取值范围：合法的IPv6地址。<br>默认值：无。<br>配置原则：无。 |
| PKTSIZE | 报文字节数 | 可选必选说明：可选参数。<br>参数含义：发送ICMP数据包的大小，不包含IP和ICMP报文头。单位为字节。<br>取值范围：28~65507。<br>默认值：56。<br>配置原则：无。 |
| PKTCOUNT | 发包数 | 可选必选说明：可选参数。<br>参数含义：发送ICMP数据包的数量。如果在发送完所有数据包之前，命令耗时达到总超时时间，命令会提前终止。<br>取值范围：1~86400。<br>默认值：5。<br>配置原则：无。 |
| INTERVAL | 报文间隔（s） | 可选必选说明：可选参数。<br>参数含义：发送ICMP数据包时，相邻两个数据包发送的时间间隔。参数单位为秒。<br>取值范围：1~10。<br>默认值：1。<br>配置原则：无。 |
| TIMEOUT | 命令总超时时间（s） | 可选必选说明：可选参数。<br>参数含义：该参数用于控制命令执行总时长。如果该参数所指定的时长到达之前发送完所有的数据包，命令会提前终止。参数单位为秒。<br>取值范围：5~86400。<br>默认值：300。<br>配置原则：无。 |
| TTL | TTL值 | 可选必选说明：可选参数。<br>参数含义：该参数用于设置ICMP数据包的TTL值。<br>取值范围：1~255。<br>默认值：255。<br>配置原则：无。 |

## 使用实例

执行OMPING命令，查看OM Portal浮动IP与目的IP之间的网络通信状况：

```
%%OMPING: IPTYPE=IPV4, DSTIPV4="192.168.10.1", PKTCOUNT=3;%%
RETCODE = 99999 实时上报成功

仍有后续报告输出
---    END

%%OMPING: IPTYPE=IPV4, DSTIPV4="192.168.10.1", PKTCOUNT=3;%%
RETCODE = 99999  实时上报成功

PING 192.168.10.1: 56 字节

仍有后续报告输出
---    END

%%OMPING: IPTYPE=IPV4, DSTIPV4="192.168.10.1", PKTCOUNT=3;%%
RETCODE = 99999 实时上报成功

答复从 192.168.10.1: 字节数=64 顺序号=1 生存时间=64 往返时间=10 毫秒

仍有后续报告输出
---    END

%%OMPING: IPTYPE=IPV4, DSTIPV4="192.168.10.1", PKTCOUNT=3;%%
RETCODE = 99999 实时上报成功

答复从 192.168.10.1: 字节数=64 顺序号=2 生存时间=64 往返时间=10 毫秒

仍有后续报告输出
---    END

%%OMPING: IPTYPE=IPV4, DSTIPV4="192.168.10.1", PKTCOUNT=3;%%
RETCODE = 99999 实时上报成功

答复从 192.168.10.1: 字节数=64 顺序号=3 生存时间=64 往返时间=10 毫秒

仍有后续报告输出
---    END

%%OMPING: IPTYPE=IPV4, DSTIPV4="192.168.10.1", PKTCOUNT=3;%%
RETCODE = 0 操作成功

--- 192.168.10.1 ping 统计 ---
    发送包数: 3
    接收包数: 3
    丢包率：  0%
    执行时长：3020 毫秒
    往返时间 最小/平均/最大：10/10/10 毫秒

共有6个报告
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/OM-Ping（OMPING）_14068638.md`
