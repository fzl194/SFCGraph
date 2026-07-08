---
id: UNC@20.15.2@MMLCommand@DSP PCRFSTATUS
type: MMLCommand
name: DSP PCRFSTATUS（显示PCRF状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PCRFSTATUS
command_category: 查询类
applicable_nf:
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- PCRF Diameter连接
- PCRF状态
status: active
---

# DSP PCRFSTATUS（显示PCRF状态）

## 功能

**适用NF：PGW-C、GGSN**

此命令用来查询所有PCRF或者指定PCRF的连接状态。

## 注意事项

- 非直连（通过DRA连接）的PCRF的状态不显示。
- 如果只显示一条“Not Ready”记录，则说明此PCRF未配置Diameter链路。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PCRFNAME | PCRF主机名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定PCRF的主机名称。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，由软参BIT 150控制是否区分大小写。<br>默认值：无<br>配置原则：必须是已经通过ADD PCRF配置过的PCRF主机名称。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PCRFSTATUS]] · PCRF状态（PCRFSTATUS）

## 使用实例

- 查询指定主机名的PCRF的状态信息：
  ```
  DSP PCRFSTATUS:PCRFNAME="pcrf1";
  ```
  ```

  RETCODE = 0  操作成功。

  PCRF状态
  --------
  PCRF主机名  =  pcrf1
     POD名称  =  uncpod-0
    本端地址  =  10.10.10.11:13400
  本端子地址  =  -
    对端地址  =  10.20.20.21:3868
     Gx 状态  =  Normal
  本端主机名  =  gxlocal 
  (结果个数 = 1)
  ---    END
  ```
- 查询所有的PCRF的状态信息：
  ```
  DSP PCRFSTATUS:;
  ```
  ```

  RETCODE = 0  操作成功。

  PCRF状态
  --------
  PCRF主机名    POD名称   本端地址               本端子地址             对端地址                Gx 状态       本端主机名       
  pcrf1         uncpod-0  10.10.10.11:13400      -                      10.20.20.21:3868        Normal        gxlocal                
  pcrfsctp      uncpod-0  10.10.10.11:13400      10.10.10.12:13400      sctp1                   Abnormal      gxlocal  
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-PCRFSTATUS.md`
