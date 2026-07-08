---
id: UDG@20.15.2@MMLCommand@LST GLBCFTEMPLATE
type: MMLCommand
name: LST GLBCFTEMPLATE（查询全局内容过滤模板）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: GLBCFTEMPLATE
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 内容过滤
- 全局内容过滤模板绑定配置
status: active
---

# LST GLBCFTEMPLATE（查询全局内容过滤模板）

## 功能

**适用NF：PGW-U、UPF**

该命令用于显示配置的全局的内容过滤模板。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/GLBCFTEMPLATE]] · 全局内容过滤模板（GLBCFTEMPLATE）

## 使用实例

显示配置的全局的内容过滤模板：

```
LST GLBCFTEMPLATE:;
```

```

RETCODE = 0  操作成功
 
全局内容过滤模板信息
--------------------
内容过滤模板名称  =  test
(结果个数 = 1)
 
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-GLBCFTEMPLATE.md`
