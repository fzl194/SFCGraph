---
id: UNC@20.15.2@MMLCommand@LST RUCPUINFO
type: MMLCommand
name: LST RUCPUINFO（查询RU CPU信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RUCPUINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务维护功能管理
- 操作维护
- 系统调测
- CPU信息
status: active
---

# LST RUCPUINFO（查询RU CPU信息）

## 功能

该命令用于查询指定RU的CPU信息，CPU信息包含CPU代数、CPU主频以及CPU类型。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：被查询的资源单元名称。通过<br>**DSP RU**<br>命令可以查询资源单元名称。<br>数据来源：本端规划<br>取值范围：1～64位字符串<br>默认值：无<br>说明：- 若不输入，则表示查询系统内所有RU的CPU信息。 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。该参数不能取值为VNFP、ACS、VNRS_VNFC的服务实例名称。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RUCPUINFO]] · RU CPU信息（RUCPUINFO）

## 使用实例

查询RU名称为USN_OM_RU_0001的CPU信息，执行以下命令：

LST RUCPUINFO: RUNAME="USN_OM_RU_0001" ,SERVICEINSTANCE=" vnfc " ;

```
RETCODE = 0  操作成功。

结果如下
--------
   RuId  =  1
 RU名称  =  USN_OM_RU_0001
CPU代数  =  Gold 6161 CPU
CPU类型  =  x86_64
CPU主频  =  2100
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-RUCPUINFO.md`
