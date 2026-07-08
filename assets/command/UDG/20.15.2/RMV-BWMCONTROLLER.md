---
id: UDG@20.15.2@MMLCommand@RMV BWMCONTROLLER
type: MMLCommand
name: RMV BWMCONTROLLER（删除带宽管理控制器）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: BWMCONTROLLER
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 带宽控制
- 带宽管理控制器
status: active
---

# RMV BWMCONTROLLER（删除带宽管理控制器）

## 功能

**适用NF：PGW-U、UPF**

该命令用于删除指定的bwm控制器。

## 注意事项

- 该命令执行后立即生效。
- 如果某个BwmController已经被引用，则它不能被删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BWMCNAME | 带宽管理控制器名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示带宽管理控制器的名字。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/BWMCONTROLLER]] · 带宽管理控制器（BWMCONTROLLER）

## 使用实例

如果要删除名为“bc1”的BwmController，则使用如下命令：

```
RMV BWMCONTROLLER:BWMCNAME="bc1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除带宽管理控制器（RMV-BWMCONTROLLER）_82837462.md`
