---
id: UNC@20.15.2@MMLCommand@DSP RU
type: MMLCommand
name: DSP RU（显示资源单元信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: RU
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

# DSP RU（显示资源单元信息）

## 功能

该命令用于显示VNFC上的资源块。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数表示资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。区分大小写。<br>默认值：无<br>配置原则：只能填写实际存在的资源单元。 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识，但不能填写0，0表示VNFP。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RU]] · 解闭CSDB RU（RU）

## 使用实例

- 显示VNFC上的所有资源单元信息：
  ```
  DSP RU:
  SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  ------------------------
  RU编号    RU名称                     RU类型                 HA角色    虚拟机名称    运行状态    注册状态      内存资源（MB）    存储资源（GB）    CPU资源    内存利用率（%）    CPU利用率（%）    HA组    亲和性组    扩展组    主机位置                                RU扩展信息    主机名称                位置信息                          父资源名称    CPU架构类型

  1         CSDB_OM_RU_0001            CSDB_OM_RU             主        OMU1          正常        注册态        16384             5                 4          20                 5                 NULL    NULL        NULL      48645528-D21D-B211-88D4-001823E5F68B    NULL          S19_RN43_SRN0_Host21    X.X.X.X,az1.dc1,az2.dc1,HASrv1    OMU1          X86
  2         CSDB_OM_RU_0002            CSDB_OM_RU             备        OMU2          正常        注册态        16384             5                 4          18                 3                 NULL    NULL        NULL      4246A128-D21D-B211-AC08-001823E5F68B    NULL          S19_RN43_SRN0_Host8     X.X.X.X,az1.dc1,az2.dc1,HASrv1    OMU2          X86
  67        CSDB_SD_RU_0067            CSDB_SD_RU             无        bb            正常        注册态        16384             5                 4          25                 9                 NULL    NULL        NULL      4246A128-D21D-B211-AC08-001823E5F68B    NULL          NULL                    X.X.X.X,az1.dc1,az2.dc1,HASrv1    bb            X86
  (结果个数 = 3)
  ---    END
  ```
- 显示VNFC上的指定资源单元，资源单元名称为CSDB_OM_RU_0001：
  ```
  DSP RU:RUNAME="CSDB_OM_RU_0001"
  ,SERVICEINSTANCE="vnfc"
  ;
  ```
  ```
  RETCODE = 0  操作成功

  结果如下:
  ------------------------
          RU编号  =  1
          RU名称  =  CSDB_OM_RU_0001
          RU类型  =  CSDB_OM_RU
          HA角色  =  主
      虚拟机名称  =  OMU1  
        运行状态  =  正常
        注册状态  =  注册态
   内存资源（MB） =  16384
   存储资源（GB） =  5
         CPU资源  =  4
  内存利用率（%） =  20
   CPU利用率（%） =  5
            HA组  =  NULL
        亲和性组  =  NULL
          扩展组  =  NULL
        主机位置  =  48645528-D21D-B211-88D4-001823E5F68B
      RU扩展信息  =  NULL
        主机名称  =  S19_RN43_SRN0_Host21
        位置信息  =  X.X.X.X,az1.dc1,az2.dc1,HASrv1
      父资源名称  =  OMU1  
     CPU架构类型  =  X86
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-RU.md`
