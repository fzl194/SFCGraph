---
id: UNC@20.15.2@MMLCommand@RTR LSPVSTATISTICS
type: MMLCommand
name: RTR LSPVSTATISTICS（清除LSPV报文统计计数）
nf: UNC
version: 20.15.2
verb: RTR
object_keyword: LSPVSTATISTICS
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 系统管理
- 系统维护
- Ping和Tracert
- LSPV
status: active
---

# RTR LSPVSTATISTICS（清除LSPV报文统计计数）

## 功能

该命令用于清除LSPV报文统计计数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LSPVSTATISTICS]] · LSPV报文统计计数（LSPVSTATISTICS）

## 使用实例

清除LSPV报文统计计数：

```
RTR LSPVSTATISTICS:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RTR-LSPVSTATISTICS.md`
