---
id: UDG@20.15.2@MMLCommand@LST LSPVGLOBALCFG
type: MMLCommand
name: LST LSPVGLOBALCFG（查询LSPV全局属性）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: LSPVGLOBALCFG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 系统管理
- 系统维护
- Ping和Tracert
- LSPV
status: active
---

# LST LSPVGLOBALCFG（查询LSPV全局属性）

## 功能

该命令用于查询LSPV全局属性。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [LSPV全局属性（LSPVGLOBALCFG）](configobject/UDG/20.15.2/LSPVGLOBALCFG.md)

## 使用实例

查询LSPV全局配置：

```
LST LSPVGLOBALCFG:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
     LSPV响应端  =  使能
最大速率（pps）  =  1000
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询LSPV全局属性（LST-LSPVGLOBALCFG）_00866665.md`
