---
id: UDG@20.15.2@MMLCommand@DSP COMCONTAINER
type: MMLCommand
name: DSP COMCONTAINER（显示组件和容器关系信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: COMCONTAINER
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

# DSP COMCONTAINER（显示组件和容器关系信息）

## 功能

该命令用于显示指定进程中组件与容器的调度关系。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定要查询组件所属进程的ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@COMCONTAINER]] · 组件和容器关系信息（COMCONTAINER）

## 使用实例

查询进程1001调度容器和组件的关系：

```
DSP COMCONTAINER:PROCID=1001
,SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
---------------------------------------------------
容器ID          绑定类型  任务ID     线程ID             组件名            组件类型          组件ID   
1               nobind    9          139906535257856    EXP_MML           1028              0x84040410 
1               nobind    9          139906535257856    NPS_MML           520               0x82080411  
1               nobind    9          139906535257856    NETCONF           151               0x80970414 
1               nobind    9          139906535257856    NETCONFC          2335              0x891F0416  
1               nobind    9          139906535257856    HTTPC             727               0x82D70417  
1               nobind    9          139906535257856    HTTPS             728               0x82D80418  
1               nobind    9          139906535257856    SSHC              146               0x80920422  
1               nobind    9          139906535257856    SSHS              147               0x80930423   
1               nobind    10         139906206557952    EXP_MML           1028              0x84040410  
1               nobind    10         139906206557952    NPS_MML           520               0x82080411 
1               nobind    10         139906206557952    NETCONF           151               0x80970414   
1               nobind    10         139906206557952    NETCONFC          2335              0x891F0416  
1               nobind    10         139906206557952    HTTPC             727               0x82D70417
1               nobind    10         139906206557952    HTTPS             728               0x82D80418
1               nobind    10         139906206557952    SSHC              146               0x80920422  
1               nobind    10         139906206557952    SSHS              147               0x80930423 
2               bind      6          139906535663360    SEM_Agent         3                 0x8003040C 
3               bind      7          139906535528192    APPCFG            207               0x80CF040D 
4               bind      8          139906535393024    DBG_AGENT         51                0x8033040E    
(结果个数 = 19)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-COMCONTAINER.md`
