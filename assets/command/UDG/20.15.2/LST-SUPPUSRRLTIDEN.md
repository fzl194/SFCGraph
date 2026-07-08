---
id: UDG@20.15.2@MMLCommand@LST SUPPUSRRLTIDEN
type: MMLCommand
name: LST SUPPUSRRLTIDEN（查询支持用户关联识别协议）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SUPPUSRRLTIDEN
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 三四层规则管理
- 支持用户关联识别协议
status: active
---

# LST SUPPUSRRLTIDEN（查询支持用户关联识别协议）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询支持用户关联识别功能的协议列表。在配置用户关联识别功能时，运营商需要查询支持该功能的协议时执行该命令。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [支持用户关联识别协议（SUPPUSRRLTIDEN）](configobject/UDG/20.15.2/SUPPUSRRLTIDEN.md)

## 使用实例

显示所有支持用户关联识别的协议：

```
LST SUPPUSRRLTIDEN:;
```

```

RETCODE = 0  操作成功。

支持用户关联识别协议信息
------------------------
子协议名称                 应用协议名称           

facebook_messenger_voip    facebook_messenger_voip
facebook_others            facebook               
niantic_data               niantic                
pokemongo_data             pokemongo              
(结果个数 = 4)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询支持用户关联识别协议（LST-SUPPUSRRLTIDEN）_82837438.md`
