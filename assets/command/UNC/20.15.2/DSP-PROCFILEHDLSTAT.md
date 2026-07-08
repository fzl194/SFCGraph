---
id: UNC@20.15.2@MMLCommand@DSP PROCFILEHDLSTAT
type: MMLCommand
name: DSP PROCFILEHDLSTAT（显示进程文件句柄使用信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PROCFILEHDLSTAT
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

# DSP PROCFILEHDLSTAT（显示进程文件句柄使用信息）

## 功能

该命令用于显示进程内的文件句柄使用信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无 |
| PROCID | 进程ID | 可选必选说明：可选参数<br>参数含义：网元内一个进程的进程ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识，但不能填写0，0表示VNFP。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PROCFILEHDLSTAT]] · 进程文件句柄使用信息（PROCFILEHDLSTAT）

## 使用实例

查询进程内的文件句柄使用情况：

```
DSP PROCFILEHDLSTAT:RUNAME="VNODE_CSLB_VNFC_OMU_0001"
,SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
------------------------
进程ID        RU名称                     文件句柄数目         文件句柄最大数目

4             VNODE_CSLB_VNFC_OMU_0001    43                   1024                  
1000          VNODE_CSLB_VNFC_OMU_0001    32                   1024                  
10002         VNODE_CSLB_VNFC_OMU_0001    33                   1024                  
10001         VNODE_CSLB_VNFC_OMU_0001    32                   1024                  
1001          VNODE_CSLB_VNFC_OMU_0001    33                   1024                  
3             VNODE_CSLB_VNFC_OMU_0001    42                   1024                  
2             VNODE_CSLB_VNFC_OMU_0001    36                   1024   
(结果个数 = 7)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示进程文件句柄使用信息（DSP-PROCFILEHDLSTAT）_59103948.md`
