---
id: UDG@20.15.2@MMLCommand@DSP PLGPKGDETAILINFO
type: MMLCommand
name: DSP PLGPKGDETAILINFO（查询扩展包详细信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: PLGPKGDETAILINFO
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 系统管理
- 系统维护
- 扩展包管理
status: active
---

# DSP PLGPKGDETAILINFO（查询扩展包详细信息）

## 功能

该命令用于显示扩展包详细信息，包括扩展包单元文件名、类型及生效时间等。

扩展包的激活、删除会触发扩展包单元状态的变化，使用该命令显示系统当前的扩展包单元状态信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PLGTYPE | 扩展包类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定要查询扩展包单元所属的扩展包的类型。可通过<br>[**DSP PLGPKG**](显示扩展包版本信息（DSP PLGPKG）_59104292.md)<br>查询获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无 |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定要查询扩展包单元所属的RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：使用<br>[**DSP RU**](../../资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>查看RU名称。 |
| PROCID | 进程号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定要查询扩展包单元所属进程的ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| TYPE | 类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定要查询扩展包单元的类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无 |
| EFFECTIVETIME | 生效时间 | 可选必选说明：可选参数<br>参数含义：该参数用于指定要查询扩展包单元的生效时间。<br>数据来源：本端规划<br>取值范围：日期时间类型，输入格式是YYYY&MM&DD&HH&NN&SS。2000/01/01 00:00:00～ 2037/12/31 23:59:59。<br>默认值：无 |
| FILENAME | 文件名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定要查询扩展包单元文件名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过<br>**LST VNFC**<br>命令查询到的管理代理标识，但不能填写0，0表示VNFP。 |

## 操作的配置对象

- [扩展包详细信息（PLGPKGDETAILINFO）](configobject/UDG/20.15.2/PLGPKGDETAILINFO.md)

## 使用实例

显示扩展包详细信息：

```
DSP PLGPKGDETAILINFO:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
-------------------------
扩展包名称   RU名称     进程ID   类型       生效时间               文件名
MOD15        OMU1       3        SCRIPT     2019-08-27 14:32:51    HM830000.mod
MOD15        OMU1       3        SCRIPT     2019-08-27 14:32:51    HM830001.mod
MOD15        OMU2       6        SCRIPT     2019-08-27 14:32:52    HM830000.mod
MOD15        OMU2       6        SCRIPT     2019-08-27 14:32:52    HM830001.mod
(结果个数 = 4)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询扩展包详细信息（DSP-PLGPKGDETAILINFO）_38829214.md`
