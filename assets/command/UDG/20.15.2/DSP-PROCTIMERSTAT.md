---
id: UDG@20.15.2@MMLCommand@DSP PROCTIMERSTAT
type: MMLCommand
name: DSP PROCTIMERSTAT（显示进程定时器计数信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: PROCTIMERSTAT
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

# DSP PROCTIMERSTAT（显示进程定时器计数信息）

## 功能

该命令用于显示进程内的定时器使用信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：当不输入时显示所有资源单元信息。 |
| PROCID | 进程ID | 可选必选说明：可选参数<br>参数含义：网元内一个进程的进程ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识，但不能填写0，0表示VNFP。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PROCTIMERSTAT]] · 进程定时器计数信息（PROCTIMERSTAT）

## 使用实例

查询进程内的定时器使用情况：

```
DSP PROCTIMERSTAT:RUNAME="VNODE_CSLB_VNFC_OMU_0001"
,SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
--------
进程ID    RU名称                       绝对定时器数目    相对定时器数目    APP定时器数目 

4         VNODE_CSLB_VNFC_OMU_0001      0                 37                69            
1002      VNODE_CSLB_VNFC_OMU_0001      0                 29                23            
1001      VNODE_CSLB_VNFC_OMU_0001      0                 68                91            
1000      VNODE_CSLB_VNFC_OMU_0001      0                 8                 15            
10002     VNODE_CSLB_VNFC_OMU_0001      0                 6                 15            
10001     VNODE_CSLB_VNFC_OMU_0001      0                 23                59            
1003      VNODE_CSLB_VNFC_OMU_0001      0                 16                25            
3         VNODE_CSLB_VNFC_OMU_0001      0                 55                21            
2         VNODE_CSLB_VNFC_OMU_0001      0                 34                40            
(结果个数 = 9)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-PROCTIMERSTAT.md`
