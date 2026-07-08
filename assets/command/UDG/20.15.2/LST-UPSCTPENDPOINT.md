---
id: UDG@20.15.2@MMLCommand@LST UPSCTPENDPOINT
type: MMLCommand
name: LST UPSCTPENDPOINT（查询SCTP端点）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UPSCTPENDPOINT
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- SCTP管理
- SCTP端点
status: active
---

# LST UPSCTPENDPOINT（查询SCTP端点）

## 功能

**适用NF：UPF**

此命令用于查询SCTP端点。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ENDPOINTNAME | 端点名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SCTP端点名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [SCTP端点（UPSCTPENDPOINT）](configobject/UDG/20.15.2/UPSCTPENDPOINT.md)

## 使用实例

查询SCTP端点：

```
LST UPSCTPENDPOINT: ENDPOINTNAME="sctp_ep1";
```

```

RETCODE = 0  操作成功
SCTP端点
--------
    端点名称  =  sctp_ep1
      端口号  =  3868
      IP版本  =  IPV4
   IPv4地址1  =  10.1.1.1
   IPv4地址2  =  10.1.1.2
SCTP模板名称  =  sctp_tp1
   IPv6地址1  =  NULL
   IPv6地址2  =  NULL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询SCTP端点（LST-UPSCTPENDPOINT）_97080187.md`
