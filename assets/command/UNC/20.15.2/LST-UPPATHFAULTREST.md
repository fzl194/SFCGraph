---
id: UNC@20.15.2@MMLCommand@LST UPPATHFAULTREST
type: MMLCommand
name: LST UPPATHFAULTREST（查询用户面链路故障恢复功能配置信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UPPATHFAULTREST
command_category: 查询类
applicable_nf:
- SMF
- SGW-C
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 可靠性管理
- N3_N9链路故障恢复
status: active
---

# LST UPPATHFAULTREST（查询用户面链路故障恢复功能配置信息）

## 功能

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用于查询用户面链路（N3/N9）故障恢复功能配置信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/UPPATHFAULTREST]] · 用户面链路故障恢复功能配置信息（UPPATHFAULTREST）

## 使用实例

查询用户面链路故障恢复功能配置信息：

```
%%LST UPPATHFAULTREST:;%%
RETCODE = 0  操作成功

结果如下
--------
       SMF是否支持用户面链路故障恢复  =  使能
双栈用户面链路仅IPv4故障是否删除会话  =  不使能
双栈用户面链路仅IPv6故障是否删除会话  =  使能
          支持同时处理的故障链路数量  =  5
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询用户面链路故障恢复功能配置信息（LST-UPPATHFAULTREST）_45986071.md`
