---
id: UNC@20.15.2@MMLCommand@LST MULTISRVPLMNEN
type: MMLCommand
name: LST MULTISRVPLMNEN（查询多Serving Plmn增强功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MULTISRVPLMNEN
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 多Serving Plmn增强管理
status: active
---

# LST MULTISRVPLMNEN（查询多Serving Plmn增强功能）

## 功能

**适用NF：AMF**

该命令用于查询多Serving Plmn增强功能参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MULTISRVPLMNEN]] · 多Serving Plmn增强功能（MULTISRVPLMNEN）

## 使用实例

查询多Serving Plmn增强功能参数，执行如下命令：

```
%%LST MULTISRVPLMNEN;%%
RETCODE = 0  操作成功

操作结果如下
------------------------
 支持多Serving Plmn功能增强  =  支持
     移动性流程增强处理策略  =  支持
         AMF设备信息通知SMF  =  支持
           AMF设备GUAMI索引  =  256
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-MULTISRVPLMNEN.md`
