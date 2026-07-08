---
id: UDG@20.15.2@MMLCommand@DSP PATCHDETAILINFO
type: MMLCommand
name: DSP PATCHDETAILINFO（显示补丁信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: PATCHDETAILINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 系统管理
- 系统维护
- 补丁管理
status: active
---

# DSP PATCHDETAILINFO（显示补丁信息）

## 功能

该命令用于显示补丁详细信息，包括补丁单元文件名、运行状态、补丁类型、是否生效及生效时间等。

补丁的加载、激活，删除会触发补丁状态的变化，使用该命令显示系统当前的补丁单元状态信息。

## 注意事项

不指定查询条件时，该命令只支持返回最多30000个补丁记录；超过30000个补丁记录查询时该命令会报错，此时请指定RU名称或进程ID进行查询操作。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定要查询补丁单元的RU的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：只能填写实际存在的资源单元，使用<br>[**DSP RU**](../../资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>查看RU名称。 |
| PROCID | 进程ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定要查询补丁单元所属进程的ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| STATE | 状态 | 可选必选说明：可选参数<br>参数含义：该参数用于指定要查询补丁单元的状态。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Idle：补丁状态为空闲。<br>- Deactive：补丁状态为去激活。<br>- Active：补丁状态为激活。<br>- Running：补丁状态为运行。<br>默认值：无 |
| PATCHTYPE | 类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定要查询补丁单元的类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无 |
| VALID | 是否生效 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询是否生效的补丁单元。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- No：补丁单元不生效。<br>- Yes：补丁单元生效。<br>默认值：无 |
| EFFECTIVETIME | 生效时间 | 可选必选说明：可选参数<br>参数含义：该参数用于指定要查询补丁单元的生效时间，补丁未生效时显示为NULL，NULL不能作为入参。<br>数据来源：本端规划<br>取值范围：日期时间类型，输入格式是YYYY&MM&DD&HH&NN&SS。01/01/2000 00:00:00～31/12/2037 23:59:59。<br>默认值：无 |
| PATCHFILENAME | 文件名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定要查询补丁单元文件名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PATCHDETAILINFO]] · 补丁信息（PATCHDETAILINFO）

## 使用实例

显示补丁详细信息：

```
DSP PATCHDETAILINFO:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
-------------------------
RU名称                         进程ID         状态    类型        是否生效          生效时间                         文件名
VNODE_CSDB_VNFC_OMU_0001       3              运行    SCRIPT      是                2015-11-29 15:22:48+02:00 DST    HP000002.pat
VNODE_CSDB_VNFC_OMU_0001       3              运行    SCRIPT      是                2015-11-29 15:22:48+02:00 DST    HP000005.pat
VNODE_CSDB_VNFC_OMU_0001       6              运行    SCRIPT      是                2015-11-29 16:34:30+02:00 DST    HP000002.pat
VNODE_CSDB_VNFC_OMU_0001       6              运行    SCRIPT      是                2015-11-29 16:34:31+02:00 DST    HP000005.pat
(结果个数 = 4)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-PATCHDETAILINFO.md`
