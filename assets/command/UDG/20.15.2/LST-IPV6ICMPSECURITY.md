---
id: UDG@20.15.2@MMLCommand@LST IPV6ICMPSECURITY
type: MMLCommand
name: LST IPV6ICMPSECURITY（查询IPv6安全配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: IPV6ICMPSECURITY
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv6管理
- IPv6安全配置
status: active
---

# LST IPV6ICMPSECURITY（查询IPv6安全配置）

## 功能

该命令用于查询IPv6安全配置。

若不指定IFNAME参数时，则显示所有接口的IPv6安全配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [IPv6安全配置（IPV6ICMPSECURITY）](configobject/UDG/20.15.2/IPV6ICMPSECURITY.md)

## 使用实例

查询IPv6安全配置：

```
LST IPV6ICMPSECURITY:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
  发送还是接收  =  发送报文
    配置的类型  =  报文类型
      报文类型  =  TTL超时
收发报文的TYPE  =  3
收发报文的CODE  =  0
          开关  =  使能
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询IPv6安全配置（LST-IPV6ICMPSECURITY）_49961394.md`
