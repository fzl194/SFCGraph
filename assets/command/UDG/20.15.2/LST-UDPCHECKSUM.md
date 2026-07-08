---
id: UDG@20.15.2@MMLCommand@LST UDPCHECKSUM
type: MMLCommand
name: LST UDPCHECKSUM（查询UDP报文是否携带checksum）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UDPCHECKSUM
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 信令QOS控制
- UDP Checksum控制
status: active
---

# LST UDPCHECKSUM（查询UDP报文是否携带checksum）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来查询系统发送的UDP报文是否携带checksum。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/UDPCHECKSUM]] · UDP报文是否携带checksum（UDPCHECKSUM）

## 使用实例

查询系统发送的UDP报文是否携带checksum：

```
LST UDPCHECKSUM:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
UDP Type     Checksum 开关

L2TP-CTRL    使能       
L2TP-DATA    不使能           
PFCP         使能          
(结果个数 = 3)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询UDP报文是否携带checksum（LST-UDPCHECKSUM）_82837688.md`
