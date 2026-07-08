---
id: UDG@20.15.2@MMLCommand@LST CUINCONSPOLICY
type: MMLCommand
name: LST CUINCONSPOLICY（查询CP和UP关键配置不一致的处理策略）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: CUINCONSPOLICY
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 配置校验控制
- CP和UP关键配置不一致策略
status: active
---

# LST CUINCONSPOLICY（查询CP和UP关键配置不一致的处理策略）

## 功能

**适用NF：PGW-U、UPF**

查询SMF/PGW-C和UPF/PGW-U关键配置不一致的处理策略。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/CUINCONSPOLICY]] · CP和UP关键配置不一致的处理策略（CUINCONSPOLICY）

## 使用实例

查询SMF/PGW-C和UPF/PGW-U关键配置不一致处理策略：

```
LST CUINCONSPOLICY:;
```

```

RETCODE = 0 操作成功。

CP和UP关键配置不一致策略
------------------------
旁路处理开关 = 使能
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询CP和UP关键配置不一致的处理策略（LST-CUINCONSPOLICY）_64015289.md`
