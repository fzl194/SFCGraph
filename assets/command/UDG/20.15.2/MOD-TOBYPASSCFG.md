---
id: UDG@20.15.2@MMLCommand@MOD TOBYPASSCFG
type: MMLCommand
name: MOD TOBYPASSCFG（设置TCP旁路配置修改）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: TOBYPASSCFG
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 对新流生效
is_dangerous: false
category_path:
- TCP优化服务管理
- TCP旁路配置
status: active
---

# MOD TOBYPASSCFG（设置TCP旁路配置修改）

## 功能

**适用NF：UPF**

该命令用于修改旁路Pod配置。

## 注意事项

该命令执行后对新数据流生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODNAME | Pod名称 | 可选必选说明：必选参数<br>参数含义：Pod名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：无 |
| MODE | 旁路模式 | 可选必选说明：必选参数<br>参数含义：设置该Pod的Bypass模式。<br>数据来源：本端规划<br>取值范围：无。<br>- mode1：所有的流量都不上送to pod。<br>- mode2：所有的流量都上送to pod，但是不上送内核。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [TCP旁路配置（TOBYPASSCFG）](configobject/UDG/20.15.2/TOBYPASSCFG.md)

## 使用实例

修改名称为“to-pod-0”的pod旁路模式为mode2模式：

```
MOD TOBYPASSCFG: PODNAME="to-pod-0", MODE=mode2;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置TCP旁路配置修改（MOD-TOBYPASSCFG）_14250207.md`
