---
id: UNC@20.15.2@MMLCommand@DSP S1APLNK
type: MMLCommand
name: DSP S1APLNK（显示S1AP连接状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: S1APLNK
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- S1AP链路
status: active
---

# DSP S1APLNK（显示S1AP连接状态）

## 功能

**适用网元：MME**

此命令用于查询当前系统中S1AP各链路的连接状态。

## 注意事项

- 此命令执行后立即生效。
- 用户不输入参数时，查询系统当前所有S1AP链路的连接状态；输入参数时，查询指定S1AP链路的连接状态。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OUTPUTTYPE | 输出类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定输出类型。<br>取值范围：<br>- “SUMMARY（统计信息）”<br>- “SCREEN（报告输出）”，最多显示30000条记录。<br>默认值：<br>“SCREEN（报告输出）” |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定<br>SPU<br>资源单元名。该参数可以通过<br>[DSP RU](../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>数据来源：整网规划<br>取值范围：0~63 位字符串<br>默认值：无 |
| PROCESSNO | 进程号 | 可选必选说明：可选参数<br>参数含义：该参数用于指示查询的目的进程号。通过<br>**[DSP PROCESSINFO](../../../../../平台服务管理/单体服务公共功能管理/操作维护/系统调测/进程和组件信息/显示进程信息（DSP PROCESSINFO）_59103523.md)**<br>获取。<br>数据来源：整网规划<br>取值范围：0~11<br>默认值：无 |
| S1APLEINDEX | S1AP本端实体标识 | 可选必选说明：可选参数<br>参数含义：待查询S1AP本端实体标识。<br>取值范围：0～63<br>默认值：无 |
| MCC | 移动国家码 | 可选必选说明：条件可选参数<br>参数含义：待查询S1AP链路的eNodeB的移动国家码。<br>前提条件：此参数在<br>“输出类型”<br>设置为<br>“SCREEN（报告输出）”<br>后生效。<br>取值范围：3位数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：条件可选参数<br>参数含义：待查询S1AP链路的eNodeB的移动网号。<br>前提条件：此参数在<br>“输出类型”<br>设置为<br>“SCREEN（报告输出）”<br>后生效。<br>取值范围：2～3位数字<br>默认值：无 |
| ENODEBTYPE | eNodeB类型 | 可选必选说明：可选参数<br>参数含义：待查询S1AP链路的eNodeB的类型。<br>取值范围：<br>- “HOME_ENB(HOME_ENB)”<br>- “MACRO_ENB(MACRO_ENB)”<br>默认值：无 |
| ENODEBID | eNodeB标识 | 可选必选说明：条件可选参数<br>参数含义：待查询S1AP链路的eNodeB的标识。该参数为十进制，由无线获取的ID值可能需要进行转换。<br>前提条件：此参数在<br>“输出类型”<br>设置为<br>“SCREEN（报告输出）”<br>后生效。<br>取值范围：0～268435455(数值型)<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/S1APLNK]] · S1AP连接（S1APLNK）

## 使用实例

1. 查询所有S1AP链路的连接状态命令如下：DSP S1APLNK:;
  ```
  O&M  #61
  %%DSP S1APLNK:;%%
  RETCODE = 0  操作成功。

  操作结果如下
  -------------------------

                             移动国家码  =  460
                               移动网号  =  03
                            IP地址类型1  =  IPv4
                         eNodeB IP地址1  =  192.168.44.1
                            IP地址类型2  =  NULL
                         eNodeB IP地址2  =  NULL
                           eNodeB端口号  =  2011
                             eNodeB类型  =  MACRO_ENB
                             eNodeB标识  =  69649
                               链路状态  =  接入中
                       S1AP本端实体标识  =  0
                                 进程号  =  1
                               进程类型  =  SGP
                                 RU名称  =  LINK_SP_RU_0066
                             eNodeB名称  =  NONAME
                           链路闪断次数  =  0
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-S1APLNK.md`
