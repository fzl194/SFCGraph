---
id: UNC@20.15.2@MMLCommand@DSP GROUPSTAT
type: MMLCommand
name: DSP GROUPSTAT（查询消费组状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: GROUPSTAT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- OMMQ管理
status: active
---

# DSP GROUPSTAT（查询消费组状态）

## 功能

该命令用于查询消费组的状态，通过识别当前消费组的状态信息，判断是否存在消息积压。

## 注意事项

- 支持输入参数为空时的全量查询，支持按照group名称查询时进行模糊匹配。
- 对部分不需要对外展示的group信息（如拨测）会进行过滤。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUP_NAME | group名称 | 可选必选说明：可选参数<br>参数含义：用于指示系统需要查询指定group的状态信息。<br>取值范围：字符串类型，取值范围2~256。<br>默认值：无。<br>配置原则：不输入参数，执行当前命令即可查询全量group名称。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GROUPSTAT]] · 消费组状态（GROUPSTAT）

## 使用实例

```
%%DSP GROUPSTAT: GROUP_NAME="runlog";%% 
RETCODE = 0  操作成功  
group状态查询结果：
-------------------
group名称  topic名称  topic分区  消费位移  消息位移  待消费消息  消费者ID                                        消费者IP     管理者  状态    分配方式  成员数  
runlog     runlog     2          0         0         0           Dynamic_1-12e3389a-9256-44fa-9539-2ca0920a6510  127.8.0.39   1002    Stable  range     1       
runlog     runlog     1          0         0         0           Dynamic_1-12e3389a-9256-44fa-9539-2ca0920a6510  127.8.0.39   1002    Stable  range     1       
runlog     runlog     0          0         0         0           Dynamic_1-12e3389a-9256-44fa-9539-2ca0920a6510  127.8.0.39   1002    Stable  range     1       
runlog     runlog     6          0         0         0           Dynamic_1-12e3389a-9256-44fa-9539-2ca0920a6510  127.8.0.39   1002    Stable  range     1       
runlog     runlog     5          92345     92345     0           Dynamic_1-12e3389a-9256-44fa-9539-2ca0920a6510  127.8.0.39   1002    Stable  range     1       
runlog     runlog     4          0         0         0           Dynamic_1-12e3389a-9256-44fa-9539-2ca0920a6510  127.8.0.39   1002    Stable  range     1       
runlog     runlog     3          0         0         0           Dynamic_1-12e3389a-9256-44fa-9539-2ca0920a6510  127.8.0.39   1002    Stable  range     1       
runlog     runlog     9          0         0         0           Dynamic_1-12e3389a-9256-44fa-9539-2ca0920a6510  127.8.0.39   1002    Stable  range     1       
runlog     runlog     8          0         0         0           Dynamic_1-12e3389a-9256-44fa-9539-2ca0920a6510  127.8.0.39   1002    Stable  range     1       
runlog     runlog     7          0         0         0           Dynamic_1-12e3389a-9256-44fa-9539-2ca0920a6510  127.8.0.39   1002    Stable  range     1
(结果个数 = 10)  
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询消费组状态（DSP-GROUPSTAT）_21110027.md`
