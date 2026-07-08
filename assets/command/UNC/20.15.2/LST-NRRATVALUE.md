---
id: UNC@20.15.2@MMLCommand@LST NRRATVALUE
type: MMLCommand
name: LST NRRATVALUE（查询5G接入用户的RAT填写值）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRRATVALUE
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 计费控制
- NR用户RAT值
status: active
---

# LST NRRATVALUE（查询5G接入用户的RAT填写值）

## 功能

**适用NF：SMF、PGW-C**

查询5G接入用户的RAT填写值。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRRATVALUE]] · 5G接入用户的RAT填写值（NRRATVALUE）

## 使用实例

查询5G接入用户的RAT填写值。

```
LST NRRATVALUE:;
RETCODE = 0  操作成功

结果如下
------------------------
                  和OCS交互使用的RAT值  =  RAT取值为51
                   和CG交互使用的RAT值  =  RAT取值为51
        和AAA计费服务器交互使用的RAT值  =  RAT取值为51
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NRRATVALUE.md`
