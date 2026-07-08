---
id: UNC@20.15.2@MMLCommand@RTR DNSSTATISTICS
type: MMLCommand
name: RTR DNSSTATISTICS（清除DNS报文统计计数）
nf: UNC
version: 20.15.2
verb: RTR
object_keyword: DNSSTATISTICS
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 域名管理
- DNS报文统计
status: active
---

# RTR DNSSTATISTICS（清除DNS报文统计计数）

## 功能

该命令用于清除DNS报文统计计数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/DNSSTATISTICS]] · DNS报文统计计数（DNSSTATISTICS）

## 使用实例

清除DNS报文统计：

```
RTR DNSSTATISTICS:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/清除DNS报文统计计数（RTR-DNSSTATISTICS）_49961758.md`
