---
id: UNC@20.15.2@MMLCommand@LST DRCOUPLINGRESET
type: MMLCommand
name: LST DRCOUPLINGRESET（查询负荷分担容灾功能开启信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DRCOUPLINGRESET
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# LST DRCOUPLINGRESET（查询负荷分担容灾功能开启信息）

## 功能

该命令用于查询负荷分担容灾功能开启信息。

## 注意事项

该命令只用于在UEG-M/UEG-L/UEG采用负荷分担容灾模式下执行。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DRCOUPLINGRESET]] · 负荷分担容灾功能开启信息（DRCOUPLINGRESET）

## 使用实例

查询负荷分担容灾功能开启信息：

```
%%LST DRCOUPLINGRESET:;%%
RETCODE = 0  操作成功

结果如下
--------
是否使能负荷分担容灾功能 =  否
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-DRCOUPLINGRESET.md`
