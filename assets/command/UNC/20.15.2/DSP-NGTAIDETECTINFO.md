---
id: UNC@20.15.2@MMLCommand@DSP NGTAIDETECTINFO
type: MMLCommand
name: DSP NGTAIDETECTINFO（显示NG TAI对象寻呼流控状态信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NGTAIDETECTINFO
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 拥塞控制
- TA LIST流控
status: active
---

# DSP NGTAIDETECTINFO（显示NG TAI对象寻呼流控状态信息）

## 功能

**适用NF：AMF**

该命令用于查询NG TAI对象寻呼流控状态信息。

## 注意事项

- 如果选择“报告输出”，且当前TAI检测对象数量较多时，该命令执行时间较长。
- 若连续多次执行该命令可能导致OMU虚机CPU使用率突增。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OUTPUTTYPE | 输出类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NG TAI对象寻呼流控状态查询的输出类型。<br>数据来源：本端规划<br>取值范围：<br>- “Summary（统计信息）”：统计信息<br>- “Screen（报告输出）”：报告输出<br>默认值：无<br>配置原则：无 |
| TAIGROUPNAME | TAI组名 | 可选必选说明：该参数在"OUTPUTTYPE"配置为"Screen"时为条件可选参数。<br>参数含义：该参数用于表示待查询的NG TAI组对象名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。<br>默认值：无<br>配置原则：<br>查询的对象名称必须先通过ADD PERFNGTAIGROUP进行配置。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGTAIDETECTINFO]] · NG TAI对象寻呼流控状态信息（NGTAIDETECTINFO）

## 使用实例

查询系统中的所有NG TAI对象寻呼流控状态，执行如下命令：

```
%%DSP NGTAIDETECTINFO: OUTPUTTYPE=Summary;%%
RETCODE = 0  操作成功

结果如下
------------------------
           任务ID  =  monitor_task_5
     检测任务状态  =  正常
    TAI组对象数量  =  0
异常TAI组对象数量  =  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-NGTAIDETECTINFO.md`
