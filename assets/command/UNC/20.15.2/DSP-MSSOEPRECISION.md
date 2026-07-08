---
id: UNC@20.15.2@MMLCommand@DSP MSSOEPRECISION
type: MMLCommand
name: DSP MSSOEPRECISION（查询MSS保序队列调度信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: MSSOEPRECISION
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- MSS
- 保序统计查询
status: active
---

# DSP MSSOEPRECISION（查询MSS保序队列调度信息）

## 功能

该命令用于查询保序队列调度信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OEID | 保序索引 | 可选必选说明：必选参数<br>参数含义：该参数用于表示保序索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示的RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MSSOEPRECISION]] · MSS保序队列调度信息（MSSOEPRECISION）

## 使用实例

查询保序队列的调度信息：

```
DSP MSSOEPRECISION:OEID=1,RUNAME="VNODE_VNRS_VNFC_IPU_0066";
```

```

RETCODE = 0  操作成功。

结果如下
--------
                                调度冲突次数  =  1001
                                调度成功次数  =  520
                                故障隔离开关  =  ON
                                故障隔离次数  =  1
                            故障隔离次数规格  =  4
                        故障隔离残留PBUF个数  =  1200
                进队列速率最大/平均值（pps）  =  100000/83042
                出队列速率最大/平均值（pps）  =  10000/9302
                 最大/平均一次发送保序节点数  =  15/10
    保序节点最大/平均处理时间（microsecond）  =  2452/1934
    保序节点最大/平均发送时间（microsecond）  =  3245/2312
用户注册函数最大/平均处理时间（microsecond）  =  2344/143
用户注册函数最大/平均发送时间（microsecond）  =  3452/256
                          用户注册的处理函数  =  SFE_RxProc
                          用户注册的发送函数  =  SFE_RxSend
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-MSSOEPRECISION.md`
