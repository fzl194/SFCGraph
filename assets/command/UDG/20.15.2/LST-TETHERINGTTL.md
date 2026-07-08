---
id: UDG@20.15.2@MMLCommand@LST TETHERINGTTL
type: MMLCommand
name: LST TETHERINGTTL（查询tethering的TTL值）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TETHERINGTTL
command_category: 查询类
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
- 配置tethering的ttl值
status: active
---

# LST TETHERINGTTL（查询tethering的TTL值）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询所有配置的TTL值。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/TETHERINGTTL]] · tethering的TTL值（TETHERINGTTL）

## 使用实例

显示所有判断tethering的TTL值：

```
%%LST TETHERINGTTL:;
```

```
%%
RETCODE = 0  操作成功

Tethering TTL
-------------
Tethering TTL值  =  2
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-TETHERINGTTL.md`
