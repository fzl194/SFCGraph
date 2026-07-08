---
id: UDG@20.15.2@MMLCommand@LST TOSERVERIPBYPASS
type: MMLCommand
name: LST TOSERVERIPBYPASS（查询异常Server IP自动bypass功能配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TOSERVERIPBYPASS
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- TCP优化服务管理
- 异常Server IP地址bypass功能
status: active
---

# LST TOSERVERIPBYPASS（查询异常Server IP自动bypass功能配置）

## 功能

**适用NF：UPF**

该命令用于查询异常Server IP自动bypass功能配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [异常Server IP自动bypass功能配置（TOSERVERIPBYPASS）](configobject/UDG/20.15.2/TOSERVERIPBYPASS.md)

## 使用实例

查询异常Server IP自动bypass功能配置：

```
LST TOSERVERIPBYPASS:;
```

```

RETCODE = 0  操作成功
 
异常Server IP自动bypass配置
-------------
异常Server IP自动bypass功能开关  =  ENABLE
老化时间（秒） =  86400
异常状态重置为初始状态时间（秒） =  21600
 
(结果个数 = 1)
 
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询异常Server-IP自动bypass功能配置（LST-TOSERVERIPBYPASS）_27956239.md`
