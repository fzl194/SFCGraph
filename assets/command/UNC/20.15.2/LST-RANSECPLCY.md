---
id: UNC@20.15.2@MMLCommand@LST RANSECPLCY
type: MMLCommand
name: LST RANSECPLCY（查询RAN侧安全策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RANSECPLCY
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 会话协议参数管理
- 会话策略管理
- 5GC用户面安全策略管理
status: active
---

# LST RANSECPLCY（查询RAN侧安全策略）

## 功能

**适用NF：SMF**

该命令用于查询RAN侧用户面安全策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [RAN侧安全策略（RANSECPLCY）](configobject/UNC/20.15.2/RANSECPLCY.md)

## 使用实例

用户需要查看配置的用户安全策略参数时，执行如下命令:

```
%%LST RANSECPLCY:;%%
RETCODE = 0  操作成功

结果如下
------------------------
             完整性保护策略  =  优先从签约数据获取
         本地完整性保护指示  =  优选
          完整性保护PDU策略  =  限速 
               加密保护策略  =  优先从签约数据获取
           本地加密保护指示  =  优选
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询RAN侧安全策略（LST-RANSECPLCY）_09653115.md`
