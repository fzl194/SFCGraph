---
id: UDG@20.15.2@MMLCommand@DSP APPCLTSTATUS
type: MMLCommand
name: DSP APPCLTSTATUS（查询第三方APP信息采集进度）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: APPCLTSTATUS
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- SFIP管理
- 第三方应用调测
- 信息采集进度
status: active
---

# DSP APPCLTSTATUS（查询第三方APP信息采集进度）

## 功能

该命令用于查询第三方APP信息采集进度。

## 注意事项

- 该命令执行后立即生效。
- 该命令当前仅支持第三方APP。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@APPCLTSTATUS]] · 第三方APP信息采集进度（APPCLTSTATUS）

## 使用实例

查询第三方应用信息采集的进度：

```
DSP APPCLTSTATUS:;
```

```

RETCODE = 0  操作成功

执行百分比
----------
  执行百分比  =  100
执行阶段信息  =  NULL
执行详细信息  =  No found the collect information task.
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-APPCLTSTATUS.md`
