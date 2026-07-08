---
id: UNC@20.15.2@MMLCommand@DSP SLADBGDATA
type: MMLCommand
name: DSP SLADBGDATA（查询SLA调试数据）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SLADBGDATA
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- Ping和Tracert调测
status: active
---

# DSP SLADBGDATA（查询SLA调试数据）

## 功能

该命令用于查询SLA调试数据。

## 注意事项

该命令最多返回8K字节，当数据内容过多时，可能会显示不全。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TYPE | 调试数据类型 | 可选必选说明：必选参数<br>参数含义：该参数用来指定SLA的调试数据类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ICMP：SLA的ICMP调试数据。<br>- TRACE：SLA的trace调试数据。<br>- LSPPING：SLA的LSP ping调试数据。<br>- LSPTRACE：SLA的LSP trace调试数据。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SLADBGDATA]] · SLA调试数据（SLADBGDATA）

## 使用实例

- 查询SLA的ICMP调试数据：
  ```
  DSP SLADBGDATA: TYPE=ICMP;
  ```
  ```
      RETCODE = 0  操作成功。

      结果如下
      --------
      查询结果信息  =
      PingTime                 AddrType  DestAddr            SourAddr      VrfIndex      IfIndex       PacketCount  PacketSize   Interval   Timeout      Ttl     Tos     SessionId    OperationType     MsgId
      2017-04-01 15:09:35.532  1         10.137.144.1        10.0.0.1       0             0             5            56           500        2000         255     255     64           0                 64
      (结果个数 = 1)
      ---    END
  ```
- 查询SLA的trace调试数据：
  ```
  DSP SLADBGDATA: TYPE=TRACE;
  ```
  ```
      RETCODE = 0  操作成功。

      结果如下
      --------
      查询结果信息  =
      TraceTime                 AddrType  DestAddr      SourAddr   VrfIndex   PacketSize   Timeout  InitTtl  MaxTtl  SessionId  OperationType  MsgId
      2017-04-01 15:13:26.330   1         10.137.144.1  10.0.0.1   0          12           5000     1        30      64         0              64
      (结果个数 = 1)
      ---    END
  ```
- 查询SLA的LSP ping调试数据：
  ```
  DSP SLADBGDATA: TYPE=LSPPING;
  ```
  ```
      RETCODE = 0  操作成功。

      结果如下
      --------
      查询结果信息  =
      PingTime                 DestAddr         MaskLen   LspType   ReplyMode  SourAddr         PacketCount   PacketSize   Interval   Timeout      Ttl   Exp   SessionId   OperationType   MsgId
      2017-04-01 15:10:45.817  10.137.144.1     32        0         2          0.0.0.0          5             100          2000       2000         64    0     64          0               64
      (结果个数 = 1)
      ---    END
  ```
- 查询SLA的LSP trace调试数据：
  ```
  DSP SLADBGDATA: TYPE=LSPTRACE;
  ```
  ```
      RETCODE = 0  操作成功。

      结果如下
      --------
      查询结果信息  =
      TraceTime                DestAddr         MaskLen   LspType   ReplyMode  SourAddr         PacketSize    Timeout      InitTtl    MaxTtl      Exp   SessionId   OperationType   MsgId
      2017-04-01 15:12:30.716  10.137.144.1     32        0         2          0.0.0.0          0             2000         0          255         0     64          0               64
      (结果个数 = 1)
      ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SLADBGDATA.md`
