---
id: UDG@20.15.2@MMLCommand@ADD TOBYPASSCFG
type: MMLCommand
name: ADD TOBYPASSCFG（增加TCP旁路配置）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: TOBYPASSCFG
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 对新流生效
is_dangerous: false
max_records: 64
category_path:
- TCP优化服务管理
- TCP旁路配置
status: active
---

# ADD TOBYPASSCFG（增加TCP旁路配置）

## 功能

**适用NF：UPF**

该命令用于设置旁路Pod配置。

## 注意事项

- 该命令执行后对新数据流生效。
- 该命令最大记录数为64。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODNAME | Pod名称 | 可选必选说明：必选参数<br>参数含义：Pod名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：无 |
| MODE | 旁路模式 | 可选必选说明：必选参数<br>参数含义：设置该Pod的Bypass模式。<br>数据来源：本端规划<br>取值范围：无。<br>- mode1：所有的流量都不上送to pod。<br>- mode2：所有的流量都上送to pod，但是不上送内核。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/TOBYPASSCFG]] · TCP旁路配置（TOBYPASSCFG）

## 使用实例

增加名称为“to-pod-0”的pod旁路模式为mode1模式：

```
ADD TOBYPASSCFG: PODNAME="to-pod-0", MODE=mode1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-TOBYPASSCFG.md`
