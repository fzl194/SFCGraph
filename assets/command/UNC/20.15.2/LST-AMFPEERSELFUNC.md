---
id: UNC@20.15.2@MMLCommand@LST AMFPEERSELFUNC
type: MMLCommand
name: LST AMFPEERSELFUNC（查询AMF对端选择功能控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AMFPEERSELFUNC
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 可靠性管理
- AMF对端选择功能管理
status: active
---

# LST AMFPEERSELFUNC（查询AMF对端选择功能控制参数）

## 功能

**适用NF：AMF**

该命令用于查询AMF对端选择功能控制参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@AMFPEERSELFUNC]] · AMF对端选择功能控制参数（AMFPEERSELFUNC）

## 使用实例

查询AMF对端选择功能控制参数，执行如下命令：

```
%%LST AMFPEERSELFUNC:;%%
RETCODE = 0  操作成功

结果如下
--------
            SCP/SEPP重选开关  =  关闭
支持使用Location的对端NF类型  =  UDM&SMF
             SCP重选增强开关  =  关闭
            AUSF重选增强开关  =  开启
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-AMFPEERSELFUNC.md`
