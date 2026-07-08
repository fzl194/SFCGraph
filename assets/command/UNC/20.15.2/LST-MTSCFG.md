---
id: UNC@20.15.2@MMLCommand@LST MTSCFG
type: MMLCommand
name: LST MTSCFG（查询消息跟踪配置参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MTSCFG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 消息跟踪
status: active
---

# LST MTSCFG（查询消息跟踪配置参数）

## 功能

本命令用于查询消息跟踪的配置参数。

## 注意事项

无。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TYPE | 类型 | 可选必选说明：可选参数。<br>参数含义：消息跟踪配置参数的类型。若不输入，则表示该参数不作为查询的限制条件。<br>取值范围：<br>- FLOW_CONTROL_SWITCH(跟踪服务资源流控开关)<br>- BASE_SUBHEALTH_SWITCH(跟踪服务Base亚健康消减开关)<br>默认值：无。<br>配置原则：无。 |
| MEID | 网元ID | 可选必选说明：该参数在<br>“类型”<br>配置为<br>“FLOW_CONTROL_SWITCH(跟踪服务资源流控开关)”<br>或者<br>“BASE_SUBHEALTH_SWITCH(跟踪服务Base亚健康消减开关)”<br>时为条件可选参数。<br>参数含义：标识网元ID。<br>取值范围：0~65535。<br>默认值：无。<br>配置原则：可以通过<br>[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)<br>命令查询获取。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MTSCFG]] · 消息跟踪配置参数（MTSCFG）

## 使用实例

查询消息跟踪配置状态：

```
LST MTSCFG:;
```

```
%%LST MTSCFG:;%% 
RETCODE = 0  操作成功  

消息跟踪配置参数（跟踪服务资源流控开关） 
---------------------------------------- 
网元ID  =  0   
开关  =  开启 
(结果个数 = 1)  

消息跟踪配置参数（跟踪服务Base亚健康消减开关）
 ---------------------------------------------- 
网元ID  =  0   
开关  =  关闭 
(结果个数 = 1) 
 
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-MTSCFG.md`
