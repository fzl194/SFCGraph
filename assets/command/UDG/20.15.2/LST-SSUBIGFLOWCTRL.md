---
id: UDG@20.15.2@MMLCommand@LST SSUBIGFLOWCTRL
type: MMLCommand
name: LST SSUBIGFLOWCTRL（查询智能板的大流判断速率阈值）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SSUBIGFLOWCTRL
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 智能板管理
- vvip
- 大流控制速率
status: active
---

# LST SSUBIGFLOWCTRL（查询智能板的大流判断速率阈值）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询智能板的大流判断速率阈值。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [智能板的大流判断速率阈值（SSUBIGFLOWCTRL）](configobject/UDG/20.15.2/SSUBIGFLOWCTRL.md)

## 使用实例

查询智能板的大流判断速率阈值：

```
%%LST SSUBIGFLOWCTRL:;
```

```
%%
RETCODE = 0  操作成功

查询智能板的大流判断速率阈值
----------------------------
VVIP业务大流速率（千比特/秒）  =  800
 CCO业务大流速率（千比特/秒）  =  800
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询智能板的大流判断速率阈值（LST-SSUBIGFLOWCTRL）_28361127.md`
