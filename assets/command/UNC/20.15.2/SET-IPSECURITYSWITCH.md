---
id: UNC@20.15.2@MMLCommand@SET IPSECURITYSWITCH
type: MMLCommand
name: SET IPSECURITYSWITCH（设置IP选项安全开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: IPSECURITYSWITCH
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 业务管理
- 安全配置
- IP安全开关
status: active
---

# SET IPSECURITYSWITCH（设置IP选项安全开关）

## 功能

该命令用于设置CSLB中IP选项安全开关配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令存在系统初始记录，参数的初始设置值如下表：
  | IPV4OPTION | IPV6EXTENSION |
  | --- | --- |
  | SW_DISABLE | SW_DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPV4OPTION | IPv4选项安全配置开关 | 可选必选说明：必选参数<br>参数含义：<br>该参数表示使能或去使能<br>IPv4<br>选项安全配置<br>。<br>数据来源：本端规划<br>取值范围：枚举类型:<br>- SW_ENABLE(IP安全开关开启)：使能IPv4选项安全开关；<br>- SW_DISABLE(IP安全开关关闭)：去使能IPv4选项安全开关；<br>默认值：无 |
| IPV6EXTENSION | IPv6扩展头选项安全配置开关 | 可选必选说明：必选参数<br>参数含义：<br>该参数表示使能或去使能<br>IPv6<br>扩展头选项安全配置<br>。<br>数据来源：本端规划<br>取值范围：枚举类型:<br>- SW_ENABLE(IP安全开关开启)：使能IPv6扩展头选项安全开关；<br>- SW_DISABLE(IP安全开关关闭)：去使能IPv6扩展头选项安全开关；<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IPSECURITYSWITCH]] · IP选项安全开关（IPSECURITYSWITCH）

## 使用实例

设置针对带有IPv4选项的报文和带有IPv6扩展头选项的报文，执行丢弃处理，命令如下：

```
SET IPSECURITYSWITCH: IPV4OPTION=SW_ENABLE, IPV6EXTENSION=SW_ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-IPSECURITYSWITCH.md`
