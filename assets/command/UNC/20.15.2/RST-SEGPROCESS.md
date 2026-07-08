---
id: UNC@20.15.2@MMLCommand@RST SEGPROCESS
type: MMLCommand
name: RST SEGPROCESS（复位NRF百万号段功能）
nf: UNC
version: 20.15.2
verb: RST
object_keyword: SEGPROCESS
command_category: 动作类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 对端NF管理
- 号段配置管理
- 号段导入管理
status: active
---

# RST SEGPROCESS（复位NRF百万号段功能）

## 功能

![](复位NRF百万号段功能（RST SEGPROCESS）_64343911.assets/notice_3.0-zh-cn_2.png)

执行该命令可能会影响NRF服务发现功能，请慎重使用该命令。

**适用NF：NRF**

本命令用于NRF百万号段功能恢复。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/SEGPROCESS]] · 复位NRF百万号段功能（SEGPROCESS）

## 使用实例

执行NRF百万号段功能恢复

```
RST SEGPROCESS:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RST-SEGPROCESS.md`
