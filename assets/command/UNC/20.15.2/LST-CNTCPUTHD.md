---
id: UNC@20.15.2@MMLCommand@LST CNTCPUTHD
type: MMLCommand
name: LST CNTCPUTHD（查询容器CPU阈值）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CNTCPUTHD
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统管理
- 资源管理
status: active
---

# LST CNTCPUTHD（查询容器CPU阈值）

## 功能

该命令用于查询容器CPU阈值。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CNTCPUTHD]] · 容器CPU阈值（CNTCPUTHD）

## 使用实例

查询容器CPU告警阈值。

```
%%LST CNTCPUTHD:;%%
RETCODE = 0  操作成功

结果如下
------------------------
告警上报门限  =  90
告警恢复门限  =  80
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CNTCPUTHD.md`
