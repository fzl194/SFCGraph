---
id: UDG@20.15.2@MMLCommand@DSP TRCTASK
type: MMLCommand
name: DSP TRCTASK（显示跟踪任务）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: TRCTASK
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 跟踪管理
status: active
---

# DSP TRCTASK（显示跟踪任务）

## 功能

该命令用于显示网元上跟踪任务信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TRACETASKID | 跟踪任务号 | 可选必选说明：可选参数<br>参数含义：跟踪任务ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967294。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [跟踪任务（TRCTASK）](configobject/UDG/20.15.2/TRCTASK.md)

## 使用实例

显示跟踪任务号为1的跟踪任务相关信息，可通过如下命令显示：

```
DSP TRCTASK: TRACETASKID=1
,SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
-------------------------
              跟踪任务号  =  1
            跟踪业务类型  =  117
                上报方式  =  文件上报
  生成的文件大小（字节）  =  204800
      生成文件周期（秒）  =  60
          握手周期（秒）  =  180
                    句柄  =  DK%s
        跟踪任务运行状态  =  正常
        Notification编号  =  1
                  跟踪ID  =  4294967295
                连接句柄  =  NULL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示跟踪任务（DSP-TRCTASK）_59103844.md`
