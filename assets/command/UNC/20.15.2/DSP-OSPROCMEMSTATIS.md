---
id: UNC@20.15.2@MMLCommand@DSP OSPROCMEMSTATIS
type: MMLCommand
name: DSP OSPROCMEMSTATIS（显示系统进程内存信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: OSPROCMEMSTATIS
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

# DSP OSPROCMEMSTATIS（显示系统进程内存信息）

## 功能

该命令用于显示OS进程内的内存统计信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：用于说明RU的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：<br>- 只能填写实际存在的资源单元或资源名称。<br>- 当本命令在VNFP上使用时，需要先使用[**DSP RES**](../../../../单体服务平台功能管理/系统管理/资源管理/资源实例管理/显示资源信息（DSP RES）_59036939.md)查到“资源名称”，然后将“资源名称”的取值配置到本参数。<br>- 当本命令在VNFC上使用时，需要先使用[**DSP RU**](../../../系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)查到“RU名称”，然后将“RU名称”的取值配置到本参数。 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@OSPROCMEMSTATIS]] · 系统进程内存信息（OSPROCMEMSTATIS）

## 使用实例

显示OS进程内存统计信息：

```
DSP OSPROCMEMSTATIS:RUNAME="VNODE_CSLB_VNFC_OMU_0001"
,SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
------------------------
进程ID        进程名称           Malloc申请内存（Kbytes）消息申请内存（Kbytes）   补丁申请内存（Kbytes）  So占用内存（Kbytes）  栈内存（Kbytes） Libc内存（Kbytes）   Mmap内存（Kbytes）  总内存（Kbytes）

17118         PROTO2             1035256                 9249                     10                      1948                  4096             200283449            4095069673          4296403681
9024          CFG                254543                  27177                    10                      1896                  4228             578533530            3716953221          4295774605
2840          dsle_boot          0                       0                        0                       332                   136              0                    532868              533336
4153          LM                 203806                  9249                     10                      1244                  4096             175949063            4119261921          4295429389
（结果个数 = 4）
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-OSPROCMEMSTATIS.md`
