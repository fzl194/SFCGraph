---
id: UNC@20.15.2@MMLCommand@LST UPCCOMMTIMER
type: MMLCommand
name: LST UPCCOMMTIMER（查询用户面控制通用定时器）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UPCCOMMTIMER
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
- 接口管理
- PFCP接口管理
- 用户面控制通用定时器管理
status: active
---

# LST UPCCOMMTIMER（查询用户面控制通用定时器）

## 功能

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用于查询用户面控制通用定时器的时长。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@UPCCOMMTIMER]] · 用户面控制通用定时器（UPCCOMMTIMER）

## 使用实例

查询用户面控制通用定时器时长，执行如下命令：

```
%%LST UPCCOMMTIMER:;%%
RETCODE = 0  操作成功

结果如下
------------------------
转发隧道不活动定时器时长(秒)  =  4
        延迟释放定时器(毫秒)  =  1000
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-UPCCOMMTIMER.md`
