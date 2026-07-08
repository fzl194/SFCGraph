---
id: UNC@20.15.2@MMLCommand@LST AMFRESTOFUNC
type: MMLCommand
name: LST AMFRESTOFUNC（查询AMF热备容灾）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AMFRESTOFUNC
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- AMF热备容灾管理
status: active
---

# LST AMFRESTOFUNC（查询AMF热备容灾）

## 功能

**适用NF：AMF**

该命令用于查询AMF热备容灾功能的运行模式及相关参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/AMFRESTOFUNC]] · AMF热备容灾（AMFRESTOFUNC）

## 使用实例

查询AMF热备容灾，执行如下命令：

```
%%LST AMFRESTOFUNC:;%%
RETCODE = 0  操作成功

结果如下
-------
                    运行模式  =  运行
容灾用户上下文合法性校验范围  =  5
          延迟删除UE Context  =  是
                    备份类型  =  全量备份
         Binding头域携带策略  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-AMFRESTOFUNC.md`
