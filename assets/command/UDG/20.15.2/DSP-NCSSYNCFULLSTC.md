---
id: UDG@20.15.2@MMLCommand@DSP NCSSYNCFULLSTC
type: MMLCommand
name: DSP NCSSYNCFULLSTC（显示全量同步操作期间的统计信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: NCSSYNCFULLSTC
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

# DSP NCSSYNCFULLSTC（显示全量同步操作期间的统计信息）

## 功能

该命令用于显示全量同步操作期间的统计信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VERBOSEFLG | 详细输出标志位 | 可选必选说明：可选参数<br>参数含义：是否输出详细信息标志位。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@NCSSYNCFULLSTC]] · 全量同步操作期间的统计信息（NCSSYNCFULLSTC）

## 使用实例

- 显示全量同步操作期间的统计信息：
  ```
  DSP NCSSYNCFULLSTC:
  SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  ------------------------
                 NETCONF会话ID  =  124
                  文件传输标识  =  0x10081
                        操作ID  =  1
                    应用错误项  =  continue-on-error
             接收RPC报文时间戳  =  2016-05-26, 15:27:41:485
                查询结束时间戳  =  2016-05-26, 15:27:45:063
        文件传输处理结束时间戳  =  2016-05-26, 15:27:45:894
       NETCONF处理时间（微秒）  =  100181
      配置管理处理时间（微秒）  =  3477819
      文件传输处理时间（微秒）  =  830732
            处理总时间（微秒）  =  4408732
                      应用个数  =  58
                      执行结果  =  Success
  (结果个数 = 1)
  ---    END
  ```
- 显示全量同步操作期间的详细统计信息：
  ```
  DSP NCSSYNCFULLSTC:VERBOSEFLG=TRUE
  ,SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  ------------------------
                                    NETCONF会话ID  =  124
                                     文件传输标识  =  0x10081
                                           操作ID  =  1
                                       应用错误项  =  continue-on-error
                                接收RPC报文时间戳  =  2016-05-26, 15:27:41:485
                                   查询结束时间戳  =  2016-05-26, 15:27:45:063
                           文件传输处理结束时间戳  =  2016-05-26, 15:27:45:894
                          NETCONF处理时间（微秒）  =  100181
                         配置管理处理时间（微秒）  =  3477819
                         文件传输处理时间（微秒）  =  830732
                               处理总时间（微秒）  =  4408732
                                         应用个数  =  58
                                         执行结果  =  Success
                                     应用错误信息  =  NULL
                                     应用成功信息  =  
  Feature Name                    Processing Time(microseconds)                 Record Number  Data Size(bytes)
  psp_perf                        3087                                          0              0
  system                          21360                                         2              1672
  timerange                       12089                                         0              0
  ecc                             31598                                         1              16
  ssl                             41426                                         4              2243
  mss                             17064                                         0              0
  RTP                             62405                                         0              0
  socket                          16778                                         1              44
  HTTPS                           47617                                         2              171
  pae                             45159                                         4              32
  auth                            0                                             0              0
  migrate                         24679                                         0              0
  STATICRT                        105095                                        3              852
  l3vpn                           165169                                        11             5326
  RM                              33553                                         7              526
  netconf                         55413                                         0              0
  SecuritySirp                    0                                             0              0
  sshc                            63143                                         6              781
  hostdefend                      33331                                         2              26
  tm                              16096                                         2              139
  nqa                             10637                                         1              8
  mqc                             71023                                         0              0
  pki                             65838                                         1              2
  TraceSirp                       64515                                         0              0
  ETHERNET                        443599                                        0              0
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-NCSSYNCFULLSTC.md`
