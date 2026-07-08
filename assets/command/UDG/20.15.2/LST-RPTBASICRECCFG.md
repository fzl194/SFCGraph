---
id: UDG@20.15.2@MMLCommand@LST RPTBASICRECCFG
type: MMLCommand
name: LST RPTBASICRECCFG（显示基础单据上报功能开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: RPTBASICRECCFG
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务报表管理
- 报表功能管理
- 报表系统级单据开关
status: active
---

# LST RPTBASICRECCFG（显示基础单据上报功能开关）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询基础单据上报功能开关。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [基础单据上报功能开关（RPTBASICRECCFG）](configobject/UDG/20.15.2/RPTBASICRECCFG.md)

## 使用实例

加入运营商需要查询基础单据上报功能开关：

```
LST RPTBASICRECCFG:;
```

```

RETCODE = 0 操作成功。

基础单据上报功能开关配置信息
------------------------
用户信息开关 = 不使能（关闭）
用户统计开关 = 不使能（关闭）
 APP统计开关 = 不使能（关闭）
    资源开关 = 不使能（关闭）

--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示基础单据上报功能开关（LST-RPTBASICRECCFG）_61159772.md`
