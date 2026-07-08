---
id: UNC@20.15.2@MMLCommand@ADD IPSECINTFCFG
type: MMLCommand
name: ADD IPSECINTFCFG（创建IPsec隧道接口）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: IPSECINTFCFG
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 1024
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP安全管理
- 互联网密钥交换
- IPsec接口配置
status: active
---

# ADD IPSECINTFCFG（创建IPsec隧道接口）

## 功能

该命令用于创建IPsec隧道。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1024。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INTERFACENAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：配置接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无 |
| TNLTYPE | Tunnel口协议类型 | 可选必选说明：必选参数<br>参数含义：Tunnel口协议类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPSEC：IP安全。<br>- IPSEC6：IPv6安全。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IPSECINTFCFG]] · 创建IPsec隧道接口（IPSECINTFCFG）

## 使用实例

创建接口名为“Tunnel1/1/1”的安全隧道：

```
ADD IPSECINTFCFG:INTERFACENAME="Tunnel1/1/1",TNLTYPE=IPSEC;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-IPSECINTFCFG.md`
