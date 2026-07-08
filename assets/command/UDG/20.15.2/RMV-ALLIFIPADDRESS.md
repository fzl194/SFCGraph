---
id: UDG@20.15.2@MMLCommand@RMV ALLIFIPADDRESS
type: MMLCommand
name: RMV ALLIFIPADDRESS（批量删除接口下IP地址）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: ALLIFIPADDRESS
command_category: 配置类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 接口管理
- 接口批量操作
status: active
---

# RMV ALLIFIPADDRESS（批量删除接口下IP地址）

## 功能

该命令用于批量删除接口下地址。

![](批量删除接口下IP地址（RMV ALLIFIPADDRESS）_50121354.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，该操作将清除该接口下的所有IPv4或IPv6配置。

## 注意事项

- 该命令执行后立即生效。
- 该操作可能会导致业务流量中断。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要删除IP地址的接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| OPTYPE | 操作类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定操作类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- AllIPv4：清除接口IPv4地址。<br>- AllIPv6：清除接口IPv6地址。<br>- AllIPAddress：清除接口所有IP地址。<br>默认值：无 |

## 操作的配置对象

- [批量删除接口下IP地址（ALLIFIPADDRESS）](configobject/UDG/20.15.2/ALLIFIPADDRESS.md)

## 使用实例

- 删除接口下所有IPv4地址：
  ```
  RMV ALLIFIPADDRESS:IFNAME="ethernet64/0/3",OPTYPE=AllIPv4;
  ```
- 删除接口下所有IPv6地址：
  ```
  RMV ALLIFIPADDRESS:IFNAME="ethernet64/0/3",OPTYPE=AllIPv6;
  ```
- 删除接口下所有IP地址：
  ```
  RMV ALLIFIPADDRESS:IFNAME="ethernet64/0/3",OPTYPE=AllIPAddress;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/批量删除接口下IP地址（RMV-ALLIFIPADDRESS）_50121354.md`
