---
id: UDG@20.15.2@MMLCommand@DSP FESMEMLIMIT
type: MMLCommand
name: DSP FESMEMLIMIT（显示FES内存界限信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: FESMEMLIMIT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎服务
- 显示FES内存界限信息
status: active
---

# DSP FESMEMLIMIT（显示FES内存界限信息）

## 功能

该命令用于显示FES内存界限信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@FESMEMLIMIT]] · FES内存界限信息（FESMEMLIMIT）

## 使用实例

显示FES内存界限信息：

```
DSP FESMEMLIMIT:;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
               RU号  =  66
       内存过载状态  =  正常状态
       过载状态标记  =  正常状态
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-FESMEMLIMIT.md`
