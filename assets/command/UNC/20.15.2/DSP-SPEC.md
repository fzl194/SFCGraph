---
id: UNC@20.15.2@MMLCommand@DSP SPEC
type: MMLCommand
name: DSP SPEC（显示规格信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SPEC
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 系统管理
- 资源管理
- 业务规格管理
status: active
---

# DSP SPEC（显示规格信息）

## 功能

**适用网元：SGSN、MME**

本命令用于查询USN_SP_RU、SPP/SGP/GBP/UPP进程的业务规格。查询结果为由于内存资源限制而允许接入的业务最大数量。

## 注意事项

具体局点单个RU、进程的业务接入能力，还受限于License、话务模型等因素，可能达不到此命令显示的规格数量。

接入USN_SP_RU、SPP进程的2G/3G PDP和4G承载共享内存资源。USN_SP_RU、SPP进程能够接入的2G/3G PDP和4G承载总量不超过其4G承载规格。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SPECTYPE | 输入信息 | 可选必选说明：可选参数<br>参数含义：按RU或者进程显示信息。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- RU(RU)。<br>- PROC(PROC)：进程。<br>默认值：RU(RU) |
| SERVICETYPE | 服务名称 | 可选必选说明：必选参数<br>参数含义：本参数用于指定服务名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。数字“0~9”，大写字母“A~Z”，小写字母“a~z”，特殊字符“-”，“_”，其他均为非法字符，并且首字符必须为字母。<br>默认值：无<br>说明：该参数可以通过<br>[**LST VNFC**](../../../../../../平台服务管理/单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)<br>命令查询得到。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SPEC]] · 规格信息（SPEC）

## 使用实例

查询USN_SP_RU的业务规格信息：

DSP SPEC: SERVICETYPE="USN_VNFC";

```
%%DSP SPEC: 
SERVICETYPE="USN_VNFC"
;%%
RETCODE = 0 操作成功。

查询结果如下
------------------------
查询结果 =
		RU information
		RU type:          USN_SP_RU
		user size:        200000
		2G/3G PDP size:   200000
		4G size:          600000

（结果个数 = 1）
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SPEC.md`
