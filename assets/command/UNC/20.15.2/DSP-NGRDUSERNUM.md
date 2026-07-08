---
id: UNC@20.15.2@MMLCommand@DSP NGRDUSERNUM
type: MMLCommand
name: DSP NGRDUSERNUM（显示5G容灾用户数）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NGRDUSERNUM
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 用户数据库管理
status: active
---

# DSP NGRDUSERNUM（显示5G容灾用户数）

## 功能

**适用NF：AMF**

该命令用于查询AMF系统内容灾用户的统计结果。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGRDUSERNUM]] · 5G容灾用户数（NGRDUSERNUM）

## 使用实例

查看AMF上容灾用户的统计结果，执行如下命令：

```
%%DSP NGRDUSERNUM:;%%
RETCODE = 0  操作成功

结果如下
------------------------
静态容灾用户数  动态容灾用户数

0               0
0               0
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示5G容灾用户数（DSP-NGRDUSERNUM）_24956626.md`
