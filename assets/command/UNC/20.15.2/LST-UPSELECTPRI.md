---
id: UNC@20.15.2@MMLCommand@LST UPSELECTPRI
type: MMLCommand
name: LST UPSELECTPRI（查询UPF选择策略次序）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UPSELECTPRI
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- UPF选择策略次序
status: active
---

# LST UPSELECTPRI（查询UPF选择策略次序）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查询SMF选择UPF场景下的UPF选择策略次序。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@UPSELECTPRI]] · UPF选择策略次序（UPSELECTPRI）

## 使用实例

查询SMF选择UPF场景下的优选条件： LST UPSELECTPRI:;

```
%%LST UPSELECTPRI:;%%
RETCODE = 0  操作成功。

结果如下
------------------------
第一优先级  =  LocS11Priority
第二优先级  =  Combined UPF
第三优先级  =  Load Balancing Policy
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-UPSELECTPRI.md`
