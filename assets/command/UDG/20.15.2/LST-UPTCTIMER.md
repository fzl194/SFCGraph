---
id: UDG@20.15.2@MMLCommand@LST UPTCTIMER
type: MMLCommand
name: LST UPTCTIMER（查询TC定时器）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UPTCTIMER
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- Diameter管理
- Diameter公共参数
status: active
---

# LST UPTCTIMER（查询TC定时器）

## 功能

**适用NF：UPF**

该命令用于查询Diameter TC定时器。

## 注意事项

该命令相关的功能当前版本暂不支持。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPTCTIMER]] · TC定时器（UPTCTIMER）

## 使用实例

查询Diameter TC定时器，则可以按如下配置：

```
LST UPTCTIMER:;
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

- 原始手册：`evidence/UDG/20.15.2/查询TC定时器（LST-UPTCTIMER）_45195168.md`
