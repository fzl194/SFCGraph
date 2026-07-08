---
id: UNC@20.15.2@MMLCommand@LST QOSACTFILTER
type: MMLCommand
name: LST QOSACTFILTER（查询流行为规则）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: QOSACTFILTER
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- 流行为规则
status: active
---

# LST QOSACTFILTER（查询流行为规则）

## 功能

该命令用于查询流行为过滤设置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BEHAVIORNAME | 行为名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定流行为。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：区分大小写，不支持空格。 |
| FILTER | 行为状态 | 可选必选说明：可选参数<br>参数含义：该参数用于指定动作为permit还是deny。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- permit：满足规则的所有报文通过。<br>- deny：满足规则的所有报文不通过。<br>默认值：无 |

## 操作的配置对象

- [流行为规则（QOSACTFILTER）](configobject/UNC/20.15.2/QOSACTFILTER.md)

## 使用实例

查询当前所有流动作的过滤设置：

```
LST QOSACTFILTER:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
行为名称  =  b1
行为状态  =  拒绝
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询流行为规则（LST-QOSACTFILTER）_50281522.md`
