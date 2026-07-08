---
id: UDG@20.15.2@MMLCommand@RMV NGVNBINDVXLAN
type: MMLCommand
name: RMV NGVNBINDVXLAN（删除5G LAN实例绑定VXLAN组配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: NGVNBINDVXLAN
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 路径管理
- VXLAN路径管理
- 5GLAN实例绑定VXLAN组
status: active
---

# RMV NGVNBINDVXLAN（删除5G LAN实例绑定VXLAN组配置）

## 功能

**适用NF：UPF**

![](删除5G LAN实例绑定VXLAN组配置（RMV NGVNBINDVXLAN）_12316747.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，删除该配置会导致对应5G LAN组下的用户和DN侧业务不通。

该命令用于删除5GLAN会话实例使用的VXLAN链路信息。

## 注意事项

- 该命令执行后立即生效。
- 删除5G LAN会话实例使用的VXLAN链路信息会中断5G LAN用户与DN侧之间的业务，请谨慎删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VNINSTANCE | 5G LAN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定5G LAN会话实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为18～37。VNINSTANCE以连字号分为4段，形式为GroupServiceID-MCC-MNC-LocalGroupID。其中，GroupServiceID长度为8，只能输入数字或者范围为A到F或a-f的字母；MCC长度为3，只能输入数字；MNC长度为2~3，只能输入数字；LocalGroupID长度为2~20的偶数，只能输入数字或者范围为A到F或a-f的字母。例如，A0000001-460-003-01，A0000001-460-003-A000000001。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@NGVNBINDVXLAN]] · 5G LAN实例绑定VXLAN组配置（NGVNBINDVXLAN）

## 使用实例

删除5GLAN会话实例"A0000001-460-003-01"的VXLAN隧道信息：

```
RMV NGVNBINDVXLAN: VNINSTANCE="A0000001-460-003-01";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-NGVNBINDVXLAN.md`
