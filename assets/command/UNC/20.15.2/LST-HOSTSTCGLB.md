---
id: UNC@20.15.2@MMLCommand@LST HOSTSTCGLB
type: MMLCommand
name: LST HOSTSTCGLB（查询全局协议报文统计配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: HOSTSTCGLB
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IP协议统计
- 主机报文统计
- 统计功能配置
status: active
---

# LST HOSTSTCGLB（查询全局协议报文统计配置）

## 功能

该命令用于查询全局协议报文统计配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/HOSTSTCGLB]] · 全局协议报文统计配置（HOSTSTCGLB）

## 使用实例

查询全局协议报文统计配置：

```
LST HOSTSTCGLB:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
协议报文统计功能状态  =  使能
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询全局协议报文统计配置（LST-HOSTSTCGLB）_49802002.md`
