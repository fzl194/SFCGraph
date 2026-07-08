---
id: UDG@20.15.2@MMLCommand@LST PAEEXAMINATION
type: MMLCommand
name: LST PAEEXAMINATION（查询PAE故障检测使能配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PAEEXAMINATION
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 配置
status: active
---

# LST PAEEXAMINATION（查询PAE故障检测使能配置）

## 功能

该命令用于查询PAE故障检测功能使能状态。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/PAEEXAMINATION]] · PAE故障检测使能配置（PAEEXAMINATION）

## 使用实例

查询所有微服务的PAE故障检测功能使能状态：

```
LST PAEEXAMINATION:;
```

```
RETCODE = 0  操作成功。

结果如下
---------
使能标志  =  是      
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询PAE故障检测使能配置（LST-PAEEXAMINATION）_92520049.md`
