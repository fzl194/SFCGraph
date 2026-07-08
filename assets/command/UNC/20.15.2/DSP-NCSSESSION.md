---
id: UNC@20.15.2@MMLCommand@DSP NCSSESSION
type: MMLCommand
name: DSP NCSSESSION（显示NETCONF会话信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NCSSESSION
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 网络配置协议
status: active
---

# DSP NCSSESSION（显示NETCONF会话信息）

## 功能

该命令用于显示NETCONF会话信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SESSIONID | NETCONF会话ID | 可选必选说明：可选参数<br>参数含义：NETCONF会话标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。<br>默认值：无 |
| VERBOSEFLG | 详细信息标志位 | 可选必选说明：可选参数<br>参数含义：该参数用于表示详细信息标志位。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～1。“0”代表查询简要的会话信息，“1”代表查询详细的会话信息。<br>默认值：无<br>配置原则：如果需要指定详细信息标志位，则必须先指定NETCONF会话ID。 该命令不带参数“VERBOSEFLG” 和带参数“VERBOSEFLG=0”最终的显示是一致的。 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [NETCONF会话信息（NCSSESSION）](configobject/UNC/20.15.2/NCSSESSION.md)

## 使用实例

- 显示NETCONF会话的信息：
  ```
  DSP NCSSESSION:
  SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  ---------
  NETCONF会话ID  用户名        通道ID  会话状态  事务状态  查询状态  多语种类型  通知状态  AAA认证会话ID  用户组ID  用户级别  会话是否被锁  协商能力集  NETCONF客户端能力集  待处理的get-next请求  任务组列表  

  59             VNFP_SYSTEM   134305  NULL      NULL      NULL      NULL        0         0              0         0         否            NULL        NULL                 NULL                  NULL        
  60             internaluser  134337  NULL      NULL      NULL      NULL        0         0              0         0         否            NULL        NULL                 NULL                  NULL        
  61             internaluser  134561  NULL      NULL      NULL      NULL        0         0              0         0         否            NULL        NULL                 NULL                  NULL        
  62             internaluser  134593  NULL      NULL      NULL      NULL        0         0              0         0         否            NULL        NULL                 NULL                  NULL        
  64             internaluser  134657  NULL      NULL      NULL      NULL        0         0              0         0         否            NULL        NULL                 NULL                  NULL        
  182            HAFG          134626  NULL      NULL      NULL      NULL        0         0              0         0         否            NULL        NULL                 NULL                  NULL        
  256            VNFP_SYSTEM   134690  NULL      NULL      NULL      NULL        0         0              0         0         否            NULL        NULL                 NULL                  NULL        
  5140           internaluser  134557  NULL      NULL      NULL      NULL        0         0              0         0         否            NULL        NULL                 NULL                  NULL        
  6282           internaluser  134828  NULL      NULL      NULL      NULL        0         0              0         0         否            NULL        NULL                 NULL                  NULL        
  9423           internaluser  134407  NULL      NULL      NULL      NULL        0         0              0         0         否            NULL        NULL                 NULL                  NULL        
  10463          internaluser  134487  NULL      NULL      NULL      NULL        0         0              0         0         否            NULL        NULL                 NULL                  NULL        
  11817          internaluser  134277  NULL      NULL      NULL      NULL        0         0              0         0         否            NULL        NULL                 NULL                  NULL        
  (结果个数 = 12)

  ---    END
  ```
- 显示指定NETCONF会话的信息：
  ```
  DSP NCSSESSION:SESSIONID=169
  ,SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  ---------
         NETCONF会话ID  =  59
                用户名  =  VNFP_SYSTEM
                通道ID  =  134305
              会话状态  =  READY
              事务状态  =  NEUTRAL
              查询状态  =  QUERY
            多语种类型  =  GENERAL
              通知状态  =  0
         AAA认证会话ID  =  1
              用户组ID  =  10
              用户级别  =  65535
          会话是否被锁  =  否
            协商能力集  =  NULL
   NETCONF客户端能力集  =  NULL
  待处理的get-next请求  =  NULL
            任务组列表  =  NULL
  (结果个数 = 1)

  ---    END
  ```
- 显示指定NETCONF会话的详细信息：
  ```
  DSP NCSSESSION:SESSIONID=169,VERBOSEFLG=1
  ,SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  ---------
         NETCONF会话ID  =  59
                用户名  =  VNFP_SYSTEM
                通道ID  =  134305
              会话状态  =  READY
              事务状态  =  NEUTRAL
              查询状态  =  QUERY
            多语种类型  =  GENERAL
              通知状态  =  0
         AAA认证会话ID  =  1
              用户组ID  =  10
              用户级别  =  65535
          会话是否被锁  =  否
            协商能力集  =  Base                     public   1.0
  Base                     private  2.0
  Writable-Running         public   1.0
  Candidate                public   1.0
  Distinct Startup         public   1.0
  Rollback on Error        public   1.0
  Confirmed Commit         public   1.0
  Exchange                 private  1.0
  Action                   private  2.0
   NETCONF客户端能力集  =  Total number of capabilities received : 7

  urn:ietf:params:netconf:base:1.0
  http://www.huawei.com/netconf/capability/action/1.0
  urn:ietf:params:netconf:capability:startup:1.0
  urn:ietf:params:netconf:capability:writable-running:1.0
  http://www.huawei.com/netconf/capability/exchange/1.0
  http://www.huawei.com/netconf/capability/base/2.0
  http://www.huawei.com/netconf/capability/action/2.0
  待处理的get-next请求  =  Total number of pending get-next requests : 0

            任务组列表  =  NULL
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示NETCONF会话信息（DSP-NCSSESSION）_59103552.md`
