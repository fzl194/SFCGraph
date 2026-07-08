---
id: UNC@20.15.2@MMLCommand@LST UDPCHECKSUM
type: MMLCommand
name: LST UDPCHECKSUM（查询UNC发送的UDP报文是否携带checksum）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UDPCHECKSUM
command_category: 查询类
applicable_nf:
- PGW-C
- GGSN
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- 发送UDP报文是否携带校验和
status: active
---

# LST UDPCHECKSUM（查询UNC发送的UDP报文是否携带checksum）

## 功能

**适用NF：PGW-C、GGSN、SMF**

该命令用来查询UNC发送的UDP报文是否携带checksum。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@UDPCHECKSUM]] · UNC发送的UDP报文是否携带checksum（UDPCHECKSUM）

## 使用实例

查询UNC发送的UDP报文是否携带checksum：

```
%%LST UDPCHECKSUM:;%%
RETCODE = 0  操作成功

结果如下
--------
    UDP Type = DHCP
Checksum开关 = 不使能   
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-UDPCHECKSUM.md`
