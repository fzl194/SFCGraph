---
id: UNC@20.15.2@MMLCommand@LST PODCPUTHD
type: MMLCommand
name: LST PODCPUTHD（查询POD CPU阈值）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PODCPUTHD
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统管理
- 资源管理
status: active
---

# LST PODCPUTHD（查询POD CPU阈值）

## 功能

该命令用于查询POD CPU阈值。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅在FusionStage裸机容器下支持。

## 权限

G_1，管理员级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PODCPUTHD]] · POD CPU阈值（PODCPUTHD）

## 使用实例

查询POD CPU告警阈值。

```
%%LST PODCPUTHD:;%%
RETCODE = 0  操作成功

结果如下
------------------------
告警上报门限  =  80
告警恢复门限  =  70
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PODCPUTHD.md`
