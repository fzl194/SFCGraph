---
id: UNC@20.15.2@MMLCommand@LST MPLSSITE
type: MMLCommand
name: LST MPLSSITE（查询MPLS全局配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MPLSSITE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- MPLS管理
- MPLS基础
- MPLS全局配置
status: active
---

# LST MPLSSITE（查询MPLS全局配置）

## 功能

该命令用于查询MPLS全局配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/MPLSSITE]] · MPLS全局配置（MPLSSITE）

## 使用实例

查询MPLS全局配置：

```
LST MPLSSITE:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
MPLS LSR ID  =  192.168.1.1
   MPLS能力  =  DISABLE
    LDP能力  =  DISABLE
 空标签类型  =  隐式空标签
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-MPLSSITE.md`
