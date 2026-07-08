---
id: UNC@20.15.2@MMLCommand@LST APN
type: MMLCommand
name: LST APN（查询APN配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APN
command_category: 查询类
applicable_nf:
- SMF
- SGW-C
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- APN管理
- APN
status: active
---

# LST APN（查询APN配置）

## 功能

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用来查看指定APN实例或者已配置所有APN实例的配置信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>输入的APN名称需要符合APN命名规则，仅支持配置APN NI（Network Identifier），例如“huawei.com”。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APN]] · APN配置（APN）

## 使用实例

- 显示指定APN实例的信息：
  ```
  %%LST APN:APN="huawei.com";%%
  RETCODE = 0  操作成功

  结果如下
  --------
                                APN名称  =  huawei.com
                                虚拟APN  =  不使能
                                绑定VPN  =  不使能
                              VPN实例名  =  NULL
                           绑定IPv6 VPN  =  不使能
                         IPv6 VPN实例名  =  NULL
                               去活用户  =  不使能
                                   锁定  =  不使能
                   根据SGSN/SGW映射PLMN  =  使能
                    根据SGSN/SGW映射RAT  =  使能
                       仅统计应用层流量  =  不使能
                          Qchat功能开关  =  不使能
                           支持紧急呼叫  =  不使能
                     支持假激活用户开关  =  继承全局
             网络侧触发业务恢复功能开关  =  继承全局
            故障重启业务恢复功能PGW开关  =  继承全局
                           PDTN功能开关  =  不使能
   去活消息携带reactivation-request开关  =  不使能
                 用户发起的二次激活开关  =  不使能
                               计费策略  =  NULL
                            Ppd功能开关  =  继承全局
                           ULCL功能开关  =  不使能
                               场景列表  =  NULL
                           局域数据网络  =  不支持
       透明传输reactivation-request开关  =  使能
                    携带skipInd信元开关  =  不使能
             S6b Emergency Service 标识  =  不使能
                          锁定的RAT类型  =  NULL
                            PPI功能开关  =  继承全局
                                位置上报 =  继承全局
                            Parking APN  =  不使能
   支持基于漫游地动态签约的分流策略控制  =  不使能
                    主锚点always分流开关 =  不使能
                           主叫号码类型  =  MSISDN
  5G HR漫游场景H-SMF虚拟APN映射功能开关  =  不使能
                        能力开放位置上报 =  继承全局
  (结果个数 = 1)

  ---    END
  ```
- 查询整机APN实例信息：
  ```
  %%LST APN:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  APN名称               虚拟APN  绑定VPN  VPN实例名  绑定IPv6 VPN  IPv6 VPN实例名  去活用户  锁定    根据SGSN/SGW映射PLMN  根据SGSN/SGW映射RAT  仅统计应用层流量  Qchat功能开关  支持紧急呼叫  支持假激活用户开关  网络侧触发业务恢复功能开关  故障重启业务恢复功能PGW开关  PDTN功能开关  去活消息携带reactivation-request开关  用户发起的二次激活开关  计费策略  Ppd功能开关  ULCL功能开关  场景列表  局域数据网络  透明传输reactivation-request开关  携带skipInd信元开关  S6b Emergency Service 标识  锁定的RAT类型  PPI功能开关  位置上报  Parking APN   支持基于漫游地动态签约的分流策略控制 主锚点always分流开关 主叫号码类型  5G HR漫游场景H-SMF虚拟APN映射功能开关  能力开放位置上报
  a.mnc003.mcc460.gprs  不使能   不使能   NULL       不使能        NULL            不使能    不使能  使能                  使能                 不使能            不使能         不使能        继承全局            继承全局                    继承全局                     不使能        不使能                                不使能                    NULL      继承全局     不使能        NULL      不支持        使能                              不使能               不使能                      NULL           继承全局     继承全局  不使能        不使能                               不使能               MSISDN        不使能
  huawei.com            不使能   不使能   NULL       不使能        NULL            不使能    不使能  使能                  使能                 不使能            不使能         不使能        继承全局            继承全局                    继承全局                     不使能        不使能                                不使能                    NULL      继承全局     不使能        NULL      不支持        使能                              不使能               不使能                      NULL           继承全局     继承全局  不使能        不使能                               不使能               MSISDN        不使能  
                 继承全局 
 
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-APN.md`
