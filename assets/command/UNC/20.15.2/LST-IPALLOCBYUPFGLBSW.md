---
id: UNC@20.15.2@MMLCommand@LST IPALLOCBYUPFGLBSW
type: MMLCommand
name: LST IPALLOCBYUPFGLBSW（查询基于UPF地址分配的全局开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IPALLOCBYUPFGLBSW
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UE地址管理
- UE地址池管理
- 基于UPF地址分配开关配置
status: active
---

# LST IPALLOCBYUPFGLBSW（查询基于UPF地址分配的全局开关）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询基于UPF地址分配的全局开关。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/IPALLOCBYUPFGLBSW]] · 基于UPF地址分配的全局开关（IPALLOCBYUPFGLBSW）

## 使用实例

查询基于UPF地址分配的全局开关：

```
%%LST IPALLOCBYUPFGLBSW:;%%
RETCODE = 0 操作成功

结果如下
-----------------------------------------------
基于UPF分配IPv4地址的全局开关  =  使能
基于UPF分配IPv6地址的全局开关  =  使能
(结果个数 = 1)

--- END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-IPALLOCBYUPFGLBSW.md`
