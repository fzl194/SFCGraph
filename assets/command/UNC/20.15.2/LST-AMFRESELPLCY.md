---
id: UNC@20.15.2@MMLCommand@LST AMFRESELPLCY
type: MMLCommand
name: LST AMFRESELPLCY（查询AMF重选控制策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AMFRESELPLCY
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- AMF区域重选功能管理
- AMF重选控制策略
status: active
---

# LST AMFRESELPLCY（查询AMF重选控制策略）

## 功能

**适用NF：AMF**

该命令用于查询AMF重选功能控制策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBGRPID | 用户群组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定应用AMF重选功能的用户群组。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967294。该用户群组标识通过ADD NGUSRGRP进行添加。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [AMF重选控制策略（AMFRESELPLCY）](configobject/UNC/20.15.2/AMFRESELPLCY.md)

## 使用实例

查询用户群组1对应的AMF重选策略，执行命令如下：

```
%%LST AMFRESELPLCY: SUBGRPID=1;%%
RETCODE = 0  操作成功

结果如下
------------------------
用户群组标识  =  1
 AMF实例标识  =  AMF-INSTANCEID-1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询AMF重选控制策略（LST-AMFRESELPLCY）_38212805.md`
