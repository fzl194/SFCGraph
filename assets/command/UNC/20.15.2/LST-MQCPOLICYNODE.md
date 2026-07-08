---
id: UNC@20.15.2@MMLCommand@LST MQCPOLICYNODE
type: MMLCommand
name: LST MQCPOLICYNODE（查询流策略节点）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MQCPOLICYNODE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- MQC
- 分类策略节点
status: active
---

# LST MQCPOLICYNODE（查询流策略节点）

## 功能

该命令用于查询已经配置的流策略信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 策略名称 | 可选必选说明：可选参数<br>参数含义：指定流策略的名称，不允许为系统预定义策略default。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：区分大小写，不支持空格。 |
| CLASSIFIERNAME | 分类名称 | 可选必选说明：可选参数<br>参数含义：指定流分类的名称。类名不允许为系统预定义类的名称default-class。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：区分大小写，不支持空格。 |
| BEHAVIORNAME | 行为名称 | 可选必选说明：可选参数<br>参数含义：指定流行为名称。定义的行为名不允许为系统预定义的流行为be。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：区分大小写，不支持空格。 |
| PRECEDENCE | 优先级 | 可选必选说明：可选参数<br>参数含义：指定策略匹配的优先级，流策略中按照优先级处理流分类的动作。取值越小优先级越高，优先被处理。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～5100。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MQCPOLICYNODE]] · 流策略节点（MQCPOLICYNODE）

## 使用实例

查询已经配置的流策略信息：

```
LST MQCPOLICYNODE:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
策略名称  =  p1
分类名称  =  c1
行为名称  =  b1
  优先级  =  1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-MQCPOLICYNODE.md`
