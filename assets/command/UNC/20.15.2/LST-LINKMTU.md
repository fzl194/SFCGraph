---
id: UNC@20.15.2@MMLCommand@LST LINKMTU
type: MMLCommand
name: LST LINKMTU（查询Link MTU值）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LINKMTU
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 本局信息管理
- SMF
- LINKMTU
status: active
---

# LST LINKMTU（查询Link MTU值）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查询设置的Link MTU值。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/LINKMTU]] · Link MTU值（LINKMTU）

## 使用实例

查询Link MTU配置：

```
%%LST LINKMTU:;%%
RETCODE = 0  操作成功

结果如下
------------------------
携带Link MTU开关  =  Enable
   IPv4 Link MTU  =  1358
 Non-IP Link MTU  =  1358
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Link-MTU值（LST-LINKMTU）_35519271.md`
