---
id: UNC@20.15.2@MMLCommand@LST SMFALLOWED5QIS
type: MMLCommand
name: LST SMFALLOWED5QIS（查询5G用户允许的5QI列表）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMFALLOWED5QIS
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- 5GC QoS配置
- 5GC允许接入的5QIs
status: active
---

# LST SMFALLOWED5QIS（查询5G用户允许的5QI列表）

## 功能

**适用NF：SMF**

该命令用于查询5G用户允许的5QI列表。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSINDEX | 用户QOS索引 | 可选必选说明：可选参数<br>参数含义：该参数表示允许用户接入的5QI列表索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：无 |
| QOS5QISTART | 5QI范围起始值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定允许接入的5QI范围的起始值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~255。<br>默认值：无<br>配置原则：无 |
| QOS5QIEND | 5QI范围结束值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定允许接入的5QI范围的结束值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMFALLOWED5QIS]] · 5G用户允许的5QI列表（SMFALLOWED5QIS）

## 使用实例

如果要查询所有的5G用户允许的5QI列表，执行如下命令:

```
%%LST SMFALLOWED5QIS:;%%
RETCODE = 0  Operation succeeded

The result is as follows
------------------------
        Subscriber QoS Index  =  1
Start value of the 5QI range  =  3
  End value of the 5QI range  =  3
(Number of results = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SMFALLOWED5QIS.md`
