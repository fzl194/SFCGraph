---
id: UDG@20.15.2@MMLCommand@LST SECPOLICYSWITCH
type: MMLCommand
name: LST SECPOLICYSWITCH（查询TCPIP报文以及应用层、黑名单、白名单防御机制使能状态）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SECPOLICYSWITCH
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- 主机防攻击
- 安全策略开关
status: active
---

# LST SECPOLICYSWITCH（查询TCPIP报文以及应用层、黑名单、白名单防御机制使能状态）

## 功能

该命令用来查询TCP/IP报文以及应用层联动、黑名单、白名单防御机制使能状态。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SECPOLICYID | 安全策略编号 | 可选必选说明：可选参数<br>参数含义：策略编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～30。<br>默认值：无 |
| SECPOLICYTYPE | 安全策略类型 | 可选必选说明：可选参数<br>参数含义：安全策略类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Tcpip：TCP/IP策略。<br>- WhiteList：白名单策略。<br>- BlackList：黑名单策略。<br>- APP：应用策略。<br>默认值：无 |
| SECPOLICYTYPEID | 安全策略类型编号 | 可选必选说明：可选参数<br>参数含义：安全策略类型编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |
| SECPOLICYENABLE | 安全策略使能标记 | 可选必选说明：可选参数<br>参数含义：协议类型。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| SUBTCPIPTYPE | TCP/IP防攻击类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SECPOLICYTYPE”配置为“Tcpip”时为必选参数。<br>参数含义：TCP/IP防攻击类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ABNORMAL：非法报文。<br>- UDPFLOOD：UDP泛洪报文。<br>- TCPSYN：TCPSYN报文。<br>- FRAGMENT：分片报文。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SECPOLICYSWITCH]] · TCPIP报文以及应用层、黑名单、白名单防御机制使能状态（SECPOLICYSWITCH）

## 使用实例

查看非法报文防御机制使能状态：

```
LST SECPOLICYSWITCH: SECPOLICYID=1, SECPOLICYTYPE=BlackList, SECPOLICYTYPEID=0;
```

```
RETCODE = 0  操作成功。

结果如下
--------
    安全策略编号  =  1
    安全策略类型  =  黑名单策略
安全策略使能标记  =  FALSE
TCP/IP防攻击类型  =  UDP泛洪报文
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-SECPOLICYSWITCH.md`
