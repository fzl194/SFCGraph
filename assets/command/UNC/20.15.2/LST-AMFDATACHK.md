---
id: UNC@20.15.2@MMLCommand@LST AMFDATACHK
type: MMLCommand
name: LST AMFDATACHK（查询AMF数据核查相关参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AMFDATACHK
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- AMF数据一致性核查
status: active
---

# LST AMFDATACHK（查询AMF数据核查相关参数）

## 功能

**适用NF：AMF**

该命令用于查询AMF数据核查相关参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DATATYPE | 数据类型 | 可选必选说明：可选参数<br>参数含义：该参数用于设置AMF待核查的数据类型。<br>数据来源：本端规划<br>取值范围：<br>- “UESR_INDEX_WITH_CTX（用户索引表与用户上下文表）”：核查用户索引表与用户上下文表数据的一致性<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/AMFDATACHK]] · AMF数据核查相关参数（AMFDATACHK）

## 使用实例

查询数据核查相关参数，执行如下命令：

```
%%LST AMFDATACHK:;%%
RETCODE = 0  操作成功

结果如下
--------
  数据类型  =  用户索引表与用户上下文表
  核查开关  =  打开
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-AMFDATACHK.md`
