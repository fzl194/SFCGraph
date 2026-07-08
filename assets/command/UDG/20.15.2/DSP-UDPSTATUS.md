---
id: UDG@20.15.2@MMLCommand@DSP UDPSTATUS
type: MMLCommand
name: DSP UDPSTATUS（查询UDP状态）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: UDPSTATUS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- SOCKET
status: active
---

# DSP UDPSTATUS（查询UDP状态）

## 功能

该命令用于查看当前UDP连接状态。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPVERSION | IP版本 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UDP socket实例的IP版本。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPv4：IPv4协议族。<br>- IPv6：IPv6协议族。<br>默认值：IPv4 |
| LOCALADDRESS | 本端地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPv4”时为可选参数。<br>参数含义：该参数用于指定本端地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| REMOTEADDRESS | 远端地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPv4”时为可选参数。<br>参数含义：该参数用于指定远端地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| LOCALPORT | 本端端口号 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPv4” 或 “IPv6”时为可选参数。<br>参数含义：该参数用于指定本端端口号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |
| REMOTEPORT | 远端端口号 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPv4” 或 “IPv6”时为可选参数。<br>参数含义：该参数用于指定远端端口号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |
| APPCID | APP组件CID | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPv4” 或 “IPv6”时为可选参数。<br>参数含义：该参数用于指定APP组件CID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |
| SOCKETFD | Socket实例ID | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPv4” 或 “IPv6”时为可选参数。<br>参数含义：该参数用于指定Socket实例ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～2147418111。<br>默认值：无 |
| LOCALV6ADDRESS | IPv6本端地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPv6”时为可选参数。<br>参数含义：该参数用于指定IPv6本端地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无 |
| REMOTEV6ADDRESS | IPv6远端地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IPVERSION”配置为“IPv6”时为可选参数。<br>参数含义：该参数用于指定IPv6远端地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UDPSTATUS]] · UDP状态（UDPSTATUS）

## 使用实例

- 显示当前系统IPv4协议下的UDP状态信息：
  ```
  DSP UDPSTATUS: APPCID="0x8093042C", SOCKETFD=1;
  ```
  ```

          RETCODE = 0  操作成功

          结果如下
          ----------------------
            APP组件CID  =  0x8093042C
          Socket实例ID  =  1
              本端地址  =  0.0.0.0
              远端地址  =  0.0.0.0
            本端端口号  =  6000
            远端端口号  =  0
          (结果个数 = 1)
          ---    END
  ```
- 显示当前系统IPv6协议下的UDP状态信息：
  ```
  DSP UDPSTATUS: IPVERSION=IPv6, APPCID="0x80740028", SOCKETFD=10;
  ```
  ```

          RETCODE = 0  操作成功

          结果如下
          ----------------------
            APP组件CID  =  0x80740028
          Socket实例ID  =  10
          IPv6本端地址  =  ::
          IPv6远端地址  =  2001:db8::11
            本端端口号  =  3784
            远端端口号  =  0
          (结果个数 = 1)
          ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-UDPSTATUS.md`
