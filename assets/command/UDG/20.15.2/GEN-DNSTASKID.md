---
id: UDG@20.15.2@MMLCommand@GEN DNSTASKID
type: MMLCommand
name: GEN DNSTASKID（生成任务ID）
nf: UDG
version: 20.15.2
verb: GEN
object_keyword: DNSTASKID
command_category: 调测类
applicable_nf:
- CloudEPSN
effect_mode: ''
is_dangerous: false
category_path:
- SFIP管理
- 第三方应用管理
- DNS配置任务管理
status: active
---

# GEN DNSTASKID（生成任务ID）

## 功能

**适用NF：CloudEPSN**

该命令用于生成一个任务ID，该任务ID用来在后续资源操作时作为标识信息。

## 注意事项

- 最多有5个任务同时处于处理流程中。
- 该命令生成的任务ID，用于作为后续资源操作命令下发时携带的标识信息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/DNSTASKID]] · 生成任务ID（DNSTASKID）

## 使用实例

产生一个任务ID：

```
%%GEN DNSTASKID:;%%
RETCODE = 0  操作成功

结果如下
--------
任务ID  =  1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/生成任务ID（GEN-DNSTASKID）_61928566.md`
