---
id: UDG@20.15.2@MMLCommand@LST LOWLATENCYSW
type: MMLCommand
name: LST LOWLATENCYSW（查询低时延业务开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: LOWLATENCYSW
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 体验分级
- 体验分级全局参数
- 低时延业务开关
status: active
---

# LST LOWLATENCYSW（查询低时延业务开关）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询低时延业务开关。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/LOWLATENCYSW]] · 低时延业务开关（LOWLATENCYSW）

## 使用实例

查询低时延业务开关：

```
%%LST LOWLATENCYSW:;
```

```
%%
RETCODE = 0 操作成功

低时延业务开关
--------------
低时延业务开关 = 不使能
(结果个数 = 1)

--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询低时延业务开关（LST-LOWLATENCYSW）_68962489.md`
