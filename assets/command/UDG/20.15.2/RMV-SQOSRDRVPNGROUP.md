---
id: UDG@20.15.2@MMLCommand@RMV SQOSRDRVPNGROUP
type: MMLCommand
name: RMV SQOSRDRVPNGROUP（删除QoS重定向VPN组）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: SQOSRDRVPNGROUP
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- 重定向VPN组
status: active
---

# RMV SQOSRDRVPNGROUP（删除QoS重定向VPN组）

## 功能

该命令用来删除指定流行为重定向VPN动作。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BEHAVIORNAME | 行为名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定流动作。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：区分大小写，不支持空格。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@SQOSRDRVPNGROUP]] · QoS重定向VPN组（SQOSRDRVPNGROUP）

## 使用实例

删除流行为b5中配置重定向VPN动作：

```
RMV SQOSRDRVPNGROUP:BEHAVIORNAME="b5";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-SQOSRDRVPNGROUP.md`
