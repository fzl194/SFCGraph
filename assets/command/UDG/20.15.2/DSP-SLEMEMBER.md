---
id: UDG@20.15.2@MMLCommand@DSP SLEMEMBER
type: MMLCommand
name: DSP SLEMEMBER（显示仲裁成员列表信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SLEMEMBER
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 系统管理
- 资源管理
- RU管理
status: active
---

# DSP SLEMEMBER（显示仲裁成员列表信息）

## 功能

该命令用于显示仲裁成员列表信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SLEMEMBER]] · 仲裁成员列表信息（SLEMEMBER）

## 使用实例

显示仲裁成员列表信息：

```
DSP SLEMEMBER:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
------------------------
RUID    RU名称                          是否候选者    角色        工作模式 

1        VNODE_VNRS_VNFC_OMU_0001        TRUE         主节点       防脑裂 
2        VNODE_VNRS_VNFC_OMU_0002        TRUE         从节点       防脑裂 
64       VNODE_VNRS_VNFC_OMU_0003        FALSE        从节点       防脑裂 
65       VNODE_VNRS_VNFC_OMU_0004        FALSE        从节点       防脑裂 
66       VNODE_VNRS_VNFC_OMU_0005        TRUE         从节点       防脑裂 
(结果个数 = 5)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-SLEMEMBER.md`
