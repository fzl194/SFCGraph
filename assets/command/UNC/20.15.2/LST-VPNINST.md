---
id: UNC@20.15.2@MMLCommand@LST VPNINST
type: MMLCommand
name: LST VPNINST（查询VPN实例）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: VPNINST
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- VPN
status: active
---

# LST VPNINST（查询VPN实例）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查询配置的VPN实例信息。

## 注意事项

- “_public_”是公网缺省VPN的实例名，查询结果中不呈现。
- 默认为输出所有VPN实例；若想查看指定VPN的信息，可加参数VPNINSTANCE。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VPNINSTANCE | VPN实例名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定VPN实例。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~31。区分大小写，不支持空格。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [VPN实例（VPNINST）](configobject/UNC/20.15.2/VPNINST.md)

## 使用实例

显示VPNInst业务配置： LST VPNINST:;

```
%%LST VPNINST:;%%
RETCODE = 0  操作成功。

VPN实例信息
------------------------
VPN实例名  =  vpn1
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询VPN实例（LST-VPNINST）_09651519.md`
