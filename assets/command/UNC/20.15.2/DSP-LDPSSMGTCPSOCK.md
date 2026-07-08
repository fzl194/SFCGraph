---
id: UNC@20.15.2@MMLCommand@DSP LDPSSMGTCPSOCK
type: MMLCommand
name: DSP LDPSSMGTCPSOCK（显示LDP的TCP Socket信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: LDPSSMGTCPSOCK
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- LDP维护
status: active
---

# DSP LDPSSMGTCPSOCK（显示LDP的TCP Socket信息）

## 功能

该命令用于显示LDP的TCP Socket信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_ |
| PEERID | 对等体的LSR ID | 可选必选说明：可选参数<br>参数含义：该参数用于表示对等体的LSR ID。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LDPSSMGTCPSOCK]] · LDP的TCP Socket信息（LDPSSMGTCPSOCK）

## 使用实例

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

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示LDP的TCP-Socket信息（DSP-LDPSSMGTCPSOCK）_00866141.md`
