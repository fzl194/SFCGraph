---
id: UDG@20.15.2@MMLCommand@LST INSAFEATTMOUT
type: MMLCommand
name: LST INSAFEATTMOUT（查询流特征节点超时时间）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: INSAFEATTMOUT
command_category: 查询类
applicable_nf:
- CloudEPSN
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 智能SA管理
- 流特征节点超时时间配置
status: active
---

# LST INSAFEATTMOUT（查询流特征节点超时时间）

## 功能

**适用NF：CloudEPSN**

查询流特征节点超时时间。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [流特征节点超时时间（INSAFEATTMOUT）](configobject/UDG/20.15.2/INSAFEATTMOUT.md)

## 使用实例

查询当前流特征节点超时时间：

```
LST INSAFEATTMOUT:;
```

```

 
INSAFEATTMOUT信息
------
      超时时间(秒) = 30
 
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询流特征节点超时时间（LST-INSAFEATTMOUT）_93024011.md`
