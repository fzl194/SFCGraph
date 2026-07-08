---
id: UNC@20.15.2@MMLCommand@LST IPV6GLOBALCONFIG
type: MMLCommand
name: LST IPV6GLOBALCONFIG（查询IPv6全局配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IPV6GLOBALCONFIG
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv6管理
- IPv6全局配置
status: active
---

# LST IPV6GLOBALCONFIG（查询IPv6全局配置）

## 功能

该命令用于查询IPv6全局配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IPV6GLOBALCONFIG]] · IPv6全局配置（IPV6GLOBALCONFIG）

## 使用实例

查询IPv6全局配置：

```
LST IPV6GLOBALCONFIG:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
      ICMPv6差错报文桶深限制  =  10
ICMPv6差错报文速率限制（ms）  =  100
             老化时间（min）  =  10
          允许IPv6黑名单报文  =  FALSE
         TOO-BIG差错报文限制  =  TRUE
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-IPV6GLOBALCONFIG.md`
