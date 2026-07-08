---
id: UNC@20.15.2@MMLCommand@DSP HTTPPROCESS
type: MMLCommand
name: DSP HTTPPROCESS（显示HTTP进程信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: HTTPPROCESS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP进程状态管理
status: active
---

# DSP HTTPPROCESS（显示HTTP进程信息）

## 功能

该命令用于显示HTTP POD内的进程信息，进程分为HTTP进程和TCP进程，显示信息包含HTTP进程、TCP进程和HTTP POD的关系以及对应进程的状态、CPU消耗、内存消耗等信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCESSTYPE | 进程类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定进程的类型。<br>数据来源：本端规划<br>取值范围：<br>- “TCP（TCP进程）”：TCP进程<br>- “HTTP（HTTP进程）”：HTTP进程<br>- “CELLWALL（CELLWALL进程）”：CELLWALL进程<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/HTTPPROCESS]] · HTTP进程信息（HTTPPROCESS）

## 使用实例

- 查询HTTP进程信息，可以执行下面的命令。
  ```
  %%DSP HTTPPROCESS: PROCESSTYPE=HTTP;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
                     POD名称  =  uncpod-0
                    进程类型  =  HTTP进程
                    进程标识  =  17
                全局进程标识  =  0
                    进程状态  =  正常
               进程CPU占用率  =  18
                进程空闲内存  =  Normal: 222220264, Body: 647756328
             已使用Reqcb数量  =  0
        已建立的HTTP链路数量  =  1
        TLS上下文资源占用总数 =  0
           用户定时器使用总数 =  21
                    链路资源  =  logic_link_2_ctx: 0, key_2_logic_link: 0, linkset_ctx: 0, key_2_request_addr_link: 0, key_timeout: 0, scp_num:0
                    跟踪资源  =  g_user_id_2_task: 0, g_ran_user_id_2_task: 0, g_e2e_user_id_2_task: 0, g_set_interface_task_handle: 0, g_task_queue: 0, bind_userid_2_handle_map: 0, bind_sdrkey_2_userid_map: 0 
                  编解码资源  =  method_string2enum: 8, g_protocol_table.protocol_string2enum: 20
                    统计资源  =  g_client_topic_send_count_map: 0, g_server_topic_send_count_map: 0
                    会话资源  =  app_data_normal_free: 31744, app_data_big_free: 1024, app_data_large_free: 8, g_ready_rid: 0, g_destroy_rid: 0
                    其他资源  =  log_fc_node: 0, bind_cpu_num: 4, msg_speed_info: sdra_recv[0.00], client_req[0.00], server_req[0.00], used_timers: 21
                 TLS证书资源  =  0 
       关键流程使用Rqqcb数量  =  0
           进程平均CPU占用率  =  18
                客户端链路数  =  18
                服务端链路数  =  18
  (结果个数 = 1)
  ```
- 查询TCP进程信息，可以执行下面的命令。
  ```
  %%DSP HTTPPROCESS: PROCESSTYPE=TCP;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
                      POD名称  =  uncpod-0
                     进程类型  =  TCP进程
                     进程标识  =  16
                     进程状态  =  正常
                进程CPU占用率  =  7
                 进程空闲内存  =  Normal: 253868544, Body: 0
              已使用Reqcb数量  =  0
          已建立的HTTP链路数量 =  0
         TLS上下文资源占用总数 =  0
            用户定时器使用总数 =  0
                      PMTU资源 =  g_PmtuConfigCache: 0, g_PmtuDetectCache: 0, tcp_cpu_env: 8
             进程平均CPU占用率 =  7
  (结果个数 = 1)
  ```
- 查询CELLWALL进程信息，可以执行下面的命令。
  ```
  %%DSP HTTPPROCESS: PROCESSTYPE=CELLWALL;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
                   POD名称  =  uncpod-0
  	   进程CPU占用率  =  2
  	    进程空闲内存  =  Normal: 263181256, Body: 0
                  其他资源  =  g_OmMsgCache: 0, static token num: 4, dynamic token num: 256, server token num: 32
  (结果个数 = 1)
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示HTTP进程信息（DSP-HTTPPROCESS）_29053327.md`
