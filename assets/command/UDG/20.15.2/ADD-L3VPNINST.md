---
id: UDG@20.15.2@MMLCommand@ADD L3VPNINST
type: MMLCommand
name: ADD L3VPNINST（增加L3VPN实例）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: L3VPNINST
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 4096
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- VPN管理
- L3VPN管理
- L3VPN实例
status: active
---

# ADD L3VPNINST（增加L3VPN实例）

## 功能

该命令用于创建L3VPN实例。

创建VPN可以使用户获得专用虚拟的网络。

专用：VPN网络与底层承载网络之间保持资源独立，即VPN资源不被网络中非该VPN的用户所使用；且VPN能够提供足够的安全保证，确保VPN内部信息不受外部侵扰。

虚拟：VPN用户内部的通信是通过公共网络进行的，而这个公共网络同时也可以被其他非VPN用户使用，VPN用户获得的只是一个逻辑意义上的专网。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为4096。
- 不能增加VPN实例 _public_、__mpp_vpn_inner__、__mpp_vpn_inner_server__。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定L3VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| VRFDESCRIPTION | VPN实例描述 | 可选必选说明：可选参数<br>参数含义：该参数用于描述L3VPN实例。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～242。<br>默认值：无<br>配置原则：可以带空格的描述性语句。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@L3VPNINST]] · L3VPN实例（L3VPNINST）

## 关联任务

- [[UDG@20.15.2@Task@0-00071]]

## 使用实例

新建名称为“vrf1”的VPN实例：

```
ADD L3VPNINST: VRFNAME="vrf1", VRFDESCRIPTION="vpn for test";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-L3VPNINST.md`
