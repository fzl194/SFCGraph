---
id: UDG@20.15.2@MMLCommand@MOD VPNVNIMAP
type: MMLCommand
name: MOD VPNVNIMAP（修改VPN VNI映射）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: VPNVNIMAP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 路径管理
- VXLAN路径管理
- VPN VNI 映射
status: active
---

# MOD VPNVNIMAP（修改VPN VNI映射）

## 功能

**适用NF：PGW-U、UPF**

![](修改VPN VNI映射（MOD VPNVNIMAP）_81234598.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，修改VPN与VNI映射关系时，需要同步修改对应MEP上VNI与VPN的映射关系。

该命令用于修改VNI与VPN映射关系对应的规则配置。

## 注意事项

- 该命令执行后立即生效。
- 执行该命令修改VPN与VNI映射关系时，需要同步修改对应MEP上VNI与VPN的映射关系。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VPNINSTANCE | VPN实例名 | 可选必选说明：必选参数<br>参数含义：该参数用于配置VPN实例。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，区分大小写。<br>默认值：无<br>配置原则：该参数使用 ADD VPNINST命令配置生成。 |
| RULENAME | 规则名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| VNI | VNI | 可选必选说明：必选参数<br>参数含义：配置VXLAN隧道头中的VNI标识的值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～16777215。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@VPNVNIMAP]] · VPN VNI映射（VPNVNIMAP）

## 使用实例

修改VNI为4096与VPN为vpn1映射的规则配置为rule1：

```
MOD VPNVNIMAP: VPNINSTANCE="vpn1", RULENAME="rule1", VNI=4096;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-VPNVNIMAP.md`
