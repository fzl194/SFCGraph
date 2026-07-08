# 显示LDP的TCP Socket信息（DSP LDPSSMGTCPSOCK）

- [命令功能](#ZH-CN_CONCEPT_0000001600866141__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001600866141__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001600866141__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001600866141__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001600866141__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000001600866141__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001600866141)

该命令用于显示LDP的TCP Socket信息。

#### [注意事项](#ZH-CN_CONCEPT_0000001600866141)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001600866141)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001600866141)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_ |
| PEERID | 对等体的LSR ID | 可选必选说明：可选参数<br>参数含义：该参数用于表示对等体的LSR ID。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。<br>默认值：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000001600866141)

显示LDP的TCP Socket信息：

```
DSP LDPSSMGTCPSOCK:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
                               VPN实例名称  =  _public_
                            对等体的LSR ID  =  10.10.10.10
                     LDP分配给Socket的编号  =  2
                     Socket分配给LDP的编号  =  2
           LDP发送协议消息时使用的管道编号  =  524337
           LDP接收协议消息时使用的管道编号  =  1074266162
                      TCP Socket创建的状态  =  Socket创建成功
                              KeyChain状态  =  未设置Socket选项
                                   MD5状态  =  未设置Socket选项
                                  GTSM状态  =  未设置Socket选项
                                Socket角色  =  建立LDP会话的被动方
           建立TCP连接时本地使用的传输地址  =  10.10.10.3
             建立TCP连接时本地使用的端口号  =  646
           建立TCP连接时对端使用的传输地址  =  10.10.10.10
             建立TCP连接时对端使用的端口号  =  55411
             LDP与Socket之间发生流控的标识  =  LDP与Socket之间未发生流控
             LDP与Socket之间发生流控的次数  =  0
         LDP与Socket之间最后一次流控的时间  =  NULL
     LDP与Socket之间最后一次流控解除的时间  =  NULL
                     LDP等待发送消息的长度  =  0
                     LDP等待发送消息的数量  =  0
LDP发送报文时PDU中可以存在的最大的消息个数  =  100
                          Socket关闭的标识  =  Socket未关闭
                    Socket从管道关闭的标识  =  管道未关闭
                          Socket的备份状态  =  空闲状态
                          Socket的备份类型  =  备份类型无效
                          Socket备份版本号  =  1
                           NSR关键要素标志  =  None
                   LDP分布式整数形式的编号  =  0
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000001600866141)

| 输出项名称 | 输出项解释 |
| --- | --- |
| VPN实例名称 | 用于表示VPN实例名称。 |
| 对等体的LSR ID | 用于表示对等体的LSR ID。 |
| LDP分配给Socket的编号 | 用于表示LDP分配给Socket的编号。 |
| Socket分配给LDP的编号 | 用于表示Socket分配给LDP的编号。 |
| LDP发送协议消息时使用的管道编号 | 用于表示LDP发送协议消息时使用的管道编号。 |
| LDP接收协议消息时使用的管道编号 | 用于表示LDP接收协议消息时使用的管道编号。 |
| TCP Socket创建的状态 | 该参数用于表示TCP Socket创建的状态，包括：<br>- 空闲状态。<br>- 创建Socket。<br>- Socket已回复了创建。<br>- 打开Socket的发送消息的管道。<br>- 已收到发送消息管道打开的回复。<br>- 备份Socket的创建到备组件。<br>- Socket创建成功。<br>- 备份Socket的删除到备组件。<br>- 删除Socket。 |
| KeyChain状态 | 该参数用于表示KeyChain状态，包括：<br>- 未设置Socket选项。<br>- 创建设置Socket选项。<br>- 正在设置Socket选项。<br>- 设置Socket选项成功。<br>- 清除设置的Socket选项。 |
| MD5状态 | 该参数用于表示MD5状态，包括：<br>- 未设置Socket选项。<br>- 创建设置Socket选项。<br>- 正在设置Socket选项。<br>- 设置Socket选项成功。<br>- 清除设置的Socket选项。 |
| GTSM状态 | 该参数用于表示GTSM状态，包括：<br>- 未设置Socket选项。<br>- 创建设置Socket选项。<br>- 正在设置Socket选项。<br>- 设置Socket选项成功。<br>- 清除设置的Socket选项。 |
| Socket角色 | 该参数用于表示Socket角色，包括：<br>- 建立LDP会话的主动方。<br>- 建立LDP会话的被动方。 |
| 建立TCP连接时本地使用的传输地址 | 用于表示建立TCP连接时本地使用的传输地址。 |
| 建立TCP连接时本地使用的端口号 | 用于表示建立TCP连接时本地使用的端口号。 |
| 建立TCP连接时对端使用的传输地址 | 用于表示建立TCP连接时对端使用的传输地址。 |
| 建立TCP连接时对端使用的端口号 | 用于表示建立TCP连接时对端使用的端口号。 |
| LDP与Socket之间发生流控的标识 | 该参数用于表示LDP与Socket之间发生流控的标识，包括：<br>- LDP与Socket之间未发生流控。<br>- LDP与Socket之间发生流控。 |
| LDP与Socket之间发生流控的次数 | 用于表示LDP与Socket之间发生流控的次数。 |
| LDP与Socket之间最后一次流控的时间 | 用于表示LDP与Socket之间最后一次流控的时间。 |
| LDP与Socket之间最后一次流控解除的时间 | 用于表示LDP与Socket之间最后一次流控解除的时间。 |
| LDP等待发送消息的长度 | 用于表示LDP等待发送消息的长度。 |
| LDP等待发送消息的数量 | 用于表示LDP等待发送消息的数量。 |
| LDP发送报文时PDU中可以存在的最大的消息个数 | 用于表示LDP发送报文时PDU中可以存在的最大的消息个数。 |
| Socket关闭的标识 | 该参数用于表示Socket关闭的标识，包括：<br>- Socket未关闭。<br>- Socket已关闭。 |
| Socket从管道关闭的标识 | 该参数用于表示Socket从管道关闭的标识，包括：<br>- 管道未关闭。<br>- 管道已关闭。 |
| Socket的备份状态 | 该参数用于表示Socket的备份状态，包括：<br>- 空闲状态。<br>- 备组件创建Socket。<br>- 备组件Socket创建成功。<br>- 备组件关闭Socket。<br>- 备组件删除Socket。<br>- 备组件打开Socket的发送消息的管道。 |
| Socket的备份类型 | 该参数用于表示Socket的备份类型， 包括：<br>- 备份类型无效。<br>- 通过批量备份将Socket备份到备组件。<br>- 通过实时备份将Socket备份到备组件。 |
| Socket备份版本号 | 用于表示Socket备份版本号。 |
| NSR关键要素标志 | 该参数用于表示NSR关键要素标志，包括：<br>- “None”表示无NSR要素。<br>- “Backup”表示批备未结束。<br>- “Snoop”表示侦听未结束。 |
| LDP分布式整数形式的编号 | 用于表示LDP分布式整数形式的编号。 |
