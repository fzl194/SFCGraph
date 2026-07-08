---
id: UNC@20.15.2@MMLCommand@DSP CGQUEUESTATUS
type: MMLCommand
name: DSP CGQUEUESTATUS（显示NCG队列状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: CGQUEUESTATUS
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务配置管理
- NCG队列状态
status: active
---

# DSP CGQUEUESTATUS（显示NCG队列状态）

## 功能

**适用NF：NCG**

该命令用于查询NCG内部队列的状态。

## 注意事项

无

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUID | RU的ID | 可选必选说明：可选参数<br>参数含义：RU的ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为64～4294967294。<br>默认值：无<br>配置原则：该值需要执行<br>[**LST SERVICERUSTATE**](../../../../../平台服务管理/单体服务编排功能管理/系统管理/资源管理/RU信息/查询RU的信息(LST SERVICERUSTATE)_29626965.md)<br>命令，查询出存在的“RU的ID”进行填写。 |
| QUEUETYPE | 队列类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询的队列类型。<br>数据来源：本端规划。<br>取值范围：枚举类型。<br>- GA_QUEUE：GA接口的相关队列。<br>- COMP_QUEUE：组件消息队列。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CGQUEUESTATUS]] · NCG队列状态（CGQUEUESTATUS）

## 使用实例

查询当前NCG内部队列状态，示例如下：

```
DSP CGQUEUESTATUS:;
```

```
RETCODE = 0  操作成功  
结果如下: 
--------- 
RU的ID  进程名  队列类型      队列名称          队列容量  当前使用量  队列超限次数  关键字1                                                                      关键字2  关键字3  关键字4  关键字5
2       QBM     组件消息队列  MSG_QUEUE         524288    0           0             QBM                                                                          NULL     NULL     NULL     NULL
64      AP64_1  组件消息队列  MSG_QUEUE         524288    0           0             CCL                                                                          NULL     NULL     NULL     NULL      
64      AP64_1  组件消息队列  MSG_QUEUE         524288    0           0             GACM                                                                         NULL     NULL     NULL     NULL      
64      AP64_1  组件消息队列  MSG_QUEUE         524288    0           0             CDW                                                                          NULL     NULL     NULL     NULL      
64      AP64_1  组件消息队列  MSG_QUEUE         524288    0           0             BILLSAVE                                                                     NULL     NULL     NULL     NULL      
64      AP64_1  组件消息队列  MSG_QUEUE         524288    0           0             FAM                                                                          NULL     NULL     NULL     NULL      
64      AP64_1  GA接口队列    DATA_QUEUE        480000    0           0             Normal:0,MayDup:0,Release:0,Cancel:0,Empty:0,Other:0                         NULL     NULL     NULL     NULL    
64      AP64_1  GA接口队列    NEW_FRAMES_QUEUE  4500      0           0             SRC:10.31.14.7:7112 DST:10.31.14.3:3386                                      NULL     NULL     NULL     NULL
64      AP64_1  GA接口队列    DUP_FRAMES_QUEUE  65535     0           0             SRC:10.31.14.7:7112 DST:10.31.14.3:3386                                      NULL     NULL     NULL     NULL
64      AP64_1  GA接口队列    REL_FRAMES_QUEUE  65535     0           0             SRC:10.31.14.7:7112 DST:10.31.14.3:3386                                      NULL     NULL     NULL     NULL
64      CBK     组件消息队列  MSG_QUEUE         524288    0           0             CBK                                                                          NULL     NULL     NULL     NULL      
64      CDM     组件消息队列  MSG_QUEUE         524288    0           0             CDM                                                                          NULL     NULL     NULL     NULL      
64      CQB     组件消息队列  MSG_QUEUE         524288    0           0             CQB                                                                          NULL     NULL     NULL     NULL      
64      RCM     组件消息队列  MSG_QUEUE         524288    0           0             RCM                                                                          NULL     NULL     NULL     NULL     
(结果个数 = 14)  
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示NCG队列状态（DSP-CGQUEUESTATUS）_28534237.md`
