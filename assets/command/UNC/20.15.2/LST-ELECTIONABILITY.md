---
id: UNC@20.15.2@MMLCommand@LST ELECTIONABILITY
type: MMLCommand
name: LST ELECTIONABILITY（查询业务进程选举能力）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ELECTIONABILITY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# LST ELECTIONABILITY（查询业务进程选举能力）

## 功能

该命令已废弃。

该命令用于查询业务进程选举能力的开关。

## 注意事项

无

## 权限

G_1，管理员级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/ELECTIONABILITY]] · 业务进程选举能力（ELECTIONABILITY）

## 使用实例

查询客户端选举能力使能状态。

```
LST ELECTIONABILITY;
RETCODE = 0  操作成功

结果如下
------------------------
业务进程选举能力使能开关  =  开启
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询业务进程选举能力（LST-ELECTIONABILITY）_42938063.md`
