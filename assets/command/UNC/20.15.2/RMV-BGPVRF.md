---
id: UNC@20.15.2@MMLCommand@RMV BGPVRF
type: MMLCommand
name: RMV BGPVRF（删除BGP VPN实例）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: BGPVRF
command_category: 配置类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- BGP VPN实例
status: active
---

# RMV BGPVRF（删除BGP VPN实例）

## 功能

该命令用来删除已创建的BGP VPN实例。

![](删除BGP VPN实例（RMV BGPVRF）_00440925.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，该操作会删除BGP所有该VPN实例下的关联配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令会删除BGP所有该VPN实例下的关联配置。
- 删除BGP VPN实例会同时删除该VPN实例下的配置内容和业务。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定BGP VPN实例。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：使用LST BGPVRF命令查看可用VPN。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@BGPVRF]] · BGP VPN实例（BGPVRF）

## 使用实例

删除名称为“vrf1”的BGP VPN实例：

```
RMV BGPVRF:VRFNAME="vrf1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-BGPVRF.md`
