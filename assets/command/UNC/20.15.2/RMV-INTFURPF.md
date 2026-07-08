---
id: UNC@20.15.2@MMLCommand@RMV INTFURPF
type: MMLCommand
name: RMV INTFURPF（删除安全接口URPF）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: INTFURPF
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- 主机防攻击
- 安全策略接口URPF
status: active
---

# RMV INTFURPF（删除安全接口URPF）

## 功能

该命令用来删除接口的URPF配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～47。<br>默认值：无<br>配置原则：使用LST INTERFACE命令查看可用接口。 |
| SECPROTOFAMILY | 安全协议族 | 可选必选说明：必选参数<br>参数含义：安全协议族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4：IPv4类型。<br>- ipv6：IPv6类型。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@INTFURPF]] · 安全接口URPF（INTFURPF）

## 使用实例

删除接口的URPF配置：

```
RMV INTFURPF: IFNAME="Ethernet66/0/2", SECPROTOFAMILY=ipv4;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-INTFURPF.md`
