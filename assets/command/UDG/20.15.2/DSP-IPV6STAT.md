---
id: UDG@20.15.2@MMLCommand@DSP IPV6STAT
type: MMLCommand
name: DSP IPV6STAT（查询IPv6统计计数）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: IPV6STAT
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv6管理
- IPv6统计计数
status: active
---

# DSP IPV6STAT（查询IPv6统计计数）

## 功能

该命令用于显示IPv6报文统计计数。

若不指定IFNAME参数时，则显示所有接口的IPv6报文统计计数。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：可选参数<br>参数含义：该参数用于显示接口名 。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IPV6STAT]] · IPv6统计计数（IPV6STAT）

## 使用实例

显示IPv6报文统计计数：

```
DSP IPV6STAT:IFNAME="Ethernet65/0/8";
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
                 发送报文总数 = 0
             本地发送报文总数 = 0
     使用Raw Socket发送的报文 = 0
       分片成功的IPv6报文总数 = 0
       分片失败的IPv6报文总数 = 0
                   转发报文数 = 0
               丢弃的发送报文 = 0
                       分片数 = 0
                 发送组播报文 = 0
                 接收报文总数 = 0
               收到组播报文数 = 0
         跳数超出限制报文总数 = 0
               收到的超大报文 = 0
             收到地址错误报文 = 0
 实际长度过小而丢弃的报文总数 = 0
           收到的分片报文总数 = 0
             重组超时报文总数 = 0
           收到的本地主机报文 = 0
             收到的头错误报文 = 0
           收到的路由错误报文 = 0
           收到的协议错误报文 = 0
           收到的选项错误报文 = 0
             重组成功报文总数 = 0
         收到的逐跳选项头报文 = 0
         收到的目的选项头报文 = 0
           收到的带路由头报文 = 0
       配置过滤规则丢弃报文数 = 0
(返回结果 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-IPV6STAT.md`
