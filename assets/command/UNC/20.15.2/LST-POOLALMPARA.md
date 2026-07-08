---
id: UNC@20.15.2@MMLCommand@LST POOLALMPARA
type: MMLCommand
name: LST POOLALMPARA（查询本地地址池使用率告警参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: POOLALMPARA
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
- 地址池使用率告警配置
status: active
---

# LST POOLALMPARA（查询本地地址池使用率告警参数）

## 功能

**适用NF：PGW-C、SMF、GGSN**

此命令用于查询本地地址池使用率告警的产生阈值和恢复阈值。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [本地地址池使用率告警参数（POOLALMPARA）](configobject/UNC/20.15.2/POOLALMPARA.md)

## 使用实例

查询本地地址池使用率告警的产生阈值和恢复阈值，执行命令如下： LST POOLALMPARA:;

```
%%LST POOLALMPARA:;%%
RETCODE = 0  操作成功。

结果如下
--------------------
   告警产生阈值 （%）  =  80
   告警恢复阈值 （%）  =  70
地址池资源过载告警开关 = 使能
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询本地地址池使用率告警参数（LST-POOLALMPARA）_37497449.md`
