---
id: UNC@20.15.2@MMLCommand@LST QOSPROP
type: MMLCommand
name: LST QOSPROP（查询QoS属性）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: QOSPROP
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务策略
- 业务质量属性
status: active
---

# LST QOSPROP（查询QoS属性）

## 功能

**适用NF：PGW-C、SMF**

该命令用来查询QoS属性，其中包括QoS属性名称、QoS等级标识、分配保留优先级、QoS抢占能力、QoS被抢占设置、保证的上下行比特率、最大上下行比特率。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSPROPNAME | QoS属性名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定QoS属性名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/QOSPROP]] · QoS属性（QOSPROP）

## 使用实例

查询名称为“test”的QoS属性的信息，命令为：

```
LST QOSPROP:QOSPROPNAME="test";
```

```

RETCODE = 0  操作成功

QoS属性信息
-----------
          QoS属性名称  =  test
          QoS等级标识  =  4
       分配保留优先级  =  1
          QoS抢占能力  =  不使能
        QoS被抢占设置  =  使能
     保证的上行比特率  =  1
     保证的下行比特率  =  100
       最大上行比特率  =  2
       最大下行比特率  =  200
          QoS属性类型  =  承载级别的QoS参数
            QoS流标识  =  0
          反射QoS指示  =  不使能
           5G QoS标识  =  0
QoS使用量上报规则名称  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询QoS属性（LST-QOSPROP）_09897166.md`
