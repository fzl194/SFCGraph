---
id: UDG@20.15.2@MMLCommand@DSP PROCMEMPT
type: MMLCommand
name: DSP PROCMEMPT（显示进程内存分区信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: PROCMEMPT
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

# DSP PROCMEMPT（显示进程内存分区信息）

## 功能

该命令用于显示进程内的分区内存使用信息。

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

- [进程内存分区信息（PROCMEMPT）](configobject/UDG/20.15.2/PROCMEMPT.md)

## 使用实例

查询进程内分区内存的使用情况：

```
DSP PROCMEMPT:RUNAME="VNODE_CSLB_VNFC_OMU_0001",PROCID=1001
,SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
--------
进程ID    RU名称                     内存分区名    分区内存总大小（Kbytes）  分区内存使用大小（Kbytes）  分区内存使用最大值（Kbytes）  分区内存使用率（%）

1001      VNODE_CSLB_VNFC_OMU_0001    SYSPT         4096                      3319                        3389                          81                
1001      VNODE_CSLB_VNFC_OMU_0001    dbPT          6144                      5191                        5199                          84                
1001      VNODE_CSLB_VNFC_OMU_0001    pipePT        15367                     14679                       14679                         95                
1001      VNODE_CSLB_VNFC_OMU_0001    msq_node      1562                      1561                        1561                          99                
1001      VNODE_CSLB_VNFC_OMU_0001    commonPt      102400                    14097                       14338                         13                
1001      VNODE_CSLB_VNFC_OMU_0001    tempPt        1536                      240                         540                           15                
1001      VNODE_CSLB_VNFC_OMU_0001    simplePt      1024                      387                         387                           37                
（结果个数 = 7）
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示进程内存分区信息（DSP-PROCMEMPT）_59103976.md`
