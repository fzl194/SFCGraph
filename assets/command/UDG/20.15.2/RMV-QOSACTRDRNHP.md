---
id: UDG@20.15.2@MMLCommand@RMV QOSACTRDRNHP
type: MMLCommand
name: RMV QOSACTRDRNHP（删除QoS重定向下一跳信息）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: QOSACTRDRNHP
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- 重定向下一跳信息
status: active
---

# RMV QOSACTRDRNHP（删除QoS重定向下一跳信息）

## 功能

该命令用来删除指定流行为重定向动作。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BEHAVIORNAME | 流行为名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定流行为名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：区分大小写，不支持空格。 |
| IPVERSION | IP协议版本 | 可选必选说明：可选参数<br>参数含义：该参数用于指定下一跳为IPv4类型还是IPv6类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPv4：IPv4类型。<br>- IPv6：IPv6类型。<br>默认值：IPv4 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@QOSACTRDRNHP]] · QoS重定向下一跳信息（QOSACTRDRNHP）

## 使用实例

- 删除流行为b5中配置的重定向IPv4下一跳信息：
  ```
  RMV QOSACTRDRNHP:BEHAVIORNAME="b5",IPVERSION=IPv4;
  ```
- 删除流行为b6中配置的重定向IPv6下一跳信息：
  ```
  RMV QOSACTRDRNHP:BEHAVIORNAME="b6",IPVERSION=IPv6;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-QOSACTRDRNHP.md`
