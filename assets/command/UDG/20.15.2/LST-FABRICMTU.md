---
id: UDG@20.15.2@MMLCommand@LST FABRICMTU
type: MMLCommand
name: LST FABRICMTU（查询PAE内联口MTU值）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: FABRICMTU
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

# LST FABRICMTU（查询PAE内联口MTU值）

## 功能

该命令用于查询PAE内联口MTU。

通过查询PAE内联口MTU值，方便故障诊断。

## 注意事项

- 该命令仅适用于非NP卡场景、NP卡非加速模式场景，以及NP卡ECMP组网模式下的fabric平面。
- 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/FABRICMTU]] · PAE内联口MTU值（FABRICMTU）

## 使用实例

查询PAE内联口MTU值：

```
%%LST FABRICMTU:;%%
RETCODE = 0  操作成功

结果如下:
---------
MTU值（byte）  =  1800
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询PAE内联口MTU值（LST-FABRICMTU）_32426909.md`
