---
id: UNC@20.15.2@MMLCommand@LST SGWPLMNORIGIN
type: MMLCommand
name: LST SGWPLMNORIGIN（查询S-GW PLMN ID来源）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SGWPLMNORIGIN
command_category: 查询类
applicable_nf:
- PGW-C
- SGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- 获取PLMN管理
- S_P合一的SGW PLMN获取策略
status: active
---

# LST SGWPLMNORIGIN（查询S-GW PLMN ID来源）

## 功能

**适用NF：PGW-C、SGW-C**

该命令用于查询SGW-C和PGW-C合一形态时SGW-C PLMN的获取方式。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SGWPLMNORIGIN]] · S-GW PLMN ID来源（SGWPLMNORIGIN）

## 使用实例

查询S-GW和P-GW合一形态时S-GW PLMN的获取方式：

```
%%LST SGWPLMNORIGIN:;%%
RETCODE = 0  操作成功

结果如下
--------
S-GW PLMN ID来源  =  P-GW PLMN
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SGWPLMNORIGIN.md`
