---
id: UDG@20.15.2@MMLCommand@DSP ACC
type: MMLCommand
name: DSP ACC（显示加速器信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: ACC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 系统管理
- 资源管理
- 加速器管理
status: active
---

# DSP ACC（显示加速器信息）

## 功能

该命令用于显示加速器的信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：用于表示资源单元的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用<br>[**DSP RU**](../RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>查看RU名称。 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识，但不能填写0，0表示VNFP。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ACC]] · 加速器信息（ACC）

## 使用实例

- 显示所有资源单元上的加速器信息：
  ```
  DSP ACC:
  SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  ------------------------
  RU名称                     加速器索引    加速器名称    加速器类型    加速器在位状态    加速器状态    配置错误码    状态错误码 

  CSDB_SD_RU_0067            0             acc0          sa            在位              不正常        0x0           0x4               
  CSDB_SD_RU_0068            0             acc0          sa            在位              不正常        0x0           0x4
  (结果个数 = 2)
  ---    END
  ```
- 显示指定资源单元上的所有加速器的信息，资源单元名称为CSDB_SD_RU_0067：
  ```
  DSP ACC:RUNAME="CSDB_SD_RU_0067"
  ,SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  ------------------------
          RU名称  =  CSDB_SD_RU_0067
      加速器索引  =  0
      加速器名称  =  acc0
      加速器类型  =  sa
  加速器在位状态  =  在位
      加速器状态  =  不正常
      配置错误码  =  0x0
      状态错误码  =  0x4
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示加速器信息（DSP-ACC）_59103794.md`
