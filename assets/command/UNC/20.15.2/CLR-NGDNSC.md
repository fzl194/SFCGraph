---
id: UNC@20.15.2@MMLCommand@CLR NGDNSC
type: MMLCommand
name: CLR NGDNSC（清除DNS缓存）
nf: UNC
version: 20.15.2
verb: CLR
object_keyword: NGDNSC
command_category: 动作类
applicable_nf:
- AMF
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- DNS Client
- DNS Cache管理
status: active
---

# CLR NGDNSC（清除DNS缓存）

## 功能

**适用NF：AMF、SMF**

该命令功能不生效，由CLR NGDNSCACHE命令代替。

该命令用于清除DNS缓存（DNS Cache）。当TOPO侧4/5G切换时查询FQDN的IP地址完成后，清除已经查询的缓存命令。

DNS Cache是使用DNS服务器解析时在系统中查找到的缓存，其主要内容为域名和IP地址信息，用于快速解析域名。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGDNSC]] · DNS缓存（NGDNSC）

## 使用实例

DNS服务器上的数据修改，通过该命令清除UNC系统DNS Cache：

```
CLR NGDNSC:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/CLR-NGDNSC.md`
