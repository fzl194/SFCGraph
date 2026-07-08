---
id: UDG@20.15.2@MMLCommand@LST MQCCLASSIFIER
type: MMLCommand
name: LST MQCCLASSIFIER（查询流分类）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: MQCCLASSIFIER
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- MQC
- 流分类
status: active
---

# LST MQCCLASSIFIER（查询流分类）

## 功能

该命令用于查询已经创建的流分类信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CLASSIFIERNAME | 分类名称 | 可选必选说明：可选参数<br>参数含义：指定流分类的名称。类名不允许为系统预定义类的名称default-class。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：区分大小写，不支持空格。 |
| CREATETYPE | 创建类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定各规则之间的逻辑运算符关系。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- system-defined：系统默认。<br>- user-defined：用户自定义。<br>默认值：无 |
| OPERATOR | 关系类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定各规则之间的逻辑运算符关系。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- or：或操作。<br>默认值：无 |

## 操作的配置对象

- [流分类（MQCCLASSIFIER）](configobject/UDG/20.15.2/MQCCLASSIFIER.md)

## 使用实例

查询已经创建的流分类信息：

```
LST MQCCLASSIFIER:CREATETYPE=user-defined,CLASSIFIERNAME="c1";
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
分类名称  =  c1
创建类型  =  用户自定义
关系类型  =  或
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询流分类（LST-MQCCLASSIFIER）_50121778.md`
