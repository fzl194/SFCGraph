---
id: UNC@20.15.2@MMLCommand@DSP TOPICSTAT
type: MMLCommand
name: DSP TOPICSTAT（查询topic状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: TOPICSTAT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- OMMQ管理
status: active
---

# DSP TOPICSTAT（查询topic状态）

## 功能

该命令用于查询topic分区的详细信息，kafka各分区副本之间数据同步是否正常，以及分区leader是否正常选举等信息。

## 注意事项

- 支持输入参数为空时的全量查询，支持按照topic名称查询时进行模糊匹配。
- 对部分不需要对外展示的topic信息（如拨测）会进行过滤。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TOPIC_NAME | topic名称 | 可选必选说明：可选参数<br>参数含义：用于指示系统需要查询指定topic的状态信息。<br>取值范围：字符串类型，取值范围2~256。<br>默认值：无。<br>配置原则：不输入参数，执行当前命令即可查询全量topic名称。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@TOPICSTAT]] · topic状态（TOPICSTAT）

## 使用实例

根据topic名称查询topic状态。

```
%%DSP TOPICSTAT: TOPIC_NAME="runlog";%% 
RETCODE = 0  操作成功  
topic状态查询结果：
-------------------
topic名称  topic分区  主分区  分区副本   分区同步列表
runlog     0          1002    1002,1001  1002,1001
runlog     1          1001    1001,1002  1002,1001
runlog     2          1002    1002,1001  1002,1001
runlog     3          1001    1001,1002  1002,1001
runlog     4          1002    1002,1001  1002,1001
runlog     5          1001    1001,1002  1002,1001
runlog     6          1002    1002,1001  1002,1001
runlog     7          1001    1001,1002  1002,1001
runlog     8          1002    1002,1001  1002,1001
runlog     9          1001    1001,1002  1002,1001     
(结果个数 = 10)  
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-TOPICSTAT.md`
