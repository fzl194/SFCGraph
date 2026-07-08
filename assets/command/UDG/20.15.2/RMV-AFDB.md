---
id: UDG@20.15.2@MMLCommand@RMV AFDB
type: MMLCommand
name: RMV AFDB（卸载计费防欺诈业务规则数据库）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: AFDB
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务防欺诈
- 防欺诈业务规则数据库
status: active
---

# RMV AFDB（卸载计费防欺诈业务规则数据库）

## 功能

**适用NF：PGW-U、UPF**

![](卸载计费防欺诈业务规则数据库（RMV AFDB）_82837785.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，卸载计费防欺诈业务规则数据库可能会影响业务匹配结果，导致用户业务受损，请谨慎使用并联系华为技术支持协助操作。

该命令用来卸载已经加载的计费防欺诈业务规则数据库。

## 注意事项

- 该命令执行后立即生效。
- 加载或者卸载命令两次执行间隔不能小于10s。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [防欺诈业务规则数据库（AFDB）](configobject/UDG/20.15.2/AFDB.md)

## 使用实例

卸载防欺诈业务规则数据库：

```
RMV AFDB:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/卸载计费防欺诈业务规则数据库（RMV-AFDB）_82837785.md`
