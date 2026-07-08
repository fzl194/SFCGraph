---
id: UNC@20.15.2@MMLCommand@LST FWAMATCHRULE
type: MMLCommand
name: LST FWAMATCHRULE（查询FWA用户匹配规则）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: FWAMATCHRULE
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- FWA用户匹配规则管理
status: active
---

# LST FWAMATCHRULE（查询FWA用户匹配规则）

## 功能

**适用NF：SMF**

该命令用于查询FWA用户匹配规则。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@FWAMATCHRULE]] · FWA用户匹配规则（FWAMATCHRULE）

## 使用实例

显示FWA用户匹配规则。

```
%%LST FWAMATCHRULE:;%%
RETCODE = 0 操作成功
结果如下
匹配类型        匹配方式        PCC规则        APN名称
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-FWAMATCHRULE.md`
