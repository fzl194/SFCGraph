---
id: UNC@20.15.2@MMLCommand@LST IPALLOCBYLOCGLBSW
type: MMLCommand
name: LST IPALLOCBYLOCGLBSW（查询基于位置区地址分配的全局开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IPALLOCBYLOCGLBSW
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
- 基于位置区地址分配开关配置
status: active
---

# LST IPALLOCBYLOCGLBSW（查询基于位置区地址分配的全局开关）

## 功能

**适用NF：PGW-C、GGSN、SMF**

该命令用于查询基于位置区地址分配的全局开关。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IPALLOCBYLOCGLBSW]] · 基于位置区地址分配的全局开关（IPALLOCBYLOCGLBSW）

## 使用实例

查询基于位置区地址分配的全局开关：

```
%%LST IPALLOCBYLOCGLBSW:;%%
RETCODE = 0 操作成功

结果如下
-----------
基于位置区地址分配的IPv4全局开关 = 使能
基于位置区地址分配的IPv6全局开关 = 使能
(结果个数 = 1)

---      END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-IPALLOCBYLOCGLBSW.md`
