---
id: UDG@20.15.2@MMLCommand@ADD VPNVNIMAP
type: MMLCommand
name: ADD VPNVNIMAP（增加VPN VNI映射）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: VPNVNIMAP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 4097
category_path:
- 用户面服务管理
- 路径管理
- VXLAN路径管理
- VPN VNI 映射
status: active
---

# ADD VPNVNIMAP（增加VPN VNI映射）

## 功能

**适用NF：PGW-U、UPF**

该命令用于添加VNI与VPN的映射关系。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为4097。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VPNINSTANCE | VPN实例名 | 可选必选说明：必选参数<br>参数含义：该参数用于配置VPN实例。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，区分大小写。<br>默认值：无<br>配置原则：该参数使用 ADD VPNINST命令配置生成。 |
| RULESWITCH | Rule开关 | 可选必选说明：必选参数<br>参数含义：该参数用于控制是否支持配置Rule。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：DISABLE<br>配置原则：1. 如果运营商希望仅基于用户VPN映射到VNI，设置该参数为DISABLE。 2. 如果运营商希望在同一个用户VPN中，基于不同业务规则映射到不同的VNI，设置该参数为ENABLE。 |
| RULENAME | 规则名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“RULESWITCH”配置为“ENABLE”时为必选参数。<br>参数含义：该参数用于设置规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：该参数通过ADD RULE命令配置生成，RULENAME绑定的RULE中POLICYTYPE必须为WORKER。 |
| VNI | VNI | 可选必选说明：必选参数<br>参数含义：配置VXLAN隧道头中的VNI标识的值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～16777215。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@VPNVNIMAP]] · VPN VNI映射（VPNVNIMAP）

## 使用实例

配置VNI为4096与VPN为vpn1的映射关系：

```
ADD VPNVNIMAP: VPNINSTANCE="vpn1", RULESWITCH=DISABLE, VNI=4096;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-VPNVNIMAP.md`
