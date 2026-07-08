---
id: UNC@20.15.2@MMLCommand@LST NSSFRTNSMAXNUM
type: MMLCommand
name: LST NSSFRTNSMAXNUM（查询NSSF响应切片最大数量配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NSSFRTNSMAXNUM
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

# LST NSSFRTNSMAXNUM（查询NSSF响应切片最大数量配置）

## 功能

**适用NF：NSSF**

该命令用于查询NSSF响应切片最大长度信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NSSFRTNSMAXNUM]] · NSSF响应切片最大数量配置（NSSFRTNSMAXNUM）

## 使用实例

若运营商希望查询所有的数据，执行下列命令。

```
LST NSSFRTNSMAXNUM:;
%%LST NSSFRTNSMAXNUM:;%%
RETCODE = 0 执行成功

结果如下
------------------------
Allowed切片最大数量  =  8
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NSSF响应切片最大数量配置（LST-NSSFRTNSMAXNUM）_44461347.md`
