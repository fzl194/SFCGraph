---
id: UNC@20.15.2@MMLCommand@LST AMFREDCAPFUNC
type: MMLCommand
name: LST AMFREDCAPFUNC（查询AMF RedCap功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AMFREDCAPFUNC
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G M2M管理
- RedCap功能管理
status: active
---

# LST AMFREDCAPFUNC（查询AMF RedCap功能）

## 功能

**适用NF：AMF**

该命令用于查询AMF RedCap功能参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/AMFREDCAPFUNC]] · AMF RedCap功能（AMFREDCAPFUNC）

## 使用实例

查询AMF RedCap功能参数，执行如下命令：

```
%%LST AMFREDCAPFUNC:;%%
RETCODE = 0  操作成功

结果如下
--------
       RedCap功能开关  =  是
    RatType兼容性开关  =  UDM&PCF&SMSF&SMF
空闲态会话通知SMF策略  =  立即通知
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询AMF-RedCap功能（LST-AMFREDCAPFUNC）_17306398.md`
