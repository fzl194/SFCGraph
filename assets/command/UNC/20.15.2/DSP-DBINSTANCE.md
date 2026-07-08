---
id: UNC@20.15.2@MMLCommand@DSP DBINSTANCE
type: MMLCommand
name: DSP DBINSTANCE（查询CSDB子实例信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DBINSTANCE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSDB功能管理
- CSDB管理
- 实例管理
status: active
---

# DSP DBINSTANCE（查询CSDB子实例信息）

## 功能

该命令用于查询CSDB的子实例信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INSTANCEID | 子实例标识 | 可选必选说明：可选参数。<br>参数含义：该参数用于指定唯一一个子实例。<br>数据来源：本端规划<br>取值范围：1～100。<br>默认值：无。<br>配置原则：如果不指定子实例标识，则显示所有子实例的信息。 |

## 操作的配置对象

- [复位CSDB子实例（DBINSTANCE）](configobject/UNC/20.15.2/DBINSTANCE.md)

## 使用实例

直接查询：

```
DSP DBINSTANCE:

%%DSP DBINSTANCE:;%%
RETCODE = 0  操作成功

操作结果如下：
--------------
子实例标识  初始容量(M)  总容量(M)  虚拟化网络功能组件标识  VNFC类型        子集群标识     服务申请

7           0            0          999                     AgfCtrlSvc      1              是
8           0            0          999                     SbiLinkCtrlSvc  1              是
(结果个数 = 2)
---    END
```

查询 “子实例标识” 为 “2” 的信息：

```
DSP DBINSTANCE: INSTANCEID=2;

%%DSP DBINSTANCE: INSTANCEID=2;%%
RETCODE = 0  操作成功

操作结果如下：
--------------
            子实例标识  =  2
           初始容量(M)  =  1024000
             总容量(M)  =  1024000
虚拟化网络功能组件标识  =  2
              VNFC类型  =  CSLB_VNFC
            子集群标识  =  1
              服务申请  =  是 
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询CSDB子实例信息（DSP-DBINSTANCE）_29626987.md`
