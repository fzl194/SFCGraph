---
id: UNC@20.15.2@MMLCommand@DSP GWFAULTINF
type: MMLCommand
name: DSP GWFAULTINF（显示网关故障信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: GWFAULTINF
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 网关故障管理
status: active
---

# DSP GWFAULTINF（显示网关故障信息）

## 功能

**适用网元：MME**

该命令用于查看系统内记录的网关故障信息，包含故障类型、故障时间、故障IP地址。

## 注意事项

无。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DT | 查询方式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询方式。<br>取值范围：<br>“PROCESS_NO(进程标识)”<br>默认值：无<br>说明：如果不设置本参数，则表示查询所有业务进程上故障信息的数目。 |
| RUNAME | RU名称 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定节点的RU名称。该参数可以通过<br>[DSP RU](../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>前提条件: 该参数在<br>“查询方式”<br>参数配置为<br>“PROCESS_NO(进程标识)”<br>后生效。<br>取值范围：0～63位字符串<br>默认值：无 |
| PN | 进程号 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定需要查看SPP进程的进程号。<br>前提条件: 该参数在<br>“查询方式”<br>参数配置为<br>“PROCESS_NO(进程标识)”<br>后生效。<br>取值范围：0~20<br>默认值：无 |

## 操作的配置对象

- [网关故障信息（GWFAULTINF）](configobject/UNC/20.15.2/GWFAULTINF.md)

## 使用实例

1. 显示所有SPP进程上的故障信息：
  DSP GWFAULTINF:;
  ```
  %%DSP GWFAULTINF:;%%
  RETCODE = 0  操作成功。

  操作结果如下
  ------------
  RU名称           进程号  接口故障个数  网关重启个数

  USN_SP_RU_0064   1       0             0           
  USN_SP_RU_0064   0       0             0           
  (结果个数 = 2)

  ---    END
  ```
2. 显示指定SPP进程上的故障信息：
  DSP GWFAULTINF:DT=PROCESS_NO, RUNAME="USN_SP_RU_0064", PN=0:;
  ```
  %%DSP GWFAULTINF: DT=PROCESS_NO, RUNAME="USN_SP_RU_0064", PN=0;%%
  RETCODE = 0  操作成功。

  接口故障信息
  ------------
    接口类型  =  S11
    故障时间  =  2014-11-25 21:07:52
  本端IP地址  =  192.168.24.48
  对端IP地址  =  10.10.10.10
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示网关故障信息(DSP-GWFAULTINF)_26146084.md`
