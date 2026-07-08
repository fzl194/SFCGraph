---
id: UNC@20.15.2@MMLCommand@DSP COMPSTATNOTIFY
type: MMLCommand
name: DSP COMPSTATNOTIFY（显示组件状态通知记录）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: COMPSTATNOTIFY
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 进程和组件信息
status: active
---

# DSP COMPSTATNOTIFY（显示组件状态通知记录）

## 功能

该命令用于查询组件状态通知历史记录。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| COMPCID | 组件ID | 可选必选说明：必选参数<br>参数含义：该参数表示组件ID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |
| PROCESS | 进程ID | 可选必选说明：必选参数<br>参数含义：该参数表示进程ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [组件状态通知记录（COMPSTATNOTIFY）](configobject/UNC/20.15.2/COMPSTATNOTIFY.md)

## 使用实例

查询组件状态通知历史记录：

```
DSP COMPSTATNOTIFY:COMPCID="80CF0010",PROCESS=2
,SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
------------------------
时间                     状态通知             运行状态

01-19 14:29:54.845778    COMP-UPDATE STATE: 1    PRIMARY       
01-19 14:30:04.663968    COMP-UPDATE STATE: 1    PRIMARY       
01-19 14:30:04.667142    COMP-UPDATE STATE: 1    PRIMARY       
01-19 14:30:04.670568    COMP-UPDATE STATE: 1    PRIMARY       
(结果个数 = 4)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示组件状态通知记录（DSP-COMPSTATNOTIFY）_59104123.md`
