---
id: UNC@20.15.2@MMLCommand@LST VLRFAULTEN
type: MMLCommand
name: LST VLRFAULTEN（查询VLR故障增强功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: VLRFAULTEN
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 可靠性管理
- VLR故障增强功能
status: active
---

# LST VLRFAULTEN（查询VLR故障增强功能）

## 功能

**适用网元：MME**

该命令用于查询VLR全故障场景增强功能开关。

## 注意事项

无。

## 权限

manage-ug;system-ug;monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/VLRFAULTEN]] · VLR故障增强功能（VLRFAULTEN）

## 使用实例

查询VLR全故障场景增强功能开关信息：

```
LST VLRFAULTEN:;
```

```
查询结果如下
-------------------------
   VLR故障增强功能开关  =  关闭
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-VLRFAULTEN.md`
