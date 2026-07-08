---
id: UNC@20.15.2@MMLCommand@ADD STATICASN
type: MMLCommand
name: ADD STATICASN（增加静态ASN）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: STATICASN
command_category: 配置类
applicable_nf:
- PGW-C
- SGW-C
- GGSN
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- GTP-C接口配置管理
- ASN静态配置
status: active
---

# ADD STATICASN（增加静态ASN）

## 功能

**适用NF：PGW-C、SGW-C、GGSN**

该命令用来增加SGSN、SGW-C信令地址和ASN映射的本地表项。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 最多可输入1000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRVNODEIP | Service Node信令IP地址 | 可选必选说明：必选参数<br>参数含义：该参数用于设置SGSN、SGW-C的信令IP。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| MASK | IP掩码 | 可选必选说明：必选参数<br>参数含义：该参数用于设置SGSN、SGW-C信令IP的掩码。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| ASN | ASN | 可选必选说明：必选参数<br>参数含义：该参数用于设置SGSN、SGW-C对应的ASN值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~65535。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@STATICASN]] · 静态ASN（STATICASN）

## 使用实例

增加一个sgsn-ip为10.13.13.0，掩码类型为掩码长度的ASN配置：

```
ADD STATICASN: SRVNODEIP="10.13.13.0", MASK="255.255.255.0", ASN=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-STATICASN.md`
