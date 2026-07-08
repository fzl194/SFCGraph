---
id: UDG@20.15.2@MMLCommand@LST MQCBEHAVIOR
type: MMLCommand
name: LST MQCBEHAVIOR（查询流行为）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: MQCBEHAVIOR
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- MQC
- 分类行为
status: active
---

# LST MQCBEHAVIOR（查询流行为）

## 功能

该命令用于查询已经创建的流行为信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BEHAVIORNAME | 行为名称 | 可选必选说明：可选参数<br>参数含义：指定流行为名称。定义的行为名不允许为系统预定义的流行为be。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：区分大小写，不支持空格。 |
| CREATETYPE | 创建类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定各规则之间的逻辑运算符关系。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- system-defined：系统默认。<br>- user-defined：用户自定义。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@MQCBEHAVIOR]] · 流行为（MQCBEHAVIOR）

## 使用实例

查询已经创建的流行为信息：

```
LST MQCBEHAVIOR:CREATETYPE=user-defined,BEHAVIORNAME="b1";
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
  创建类型  =  用户自定义
  行为名称  =  b1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-MQCBEHAVIOR.md`
