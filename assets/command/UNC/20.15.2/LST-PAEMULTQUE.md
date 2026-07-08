---
id: UNC@20.15.2@MMLCommand@LST PAEMULTQUE
type: MMLCommand
name: LST PAEMULTQUE（查询PAE多队列功能开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PAEMULTQUE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 配置
status: active
---

# LST PAEMULTQUE（查询PAE多队列功能开关）

## 功能

该命令用于查询PAE多队列功能是否使能。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [PAE多队列功能开关（PAEMULTQUE）](configobject/UNC/20.15.2/PAEMULTQUE.md)

## 使用实例

查询PAE多队列功能开关：

```
%%LST PAEMULTQUE:;%%
RETCODE = 0  操作成功

结果如下:
---------
功能是否开启  =  是
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询PAE多队列功能开关（LST-PAEMULTQUE）_11416582.md`
