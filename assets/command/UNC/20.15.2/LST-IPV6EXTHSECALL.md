---
id: UNC@20.15.2@MMLCommand@LST IPV6EXTHSECALL
type: MMLCommand
name: LST IPV6EXTHSECALL（查询IPv6扩展头选项安全配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IPV6EXTHSECALL
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv6管理
- IPv6扩展头选项安全配置
status: active
---

# LST IPV6EXTHSECALL（查询IPv6扩展头选项安全配置）

## 功能

该命令用于查询IPv6扩展头选项安全配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [IPv6扩展头选项安全配置（IPV6EXTHSECALL）](configobject/UNC/20.15.2/IPV6EXTHSECALL.md)

## 使用实例

查询IPv6扩展头选项安全配置：

```
LST IPV6EXTHSECALL:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
IPv6过滤配置  =  使能
(返回结果 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询IPv6扩展头选项安全配置（LST-IPV6EXTHSECALL）_00866237.md`
