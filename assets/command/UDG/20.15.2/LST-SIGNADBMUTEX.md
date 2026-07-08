---
id: UDG@20.15.2@MMLCommand@LST SIGNADBMUTEX
type: MMLCommand
name: LST SIGNADBMUTEX（显示特征库规则加载区域ID）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SIGNADBMUTEX
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 协议识别
- 特征库管理
- SA特征库规则加载条件
- 特征库规则加载条件相关配置
status: active
---

# LST SIGNADBMUTEX（显示特征库规则加载区域ID）

## 功能

**适用NF：PGW-U、UPF**

该命令用于显示配置的特征库的加载条件。

## 注意事项

启用之前需要先和华为工程师联系，确认当前知识库是否支持，以及需要配置的area-id和mutex-id。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/SIGNADBMUTEX]] · 特征库规则加载区域ID（SIGNADBMUTEX）

## 使用实例

查询特征库的加载条件：

```
LST SIGNADBMUTEX:;
```

```

RETCODE = 0 操作成功.

SA特征库加载条件信息
---------------------------------------------------------------------
分类ID = 2
区域ID = 1
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-SIGNADBMUTEX.md`
