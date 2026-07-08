---
id: UNC@20.15.2@MMLCommand@LST NSSFFUNCPARA
type: MMLCommand
name: LST NSSFFUNCPARA（查询NSSF数据源以及切片选择流程返回信元）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NSSFFUNCPARA
command_category: 查询类
applicable_nf:
- NSSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NSSF业务及策略管理
- NSSF功能参数配置
status: active
---

# LST NSSFFUNCPARA（查询NSSF数据源以及切片选择流程返回信元）

## 功能

**适用NF：NSSF**

该命令用于查询NSSF在业务流程中所使用的数据源以及切片选择流程中需要返回的具体信元。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NSSFFUNCPARA]] · NSSF数据源以及切片选择流程返回信元（NSSFFUNCPARA）

## 使用实例

运营商希望查询NSSF在业务流程中所使用的数据源以及切片选择流程中返回的具体信元时 ，执行此命令：

```
LST NSSFFUNCPARA:;
%%LST NSSFFUNCPARA:;%%
RETCODE = 0  执行成功

结果如下
-------------------------
          数据源设置  =  本地配置可用性信息
切片选择返回信元设置  =  targetAmfSet 
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NSSFFUNCPARA.md`
