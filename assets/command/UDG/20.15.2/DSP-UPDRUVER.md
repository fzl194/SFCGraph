---
id: UDG@20.15.2@MMLCommand@DSP UPDRUVER
type: MMLCommand
name: DSP UPDRUVER（显示RU版本信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: UPDRUVER
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 升级维护
status: active
---

# DSP UPDRUVER（显示RU版本信息）

## 功能

该命令用于显示RU版本信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示资源单元名称。<br>数据来源：本端规划<br>取值范围：1-63位字符串，区分大小写，不支持空格。<br>默认值：无 |
| BASICPKGVERSIONID | 基础软件包版本号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定要加载的基础软件包版本号。<br>数据来源：本端规划<br>取值范围：1-63位字符串，区分大小写，不支持空格。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识，但不能填写0，0表示VNFP。 |

## 操作的配置对象

- [RU版本信息（UPDRUVER）](configobject/UDG/20.15.2/UPDRUVER.md)

## 使用实例

显示RU版本信息：

```
DSP UPDRUVER:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功 

结果如下:  
-------------------------  
RU名称                     基础软件包版本号 
VNODE_UGW_VNFC_OMU_0001    V100R020C00B021
VNODE_UGW_VNFC_OMU_0002    V100R020C00B021
VNODE_UGW_VNFC_SPU_0064    V100R020C00B021
VNODE_UGW_VNFC_SPU_0065    NULL
(结果个数 = 4)  
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示RU版本信息（DSP-UPDRUVER）_90871556.md`
