---
id: UNC@20.15.2@MMLCommand@STR S1BALANCE
type: MMLCommand
name: STR S1BALANCE（启动S1接口均衡操作）
nf: UNC
version: 20.15.2
verb: STR
object_keyword: S1BALANCE
command_category: 动作类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- S1接口均衡管理
status: active
---

# STR S1BALANCE（启动S1接口均衡操作）

## 功能

![](启动S1接口均衡操作(STR S1BALANCE)_26306050.assets/notice_3.0-zh-cn_2.png)

- 此命令启动后，正在迁移的eNodeB上进行信令业务的用户会有影响，这部分用户状态会迁移到ECM-IDLE态，造成流程失败或延迟。
- 在执行迁移命令过程中，不允许进行复位等操作。
- 在执行迁移命令过程中，不要与割接eNodeB操作并行，否则会增加迁移前后eNodeB一致性检查的复杂度，而且会再次造成SGP进程间eNodeB分布不均匀。

**适用网元：MME**

- 此命令用于启动S1AP链路在SGP进程间的迁移。
- 系统SGP进程异常复位等场景造成到eNodeB的S1AP链路在SGP进程上分布不均匀，而没有其它场景能够触发到eNodeB的S1AP链路在SGP进程上再次均匀分布，从而使系统长期负载不均匀，只能通过此命令迁移SGP进程间的S1AP链路实现均匀分布。
- 迁移流程简介：系统通过向需要迁移的eNodeB发起偶联重建请求，当eNodeB收到请求后，重新进行SCTP偶联建立流程，此时系统通过重选接入的SGP进程来达到迁移的目的。

## 注意事项

- 此命令执行后立即生效。
- 此命令启动后，正在迁移的eNodeB上进行信令业务的用户会有影响，这部分用户状态会迁移到ECM-IDLE态，造成流程失败或延迟。
- 请在业务低峰期执行此命令。
- 在执行迁移命令过程中，不允许进行复位等操作。
- 在执行迁移命令过程中，不要与割接eNodeB操作并行，否则会增加迁移前后eNodeB一致性检查的复杂度，而且会再次造成SGP进程间eNodeB分布不均匀。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MIGRATERANGE | 迁移范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定eNodeB迁移的范围。<br>数据来源：本端规划<br>取值范围：<br>- “SYSTEM(系统自动均衡迁移)”：一般用于系统扩容、系统异常等场景导致SGP进程上的eNodeB分布不均匀，且不关注eNodeB迁移的源侧和目标侧SGP和eNodeB的迁移个数，系统自动迁移达到均衡。<br>默认值：无 |
| S1ALMRPT | S1AP链路故障告警 | 可选必选说明：可选参数<br>参数含义：该参数用于指定eNodeB链路迁移异常时是否上报“ALM-80589 S1ap链路故障”告警。<br>前置条件：该参数在<br>“迁移范围”<br>为<br>“SYSTEM(系统自动均衡迁移)”<br>时才生效。<br>数据来源：本端规划<br>取值范围：<br>- “YES(YES)”：eNodeB链路迁移过程发生异常时上报“ALM-80589 S1ap链路故障”告警。<br>- “NO(NO)”：eNodeB链路迁移过程发生异常时不上报“ALM-80589 S1ap链路故障”告警。<br>默认值：<br>“NO(NO)” |

## 操作的配置对象

- [[configobject/UNC/20.15.2/S1BALANCE]] · S1接口均衡操作（S1BALANCE）

## 使用实例

1. 运营商A不关注eNodeB迁移的源侧和目标侧SGP和eNodeB的迁移个数，希望通过系统自动均衡迁移SGP进程上的eNodeB，达到均衡状态，执行命令如下：STR S1BALANCE: MIGRATERANGE=SYSTEM;
  ```
  %%STR S1BALANCE: MIGRATERANGE=SYSTEM;%%
  RETCODE = 0  操作成功。

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/STR-S1BALANCE.md`
