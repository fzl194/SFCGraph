---
id: UNC@20.15.2@MMLCommand@LST VLRTIMERPARA
type: MMLCommand
name: LST VLRTIMERPARA（查询VLR网元定时器）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: VLRTIMERPARA
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- VLR业务管理
- 定时器管理
status: active
---

# LST VLRTIMERPARA（查询VLR网元定时器）

## 功能

**适用NF：SMSF**

该命令用于查询VLR配置的相关业务定时器信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@VLRTIMERPARA]] · VLR网元定时器（VLRTIMERPARA）

## 使用实例

运营商希望查询VLR相关的业务定时器信息，执行如下命令：

```
LST VLRTIMERPARA:;
%%LST VLRTIMERPARA:;%%
RETCODE = 0  操作成功

结果如下：
------------------------
等待HLR发送MAP-OPEN Confirm定时器(秒)  =  6
等待HLR发送MAP-INSERT-SUBSCRIBER-DATA Indication定时器(秒)  =  6
          等待HLR响应MAP_UPDATE_LOCATION Confirm定时器(秒)  =  6
                 等待HLR响应MAP_PURGE_MS Confirm定时器(秒)  =  6
	     等待HLR响应MAP-READY-FOR-SM Confirm定时器(秒)  =  6
                        等待注册中心位置更新响应定时器(秒)  =  6
                            等待注册中心查询响应定时器(秒)  =  6
                            等待注册中心分离响应定时器(秒)  =  6
                          MO流程等待MME响应CpAck定时器(秒)  =  6
                        MT流程等待MME Paging响应定时器(秒)  =  6
                         MT流程等待MME Alert响应定时器(秒)  =  6
                             MT流程等待MME CpAck定时器(秒)  =  6
                    MT流程等待MME DELIVER REPORT定时器(秒)  =  6
                   等待NCG响应ChargingDataRequest定时器(秒)  =  6
       
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-VLRTIMERPARA.md`
