---
id: UDG@20.15.2@MMLCommand@LST DRKEYNF
type: MMLCommand
name: LST DRKEYNF（查询监控的关键部件信息）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: DRKEYNF
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# LST DRKEYNF（查询监控的关键部件信息）

## 功能

该命令用于查询监控的关键部件信息。

> **说明**
> - 该命令只用于在UEG-L/UEN网元采用主备（冷备）容灾模式下执行。
> - 该命令只用于在UEG-M/UEG-L/UEG采用负荷分担容灾模式下执行。
> - 该命令只用于在UEG-M/UEG网元采用主备（热备）容灾模式下执行。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@DRKEYNF]] · 监控的关键部件信息（DRKEYNF）

## 使用实例

查询监控的关键网元部件信息：

```
%%LST DRKEYNF:;%%
RETCODE = 0  操作成功
结果如下
--------
是否监控MME服务   =  是
是否监控AMF服务   =  是
是否监控HSS服务   =  是
是否监控UDM服务   =  是
是否监控GW-C服务  =  是
是否监控SMF服务   =  是
是否监控PCF服务   =  是
是否监控PCRF服务  =  是
是否监控UPF服务   =  是
是否监控UDR服务   =  是
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-DRKEYNF.md`
