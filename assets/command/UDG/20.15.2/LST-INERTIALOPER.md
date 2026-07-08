---
id: UDG@20.15.2@MMLCommand@LST INERTIALOPER
type: MMLCommand
name: LST INERTIALOPER（查询惯性运行功能配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: INERTIALOPER
command_category: 查询类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话信息管理
- 业务惯性运行
status: active
---

# LST INERTIALOPER（查询惯性运行功能配置）

## 功能

**适用NF：UPF**

该命令用于查询惯性运行功能的配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/INERTIALOPER]] · 惯性运行功能配置（INERTIALOPER）

## 使用实例

查询惯性运行功能配置：

```
LST INERTIALOPER:;
```

```

RETCODE = 0  执行成功

业务惯性运行配置
---------------------------
数据面非连接态用户是否支持惯性运行功能  =  ENABLE
PFCP路径断后进入惯性运行的时间  =  30
非5G用户是否支持惯性运行功能开关 = DISABLE
多路径场景下路径异常时是否支持用户在线 = DISABLE
(Number of results = 1)
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-INERTIALOPER.md`
