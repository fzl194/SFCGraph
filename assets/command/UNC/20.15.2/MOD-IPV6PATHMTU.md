---
id: UNC@20.15.2@MMLCommand@MOD IPV6PATHMTU
type: MMLCommand
name: MOD IPV6PATHMTU（修改IPv6 Path MTU配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: IPV6PATHMTU
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv6管理
- IPv6 Path MTU
status: active
---

# MOD IPV6PATHMTU（修改IPv6 Path MTU配置）

## 功能

该命令用于修改IPv6路径MTU配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPV6ADDRESS | IPv6地址 | 可选必选说明：必选参数<br>参数含义：该参数用于表示IPv6地址。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。<br>默认值：无 |
| VRFNAME | VPN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示VPN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| PATHMTU | 路径MTU值（byte） | 可选必选说明：必选参数<br>参数含义：该参数用于表示路径MTU。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1280～10000，单位是字节。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IPV6PATHMTU]] · IPv6 Path MTU配置（IPV6PATHMTU）

## 使用实例

修改IPv6 Path MTU配置：

```
MOD IPV6PATHMTU:VRFNAME="vpn1",IPV6ADDRESS="2001:db8::11",PATHMTU=1500;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-IPV6PATHMTU.md`
