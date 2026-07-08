# 显示LDP邻居管理的Socket信息（DSP LDPNEMGSOCKET）

- [命令功能](#ZH-CN_CONCEPT_0000001600841161__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001600841161__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001600841161__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001600841161__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001600841161__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000001600841161__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001600841161)

该命令用于显示LDP邻居管理的Socket信息。

#### [注意事项](#ZH-CN_CONCEPT_0000001600841161)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001600841161)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001600841161)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_ |

#### [使用实例](#ZH-CN_CONCEPT_0000001600841161)

显示LDP邻居管理的Socket信息：

```
DSP LDPNEMGSOCKET: VRFNAME="_public_";
```

```

RETCODE = 0  操作成功

结果如下
------------------------
VPN实例名称    LDP分配给Socket的编号    Socket分配给LDP的编号    UDP Socket的类型    LDP发送协议消息时使用的管道编号    LDP接收协议消息时使用的管道编号    UDP Socket被引用的次数      TCP Socket创建的状态    Socket的备份状态    LDP与Socket之间发生流控的标识    LDP与Socket之间发生流控的次数    Socket的备份类型    Socket备份版本号    拒绝UDP报文的数量统计     最后一次丢弃标识    最后拒绝UDP报文的时间
_public_       21                       1                        IPv4的多播Socket    524342                             1074266165                         2                           Socket创建成功          空闲状态            LDP与Socket之间未发生流控        41891                            备份类型无效        1                   0                         0                   NULL
_public_       22                       2                        IPv4的单播Socket    524344                             1074266167                         0                           Socket创建成功          空闲状态            LDP与Socket之间未发生流控        41891                            备份类型无效        1                   0                         0                   NULL
(结果个数 = 2)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000001600841161)

| 输出项名称 | 输出项解释 |
| --- | --- |
| VPN实例名称 | 用于表示VPN实例名称。 |
| LDP分配给Socket的编号 | 用于表示LDP分配给Socket的编号。 |
| Socket分配给LDP的编号 | 用于表示Socket分配给LDP的编号。 |
| UDP Socket的类型 | 该参数用于表示UDP Socket的类型，包括：<br>- IPv4的单播Socket。<br>- IPv4的多播Socket。<br>- IPv6的多播Socket。<br>- IPv6的单播Socket。 |
| LDP发送协议消息时使用的管道编号 | 用于表示LDP发送协议消息时使用的管道编号。 |
| LDP接收协议消息时使用的管道编号 | 用于表示LDP接收协议消息时使用的管道编号。 |
| UDP Socket被引用的次数 | 用于表示LDP的UDP Socket被引用的次数。 |
| TCP Socket创建的状态 | 用于表示TCP Socket创建的状态，包括：空闲状态、创建Socket、打开Socket的发送消息的管道、重新尝试创建Socket、备份Socket的创建到备组件、Socket创建成功、备份Socket的删除到备组件、删除Socket。 |
| Socket的备份状态 | 该参数用于表示Socket的备份状态，包括：<br>- 空闲状态。<br>- 备组件创建Socket。<br>- 组件打开Socket的发送消息的管道。<br>- 备组件Socket创建成功。<br>- 备组件关闭Socket。<br>- 备组件删除Socket。 |
| LDP与Socket之间发生流控的标识 | 该参数用于表示LDP与Socket之间发生流控的标识，包括：<br>- LDP与Socket之间未发生流控。<br>- LDP与Socket之间发生流控。 |
| LDP与Socket之间发生流控的次数 | 用于表示LDP与Socket之间发生流控的次数。 |
| Socket的备份类型 | 该参数用于表示Socket的备份类型，包括：<br>- 备份类型无效。<br>- 通过批量备份将Socket备份到备组件。<br>- 通过实时备份将Socket备份到备组件。 |
| Socket备份版本号 | 用于表示Socket备份版本号。 |
| 拒绝UDP报文的数量统计 | 用于表示拒绝UDP报文的数量统计。 |
| 最后一次丢弃标识 | 用于表示最后一次丢弃标识，取值为对等体的LSR ID或接口索引值。 |
| 最后拒绝UDP报文的时间 | 用于表示最后拒绝UDP报文的时间。 |
