---
id: UDG@20.15.2@MMLCommand@LST VPNVNIMAP
type: MMLCommand
name: LST VPNVNIMAP（查询VPN VNI映射）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: VPNVNIMAP
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 路径管理
- VXLAN路径管理
- VPN VNI 映射
status: active
---

# LST VPNVNIMAP（查询VPN VNI映射）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询VNI与VPN的映射关系。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VPNINSTANCE | VPN实例名 | 可选必选说明：可选参数<br>参数含义：该参数用于配置VPN实例。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，区分大小写。<br>默认值：无<br>配置原则：无 |
| RULENAME | 规则名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@VPNVNIMAP]] · VPN VNI映射（VPNVNIMAP）

## 使用实例

查询所有VNI与VPN的映射关系：

```
LST VPNVNIMAP:;
```

```

RETCODE = 0 操作成功。

UPF VNI映射信息
-----------------------
VPN实例名  =  vpn1
规则名称  =  rule1
VNI  =  4096
Rule开关  =  使能
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-VPNVNIMAP.md`
