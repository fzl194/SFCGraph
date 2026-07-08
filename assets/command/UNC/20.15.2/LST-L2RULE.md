---
id: UNC@20.15.2@MMLCommand@LST L2RULE
type: MMLCommand
name: LST L2RULE（查询层二规则）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: L2RULE
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务模板
- 层二规则
status: active
---

# LST L2RULE（查询层二规则）

## 功能

**适用NF：SMF**

该命令用于查询层二规则。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| L2RULENAME | 层二规则名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定层二规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/L2RULE]] · 层二规则（L2RULE）

## 使用实例

- 查询层二规则名称为“rule1”的层二规则：
  ```
  LST L2RULE: L2RULENAME="rule1";
  RETCODE = 0  操作成功

  结果如下
  --------
    层二规则名称  =  rule1
     QoS属性名称  =  qosprop1
   层二过滤器名称  =  filter1
  (结果个数 = 1)

  ---    END
  ```
- 查询所有的层二规则：
  ```
  LST L2RULE:;
  RETCODE = 0  操作成功

  结果如下
  --------
    层二规则名称  =  rule1
     QoS属性名称  =  qosprop1
   层二过滤器名称  =  filter1
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-L2RULE.md`
