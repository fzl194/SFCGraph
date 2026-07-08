---
id: UNC@20.15.2@MMLCommand@RTR SECIPURPFSTAT
type: MMLCommand
name: RTR SECIPURPFSTAT（清除URPF丢包信息）
nf: UNC
version: 20.15.2
verb: RTR
object_keyword: SECIPURPFSTAT
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- 主机防攻击
- URPF统计
status: active
---

# RTR SECIPURPFSTAT（清除URPF丢包信息）

## 功能

该命令用来重置IP URPF统计丢包信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～49。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |
| SECPROTOFAMILY | 安全协议族 | 可选必选说明：必选参数<br>参数含义：安全协议族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4：IPv4类型。<br>- ipv6：IPv6类型。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SECIPURPFSTAT]] · URPF丢弃报文计数信息（SECIPURPFSTAT）

## 使用实例

重置IP URPF统计丢包信息：

```
RTR SECIPURPFSTAT:SECPROTOFAMILY=ipv4;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RTR-SECIPURPFSTAT.md`
