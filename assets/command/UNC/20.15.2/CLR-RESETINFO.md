---
id: UNC@20.15.2@MMLCommand@CLR RESETINFO
type: MMLCommand
name: CLR RESETINFO（清除资源单元复位信息）
nf: UNC
version: 20.15.2
verb: CLR
object_keyword: RESETINFO
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 设备管理
status: active
---

# CLR RESETINFO（清除资源单元复位信息）

## 功能

该命令用于清除资源单元复位信息。当不需要查看资源单元的历史复位信息时，执行该命令可以用来清除资源单元复位信息。

## 注意事项

- 该命令执行后立即生效。
- 执行该命令后，用户将无法查到该命令生效时间点之前的资源单元复位信息。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | 资源单元名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：使用<br>[**DSP RU**](../../../系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>查看RU名称。 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过<br>**LST VNFC**<br>命令获取。<br>默认值：无<br>配置原则：只能填写通过<br>**LST VNFC**<br>命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RESETINFO]] · 资源单元复位信息（RESETINFO）

## 使用实例

用于清除资源单元复位信息：

```
CLR RESETINFO:RUNAME="CSDB_OM_RU_0001"
,SERVICEINSTANCE="vnfc"
;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/CLR-RESETINFO.md`
