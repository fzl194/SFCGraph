---
id: UDG@20.15.2@MMLCommand@LST AFMATCHCFG
type: MMLCommand
name: LST AFMATCHCFG（查询软参欺诈场景开关状态）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: AFMATCHCFG
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务防欺诈
- HTTP欺诈场景的匹配情况统计
status: active
---

# LST AFMATCHCFG（查询软参欺诈场景开关状态）

## 功能

**适用NF：PGW-U、UPF**

该命令用来查询软参场景欺诈统计功能开关。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/AFMATCHCFG]] · 软参欺诈场景开关状态（AFMATCHCFG）

## 使用实例

查询软参场景欺诈统计功能配置信息：

```
LST AFMATCHCFG:;
```

```

RETCODE = 0  操作成功。

软参欺诈场景开关状态
--------------------
软参欺诈场景功能开关  =  使能
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-AFMATCHCFG.md`
