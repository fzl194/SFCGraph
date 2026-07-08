---
id: UDG@20.15.2@MMLCommand@LST PWDBLACKLIST
type: MMLCommand
name: LST PWDBLACKLIST（查询密码禁用词）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PWDBLACKLIST
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务平台功能管理
- 操作维护
- 用户管理
- 密码黑名单
status: active
---

# LST PWDBLACKLIST（查询密码禁用词）

## 功能

该命令用于查看密码禁用词。

## 注意事项

无。

## 权限

G_1，管理员级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/PWDBLACKLIST]] · 密码禁用词（PWDBLACKLIST）

## 使用实例

查询密码禁用词：

```
LST PWDBLACKLIST:;
```

```
RETCODE = 0  操作成功

结果如下:
-------------------------
密码禁用词 = a
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询密码禁用词（LST-PWDBLACKLIST）_59036662.md`
