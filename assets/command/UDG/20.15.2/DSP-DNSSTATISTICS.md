---
id: UDG@20.15.2@MMLCommand@DSP DNSSTATISTICS
type: MMLCommand
name: DSP DNSSTATISTICS（查询DNS报文统计计数）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: DNSSTATISTICS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 域名管理
- DNS报文统计
status: active
---

# DSP DNSSTATISTICS（查询DNS报文统计计数）

## 功能

该命令用于显示DNS报文统计，用户可以通过此命令的显示信息，查看到接收和发送的DNS报文的统计信息，掌握各类型报文的具体统计数据。其中，A类RR中记录的是根据域名显示到的IPv4地址，AAAA类RR中记录的是根据域名显示到的IPv6地址。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@DNSSTATISTICS]] · DNS报文统计计数（DNSSTATISTICS）

## 使用实例

显示DNS报文统计：

```
DSP DNSSTATISTICS:;
```

```

        RETCODE = 0  操作成功。

        结果如下
        --------
                        收到报文个数  =  0
                        发出报文个数  =  0
                        丢弃报文个数  =  0
                 接收报文中A类RR个数  =  0
              接收报文中AAAA类RR个数  =  0
             接收报文中CNAME类RR个数  =  0
               接收报文中PTR类RR个数  =  0
          接收报文中不识别RR类型个数  =  0
          发送报文中正向查询报文个数  =  0
          发送报文中反向查询报文个数  =  0
             发送报文中A类查询块个数  =  0
          发送报文中AAAA类查询块个数  =  0
           发送报文中PTR类查询块个数  =  0
        (结果个数 = 1)

        ---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-DNSSTATISTICS.md`
