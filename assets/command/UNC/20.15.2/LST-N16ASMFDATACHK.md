---
id: UNC@20.15.2@MMLCommand@LST N16ASMFDATACHK
type: MMLCommand
name: LST N16ASMFDATACHK（查询N16aSMF数据核查功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: N16ASMFDATACHK
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 可靠性管理
- N16aSMF数据核查管理
status: active
---

# LST N16ASMFDATACHK（查询N16aSMF数据核查功能）

## 功能

**适用NF：SMF**

该命令用于查询N16aSMF数据核查功能，如是否支持基于UserAgent的数据核查。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/N16ASMFDATACHK]] · N16aSMF数据核查功能（N16ASMFDATACHK）

## 使用实例

查询所有N16ASMFDATACHK记录：

```
%%LST N16ASMFDATACHK:;%%
RETCODE = 0  操作成功

结果如下
------------------------
USERAGENTCHK  =  ON
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-N16ASMFDATACHK.md`
