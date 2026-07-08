---
id: UNC@20.15.2@MMLCommand@DSP RESETINFO
type: MMLCommand
name: DSP RESETINFO（显示资源单元复位信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: RESETINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 系统管理
- 资源管理
- RU管理
status: active
---

# DSP RESETINFO（显示资源单元复位信息）

## 功能

该命令用于显示资源单元复位信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用<br>[**DSP RU**](显示资源单元信息（DSP RU）_59103857.md)<br>查看RU名称。 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [资源单元复位信息（RESETINFO）](configobject/UNC/20.15.2/RESETINFO.md)

## 使用实例

- 显示所有资源单元的复位信息：
  ```
  DSP RESETINFO:
  SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  -------------------------
  RU名称                     序号    复位时间               复位次数    复位原因              复位码    

  CSDB_OM_RU_0001            1       2015-08-20 13:35:21    0           资源单元注册。        0x60100FF 
  CSDB_OM_RU_0002            1       2015-08-20 13:37:28    0           资源单元注册。        0x60100FF 
  (结果个数 = 2)
  ---    END
  ```
- 显示对应资源单元的复位信息，资源单元名称为CSDB_OM_RU_0001：
  ```
  DSP RESETINFO:RUNAME="CSDB_OM_RU_0001"
  ,SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  -------------------------
    RU名称  =  CSDB_OM_RU_0001
      序号  =  1
  复位时间  =  2015-08-20 13:35:21
  复位次数  =  0
  复位原因  =  资源单元注册。
    复位码  =  0x60100FF
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示资源单元复位信息（DSP-RESETINFO）_59104168.md`
