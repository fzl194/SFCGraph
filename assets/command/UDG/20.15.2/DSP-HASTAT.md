---
id: UDG@20.15.2@MMLCommand@DSP HASTAT
type: MMLCommand
name: DSP HASTAT（查询系统HA状态）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: HASTAT
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

# DSP HASTAT（查询系统HA状态）

## 功能

该命令用于查询系统RU的HA状态，HA（High Availability）是为对象存储服务提供高可靠性的模块。灰度升级，需要确保所有组件状态正常。当系统进行灰度升级时，可以使用该命令确定RU的组件状态是否正常。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数表示RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63，区分大小写。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识，但不能填写0，0表示VNFP。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@HASTAT]] · 系统HA状态（HASTAT）

## 使用实例

查询系统HA状态：

```
DSP HASTAT:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功
 
结果如下:
 -------------------------
 RU ID = 1
RU名称 = VNODE_CSLB_VNFC_OMU_0001
HA状态 = 正常    
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-HASTAT.md`
