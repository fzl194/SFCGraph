---
id: UDG@20.15.2@MMLCommand@LST DNSINFO
type: MMLCommand
name: LST DNSINFO（查询DNS信息）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: DNSINFO
command_category: 查询类
applicable_nf:
- CloudEPSN
effect_mode: ''
is_dangerous: false
category_path:
- SFIP管理
- 第三方应用管理
- DNS公共配置管理
status: active
---

# LST DNSINFO（查询DNS信息）

## 功能

**适用NF：CloudEPSN**

该命令用于查询具有API权限和管理员权限的用户名和密码、配置模板信息、最后一次修改这些信息的时间。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/DNSINFO]] · DNS信息（DNSINFO）

## 使用实例

查询具有API权限和管理员权限的用户名和密码、配置模板名称、最后一次修改这些信息的时间：

```
%%LST DNSINFO:;
```

```
%%
RETCODE = 0  操作成功

结果如下
--------
配置模板  =  config_provA
  用户名  =  scale
    密码  =  *****
修改时间  =  2024-02-20 13:41:43
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询DNS信息（LST-DNSINFO）_61692892.md`
