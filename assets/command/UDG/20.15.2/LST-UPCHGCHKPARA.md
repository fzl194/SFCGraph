---
id: UDG@20.15.2@MMLCommand@LST UPCHGCHKPARA
type: MMLCommand
name: LST UPCHGCHKPARA（显示计费检查参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UPCHGCHKPARA
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 计费控制
- 用户面计费检查参数
status: active
---

# LST UPCHGCHKPARA（显示计费检查参数）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

用于查询用户面计费检查相关参数。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPCHGCHKPARA]] · 计费检查参数（UPCHGCHKPARA）

## 使用实例

使用LST MULTIDNNPARA命令查询用户面计费检查相关参数：

```
LST UPCHGCHKPARA:;
```

```

RETCODE = 0 操作成功

计费检查参数
----------------------
用户资源告警开关 = 否
流量核查告警开关 = 否
流量核查告警上报阈值 = 500
流量核查告警恢复阈值 = 300
(结果数 = 1)
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-UPCHGCHKPARA.md`
