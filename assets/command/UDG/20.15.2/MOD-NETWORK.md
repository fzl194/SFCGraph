---
id: UDG@20.15.2@MMLCommand@MOD NETWORK
type: MMLCommand
name: MOD NETWORK（网络配置）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: NETWORK
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统管理
- 路由管理
- 网络管理
status: active
---

# MOD NETWORK（网络配置）

## 功能

用于修改系统网络的网卡VLANID。

## 注意事项

当前场景不支持此命令。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| IPTYPE | IP类型 | 可选必选说明：必选参数<br>参数含义：网络的IP类型。<br>取值范围：<br>- IPV4(IPV4类型)<br>- IPV6(IPV6类型)<br>- IPV4/IPV6(IPV4/IPV6类型)：双栈环境，同时支持IPV4和IPV6。<br>默认值：无。<br>配置原则：无。 |
| NWNAME | 网络名称 | 可选必选说明：必选参数<br>参数含义：网络名称。<br>取值范围： 1~512的字符串<br>默认值：无。<br>配置原则：网络名称需要与服务适配包里定义的nwName完全一致（注意大小写及空白字符），否则无法识别。 |
| VLANID | VLANID | 可选必选说明：必选参数<br>参数含义：网络的VLANID。<br>取值范围：0~4094<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [网络查询（NETWORK）](configobject/UDG/20.15.2/NETWORK.md)

## 使用实例

无。

## 证据

- 原始手册：`evidence/UDG/20.15.2/网络配置（MOD-NETWORK）_18720733.md`
