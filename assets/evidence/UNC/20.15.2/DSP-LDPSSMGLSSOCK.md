# 显示LDP的Listen Socket信息（DSP LDPSSMGLSSOCK）

- [命令功能](#ZH-CN_CONCEPT_0000001600440549__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001600440549__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001600440549__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001600440549__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001600440549__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000001600440549__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001600440549)

该命令用于显示LDP的Listen Socket信息。

#### [注意事项](#ZH-CN_CONCEPT_0000001600440549)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001600440549)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001600440549)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_ |
| PEERID | 对等体的LSR ID | 可选必选说明：可选参数<br>参数含义：该参数用于表示对等体的LSR ID。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。<br>默认值：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000001600440549)

显示LDP的Listen Socket信息：

```
DSP LDPSSMGLSSOCK:VRFNAME="_public_";
```

```

RETCODE = 0  操作成功。

结果如下
--------
            VPN实例名称  =  _public_
         对等体的LSR ID  =  10.10.10.10
  LDP分配给Socket的编号  =  12
  Socket分配给LDP的编号  =  12
    LDP TCP连接的源地址  =  10.10.10.3
  LDP TCP连接的目的地址  =  10.10.10.10
   TCP Socket创建的状态  =  Socket创建成功
           KeyChain状态  =  未设置Socket选项
                MD5状态  =  未设置Socket选项
               GTSM状态  =  未设置Socket选项
       Socket的备份状态  =  空闲状态
       Socket的备份类型  =  备份类型无效
       Socket备份版本号  =  0
LDP分布式整数形式的编号  =  0
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000001600440549)

| 输出项名称 | 输出项解释 |
| --- | --- |
| VPN实例名称 | 用于表示VPN实例名称。 |
| 对等体的LSR ID | 用于表示对等体的LSR ID。 |
| LDP分配给Socket的编号 | 用于表示LDP分配给Socket的编号。 |
| Socket分配给LDP的编号 | 用于表示Socket分配给LDP的编号。 |
| LDP TCP连接的源地址 | 用于表示LDP TCP连接的源地址。 |
| LDP TCP连接的目的地址 | 用于表示LDP TCP连接的目的地址。 |
| TCP Socket创建的状态 | 该参数用于表示TCP Socket创建的状态，包括：<br>- 空闲状态。<br>- 创建Socket。<br>- Socket已回复了创建。<br>- 打开Socket的发送消息的管道。<br>- 已收到发送消息管道打开的回复。<br>- 备份Socket的创建到备组件。<br>- Socket创建成功。<br>- 备份Socket的删除到备组件。<br>- 删除Socket。 |
| KeyChain状态 | 该参数用于表示KeyChain状态，包括：<br>- 未设置Socket选项。<br>- 创建设置Socket选项。<br>- 正在设置Socket选项。<br>- 设置Socket选项成功。<br>- 清除设置的Socket选项。 |
| MD5状态 | 该参数用于表示MD5状态，包括：<br>- 未设置Socket选项。<br>- 创建设置Socket选项。<br>- 正在设置Socket选项。<br>- 设置Socket选项成功。<br>- 清除设置的Socket选项。 |
| GTSM状态 | 该参数用于表示GTSM状态，包括：<br>- 未设置Socket选项。<br>- 创建设置Socket选项。<br>- 正在设置Socket选项。<br>- 设置Socket选项成功。<br>- 清除设置的Socket选项。 |
| Socket的备份状态 | 该参数用于表示Socket的备份状态标识，包括：<br>- 空闲状态。<br>- 备组件创建Socket。<br>- 备组件Socket创建成功。<br>- 备组件关闭Socket。<br>- 备组件删除Socket。<br>- 备组件打开Socket的发送消息的管道。 |
| Socket的备份类型 | 该参数用于表示Socket的备份类型标识，包括：<br>- 备份类型无效。<br>- 通过批量备份将Socket备份到备组件。<br>- 通过实时备份将Socket备份到备组件。 |
| Socket备份版本号 | 用于表示Socket备份版本号。 |
| LDP分布式整数形式的编号 | 用于表示LDP分布式整数形式的编号。 |
