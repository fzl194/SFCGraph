---
id: UDG@20.15.2@MMLCommand@DSP UPSCTPASSOC
type: MMLCommand
name: DSP UPSCTPASSOC（显示SCTP耦联信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: UPSCTPASSOC
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- SCTP管理
- SCTP偶联
status: active
---

# DSP UPSCTPASSOC（显示SCTP耦联信息）

## 功能

**适用NF：UPF**

此命令用于显示SCTP耦联信息。

当建立SCTP协议耦联后，需要查看耦联具体信息时执行此命令。

## 注意事项

- 该命令相关的功能当前版本暂不支持。
- 命令显示信息包含耦联源端和目的端的ip地址和端口号以及耦联的实时状态。
- 命令不指定本端主IP地址和对端主IP地址时，将显示本地设备建立的所有SCTP耦联信息。
- 查询前需先使用ADD UPSCTPASSOC命令添加指定的SCTP耦联测量对象。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPVERSION | IP地址类型 | 可选必选说明：可选参数<br>参数含义：SCTP耦联IP地址类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPV4：IPv4地址类型。<br>- IPV6：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| LOCALIPV4 | 本端IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：该参数用于指定SCTP耦联本端主IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| PEERIPV4 | 对端IPv4地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV4”时为必选参数。<br>参数含义：该参数用于指定SCTP耦联对端主IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| LOCALIPV6 | 本端IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：该参数用于指定SCTP耦联本端主IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| PEERIPV6 | 对端IPv6地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPV6”时为必选参数。<br>参数含义：该参数用于指定SCTP耦联对端主IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@UPSCTPASSOC]] · SCTP耦联信息（UPSCTPASSOC）

## 使用实例

- 查询本端IP地址为10.1.1.1，对端地址为10.1.1.2的SCTP耦联信息：
  ```
  DSP UPSCTPASSOC: IPVERSION=IPV4, LOCALIPV4="10.1.1.1", PEERIPV4="10.1.1.2";
  ```
  ```

  RETCODE = 0  操作成功
  SCTP耦联
  --------
     耦联索引  =  1
   本端端口号  =  13400
  本端IP地址1  =  10.1.1.1
  本端IP地址2  =  0.0.0.0
   对端端口号  =  3868
  对端IP地址1  =  10.1.1.2
  对端IP地址2  =  0.0.0.0
     管理状态  =  未锁定
     操作状态  =  禁止
  (结果个数 = 1)
  ---    END
  ```
- 查询全部SCTP耦联信息：
  ```
  DSP UPSCTPASSOC:;
  ```
  ```

  RETCODE = 0  操作成功
  SCTP耦联
  --------
  耦联索引  本端端口号  本端IP地址1  本端IP地址2  对端端口号  对端IP地址1  对端IP地址2  管理状态  操作状态  
  1         13400       10.1.1.1     0.0.0.0      3868        10.1.1.2     0.0.0.0      未锁定    禁止      
  2         13400       10.1.1.3     0.0.0.0      3868        10.1.1.4     0.0.0.0      未锁定    禁止      
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-UPSCTPASSOC.md`
