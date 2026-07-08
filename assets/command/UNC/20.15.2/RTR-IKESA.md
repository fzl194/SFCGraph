---
id: UNC@20.15.2@MMLCommand@RTR IKESA
type: MMLCommand
name: RTR IKESA（恢复IKE安全联盟）
nf: UNC
version: 20.15.2
verb: RTR
object_keyword: IKESA
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- IP安全管理
- 互联网密钥交换
- IKE安全联盟
status: active
---

# RTR IKESA（恢复IKE安全联盟）

## 功能

![](恢复IKE安全联盟（RTR IKESA）_80592514.assets/notice_3.0-zh-cn_2.png)

恢复IKE安全联盟后，IKE安全联盟会重新协商，会导致业务短时间中断。

该命令用于恢复IKE安全联盟。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESETTYPE | 清除类型 | 可选必选说明：必选参数<br>参数含义：清除类型。<br>数据来源：本端规划<br>取值范围：枚举类型。 all：指定IP版本的所有安全联盟。 connId：指定IP版本的连接ID。 remAddr：指定IP版本的远端地址。<br>- “All（所有）”：所有<br>- “ConnId（连接ID）”：连接ID<br>- “RemAddr（远端地址）”：远端地址<br>默认值：无<br>配置原则：<br>必选参数。 |
| CONNECTIONID | 连接ID | 可选必选说明：该参数在"RESETTYPE"配置为"ConnId"时为条件必选参数。<br>参数含义：连接ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~65535。整数类型，取值范围为1～65535。<br>默认值：无<br>配置原则：无 |
| IPVERSION | 远端地址IP版本 | 可选必选说明：可选参数<br>参数含义：IP版本。<br>数据来源：本端规划<br>取值范围：枚举类型。IPv4或IPv6。<br>- “IPv4（远端地址格式为IPv4）”：远端地址格式为IPv4<br>- “IPv6（远端地址格式为IPv6）”：远端地址格式为IPv6<br>默认值：IPv4<br>配置原则：<br>必选参数。 |
| REMOTEADDR | 远端地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPv4"时为条件可选参数。<br>参数含义：远端地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| REMOTEADDR6 | 远端地址IPv6 | 可选必选说明：该参数在"IPVERSION"配置为"IPv6"时为条件可选参数。<br>参数含义：IPv6远端地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。IPv6地址类型。<br>默认值：无<br>配置原则：无 |
| PODNAME | POD名称 | 可选必选说明：可选参数<br>参数含义：POD名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~63。字符串类型，输入长度范围为0～63。<br>默认值：无<br>配置原则：<br>该参数在“RESETTYPE”配置为“all”、“connId” 或 “remAddr”时为可选参数。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IKESA]] · IKE安全联盟（IKESA）

## 使用实例

恢复Connection ID为1，IP协议版本为IPv4，的IKE SA：

```
RTR IKESA:RESETTYPE=ConnId,CONNECTIONID=1,IPVERSION=IPv4;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/恢复IKE安全联盟（RTR-IKESA）_80592514.md`
