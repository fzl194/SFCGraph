---
id: UDG@20.15.2@MMLCommand@LST LINKALMCFG
type: MMLCommand
name: LST LINKALMCFG（查询TWAMP的Light模式“链路丢包率过高告警”配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: LINKALMCFG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPAPM功能管理
- TWAMP
- IPAPM链路告警配置
status: active
---

# LST LINKALMCFG（查询TWAMP的Light模式“链路丢包率过高告警”配置）

## 功能

该命令用于查询TWAMP的Light模式“ALM-100395 链路丢包率过高告警”配置。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@LINKALMCFG]] · TWAMP的Light模式“链路丢包率过高告警”配置（LINKALMCFG）

## 使用实例

查询TWAMP链路告警配置的实例：

```
%%LST LINKALMCFG:;%%
RETCODE = 0  操作成功
 
结果如下
--------
    阈值  =  10
恢复阈值  =  5
检测周期  =  30
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-LINKALMCFG.md`
