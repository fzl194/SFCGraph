---
id: UDG@20.15.2@MMLCommand@LST HAFEDETECT
type: MMLCommand
name: LST HAFEDETECT（查询HAFETCD网络亚健康探测参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: HAFEDETECT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# LST HAFEDETECT（查询HAFETCD网络亚健康探测参数）

## 功能

该命令用于查询HAFETCD网络亚健康探测功能的开关、探测发包间隔、丢错包阈值、租约到期阈值、统计周期等参数。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/HAFEDETECT]] · HAFETCD网络亚健康探测参数（HAFEDETECT）

## 使用实例

查询HAFETCD网络亚健康探测参数。

```
%%LST HAFEDETECT:;%%
RETCODE = 0  操作成功

结果如下
--------
   探测功能开关  =  开启
探测间隔(100ms)  =  5
 亚健康阈值(‰)  =  300
租约到期阈值(%)  =  50
    统计周期(s)  =  30
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-HAFEDETECT.md`
