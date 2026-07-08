---
id: UDG@20.15.2@MMLCommand@LST EVTSW
type: MMLCommand
name: LST EVTSW（查询事件开关状态）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: EVTSW
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# LST EVTSW（查询事件开关状态）

## 功能

该命令用于查询事件开关状态。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICE | 服务名称 | 可选必选说明：可选参数<br>参数含义：该参数表示事件绑定的服务名称。可以通过<br>[**LST EVTSW**](查询事件开关状态（LST EVTSW）_82380493.md)<br>命令获取参数。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~16。<br>默认值：无<br>配置原则：无 |
| EVENTID | 事件ID | 可选必选说明：可选参数<br>参数含义：该参数用于表示服务名称下的事件ID，可以通过<br>[**LST EVTSW**](查询事件开关状态（LST EVTSW）_82380493.md)<br>命令获取参数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：<br>只支持配置<br>[**LST EVTSW**](查询事件开关状态（LST EVTSW）_82380493.md)<br>命令获取到的服务实例。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/EVTSW]] · 事件开关状态（EVTSW）

## 使用实例

查询配置表内事件1的开关状态。

```
%%LST EVTSW: SERVICE="SDRS", EVENTID=1;%%
RETCODE = 0  操作成功

结果如下
-----------
服务名称 = SDRS
  事件ID = 1
开关状态 = 打开
事件名称 = sdrs link down1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-EVTSW.md`
