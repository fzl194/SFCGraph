---
id: UDG@20.15.2@MMLCommand@DSP NDSECURITYSTATISTICS
type: MMLCommand
name: DSP NDSECURITYSTATISTICS（查询ND安全统计）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: NDSECURITYSTATISTICS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv6管理
- IPv6 ND安全
status: active
---

# DSP NDSECURITYSTATISTICS（查询ND安全统计）

## 功能

该命令用于显示ND安全统计。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [ND安全统计（NDSECURITYSTATISTICS）](configobject/UDG/20.15.2/NDSECURITYSTATISTICS.md)

## 使用实例

显示ND安全统计：

```
DSP NDSECURITYSTATISTICS:IFNAME="Ethernet65/0/8";
```

```

        RETCODE = 0  操作成功。

        结果如下
        --------
        类型                                                            NS计数    NA计数    RS计数    RA计数    REDIRECT计数

        接收的ND报文总数                                                0         0         0         0         0
        接收到的安全ND报文的总数                                        0         0         0         0         0
        接收到的没有CGA的报文的总数                                     0         0         0         0         0
        接收到的没有RSA的报文的总数                                     0         0         0         0         0
        RSA密钥长度超出的非安全ND报文的总数                             0         0         0         0         0
        接收的其他非安全ND报文的总数                                    0         0         0         0         0
        发送的ND安全报文总数                                            3         1         0         0         0
        发送前被丢弃的报文总数                                          0         0         0         0         0
        没有携带随机数的丢弃的报文总数                                  0         0         0         0         0
        没有携带时间戳的报文总数                                        0         0         0         0         0
        CGA认证失败的报文总数                                           0         0         0         0         0
        RSA签名认证失败和RSA密钥长度超出可以接受的长度范围的报文总数    0         0         0         0         0
        随机数选项认证失败的报文总数                                    0         0         0         0         0
        时间戳选项认证失败的报文总数                                    0         0         0         0         0
        RSA签名的计算和认证速率超过上限值而被丢弃的报文总数             0         0         0         0         0
        使能了严格安全模式功能的接口接收到的非安全报文总数              0         0         0         0         0
        代理丢弃的报文总数                                              0         0         0         0         0
        (结果个数 = 17)
        ---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询ND安全统计（DSP-NDSECURITYSTATISTICS）_00866013.md`
