---
id: UNC@20.15.2@MMLCommand@LST TCTIMER
type: MMLCommand
name: LST TCTIMER（查询TC定时器）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: TCTIMER
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- Diameter管理
- 公共参数
- Diameter公共参数
status: active
---

# LST TCTIMER（查询TC定时器）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询Diameter TC定时器。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [TC定时器（TCTIMER）](configobject/UNC/20.15.2/TCTIMER.md)

## 使用实例

查询Diameter TC定时器，则可以按如下配置：

```
LST TCTIMER:;
```

```

RETCODE = 0  操作成功。

TC定时器配置
------------
TC定时器时长（单位500ms）  =  3
               定时器模式  =  固定方式
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询TC定时器（LST-TCTIMER）_09897237.md`
