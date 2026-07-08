---
id: UNC@20.15.2@MMLCommand@DSP CHGFILEDIR
type: MMLCommand
name: DSP CHGFILEDIR（显示话单文件的工作目录）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: CHGFILEDIR
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 计费管理
- 话单文件的工作目录
status: active
---

# DSP CHGFILEDIR（显示话单文件的工作目录）

## 功能

**适用网元：SGSN**

该命令用于显示话单文件的工作目录。用户的话单文件被保存在磁盘的CDR目录下，该目录下有CDR1和CDR2两个子目录，其中一个子目录是工作目录，无法发往CG的话单将被写入该工作目录下的话单文件。为了防止话单文件的操作冲突，工作目录下的话单文件不能进行导入导出操作。因此用户需要对磁盘上的话单文件进行导入导出操作前，需要通过本命令查询希望进行导入导出操作的目录是否属于工作目录，如果是，需要执行 [**SWP CHGFILEDIR**](切换话单文件的工作目录(SWP CHGFILEDIR)_72225043.md) 命令切换话单文件的工作目录，然后再针对非工作目录执行话单文件的导入导出操作。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要显示话单文件工作目录的RU。该参数可以通过<br>[DSP RU](../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>数据来源：本端规划<br>取值范围：0~63 位字符串，通过<br>[DSP RU](../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令获取。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CHGFILEDIR]] · 切换话单文件的工作目录（CHGFILEDIR）

## 使用实例

查询USN_SP_RU_0064上话单文件的工作目录：

DSP CHGFILEDIR: RUNAME="USN_SP_RU_0064";

```
%%DSP CHGFILEDIR: RUNAME="USN_SP_RU_0064";%%
RETCODE = 0  操作成功。

输出结果如下
-------------
  RU名称   =  USN_SP_RU_0064
工作目录   =  CDR1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-CHGFILEDIR.md`
