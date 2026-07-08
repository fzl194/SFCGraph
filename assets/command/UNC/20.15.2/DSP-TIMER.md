---
id: UNC@20.15.2@MMLCommand@DSP TIMER
type: MMLCommand
name: DSP TIMER（显示定时器信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: TIMER
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 进程和组件信息
status: active
---

# DSP TIMER（显示定时器信息）

## 功能

该命令用于显示定时器信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：用于表示RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [定时器信息（TIMER）](configobject/UNC/20.15.2/TIMER.md)

## 使用实例

显示VNODE_CSLB_VNFC_OMU_0002的定时器信息：

```
DSP TIMER:RUNAME="VNODE_CSLB_VNFC_OMU_0002"
,SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
--------
进程ID     进程名称        定时器超时时长    定时器参数    定时器类型    定时器选项    组件ID        组件名称    

1001       HSM             1000              0x757347C9    0x10002       0x80000002    0x80030020    SEM_Agent           
1001       HSM             500               0x757347C8    0x10003       0x80000002    0x80030020    SEM_Agent           
1001       HSM             1000              0x1050000     0x0           0x80000002    0x80030020    SEM_Agent           
1001       HSM             1000              0x1070000     0x0           0x80000002    0x80030020    SEM_Agent           
1001       HSM             1000              0x757348BC    0x10005       0x80000002    0x80030020    SEM_Agent           
1001       HSM             1000              0x1180000     0x0           0x80000002    0x80030020    SEM_Agent           
1001       HSM             3000              0x1030000     0x0           0x80000002    0x80030020    SEM_Agent           
1001       HSM             10000             0x0           0x10001       0x80000002    0x80030020    SEM_Agent           
1001       HSM             10000             0x0           0x10004       0x80000002    0x80030020    SEM_Agent           
1001       HSM             10000             0x1080000     0x0           0x80000002    0x80030020    SEM_Agent           
1001       HSM             10000             0x1000000     0x0           0x80000002    0x80030020    SEM_Agent           
1001       HSM             5000              0x10A0000     0x0           0x80000002    0x80030020    SEM_Agent           
1001       HSM             10000             0x1040000     0x0           0x80000002    0x80030020    SEM_Agent           
1001       HSM             6000              0x1020000     0x0           0x80000002    0x80030020    SEM_Agent           
1001       HSM             120000            0x10D0000     0x0           0x80000002    0x80030020    SEM_Agent
(结果个数 = 16)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示定时器信息（DSP-TIMER）_59103751.md`
