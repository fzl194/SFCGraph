---
id: UDG@20.15.2@MMLCommand@LST FCPARAM
type: MMLCommand
name: LST FCPARAM（查询流控参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: FCPARAM
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 流控管理
status: active
---

# LST FCPARAM（查询流控参数）

## 功能

该命令用于查询指定微服务实例的流控参数。

> **说明**
> 无

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICETYPE | 服务类型 | 可选必选说明：该参数在"CONTENTTYPE"配置为"DETAIL"时为条件必选参数。该参数在"CONTENTTYPE"配置为"SUMMARY"时为条件可选参数。<br>参数含义：该参数用于指定微服务实例的服务类型。 可以使用<br>[**DSP DBGDATAEX**](../工程调测/5G工程命令/显示调试信息（DSP DBGDATAEX）_09587885.md)<br>命令查询到各个服务对应的SERVICETYPE参数。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| SERVICEID | 实例组ID | 可选必选说明：该参数在"CONTENTTYPE"配置为"DETAIL"时为条件必选参数。该参数在"CONTENTTYPE"配置为"SUMMARY"时为条件可选参数。<br>参数含义：该参数用于指定微服务实例的实例ID。可以使用<br>[**DSP DBGDATAEX**](../工程调测/5G工程命令/显示调试信息（DSP DBGDATAEX）_09587885.md)<br>命令查询到各个服务对应的SERVICEID的值。注意这里serviceid已经废弃改为groupid，因为原有serviceid为主键禁止更新。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| CASEID | 流控套餐ID | 可选必选说明：该参数在"CONTENTTYPE"配置为"DETAIL"时为条件必选参数。该参数在"CONTENTTYPE"配置为"SUMMARY"时为条件可选参数。<br>参数含义：该参数用于指定微服务实例内的流控套餐ID。每个微服务实例可以配置多个流控套餐，每个流控套餐对应唯一的一个ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| CONTENTTYPE | 输出类型 | 可选必选说明：可选参数<br>参数含义：该参数用于打印流控套餐配置时需要展示的表类型。<br>数据来源：本端规划<br>取值范围：<br>- SUMMARY（流控参数简要信息）<br>- DETAIL（流控套餐详细信息 ）<br>默认值：DETAIL<br>配置原则：无 |
| PARAMCAT | 参数类别 | 可选必选说明：该参数在"CONTENTTYPE"配置为"DETAIL"时为条件必选参数。该参数在"CONTENTTYPE"配置为"SUMMARY"时为条件可选参数。<br>参数含义：该参数用于指定本次配置的参数类别。<br>数据来源：本端规划<br>取值范围：<br>- GENERAL（常用参数）<br>- WEIGHTS（权重）<br>- THRESHOLD（阈值）<br>- TARGETCPU（目标cpu）<br>- OVERLOADLEVEL（过载级别）<br>- STOPALGO（停控算法）<br>- BPBACKEND（后端反压）<br>- BPFRONTEND（前端反压）<br>- WALPARAMETER（WAL算法参数）<br>- GCCPUCONFIG（GC时的CPU平滑策略配置）<br>默认值：无<br>配置原则：<br>当取值为“GERNERAL(常用参数)”时，可以配置最小令牌数和最大令牌数，通过修改令牌数来控制业务消息的数量，从而达到流控的目的；当取值为“WEIGHTS(权重)”时，可以配置业务权重获取方式、优先级权重0~15、预期系数0~15。修改权重和预期系数，可以控制被流控的消息的优先级。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/FCPARAM]] · 流控参数（FCPARAM）

## 使用实例

查询微服务类型为UesmCtrlSvc、微服务实例ID为999、流控套餐ID为0的常用参数。

```
%%LST FCPARAM: CONTENTTYPE=DETAIL, SERVICETYPE="UsemCtrlSvc", SERVICEID=999, CASEID=0, PARAMCAT=GENERAL;%%
RETCODE = 0  操作成功

结果如下
--------
  服务类型  =  UsemCtrlSvc
  实例组ID  =  999
流控套餐ID  =  0
  参数类别  =  常用参数
最小令牌数  =  30
最大令牌数  =  5000
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询流控参数（LST-FCPARAM）_09587880.md`
