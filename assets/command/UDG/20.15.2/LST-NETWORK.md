---
id: UDG@20.15.2@MMLCommand@LST NETWORK
type: MMLCommand
name: LST NETWORK（网络查询）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: NETWORK
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统管理
- 路由管理
- 网络管理
status: active
---

# LST NETWORK（网络查询）

## 功能

用于查询系统网络的网卡VLANID。

## 注意事项

当前场景不支持此命令。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| ISVLANIDALLOWMODIFY | 是否允许修改VLANID | 可选必选说明：可选参数<br>参数含义：VLANID是否允许修改。<br>取值范围：<br>- Y(是)：查询允许修改VLANID的网络。<br>- N(否)：查询不允许修改VLANID的网络。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@NETWORK]] · 网络查询（NETWORK）

## 使用实例

无。

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-NETWORK.md`
