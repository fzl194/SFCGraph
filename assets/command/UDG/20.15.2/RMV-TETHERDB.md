---
id: UDG@20.15.2@MMLCommand@RMV TETHERDB
type: MMLCommand
name: RMV TETHERDB（卸载Tethering检测特征库）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: TETHERDB
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- Tethering检测
- Tethering检测特征库
status: active
---

# RMV TETHERDB（卸载Tethering检测特征库）

## 功能

**适用NF：PGW-U、UPF**

该命令用来卸载已经加载的Tethering检测特征库。

## 注意事项

- 该命令执行后立即生效。
- 此命令的生效范围为整机。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/TETHERDB]] · Tethering检测特征库（TETHERDB）

## 使用实例

假如运营商需卸载已经加载的Tethering检测特征库：

```
RMV TETHERDB:;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-TETHERDB.md`
