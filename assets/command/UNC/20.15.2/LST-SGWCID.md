---
id: UNC@20.15.2@MMLCommand@LST SGWCID
type: MMLCommand
name: LST SGWCID（查询SGW-C网络标识符）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SGWCID
command_category: 查询类
applicable_nf:
- SGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 本局信息管理
- SMF
- SGW-C信息管理
status: active
---

# LST SGWCID（查询SGW-C网络标识符）

## 功能

**适用NF：SGW-C**

该命令用于查询SGW-C的全球唯一标识。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/SGWCID]] · SGW-C网络标识符（SGWCID）

## 使用实例

查询SGW-C的全球唯一标识，执行命令如下：

```
%%LST SGWCID:;%%
            RETCODE = 0  操作成功

            结果如下
            ------------------------
            移动国家码  =  460
            移动网号  =  01
            SGW-C标识  =  0
            (结果个数 = 1)

            ---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SGWCID.md`
