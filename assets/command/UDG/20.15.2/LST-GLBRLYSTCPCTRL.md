---
id: UDG@20.15.2@MMLCommand@LST GLBRLYSTCPCTRL
type: MMLCommand
name: LST GLBRLYSTCPCTRL（查询媒体中继全局业务TCP控制）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: GLBRLYSTCPCTRL
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继全局业务TCP控制
status: active
---

# LST GLBRLYSTCPCTRL（查询媒体中继全局业务TCP控制）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询媒体中继全局业务TCP控制。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@GLBRLYSTCPCTRL]] · 媒体中继全局业务TCP控制（GLBRLYSTCPCTRL）

## 使用实例

假如需要查询媒体中继全局业务TCP控制，则命令如下：

```
LST GLBRLYSTCPCTRL:;
```

```

RETCODE = 0  操作成功
结果如下
------------------------
      IPv4最大报文段长度  =  1380
    重新发送总时间（秒）  =  5
发送缓冲区大小（千字节）  =  80
接收缓冲区大小（千字节）  =  20
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-GLBRLYSTCPCTRL.md`
