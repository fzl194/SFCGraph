---
id: UDG@20.15.2@MMLCommand@RTR SECARPSGPKTSTC
type: MMLCommand
name: RTR SECARPSGPKTSTC（清除ARP双相分离报文统计）
nf: UDG
version: 20.15.2
verb: RTR
object_keyword: SECARPSGPKTSTC
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- 主机防攻击
- ARP双向分离
status: active
---

# RTR SECARPSGPKTSTC（清除ARP双相分离报文统计）

## 功能

该命令用来清除ARP双向分离报文统计。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数表示资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～49。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |

## 操作的配置对象

- [ARP双向分离报文统计（SECARPSGPKTSTC）](configobject/UDG/20.15.2/SECARPSGPKTSTC.md)

## 使用实例

清除ARP双向分离报文统计：

```
RTR SECARPSGPKTSTC:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/清除ARP双相分离报文统计（RTR-SECARPSGPKTSTC）_50281642.md`
