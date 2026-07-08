---
id: UDG@20.15.2@MMLCommand@DSP COMPONENTSUB
type: MMLCommand
name: DSP COMPONENTSUB（显示组件订阅信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: COMPONENTSUB
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 进程和组件信息
status: active
---

# DSP COMPONENTSUB（显示组件订阅信息）

## 功能

该命令用于显示指定进程内的组件订阅信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| COMPCID | 组件ID | 可选必选说明：必选参数<br>参数含义：组件ID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |
| PROCID | 进程ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定要查询组件所属进程的ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@COMPONENTSUB]] · 组件订阅信息（COMPONENTSUB）

## 使用实例

在VNFC侧显示进程1001上组件0x80CF001F的订阅信息：

```
DSP COMPONENTSUB:COMPCID="0x80CF001F",PROCID=1001
,SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
------------------------
订阅时间                 组件ID           对端组件ID     组件状态      通知          

11-15 11:40:43.291362    0x80CF001F       0xCB0009       NULL          SUBSCRIBE             
11-15 11:40:43.291424    0x80CF001F       0xCD0008       NULL          SUBSCRIBE                  
11-15 11:40:43.291480    0x80CF001F       0x8003001E     NULL          SUBSCRIBE             
11-15 11:40:43.291597    0x80CF001F       0x8003001E     PRIMARY       COMP-UPDATE STATE: OK 
11-15 11:40:43.291653    0x80CF001F       0x80CF001F     NULL          SUBSCRIBE             
11-15 11:40:43.291664    0x80CF001F       0x80CF001F     BACKUP        COMP-UPDATE STATE: OK 
11-15 11:40:43.298049    0x80CF001F       0xCB0009       NULL          PID WAITABLE          
11-15 11:40:43.298050    0x80CF001F       0xCB0009       PRIMARY       COMP-UPDATE STATE: OK 
11-15 11:40:43.298160    0x80CF001F       0xCD0008       NULL          PID WAITABLE          
11-15 11:40:43.298161    0x80CF001F       0xCD0008       PRIMARY       COMP-UPDATE STATE: OK 
11-15 11:40:47.961245    0x80CF001F       0x80650020     NULL          SUBSCRIBE             
11-15 11:40:47.962689    0x80CF001F       0x84040021     NULL          SUBSCRIBE             
11-15 11:40:47.963011    0x80CF001F       0x82080022     NULL          SUBSCRIBE             
11-15 11:40:47.993768    0x80CF001F       0x80970027     NULL          SUBSCRIBE             
11-15 11:40:48.046106    0x80CF001F       0x81970029     NULL          SUBSCRIBE             
11-15 11:40:48.046648    0x80CF001F       0x80920032     NULL          SUBSCRIBE             
11-15 11:40:48.047589    0x80CF001F       0x80930033     NULL          SUBSCRIBE             
11-15 11:40:48.050176    0x80CF001F       0x80650020     BACKUP        COMP-UPDATE STATE: OK 
11-15 11:40:48.051249    0x80CF001F       0x84040021     BACKUP        COMP-UPDATE STATE: OK 
11-15 11:40:48.051569    0x80CF001F       0x82080022     BACKUP        COMP-UPDATE STATE: OK 
11-15 11:40:48.052651    0x80CF001F       0x80970027     BACKUP        COMP-UPDATE STATE: OK 
11-15 11:40:48.052764    0x80CF001F       0x81970029     BACKUP        COMP-UPDATE STATE: OK 
11-15 11:40:48.053138    0x80CF001F       0x80920032     BACKUP        COMP-UPDATE STATE: OK 
11-15 11:40:48.053696    0x80CF001F       0x80930033     BACKUP        COMP-UPDATE STATE: OK 
11-15 11:42:41.721464    0x80CF001F       0xCB0009       NULL          COMP-UPDATE STATE: NG 
11-15 11:42:41.721494    0x80CF001F       0xCD0008       NULL          COMP-UPDATE STATE: NG 
11-15 11:42:41.784603    0x80CF001F       0xCB0009       PRIMARY       COMP-UPDATE STATE: OK 
11-15 11:42:41.784811    0x80CF001F       0xCD0008       PRIMARY       COMP-UPDATE STATE: OK 
(结果个数 = 28)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-COMPONENTSUB.md`
