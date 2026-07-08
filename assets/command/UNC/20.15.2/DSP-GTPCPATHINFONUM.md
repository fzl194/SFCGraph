---
id: UNC@20.15.2@MMLCommand@DSP GTPCPATHINFONUM
type: MMLCommand
name: DSP GTPCPATHINFONUM（显示GTPC路径数目）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: GTPCPATHINFONUM
command_category: 查询类
applicable_nf:
- AMF
- PGW-C
- SGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- GTP-C接口配置管理
- GTP-C路径维护
status: active
---

# DSP GTPCPATHINFONUM（显示GTPC路径数目）

## 功能

**适用NF：AMF、PGW-C、SGW-C、GGSN**

该命令用于查询GTP-C路径数目。

## 注意事项

当SET AMFN26PLCY命令中N26ITFMODE取值为“COMBINE”时，当前命令无效，请使用命令DSP GTPCPATHNUM查询。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/GTPCPATHINFONUM]] · GTPC路径数目（GTPCPATHINFONUM）

## 使用实例

查询GTP-C路径数目：DSP GTPCPATHINFONUM:;

```
%%DSP GTPCPATHINFONUM:;%%
RETCODE = 0  操作成功

结果如下
--------
路径数目  =  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-GTPCPATHINFONUM.md`
