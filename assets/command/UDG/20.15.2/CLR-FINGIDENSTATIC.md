---
id: UDG@20.15.2@MMLCommand@CLR FINGIDENSTATIC
type: MMLCommand
name: CLR FINGIDENSTATIC（清零SA指纹识别统计结果）
nf: UDG
version: 20.15.2
verb: CLR
object_keyword: FINGIDENSTATIC
command_category: 动作类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 协议识别
- SA指纹识别
- SA指纹识别统计
status: active
---

# CLR FINGIDENSTATIC（清零SA指纹识别统计结果）

## 功能

**适用NF：PGW-U、UPF**

该命令用于清零SA指纹识别的统计结果。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/FINGIDENSTATIC]] · SA指纹识别统计结果（FINGIDENSTATIC）

## 使用实例

清零SA指纹识别的统计结果，配置如下：

```
CLR FINGIDENSTATIC:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/清零SA指纹识别统计结果（CLR-FINGIDENSTATIC）_31865726.md`
