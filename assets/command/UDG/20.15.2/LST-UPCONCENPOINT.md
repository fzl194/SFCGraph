---
id: UDG@20.15.2@MMLCommand@LST UPCONCENPOINT
type: MMLCommand
name: LST UPCONCENPOINT（查询集中点部署模式）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UPCONCENPOINT
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- Diameter管理
- 集中点模式
status: active
---

# LST UPCONCENPOINT（查询集中点部署模式）

## 功能

**适用NF：UPF**

此命令用于查询集中点的部署模式。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@UPCONCENPOINT]] · 集中点部署模式（UPCONCENPOINT）

## 使用实例

查询集中点部署模式：

```
LST UPCONCENPOINT:;
```

```

RETCODE = 0  操作成功。
集中点信息
----------
 Swm集中点模式  =  本端IP和Diameter对端主机名
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-UPCONCENPOINT.md`
