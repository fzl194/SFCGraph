---
id: UNC@20.15.2@MMLCommand@DSP SDRTOPIC
type: MMLCommand
name: DSP SDRTOPIC（查询SDRC中的TOPIC信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SDRTOPIC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 策略查询
status: active
---

# DSP SDRTOPIC（查询SDRC中的TOPIC信息）

## 功能

该命令用于查询SDRC中指定topicId的TOPIC策略信息。若命令不接任何参数，则该命令列出SDRC中所有TOPIC的信息，否则显示特定的TOPIC信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TOPICID | TOPIC ID | 可选必选说明：可选参数<br>参数含义：该参数用于表示topic策略的id。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SDRTOPIC]] · SDRC中的TOPIC信息（SDRTOPIC）

## 使用实例

使用如下命令查询SDRC中缓存的topic策略信息：

```
%%DSP SDRTOPIC: TOPICID=4128;%%
RETCODE = 0  操作成功

结果如下
--------
    TOPIC ID  =  4128
    驱动类型  =  0
使用外部通信  =  否
      优先级  =  0
安全开关  =  false
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SDRTOPIC.md`
