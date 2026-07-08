---
id: UNC@20.15.2@MMLCommand@LST SCTPENDPOINT
type: MMLCommand
name: LST SCTPENDPOINT（查询SCTP端点）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SCTPENDPOINT
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- SCTP管理
- SCTP端点
status: active
---

# LST SCTPENDPOINT（查询SCTP端点）

## 功能

**适用NF：PGW-C、SMF**

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

- [[configobject/UNC/20.15.2/SCTPENDPOINT]] · SCTP端点（SCTPENDPOINT）

## 使用实例

查询SCTP端点：

```
LST SCTPENDPOINT: ENDPOINTNAME="sctp_ep1";
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
   IPv6地址2  =  NULL
   IPv6地址1  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SCTP端点（LST-SCTPENDPOINT）_09897324.md`
