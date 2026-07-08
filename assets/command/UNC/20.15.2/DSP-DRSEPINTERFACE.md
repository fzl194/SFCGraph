---
id: UNC@20.15.2@MMLCommand@DSP DRSEPINTERFACE
type: MMLCommand
name: DSP DRSEPINTERFACE（显示故障隔离逻辑接口的状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DRSEPINTERFACE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# DSP DRSEPINTERFACE（显示故障隔离逻辑接口的状态）

## 功能

该命令用于查询添加故障隔离的逻辑接口的管理状态。

## 注意事项

该命令只用于在UEG-M/UEG网元采用主备（热备）容灾模式下执行。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/DRSEPINTERFACE]] · 故障隔离接口（DRSEPINTERFACE）

## 使用实例

查询添加故障隔离的逻辑接口的管理状态。

```
%%DSP DRSEPINTERFACE:;%%
RETCODE = 0  操作成功

结果如下
--------
        接口名  =  itf1
      管理状态  =  开启
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示故障隔离逻辑接口的状态（DSP-DRSEPINTERFACE）_86030325.md`
