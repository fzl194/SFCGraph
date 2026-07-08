---
id: UDG@20.15.2@MMLCommand@DSP IPV6HASTATE
type: MMLCommand
name: DSP IPV6HASTATE（查询IPv6组件与其他组件交互信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: IPV6HASTATE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- IPV6
status: active
---

# DSP IPV6HASTATE（查询IPv6组件与其他组件交互信息）

## 功能

该命令用于查询IPv6组件与其他组件交互信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TYPE | 交互组件类型 | 可选必选说明：必选参数<br>参数含义：该参数用来指定与IPv6组件交互组件类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FES：与FES组件交互信息。<br>- SOCK：与SOCK组件交互信息。<br>- CACHEM：与CACHEM组件交互信息。<br>- LDM：与LDM组件交互信息。<br>- PP6：IPv6组件状态。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@IPV6HASTATE]] · IPv6组件与其他组件交互信息（IPV6HASTATE）

## 使用实例

- 显示IPv6组件与FES组件交互信息：
  ```
  DSP IPV6HASTATE: TYPE=FES;
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
  查询结果信息

      PID: 0x6A0016,ucSubFlag: 0x1,ucCompStatus: 0x0,uiReferCount: 0x1
      PID: 0x6A0016  HaState: 0x0
      State: LSMLIB_SOCK_FSM_INIT FESState: (LSMLIB_FES_FSM_RUNNING LSMLIB_FES_FSM_RUNNING LSMLIB_FES_FSM_RUNNING)
      BatchUpdateSeq: 7 RealUpdateSeq: 990
      Version: 0 LastMsgSendTime: 0
      FlowCtl State: 0 CurFlowCtlBeginTime: 0 LastFlowCtlEndTime: 0
      RecvFlowCtlMsgTime: 0 TotalFlowCtlTimes: 0

      PID: 0x6A0016,ucSubFlag: 0x0,ucCompStatus: 0x1,uiReferCount: 0x1
      PID: 0x6A0016  HaState: 0x1
      State: LSMLIB_SOCK_FSM_INIT FESState: (LSMLIB_FES_FSM_INIT LSMLIB_FES_FSM_INIT LSMLIB_FES_FSM_INIT)
      BatchUpdateSeq: 0 RealUpdateSeq: 0
      Version: 0 LastMsgSendTime: 0
      FlowCtl State: 0 CurFlowCtlBeginTime: 0 LastFlowCtlEndTime: 0
      RecvFlowCtlMsgTime: 0 TotalFlowCtlTimes: 0

  (结果个数 = 2)
  ---    END
  ```
- 显示IPv6组件与SOCK组件交互信息：
  ```
  DSP IPV6HASTATE: TYPE=SOCK;
  ```
  ```

  RETCODE = 0  操作成功。

  结果如下
  --------
  查询结果信息

      PID: 0x650004  HaState: 0x0 State: LSMLIB_SOCK_FSM_RUNNING
      BatchUpdateSeq: 1 RealUpdateSeq: 2
      Version: 1 LastMsgSendTime: 5
      PID: 0x650008  HaState: 0x0 State: LSMLIB_SOCK_FSM_RUNNING
      BatchUpdateSeq: 1 RealUpdateSeq: 1
      Version: 1 LastMsgSendTime: 3
      PID: 0x650019  HaState: 0x0 State: LSMLIB_SOCK_FSM_RUNNING
      BatchUpdateSeq: 1 RealUpdateSeq: 2
      Version: 1 LastMsgSendTime: 5
      PID: 0x65002A  HaState: 0x0 State: LSMLIB_SOCK_FSM_RUNNING
      BatchUpdateSeq: 1 RealUpdateSeq: 2
      Version: 1 LastMsgSendTime: 5
      PID: 0x650037  HaState: 0x0 State: LSMLIB_SOCK_FSM_RUNNING
      BatchUpdateSeq: 1 RealUpdateSeq: 1
      Version: 1 LastMsgSendTime: 78

      PID: 0x650004  HaState: 0x1 State: LSMLIB_SOCK_FSM_INIT
      BatchUpdateSeq: 0 RealUpdateSeq: 0
      Version: 0 LastMsgSendTime: 0
      PID: 0x650008  HaState: 0x1 State: LSMLIB_SOCK_FSM_INIT
      BatchUpdateSeq: 0 RealUpdateSeq: 0
      Version: 0 LastMsgSendTime: 0
      PID: 0x650019  HaState: 0x1 State: LSMLIB_SOCK_FSM_INIT
      BatchUpdateSeq: 0 RealUpdateSeq: 0
      Version: 0 LastMsgSendTime: 0
      PID: 0x65002A  HaState: 0x1 State: LSMLIB_SOCK_FSM_INIT
      BatchUpdateSeq: 0 RealUpdateSeq: 0
      Version: 0 LastMsgSendTime: 0
      PID: 0x650037  HaState: 0x1 State: LSMLIB_SOCK_FSM_INIT
      BatchUpdateSeq: 0 RealUpdateSeq: 0
      Version: 0 LastMsgSendTime: 0

  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-IPV6HASTATE.md`
