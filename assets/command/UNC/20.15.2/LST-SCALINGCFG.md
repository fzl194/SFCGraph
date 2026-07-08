---
id: UNC@20.15.2@MMLCommand@LST SCALINGCFG
type: MMLCommand
name: LST SCALINGCFG（查询自动扩缩容配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SCALINGCFG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 编排管理
- 弹性开关
status: active
---

# LST SCALINGCFG（查询自动扩缩容配置）

## 功能

此命令用于查询自动扩缩容的相关参数设置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [自动扩缩容配置（SCALINGCFG）](configobject/UNC/20.15.2/SCALINGCFG.md)

## 使用实例

LST SCALINGCFG:;

```
%%LST SCALINGCFG:;%%
RETCODE = 0  操作成功 
结果如下 
-------- 
扩容门槛 = 81
缩容门槛 = 19
扩缩容步进方式 = PodNumber
扩缩容步长 = 48
(结果个数 = 1) 
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询自动扩缩容配置（LST-SCALINGCFG）_09587906.md`
