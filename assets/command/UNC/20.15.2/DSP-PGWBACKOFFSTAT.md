---
id: UNC@20.15.2@MMLCommand@DSP PGWBACKOFFSTAT
type: MMLCommand
name: DSP PGWBACKOFFSTAT（显示P-GW Back-Off流控状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PGWBACKOFFSTAT
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 设备管理
- 流控管理
- 业务流控管理
- P-GW Backoff流控管理
status: active
---

# DSP PGWBACKOFFSTAT（显示P-GW Back-Off流控状态）

## 功能

**适用网元：MME**

该命令用于显示处于P-GW Back-off流控状态的SPP进程信息。MME支持基于P-GW Back-off timer的APN级流控功能会使用到本命令。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SPU资源单元名称。该参数可以通过<br>[DSP RU](../../../../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>数据来源：本端规划<br>取值范围：1～63位字符串<br>默认值：无 |
| PROCNO | 进程号 | 可选必选说明：必选参数<br>参数含义：该参数用于显示业务进程所属的SPP进程序号。<br>数据来源：本端规划<br>取值范围：0～20<br>默认值：无 |
| APNNI | APNNI | 可选必选说明：可选参数<br>参数含义：该参数用来设置APNNI信息。<br>数据来源：本端规划<br>取值范围：0～62位字符串<br>默认值：无<br>配置原则：<br>- APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PGWBACKOFFSTAT]] · P-GW Back-Off流控状态（PGWBACKOFFSTAT）

## 使用实例

1. 运营商希望查看当前流控任务的状态：
  DSP PGWBACKOFFSTAT: RUNAME="USN_SP_RU_0066", PROCNO=1;
  ```
  %%DSP PGWBACKOFFSTAT: RUNAME="USN_SP_RU_0066", PROCNO=1;%%
  RETCODE = 0  操作成功。

  操作结果如下：
  --------------
  RU名称            进程号     APNNI      

  USN_SP_RU_0066    1          HUAWEI2.COM
  USN_SP_RU_0066    1          HUAWEI3.COM
  (结果个数 = 2)

  ---    END
  ```
2. 运营商希望查看当前 “APNNI” 为 “huawei1.com” 的流控任务的状态：
  DSP PGWBACKOFFSTAT: RUNAME="USN_SP_RU_0066", PROCNO=1, APNNI="huawei1.com";
  ```
  %%DSP PGWBACKOFFSTAT: RUNAME="USN_SP_RU_0066", PROCNO=1, APNNI="huawei1.com";%%
  RETCODE = 0  操作成功。

  操作结果如下：
  --------------
  RU名称            进程号     APNNI        PGW Node Name                      P-GW Back-off timer 通过率

  USN_SP_RU_0066    4          HUAWEI1.COM  EPC.MNC03.MCC460.3GPPNETWORK.ORG   31                  50    
  USN_SP_RU_0066    4          HUAWEI1.COM  EPC1.MNC03.MCC460.3GPPNETWORK.ORG  30                  60    
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-PGWBACKOFFSTAT.md`
