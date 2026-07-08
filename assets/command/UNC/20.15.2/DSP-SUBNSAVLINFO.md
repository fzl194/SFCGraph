---
id: UNC@20.15.2@MMLCommand@DSP SUBNSAVLINFO
type: MMLCommand
name: DSP SUBNSAVLINFO（显示网络切片可用性订阅信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SUBNSAVLINFO
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 网络切片选择管理
- 网络切片可用性信息查询
status: active
---

# DSP SUBNSAVLINFO（显示网络切片可用性订阅信息）

## 功能

**适用NF：AMF**

该命令用于显示NSSF向AMF返回的网络切片可用性的订阅信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SUBNSAVLINFO]] · 网络切片可用性订阅信息（SUBNSAVLINFO）

## 使用实例

显示NSSF向AMF返回的网络切片可用性的订阅信息，执行如下命令：

```
DSP SUBNSAVLINFO:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SUBNSAVLINFO.md`
