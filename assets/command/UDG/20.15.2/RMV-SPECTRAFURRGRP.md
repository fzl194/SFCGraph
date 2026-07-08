---
id: UDG@20.15.2@MMLCommand@RMV SPECTRAFURRGRP
type: MMLCommand
name: RMV SPECTRAFURRGRP（删除全局缺省费率的流量使用量上报规则组）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: SPECTRAFURRGRP
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务控制策略
- 计费控制
- 特殊流量使用量上报规则组
status: active
---

# RMV SPECTRAFURRGRP（删除全局缺省费率的流量使用量上报规则组）

## 功能

**适用NF：UPF**

![](删除全局缺省费率的流量使用量上报规则组（RMV SPECTRAFURRGRP）_36146717.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，删除配置会导致未匹配上计费费率的业务免费通过，造成运营商计费损失。

命令用于删除全局缺省费率的使用量上报规则组。

## 注意事项

- 该命令执行后立即生效。
- 删除配置会导致未匹配上计费费率的业务免费通过，造成运营商计费损失。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/SPECTRAFURRGRP]] · 全局缺省费率的流量使用量上报规则组（SPECTRAFURRGRP）

## 使用实例

假如用户要删除全局缺省费率的使用量上报规则组：

```
RMV SPECTRAFURRGRP:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除全局缺省费率的流量使用量上报规则组（RMV-SPECTRAFURRGRP）_36146717.md`
