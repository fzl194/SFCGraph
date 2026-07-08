---
id: UNC@20.15.2@MMLCommand@LST AMFPROFILEPLCY
type: MMLCommand
name: LST AMFPROFILEPLCY（查询AMF上报NFPROFILE策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AMFPROFILEPLCY
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- AMF概述信息控制策略
status: active
---

# LST AMFPROFILEPLCY（查询AMF上报NFPROFILE策略）

## 功能

**适用NF：AMF**

该命令用于查询AMF向NRF上报NFPROFILE信息的策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/AMFPROFILEPLCY]] · AMF上报NFPROFILE策略（AMFPROFILEPLCY）

## 使用实例

查询AMF向NRF上报NFPROFILE信息的策略。

```
%%LST AMFPROFILEPLCY:;%%
RETCODE = 0  操作成功

结果如下
--------
TAI上报策略  =  TAILIST格式
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-AMFPROFILEPLCY.md`
