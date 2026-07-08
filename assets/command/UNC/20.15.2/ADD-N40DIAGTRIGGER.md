---
id: UNC@20.15.2@MMLCommand@ADD N40DIAGTRIGGER
type: MMLCommand
name: ADD N40DIAGTRIGGER（增加N40去活原因的映射关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: N40DIAGTRIGGER
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- N40诊断值Trigger
status: active
---

# ADD N40DIAGTRIGGER（增加N40去活原因的映射关系）

## 功能

**适用NF：PGW-C、SMF**

该命令用于增加用户去活时内部诊断字段取值到去活原因的映射关系。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入1001条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DIAGNOSTICS | 诊断原因值 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SMF内部的去活诊断字段原因值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~1000。<br>默认值：无<br>配置原则：无 |
| RELEASETRIGGER | 去活原因 | 可选必选说明：必选参数<br>参数含义：该参数用于指定内部去活诊断字段对应的去活原因。<br>数据来源：本端规划<br>取值范围：<br>- FINAL（正常去活）<br>- ABNORMALRELEASE（异常去活）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/N40DIAGTRIGGER]] · N40去活原因的映射关系（N40DIAGTRIGGER）

## 使用实例

CHF通过Notify消息通知用户去活时，内部诊断字段对应取值为259，设置该场景下去活原因（TriggerType）为“FINAL”：

```
ADD N40DIAGTRIGGER: DIAGNOSTICS =259, RELEASETRIGGER = FINAL;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-N40DIAGTRIGGER.md`
