---
id: UNC@20.15.2@MMLCommand@LST SMARTCL
type: MMLCommand
name: LST SMARTCL（查询智能分流功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMARTCL
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
- 会话管理
- 智能分流管理
status: active
---

# LST SMARTCL（查询智能分流功能）

## 功能

**适用网元：MME**

该命令用于查询智能分流功能参数。

## 注意事项

无。

## 权限

manage-ug;system-ug;monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMARTCL]] · 智能分流功能（SMARTCL）

## 使用实例

查询智能分流功能参数：

```
LST SMARTCL:;
```

```
查询结果如下
-------------------------
                 智能分流开关  =  打开
            APN智能分流关键字  =  multidomain
APN智能分流关键字定制标识位置  =  BEFORE
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SMARTCL.md`
