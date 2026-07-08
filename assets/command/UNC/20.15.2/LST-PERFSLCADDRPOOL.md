---
id: UNC@20.15.2@MMLCommand@LST PERFSLCADDRPOOL
type: MMLCommand
name: LST PERFSLCADDRPOOL（查询切片地址池性能统计对象）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PERFSLCADDRPOOL
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- SMF性能对象管理
status: active
---

# LST PERFSLCADDRPOOL（查询切片地址池性能统计对象）

## 功能

**适用NF：SMF**

该命令用于查询切片地址池性能统计对象。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IDX | 索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定切片地址池性能统计对象的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~499。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [切片地址池性能统计对象（PERFSLCADDRPOOL）](configobject/UNC/20.15.2/PERFSLCADDRPOOL.md)

## 使用实例

查询所有的切片地址池性能统计对象： LST PERFSLCADDRPOOL:;

```
%%LST PERFSLCADDRPOOL:;%%
RETCODE = 0  操作成功。

结果如下
------------------------
        索引  =  1
切片业务类型  =  1
切片细分标识  =  010101
  地址池名称  =  pool1
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询切片地址池性能统计对象（LST-PERFSLCADDRPOOL）_88248950.md`
