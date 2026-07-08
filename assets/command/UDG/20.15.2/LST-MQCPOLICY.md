---
id: UDG@20.15.2@MMLCommand@LST MQCPOLICY
type: MMLCommand
name: LST MQCPOLICY（查询流策略）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: MQCPOLICY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- MQC
- 分类策略
status: active
---

# LST MQCPOLICY（查询流策略）

## 功能

该命令用于查询已经创建的流量策略信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 策略名称 | 可选必选说明：可选参数<br>参数含义：指定流策略的名称，不允许为系统预定义策略default。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：区分大小写，不支持空格。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MQCPOLICY]] · 流策略配置（MQCPOLICY）

## 使用实例

查询已经创建的流量策略信息：

```
LST MQCPOLICY:;
```

```

RETCODE = 0  操作成功

结果如下
------------------------
    策略名称  =  p1
统计使能标志  =  去使能
    共享模式  =  非共享模式
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-MQCPOLICY.md`
