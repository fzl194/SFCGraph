---
id: UNC@20.15.2@MMLCommand@MOD VNFMINFO
type: MMLCommand
name: MOD VNFMINFO（修改VNFM对接信息）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: VNFMINFO
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- VNFM管理
status: active
---

# MOD VNFMINFO（修改VNFM对接信息）

## 功能

预安装的网元到现网使用前，需要根据现网VNFM组网信息使用此命令修改网元与VNFM对接的主节点IP、备节点IP、用户名、密码信息。

> **说明**
> 该命令仅在非TCA场景下支持。

## 注意事项

VNFM组网信息为IPV6+IPV4双栈场景时，该命令中的主节点IP、备节点IP填写IPV6的地址信息。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| MASTERIP | 主节点IP | 可选必选说明：必选参数。<br>参数含义：网元对接的VNFM主节点IP。<br>取值范围：IPv4地址类型或者IPv6地址类型，长度不超过80的IP字符串。<br>默认值：无。<br>配置原则：VNFM主节点IP请从网设文档中获取。VNFM组网信息为IPV6+IPV4双栈场景时，主节点IP填写IPV6的地址信息。 |
| SLAVEIP | 备节点IP | 可选必选说明：可选参数。<br>参数含义：网元对接的VNFM备节点IP。<br>取值范围：IPv4地址类型或者IPv6地址类型，长度不超过80的IP字符串。<br>默认值：无。<br>配置原则：VNFM备节点IP请从网设文档中获取。VNFM组网信息为IPV6+IPV4双栈场景时，备节点IP填写IPV6的地址信息。 |
| USER | 用户名 | 可选必选说明：必选参数。<br>参数含义：网元对接的VNFM的用户名。<br>取值范围：长度不超过60的字符串。<br>默认值：无。<br>配置原则：请从VNFM获取。 |
| PWD | 密码 | 可选必选说明：必选参数。<br>参数含义：网元对接VNFM的用户的密码。<br>取值范围：长度为6~32位字符串。<br>默认值：无。<br>配置原则：请从VNFM获取。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/VNFMINFO]] · VNFM对接信息（VNFMINFO）

## 使用实例

修改VNFM链接信息。

```
%%MOD VNFMINFO: MASTERIP="10.10.10.10", SLAVEIP="10.10.10.11", USER="user", PWD="******";%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-VNFMINFO.md`
