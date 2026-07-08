---
id: UNC@20.15.2@MMLCommand@LST IPALLOCRULE
type: MMLCommand
name: LST IPALLOCRULE（查询全局地址分配规则）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IPALLOCRULE
command_category: 查询类
applicable_nf:
- PGW-C
- GGSN
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- UE地址池管理
- 地址分配规则配置
status: active
---

# LST IPALLOCRULE（查询全局地址分配规则）

## 功能

**适用NF：PGW-C、GGSN、SMF**

该命令用于查询全局地址分配规则。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [全局地址分配规则（IPALLOCRULE）](configobject/UNC/20.15.2/IPALLOCRULE.md)

## 使用实例

查询全局地址分配规则：

```
%%LST IPALLOCRULE:;%%
RETCODE = 0 操作成功

结果如下
---------------------
IPv4第一级规则开关 = 使能
    IPv4第一级规则 = APN
IPv4第二级规则开关 = 去使能
    IPv4第二级规则 = NULL
IPv4第三级规则开关 = 去使能
    IPv4第三级规则 = NULL
IPv6第一级规则开关 = 使能
    IPv6第一级规则 = APN
IPv6第二级规则开关 = 去使能
    IPv6第二级规则 = NULL
IPv6第三级规则开关 = 去使能
    IPv6第三级规则 = NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询全局地址分配规则（LST-IPALLOCRULE）_49644923.md`
