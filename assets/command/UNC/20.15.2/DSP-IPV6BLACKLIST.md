---
id: UNC@20.15.2@MMLCommand@DSP IPV6BLACKLIST
type: MMLCommand
name: DSP IPV6BLACKLIST（查询IPv6黑名单统计信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: IPV6BLACKLIST
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- IPV6
status: active
---

# DSP IPV6BLACKLIST（查询IPv6黑名单统计信息）

## 功能

该命令用来查询IPv6黑名单统计信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IPV6BLACKLIST]] · IPv6黑名单统计信息（IPV6BLACKLIST）

## 使用实例

查询IPv6黑名单开关状态：

```
DSP IPV6BLACKLIST:IFNAME="Ethernet64/0/4";
```

```

RETCODE = 0  操作成功。

结果如下
--------
    FIB6 Miss事件报文统计  =  0
   TTL Exceed事件报文统计  =  0
      Too Big事件报文统计  =  0
ICMP Redirect事件报文统计  =  0
        TCP黑名单报文统计  =  0
        UDP黑名单报文统计  =  0
        TCP Reset报文统计  =  0
   目的端口不可达报文统计  =  0
           IPv6黑名单状态  =  IPv6 BlackList Packet: Deny

(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询IPv6黑名单统计信息（DSP-IPV6BLACKLIST）_50281278.md`
