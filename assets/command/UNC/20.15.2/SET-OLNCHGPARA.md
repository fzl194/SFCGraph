---
id: UNC@20.15.2@MMLCommand@SET OLNCHGPARA
type: MMLCommand
name: SET OLNCHGPARA（配置在线计费全局参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: OLNCHGPARA
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 对新用户生效
is_dangerous: false
max_records: 1
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 在线计费
- 在线计费参数管理
- 在线计费参数
status: active
---

# SET OLNCHGPARA（配置在线计费全局参数）

## 功能

**适用NF：PGW-C、SMF**

该命令用于配置在线计费参数。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为1。
- 当前版本不支持RPTLVLSID设置为REQBYRG。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | RPTLVLSID | IPV6IFID |
| --- | --- | --- |
| 初始值 | REQBYRGSID | INTERFACE_ID_EMPTY |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RPTLVLSID | Reporting Level为SID时的配额申请方式 | 可选必选说明：可选参数<br>参数含义：该字段用于指定Reporting Level为SID时，在线计费配额的申请和使用方式。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- REQBYRGSID：UNC按RG和SID的组合通过MSCC AVP申请配额；OCS按RG和SID的组合通过MSCC AVP下发配额；UNC上对应SID的业务独享OCS为该SID下发的配额，并按RG和SID的组合通过MSCC AVP上报使用的配额。<br>- REQBYRG：UNC按RG通过MSCC AVP申请配额；OCS按RG通过MSCC AVP下发配额；UNC上属于该RG不同SID的业务共享使用OCS为该RG下发的配额，UNC按RG通过MSCC AVP上报配额，在MSCC AVP中通过SID和USU AVP区分不同SID的配额。<br>默认值：无<br>配置原则：当前版本不支持RPTLVLSID设置为REQBYRG |
| IPV6IFID | CCR消息中用户IPv6地址Interface Identifier的填充方式 | 可选必选说明：可选参数<br>参数含义：该字段用于指定CCR消息中用户IPv6地址Interface Identifier的填充方式。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- INTERFACE_ID_EMPTY：IPv6地址Interface Identifier填写全0。<br>- INTERFACE_ID_REAL：IPv6地址Interface Identifier填写真实值。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/OLNCHGPARA]] · 在线计费全局参数配置（OLNCHGPARA）

## 使用实例

为使用相同RG不同SID的业务设置配额申请方式和使用方式，按照RG申请配额，按照RG和SID上报配额：

```
SET OLNCHGPARA: RPTLVLSID=REQBYRG;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/配置在线计费全局参数（SET-OLNCHGPARA）_09896981.md`
