---
id: UNC@20.15.2@MMLCommand@LST LBTNIPINIPSWITCH
type: MMLCommand
name: LST LBTNIPINIPSWITCH（查询CSLB隧道IP-in-IP开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LBTNIPINIPSWITCH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 业务管理
- 隧道管理
- CSLB隧道探测参数
status: active
---

# LST LBTNIPINIPSWITCH（查询CSLB隧道IP-in-IP开关）

## 功能

该命令用于查询CSLB隧道IP-in-IP功能开关配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [CSLB隧道IP-in-IP开关（LBTNIPINIPSWITCH）](configobject/UNC/20.15.2/LBTNIPINIPSWITCH.md)

## 使用实例

查询CSLB隧道IP-in-IP功能开关的配置，命令如下：

```
%%LST LBTNIPINIPSWITCH:;%%
RETCODE = 0  操作成功

操作结果如下：
--------------
CSLB隧道IP-in-IP配置开关  =  CSLB隧道IP-in-IP开启
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询CSLB隧道IP-in-IP开关（LST-LBTNIPINIPSWITCH）_21904504.md`
