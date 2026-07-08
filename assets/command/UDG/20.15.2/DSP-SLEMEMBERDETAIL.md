---
id: UDG@20.15.2@MMLCommand@DSP SLEMEMBERDETAIL
type: MMLCommand
name: DSP SLEMEMBERDETAIL（显示仲裁成员详细信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SLEMEMBERDETAIL
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

# DSP SLEMEMBERDETAIL（显示仲裁成员详细信息）

## 功能

该命令用于显示仲裁成员详细信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于显示RU名称。通过<br>[**DSP SLEMEMBER**](显示仲裁成员列表信息（DSP SLEMEMBER）_35678578.md)<br>命令可以查询所有仲裁成员对应的资源单元信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：<br>- 只能填写实际存在的资源单元或资源名称。<br>- 当本命令在VNFP上使用时，需要先使用[**DSP RES**](../../../../单体服务平台功能管理/系统管理/资源管理/资源实例管理/显示资源信息（DSP RES）_59036939.md)查到“资源名称”，然后将“资源名称”的取值配置到本参数。<br>- 当本命令在VNFC上使用时，需要先使用[**DSP RU**](显示资源单元信息（DSP RU）_59103857.md)查到“RU名称”，然后将“RU名称”的取值配置到本参数。 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [仲裁成员详细信息（SLEMEMBERDETAIL）](configobject/UDG/20.15.2/SLEMEMBERDETAIL.md)

## 使用实例

显示仲裁成员详细信息：

```
DSP SLEMEMBERDETAIL:RUNAME="VNODE_VNRS_VNFC_OMU_0001"
,SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
------------------------
                 RU名称  =  VNODE_VNRS_VNFC_OMU_0001
             是否候选者  =  TRUE
                   角色  =  主节点
               工作模式  =  防脑裂
                 区域ID  =  0
               主节点ID  =  1
       仲裁区域节点总数  =  5
             心跳连接数  =  4
               通讯方式  =  MAC模式
         消息队列出错数  =  0
         申请内存出错数  =  0
         消息发送出错数  =  0
         消息接收出错数  =  0
           仲裁启动时间  =  2016-12-11 18:31:28
软仲裁选主容忍时间（ms） =  3000
软仲裁停主容忍时间（ms） =  3000
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示仲裁成员详细信息（DSP-SLEMEMBERDETAIL）_81883493.md`
