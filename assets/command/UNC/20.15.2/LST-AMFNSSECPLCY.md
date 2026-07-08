---
id: UNC@20.15.2@MMLCommand@LST AMFNSSECPLCY
type: MMLCommand
name: LST AMFNSSECPLCY（查询AMF切片安全策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AMFNSSECPLCY
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 业务安全管理
- 切片安全策略管理
status: active
---

# LST AMFNSSECPLCY（查询AMF切片安全策略）

## 功能

**适用NF：AMF**

该命令用于查询AMF切片安全策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/AMFNSSECPLCY]] · AMF切片安全策略（AMFNSSECPLCY）

## 使用实例

查询AMF切片安全策略，执行如下命令：

```
%%LST AMFNSSECPLCY:;%%
RETCODE = 0  操作成功

结果如下
------------------------
跨切片访问保护开关  =  ON
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询AMF切片安全策略（LST-AMFNSSECPLCY）_97815871.md`
