---
id: UNC@20.15.2@MMLCommand@DSP E2ETRCEX
type: MMLCommand
name: DSP E2ETRCEX（显示端到端用户跟踪）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: E2ETRCEX
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 扩展调测
- 平台调测
- OM调测
status: active
---

# DSP E2ETRCEX（显示端到端用户跟踪）

## 功能

**适用网元：MME**

该命令用于显示全网跟踪任务信息。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数。<br>参数含义：该参数表示资源单元名称。该参数可以通过<br>[DSP RU](../../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>数据来源：本端规划。<br>取值范围：1~63位字符串。<br>默认值：无。 |
| PROCTYPE | 进程类型 | 可选必选说明：可选参数。<br>参数含义：该参数用于指定所需查询的进程类型。<br>数据来源：本端规划。<br>取值范围：<br>- SPP（SPP）<br>- SGP（SGP）<br>- OMP（OMP）<br>默认值：OMP（OMP） |
| PROCNO | 进程号 | 可选必选说明：可选参数。<br>参数含义：该参数用于指定所需查询的进程序号<br>数据来源：本端规划。<br>取值范围：0~31<br>默认值：无。 |
| TRCID | 跟踪ID | 可选必选说明：可选参数。<br>参数含义：该参数用于指定需要查询的全网跟踪任务的跟踪参考号。<br>数据来源：全网规划。<br>取值范围：0~65535<br>默认值：无。 |
| IMSI | IMSI | 可选必选说明：可选参数。<br>参数含义：该参数用于指定需要查询的全网跟踪任务的IMSI。<br>数据来源：全网规划。<br>取值范围：1到15位数字。<br>默认值：无。 |
| MSISDN | MSISDN | 可选必选说明：可选参数。<br>参数含义：该参数用于指定需要查询的全网跟踪任务的MSISDN。<br>数据来源：全网规划。<br>取值范围：1到15位数字。<br>默认值：无。 |
| SERVICETYPE | VNFC类型 | 可选必选说明：必选参数<br>参数含义：VNFC类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。数字“0~9”，大写字母“A~Z”，小写字母“a~z”，特殊字符“-”，“_”，其他均为非法字符，并且首字符必须为字母。<br>默认值：无<br>说明：该参数可以通过VNFP上的<br>[**LST VNFC**](../../../../../../平台服务管理/单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)<br>命令查询得到。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/E2ETRCEX]] · 端到端用户跟踪（E2ETRCEX）

## 使用实例

显示全网跟踪任务信息

DSP E2ETRCEX: SERVICETYPE="USN_VNFC";

```
%%DSP E2ETRCEX: 
SERVICETYPE="USN_VNFC"
;%%
RETCODE = 0  操作成功。

操作结果如下
------------------------
                 RU名称  =  USN_OM_RU_0001
               进程类型  =  OMP
                 进程号  =  0
                 跟踪ID  =  54738
                 ID类型  =  IMSI
                   IMSI  =  12300123456789
                 MSISDN  =  NULL
               跟踪深度  =  全覆盖跟踪
           跟踪有效天数  =  0
           跟踪创建途径  =  U2020/MAE
                MME接口  =  S1-MME & S3 & S6a & S10 & S11
                ENB接口  =  S1-MME & X2 & Uu
                SGW接口  =  S4 & S5 & S8 & S11
                PGW接口  =  S5 & Gx & S8 & SGi
               (结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-E2ETRCEX.md`
