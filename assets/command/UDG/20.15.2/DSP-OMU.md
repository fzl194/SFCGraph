---
id: UDG@20.15.2@MMLCommand@DSP OMU
type: MMLCommand
name: DSP OMU（显示主备操作维护单元信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: OMU
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 系统管理
- 系统维护
- 倒换主备资源单元
status: active
---

# DSP OMU（显示主备操作维护单元信息）

## 功能

该命令用于显示VNFC主控主和主控备以及是否能够倒换的信息。

VNFC主控分为主控主和主控备，也可以称为主主控和备主控。以VNFC主控为例，在系统正常工作时，只有VNFC主控主实现业务。当VNFC主控主发生故障时，则会发生倒换过程，VNFC主控备将升为VNFC主控主，继续处理业务。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/OMU]] · 倒换主备操作维护单元（OMU）

## 使用实例

查询VNFC环境中，主备主控的信息，并确认是否具有倒换能力：

```
DSP OMU:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
-----------------------------------
倒换状态  =  就绪
 主用OMU  =  VNODE_CSLB_VNFC_OMU_0001
 备用OMU  =  VNODE_CSLB_VNFC_OMU_0002
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示主备操作维护单元信息（DSP-OMU）_59103381.md`
