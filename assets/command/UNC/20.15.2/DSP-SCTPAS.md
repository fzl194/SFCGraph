---
id: UNC@20.15.2@MMLCommand@DSP SCTPAS
type: MMLCommand
name: DSP SCTPAS（显示SCTP统计信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SCTPAS
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 扩展调测
- 业务调测
- SCTP统计信息
status: active
---

# DSP SCTPAS（显示SCTP统计信息）

## 功能

**适用网元：SGSN、MME**

此命令用于查询SCTP偶联统计信息。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DSPAST | 统计类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SCTP偶联统计类型。<br>取值范围：<br>- “PROINT(协议内部实体)”<br>- “GLBTR(全局实体)”<br>- “ERROR(错误实体)”<br>- “ASSOC(偶联实体)”<br>默认值：无 |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SPU资源单元名。该参数可以通过<br>[DSP RU](../../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>数据来源：整网规划。<br>取值范围：1~63 位字符串<br>默认值：无 |
| PN | 进程号 | 可选必选说明：必选参数<br>参数含义：该参数用于设置需要查询的SGP进程的进程号。<br>取值范围：0～11<br>默认值：无 |
| ASSID | 偶联ID | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定偶联ID。<br>前提条件：此参数在<br>“统计类型”<br>参数配置为<br>“ASSOC(偶联实体)”<br>值后生效。<br>取值范围：0～4294967295<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SCTPAS]] · SCTP统计信息（SCTPAS）

## 使用实例

1. 查询偶联ID为114，进程号为0的SCTP特定偶联统计信息：
  DSP SCTPAS: DSPAST=ASSOC, RUNAME="USN_SP_RU_0064", PN=0, ASSID=114;
  ```
  %%DSP SCTPAS: DSPAST=ASSOC, RUNAME="USN_SP_RU_0064", PN=0, ASSID=114;%%
  RETCODE = 0 操作成功。
 
  显示SCTP统计信息 
  ----------------------------------
                    偶联标识  =  114
              重发的数据块数  =  0
  偶联建立T1定时器超时的次数  =  0
  数据重传T2定时器超时的次数  =  0
                目的地址个数  =  1
              发送的数据块数  =  1
              接收的数据块数  =  1
                    发送包数  =  4443
                    接收包数  =  4443
                接收错误包数  =  0

  (结果个数 = 1)

  显示SCTP统计信息 
  ----------------------------------
        IP地址类型  =  IPV4
            IP地址  =  192.168.11.1
    重传的数据块数  =  0
    发送的数据块数  =  1
  未确认的数据块数  =  0
    接收的数据块数  =  1
      发送的字节数  =  27
      接收的字节数  =  35
  (结果个数 = 1)
 
  --- END
  ```
2. 进程号为0的SCTP全局统计信息：DSP SCTPAS: DSPAST=GLBTR, RUNAME="USN_SP_RU_0064", PN=0;
  ```
  %%DSP SCTPAS: DSPAST=GLBTR, RUNAME="USN_SP_RU_0064", PN=0;%%
  RETCODE = 0 操作成功。
 
  显示SCTP统计信息
  ----------------------------------
               接受的偶联数  =  7
             初始化的偶联数  =  0
           优雅关闭的偶联数  =  0
         非优雅关闭的偶联数  =  145
               发送数据块数  =  775704
     未回确认消息的数据块数  =  24
               接收数据块数  =  664771
             发送成功字节数  =  62533812
             接收成功字节数  =  99030624
           发送的Init消息数  =  1083
           接收的Init消息数  =  0
       发送的Init Ack消息数  =  8
       接收的Init Ack消息数  =  0
         发送的Cookie消息数  =  0
         接收的Cookie消息数  =  0
     发送的Cookie Ack消息数  =  7
     接收的Cookie Ack消息数  =  0
      发送的Heartbeat消息数  =  499
      接收的Heartbeat消息数  =  304
  发送的Heartbeat Ack消息数  =  304
  接收的Heartbeat Ack消息数  =  493
           发送的Sack消息数  =  139655
           接收的Sack消息数  =  117810
          发送的Abort消息数  =  109
          接收的Abort消息数  =  0
       发送的Shutdown消息数  =  0
       接收的Shutdown消息数  =  0
        发送的Shutack消息数  =  0
        接收的Shutack消息数  =  0
          发送的Error消息数  =  0
          接收的Error消息数  =  0
            发送的ECN消息数  =  0
            接收的ECN消息数  =  0
            发送的CWR消息数  =  0
            接收的CWR消息数  =  0
         接收的错误数据块数  =  0
         接收到的OOTB消息数  =  15
       处于建立状态的偶联数  =  6
           偶联主动失败次数  =  54
           偶联被动失败次数  =  0
           发送的控制消息数  =  141665
         发送的有序数据块数  =  775718
         发送的无序数据块数  =  0
               校验错误次数  =  0
             接收的控制块数  =  118637
         接收的有序数据块数  =  664771
         接收的无序数据块数  =  0
             重传的数据块数  =  1
           分段的用户消息数  =  0
           重组的用户消息数  =  0
       接收的错误的SCTP包数  =  0
             发送的SCTP包数  =  187986
             接收的SCTP包数  =  181338
  (结果个数 = 1)
 
  --- END
  ```
3. 进程号为0的SCTP协议内部统计信息：DSP SCTPAS: DSPAST=PROINT, RUNAME="USN_SP_RU_0064", PN=0;
  ```
  %%DSP SCTPAS: DSPAST=PROINT, RUNAME="USN_SP_RU_0064", PN=0;%%
  RETCODE = 0 操作成功。
 
  显示SCTP统计信息
  ----------------------------------
      注册的上层用户号  =  5
        分配的偶联号数  =  30
    标记为激活的地址数  =  0
  标记为不可用的地址数  =  1
  标记为已建链的端点数  =  0
  标记为已拆链的端点数  =  157
  (结果个数 = 1)
  --- END
  ```
4. 进程号为0的SCTP协议错误统计信息：DSP SCTPAS: DSPAST=ERROR, RUNAME="USN_SP_RU_0064", PN=0;
  ```
  %%DSP SCTPAS: DSPAST=ERROR, RUNAME="USN_SP_RU_0064", PN=0;%%
  RETCODE = 0 操作成功。
 
  显示SCTP统计信息
  ----------------------------------
         API错误次数  =  191565
        协议错误次数  =  0
        系统错误次数  =  4
    系统资源错误次数  =  0
        内部错误次数  =  0
  接收缓冲区满的次数  =  0
  (结果个数 = 1)
 
  --- END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SCTPAS.md`
